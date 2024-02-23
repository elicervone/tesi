import pymongo, sys
from datetime import datetime, timedelta
from openpyxl import Workbook
from style import *
from writeExcel import *
import grafici


def info_ese(testo, collection, collection4, sheet, td, num_c):
    ''' Funzione che stampa le informazioni relative all'esercitazione passata come argomento '''
    
    ris = collection.find({})   # Risultati della query
    title = ""

    for r in ris:
        # Ottiene i dati dell'esercitazione
        query = {"Title" : r.get("title"), "Slug" : r.get("slug"), "Accepted" : str(r.get("accepted")), "Submissions" : str(r.get("submissions")), "Passing" : str(r.get("passing")), "Files" : str(r.get("files"))}

        # Se l'esercitazione è quella cercata
        if testo in query.get("Title"):
            title = query.get("Title")  # Titolo dell'esercitazione

            sheet["A1"] = title # Scrive il titolo dell'esercitazione sul file excel

            current_row = 2 # Riga corrente del foglio di lavoro (parte dalla riga 2 perché abbiamo già scritto il titolo dell'esercitazione nella riga 1)

            # Scrive le informazioni riguardo l'esercitazione sul file excel
            current_row = write_to_sheet(sheet, "Numero totale di studenti", query.get("Accepted"), 
                                        "Numero di studenti che hanno consegnato", query.get("Submissions"), 
                                        "Numero di studenti che hanno passato l'esercitazione", query.get("Passing"), "", "", current_row)

            files = query.get("Files")  # File dell'esercitazione
            file_list = files.split(",")    # Lista dei file dell'esercitazione ottenuta separando la stringa files per virgola
            nuova_lista = [s.strip().replace("[", "").replace("]", "").replace("'", "") for s in file_list] # Lista dei file dell'esercitazione senza spazi e caratteri speciali

    totale = collection4.count_documents({"title" : title}) # Numero totale di commit per l'esercitazione
    med = media(title, collection4, totale, num_c)  # Numero medio di commit per studente

    agg, rim = lineeCodice(title, collection4)  # Numero medio di righe aggiunte e rimosse per studente

    # Scrive le informazioni riguardo l'esercitazione sul file excel
    current_row = write_to_sheet(sheet, "Numero totale di commit", totale,
                                "Numero di commit medio per studente", med,
                                "Numero medio di righe aggiunte ad ogni commit per studente", agg, 
                                "Numero medio di righe rimosse ad ogni commit per studente", rim, current_row)

    produttivita(title, collection4, sheet, current_row+1, td)  # Tempo medio impiegato da ogni studente per svolgere l'esercitazione
    
    # Restituisce il titolo dell'esercitazione e la lista dei file dell'esercitazione
    return title, nuova_lista


def media(title, collection4, totale, num_c):
    ''' Funzione che calcola il numero medio di commit per studente '''

    nc = [] # Lista per tenere traccia del numero di commit per ogni studente

    ris = collection4.find({"title" : title})    # Risultati della query
    authors = {}  # Dizionario per tenere traccia dei commit per ogni autore

    for r in ris:
        author = r.get("author")    # Autore del commit

        # Controlla se l'autore è già nel dizionario authors. Se sì, ottiene il numero di commit effettuati dall'autore finora, altrimenti imposta il valore a 0.
        authors[author] = authors.get(author, 0) + 1  # Incrementa il conteggio dei commit per l'autore

    num_authors = len(authors)  # Numero di autori unici

    #   GRAFICO COMMIT
    grafici.grafico_commits(title, authors) # Crea il grafico per media e deviazione standard del numero di commit
    
    nc.extend(authors.values())
    num_c.append(nc)    # Aggiunge la lista dei commit per ogni studente alla lista num_c passata come parametro

    # Calcola e restituisce la media dei commit dividendo il totale dei commit per il numero di autori unici 
    return totale / num_authors


def lineeCodice(title, collection4):
    ''' Funzione che calcola il numero medio di righe aggiunte e rimosse per studente '''

    ris = collection4.find({"title": title})    # Risultati della query
    authors = {}  # Dizionario per tenere traccia delle linee di codice per ogni autore

    agg_tot = 0
    rim_tot = 0

    for r in ris:
        author = r.get("author")    # Autore del commit

        # Inizializza l'autore se non è già presente nel dizionario
        if author not in authors:
            authors[author] = {"aggiunte": 0, "rimozioni": 0}  

        # Aggiorna il conteggio delle righe aggiunte e rimosse per l'autore
        if r.get("aggiunte") is not None:
            authors[author]["aggiunte"] += r.get("aggiunte")
            agg_tot += r.get("aggiunte")

        if r.get("rimozioni") is not None:
            authors[author]["rimozioni"] += r.get("rimozioni")
            rim_tot += r.get("rimozioni")

    #   GRAFICO CODICE MODIFICATO
    grafici.grafico_codice(title, authors) # Crea il grafico per media e deviazione standard del numero di righe di codice
    
    # Calcola e restituisce la media delle righe aggiunte e rimosse dividendo il totale delle righe per il numero di autori unici
    return agg_tot/len(authors), rim_tot/len(authors)
    

def produttivita(title, collection4, sheet, current_row, td):
    ''' Funzione che calcola il tempo medio impiegato da ogni studente per svolgere l'esercitazione '''

    ris = collection4.find({"title": title})    # Risultati della query
    date_format = "%Y-%m-%dT%H:%M:%SZ"  # Formato della data
    commit_dates = {}  # Dizionario per tenere traccia delle date dell'ultimo commit per studente
    
    for r in ris:
        # Se esiste una data di commit e una data di commit iniziale
        if r.get("date_initial_commit") is not None and r.get("date") is not None:
            author = r.get("author")    # Autore del commit
            commit_date_string = r.get("date")   # Data dell'ultimo commit
            initial_commit_date_string = r.get("date_initial_commit")  # Data del clone della repository

            # Converte le date in formato datetime
            commit_date = datetime.strptime(commit_date_string, date_format)
            initial_commit_date = datetime.strptime(initial_commit_date_string, date_format)

            # Aggiorna la data dell'ultimo commit per lo studente
            if author in commit_dates:
                # Se esiste già una data di commit per lo studente, confronta e aggiorna se la nuova data è più recente
                if commit_date > commit_dates[author]["last_commit_date"]:
                    commit_dates[author]["last_commit_date"] = commit_date
            else:
                # Se è la prima volta che si incontra lo studente, registra la data del suo commit
                commit_dates[author] = {
                    "last_commit_date": commit_date,
                    "initial_commit_date": initial_commit_date
                }


    time_differences = []  # Lista per memorizzare le differenze di tempo per studente
    time_diff_formatted = [] # Lista per memorizzare le differenze di tempo formattate per studente

    # Itera attraverso il dizionario dei commit per studente
    for author, commit_info in commit_dates.items():
            last_commit_date = commit_info["last_commit_date"]
            initial_commit_date = commit_info["initial_commit_date"]

            time_difference = last_commit_date - initial_commit_date    # Differenza di tempo tra l'ultimo commit e il clone della repository
            time_differences.append(time_difference)

            # Conversione in timestamp (numero di secondi dall'epoch)
            secondi_totali = time_difference.total_seconds()

            # Conversione in giorni
            giorni_totali = int(secondi_totali / (24 * 60 * 60))
            time_diff_formatted.append(giorni_totali)

    #   GRAFICO PRODUTTIVITA
    grafici.grafico_produttivita(title, time_diff_formatted) # Crea il grafico per media e deviazione standard del tempo impiegato per svolgere l'esercitazione
    
    td.append(time_diff_formatted)  # Aggiunge la lista delle differenze di tempo per ogni studente alla lista td passata come parametro

    # Calcola la somma delle differenze di tempo
    total_diff = sum(time_differences, timedelta())

    # Calcola la media delle differenze di tempo per studente se la lista non è vuota, altrimenti imposta la media a 0
    average_time_differences = total_diff / len(time_differences) if time_differences else timedelta(seconds=0)
    
    # Scrive le informazioni riguardo l'esercitazione sul file excel
    sheet[f"A{current_row}"] = "Tempo impiegato in media da ogni studente per svolgere l'esercitazione"
    sheet[f"B{current_row}"] = formatta_data(average_time_differences)



def perEs(title, file_list, collection4, sheet, slug, td, num_c):
    ''' Funzione che stampa le informazioni relative ad ogni esercizio dell'esercitazione passata come argomento '''

    current_row = 12 # Riparte dalla riga 12 nel file excel
    new_file_list = []  # Lista dei file dell'esercitazione senza spazi e caratteri speciali
    risultati_finali = []   # Lista per tenere traccia dei risultati finali dei check
    esercizi = []   # Lista per tenere traccia dei risultati dei check
    ris = {}    # Dizionario per tenere traccia dei risultati dei check

    for f in file_list:
        current_row += 2

        file_con_spazi = f.replace("_", " ") # Nome dell'esercizio con gli spazi

        sheet[f"A{current_row}"] = file_con_spazi # Scrive il nome dell'esercizio sul file excel
        current_row += 1

        totale = collection4.count_documents({"title" : title, "files": {"$regex": f}})  # Numero totale di commit per l'esercizio

        media = media_perEs(title, f, collection4, totale, num_c)  # Numero medio di commit per studente

        agg_tot, rim_tot = linee_codice_perEs(title, f, collection4) # Numero medio di righe aggiunte e rimosse per studente

        # Scrive le informazioni riguardo l'esercizio sul file excel
        current_row = write_to_sheet(sheet, "Numero totale di commit", totale,
                                    "Numero di commit medio per studente", media,
                                    "Numero medio di righe aggiunte ad ogni commit per studente", agg_tot,
                                    "Numero medio di righe rimosse ad ogni commit per studente", rim_tot,
                                    current_row)

        prodPerEs(title, f, collection4, sheet, current_row, td)    # Tempo medio impiegato da ogni studente per svolgere l'esercizio

        #   Chiamata alla funzione per controllare i check statici e dinamici
        file, esercizi = check_statici(title, file_con_spazi, slug, esercizi) # Restituisce il nome del file e la lista dei risultati dei check
        ris = {file: esercizi}  # Aggiunge i risultati dei check al dizionario ris (per ogni esercizio salva la lista del tipo 
                                # [numero di commit che non passano il check dinamico, numero di commit che non passano il check statico, numero di commit che passano entrambi i check])
        risultati_finali.append(ris) # Aggiunge il dizionario ris alla lista risultati_finali per tenere traccia dei risultati finali dei check per tutti gli esercizi
        new_file_list.append(file) # Aggiunge il nome del file alla lista new_file_list
        esercizi = [] # Resetta la lista esercizi

    # Restituisce la lista dei file dell'esercitazione senza spazi e caratteri speciali e la lista dei risultati finali dei check
    return new_file_list, risultati_finali


def media_perEs(title, file, collection4, totale, num_c):
    ''' Funzione che calcola il numero medio di commit per studente per singolo esercizio'''
    
    # Pipeline usata come filtro nella ricerca nel DB (cerca fra i commit quelli relativi 
    # all'esercitazione richiesta e quelli per cui il nome del file modificato contiene 
    # il nome dell'esercizio al suo interno)
    pipeline = [
        {"$match": {"title": title, "files": {"$regex": file}}},
        {"$group": {"_id": "$author", "count": {"$sum": 1}}}  # Conta il numero di commit per ogni autore
    ]

    result = collection4.aggregate(pipeline)    # Risultati della query

    num_commits_per_author = []  # Lista per tenere traccia dei commit per ogni autore

    for r in result:
        num_commits_per_author.append(r['count'])  # Aggiungi il conteggio dei commit per l'autore corrente alla lista

    #  GRAFICO COMMIT
    grafici.grafico_commits(file, num_commits_per_author)  # Crea il grafico per media e deviazione standard del numero di commit (per singolo esercizio)
    
    num_c.append(num_commits_per_author)    # Aggiunge la lista dei commit per ogni studente alla lista num_c passata come parametro

    return totale / len(num_commits_per_author)  # Numero medio di commit per studente


def linee_codice_perEs(title, file, collection4):
    ''' Funzione che calcola il numero medio di righe aggiunte e rimosse per studente per singolo esercizio'''

    ris = collection4.find({"title": title, "files": {"$regex": file}})
    authors = {}  # Dizionario per tenere traccia delle linee di codice per ogni autore

    agg_tot = 0
    rim_tot = 0

    for r in ris:
        author = r.get("author")    # Autore del commit

        # Inizializza l'autore se non è già presente nel dizionario
        if author not in authors:
            authors[author] = {"aggiunte": 0, "rimozioni": 0}  

        # Aggiorna il conteggio delle righe aggiunte e rimosse per l'autore
        if r.get("aggiunte") is not None:
            authors[author]["aggiunte"] += r.get("aggiunte")
            agg_tot += r.get("aggiunte")

        if r.get("rimozioni") is not None:
            authors[author]["rimozioni"] += r.get("rimozioni")
            rim_tot += r.get("rimozioni")

    #   GRAFICO CODICE MODIFICATO
    grafici.grafico_codice(file, authors) # Crea il grafico per media e deviazione standard del numero di righe di codice (per singolo esercizio)

    # Calcola e restituisce la media delle righe aggiunte e rimosse dividendo il totale delle righe per il numero di autori unici
    return agg_tot/len(authors), rim_tot/len(authors)


def prodPerEs(title, file, collection4, sheet, current_row, td):
    ''' Funzione che calcola il tempo medio impiegato da ogni studente per svolgere l'esercizio '''

    ris = collection4.find({"title": title, "files": {"$regex": file}})   # Risultati della query
    date_format = "%Y-%m-%dT%H:%M:%SZ"  # Formato della data
    commit_dates = {}  # Dizionario per tenere traccia delle date dell'ultimo commit per studente

    for r in ris:
        # Se esiste una data di commit e una data di commit iniziale
        if r.get("date_initial_commit") is not None and r.get("date") is not None:
            author = r.get("author")    # Autore del commit
            commit_date_string = r.get("date")  # Data dell'ultimo commit
            initial_commit_date_string = r.get("date_initial_commit")   # Data del clone della repository

            # Se esiste un punteggio
            if r.get("points") is not None:
                punteggio = r.get("points") # Punteggio dell'esercizio rappresentato come stringa (es. "Punteggio: 1/4")
                punteggio_string = punteggio.split(" ")[1].split("/")[0] # Punteggio dell'esercizio rappresentato come stringa (es. "1")

                # Converte le date in formato datetime
                commit_date = datetime.strptime(commit_date_string, date_format)
                initial_commit_date = datetime.strptime(initial_commit_date_string, date_format)

                # Aggiorna la data dell'ultimo commit per lo studente
                if author in commit_dates:
                    # Se lo studente è già presente, aggiungi il nuovo commit alla lista ordinata
                    commit_dates[author]["commit_list"].append({
                        "commit_date": commit_date,
                        "commit_info": {"commit_date": commit_date_string, "punteggio": punteggio_string}
                    })
                    commit_dates[author]["commit_list"].sort(key=lambda x: x["commit_date"])  # Ordina la lista dei commit per data
                else:
                    # Se è la prima volta che si incontra lo studente, registra la data del suo commit
                    commit_dates[author] = {
                        "commit_list": [{
                            "commit_date": commit_date,
                            "commit_info": {"commit_date": commit_date_string, "punteggio": punteggio_string}
                        }],
                        "initial_commit_date": {"commit_date": initial_commit_date, "commit_date_string": initial_commit_date_string}
                    }


    time_differences = []  # Lista per memorizzare le differenze di tempo per studente
    date_effettive = [] # Lista per memorizzare le date effettive di consegna dell'esercizio
    time_diff_formatted = [] # Lista per memorizzare le differenze di tempo formattate per studente


    # Itera attraverso il dizionario dei commit per studente
    for author, commit_info in commit_dates.items():
        commit_list = commit_info["commit_list"]    # Lista dei commit per lo studente
        initial_commit_date = commit_info["initial_commit_date"]["commit_date"] # Data del clone della repository

        # Inizializza una variabile per tenere traccia del commit precedente
        commit_precedente = None

        # Itera attraverso la lista dei commit
        for current_index, current_commit in enumerate(commit_list):
            # Effettua il confronto solo se il commit corrente non è il primo
            if commit_precedente is not None and current_index > 0:
                # Se il punteggio al commit corrente è maggiore di quello al commit precedente, aggiungi la data del commit corrente alla lista delle date effettive
                # In questo caso, la data del commit corrente coincide con la data effettiva di consegna dell'esercizio (è stato assegnato un punto)
                if current_commit["commit_info"]["punteggio"] > commit_precedente["commit_info"]["punteggio"]:
                    date_effettive.append({
                        "last_commit_date": current_commit["commit_date"],
                        "initial_commit_date": initial_commit_date,
                        "author": author
                    })

            # Se il commit corrente è l'unico, aggiunge la data del commit corrente alla lista delle date effettive 
            # (è sicuramente la data effettiva di consegna dell'esercizio in quanto non ci sono altri commit successivi)
            elif len(commit_list)==1:
                date_effettive.append({
                    "last_commit_date": current_commit["commit_date"],
                    "initial_commit_date": initial_commit_date,
                    "author": author
                })

            # Aggiorna il commit precedente
            commit_precedente = current_commit

    # Itera attraverso la lista delle date effettive
    for commit_info in date_effettive:
        last_commit_date = commit_info["last_commit_date"]
        initial_commit_date = commit_info["initial_commit_date"]

        # Calcola la differenza di tempo tra l'ultimo commit e il clone della repository
        time_difference = last_commit_date - initial_commit_date
        time_differences.append(time_difference)
        # Conversione in timestamp (numero di secondi dall'epoch)
        secondi_totali = time_difference.total_seconds()

        # Conversione in giorni
        giorni_totali = int(secondi_totali / (24 * 60 * 60))
        time_diff_formatted.append(giorni_totali)

    #   GRAFICO PRODUTTIVITA
    grafici.grafico_produttivita(file, time_diff_formatted) # Crea il grafico per media e deviazione standard del tempo impiegato per svolgere l'esercizio
    
    td.append(time_diff_formatted)  # Aggiunge la lista delle differenze di tempo per ogni studente alla lista td passata come parametro

    # Calcola la media delle differenze di tempo per studente se la lista non è vuota, altrimenti imposta la media a 0
    total_diff = sum(time_differences, timedelta())
    average_time_differences = total_diff / len(time_differences) if time_differences else timedelta(seconds=0)
    
    # Scrive le informazioni riguardo l'esercizio sul file excel
    sheet[f"A{current_row}"] = "Tempo impiegato in media da ogni studente per svolgere l'esercizio"
    sheet[f"B{current_row}"] = formatta_data(average_time_differences)



def formatta_data(data):
    ''' Funzione che formatta la data nel formato desiderato '''

    total_seconds = data.total_seconds()

    # Calcola i giorni e le ore
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600

    # Formatta il tempo in una stringa leggibile
    return f"{int(days)} giorni, {int(hours)} ore"



def check_statici(title, file, slug, risultati):
    ''' Funzione che restituisce il numero di commit che passano i check statici per l'esercizio passato come argomento '''
    print(title)
    file_m = ""

    #region Cambio nome esercizi (perché alcuni nomi sono diversi nel file feedback.md rispetto al database)
    # SEMAFORI
    if file == "calcolo parallelo su un vettore condiviso":
        file_m = "calcolo parallelo"
    elif file == "coppia di buffer":
        file_m = "coppia di buffer"
    elif file == "lettori-scrittori con semafori su una coppia di valori condivisa":
        file_m = "lettori-scrittori"
    elif file == "simulazione di un disco con un vettore circolare" and title == "Esercitazione 1 (Semafori)":
        file_m = "simulazione disco, con semafori"

    # MONITOR
    elif file == "lettori-scrittori con monitor e processi":
        file_m = "lettori-scrittori"
    elif file == "prelievi multipli":
        file_m = "prelievi multipli"
    elif file == "produttore-consumatore con priorita":
        file_m = "produttore-consumatore"
    elif file == "simulazione di un disco con un vettore circolare" and title == "Esercitazione 2 (Monitor)":
        file_m = "simulazione disco, con monitor"

    # THREADS
    elif "lettori-scrittori su piu oggetti monitor" in file:
        file_m = "lettori-scrittori su" 
    elif file == "produttore-consumatore con priorita":
        file_m = "produttore-consumatore"
    elif file == "una struttura dati stack thread-safe":
        file_m = "struttura dati thread-safe"

    # MESSAGGI
    elif file == "grafo delle dipendenze":
        file_m = "grafo delle dipendenze"
    elif file == "load balancing":
        file_m = "load balancing"
    elif file == "registro distribuito":
        file_m = "registro distribuito"
    elif file == "server sincroni multipli":
        file_m = "server sincroni"

    # SERVER MUTLITHREAD
    elif file == "remote procedure call":
        file_m = "remote procedure call"
    elif file == "server aggregatore thread":
        file_m = "server aggregatore"
    elif file == "un primo esempio di server multithread":
        file_m = "primo esempio di server multithread"
    #endregion


    # Apre e legge il file feedback.md
    with open("feedback.md", "r") as f:        
        line = f.readline()
        non_passa_statico = 0   # Numero di commit che non passano il check statico
        non_passa_dinamico = 0  # Numero di commit che non passano il check dinamico
        passa_tutto = 0         # Numero di commit che passano entrambi i check

        nps_temp = 0    # Variabile temporanea per tenere traccia del numero di commit che non passano il check statico
        npd_temp = 0    # Variabile temporanea per tenere traccia del numero di commit che non passano il check dinamico
        pt_temp = 0     # Variabile temporanea per tenere traccia del numero di commit che passano entrambi i check

        esercizi = []   # Lista per tenere traccia dei risultati dei check
        titolo = False  # Variabile per tenere traccia se si è all'interno di una sezione relativa all'esercizio di interesse

        for line in f:
            if file_m in line and "##" in line:     # Se il nome dell'esercizio è presente nella riga e la riga contiene "##" allora si sta entrando nella sezione relativa all'esercizio di interesse
                titolo = True
            elif file_m not in line and "##" in line:   # Se il nome dell'esercizio non è presente nella riga e la riga contiene "##" allora si sta uscendo dalla sezione relativa all'esercizio di interesse
                titolo = False

            # Se si è all'interno della sezione relativa all'esercizio di interesse
            if titolo:               

                # Controlla se la riga contiene i risultati dei check
                if line.startswith(":warning"):

                    if "Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice" in line:
                        # Incrementa temporaneamente il numero di commit che non passano il check statico
                        nps_temp += 1          
                    else:
                        # Incrementa temporaneamente il numero di commit che non passano il check dinamico
                        npd_temp += 1

                elif line.startswith(":white_check_mark"):
                    # Incrementa il numero di commit che passano entrambi i check
                    pt_temp += 1

                elif line.startswith("e"):  # Se la riga inizia con "e" allora questa contiene lo slug dell'esercitazione
                    # Controlla se lo slug dell'esercitazione è presente nella riga (necessario perché alcuni esercizi in esercitazioni diverse hanno lo stesso nome)
                    if slug in line:
                        #print(line)
                        #print(slug)
                        # Se lo slug dell'esercitazione è presente nella riga, allora siamo all'interno della sezione relativa all'esercitazione di interesse
                        # e quindi aggiorna i valori dei contatori
                        non_passa_statico += nps_temp
                        non_passa_dinamico += npd_temp
                        passa_tutto += pt_temp

                        # Estrae lo sha del commit
                        if "5" in title:
                            sha = line.split("-")[5].split("/")[0]
                            if len(sha) != 40:
                                sha = line.split("-")[6].split("/")[0]
                        else:
                            sha = line.split("-")[4].split("/")[0]
                            if len(sha) != 40:
                                sha = line.split("-")[5].split("/")[0]

                        #print(sha, npd_temp, nps_temp, pt_temp)

                        # Per ogni commit, aggiorna il database specificando se e quali check ha passato
                        # Se si è deciso di clonare tutti i commit, si usa il database collection4, se se ne clonano solo alcuni si usa collection6
                        if npd_temp > 0:                   
                            #collection6.update_one({"sha": sha}, {"$set": {file_m: "non passa"}})
                            #print("non passa", file_m)
                            collection4.update_one({"sha": sha}, {"$set": {file_m: "non passa"}})
                        elif nps_temp > 0:
                            #collection6.update_one({"sha": sha}, {"$set": {file_m: "passa dinamico"}})     
                            #print("passa dinamico", file_m)     
                            collection4.update_one({"sha": sha}, {"$set": {file_m: "passa dinamico"}})
                        elif pt_temp > 0:
                            #collection6.update_one({"sha": sha}, {"$set": {file_m: "passa tutto"}})
                            #print("passa tutto", file_m)
                            collection4.update_one({"sha": sha}, {"$set": {file_m: "passa tutto"}})

                        #collection6.update_one({"sha": sha}, {"$set": {"usato": "si"}}) # Indica che quel determinato commit è stato clonato e quindi presenta il campo relativo ai check

                    # Resetta i valori dei contatori temporanei
                    nps_temp = 0
                    npd_temp = 0
                    pt_temp = 0
                        
        #print("fine, ", file)
        #print("non passa statico: ", non_passa_statico)
        #print("non passa dinamico: ", non_passa_dinamico)
        #print("passa tutto: ", passa_tutto)
        esercizi = [non_passa_dinamico, non_passa_statico, passa_tutto] # Aggiunge i risultati dei check all'array esercizi per tenere traccia del numero totale di commit che passano i check
        #   GRAFICO CHECK A TORTA
        #grafici.grafico_check_statici(file, esercizi)

    # Restituisce il nome del file e la lista dei risultati dei check
    return file_m, esercizi



def count_commits(title, file):
    ''' Funzione che conta il numero di commit per ogni studente per un determinato esercizio '''

    # Se si è deciso di clonare tutti i commit, si usa il database collection4, se se ne clonano solo alcuni si usa collection6
    #ris = collection6.find({"title" : title, "usato" : "si"})   # Risultati della query
    ris = collection4.find({"title" : title})   # Risultati della query
    
    date_format = "%Y-%m-%dT%H:%M:%SZ"  # Formato della data
    commit = {} # Dizionario per tenere traccia del commit corrente
    c_dict = {} # Dizionario per tenere traccia di tutti i commit per autore
    c_list = [] # Lista per tenere traccia dei commit per autore
    author = ""

    print(file)
    i=0

    for r in ris:
        # Se non è la prima iterazione
        if i > 0:
            # Crea un dizionario per il commit corrente
            commit = {
                "date": r.get("date"),
                "date_initial_commit": r.get("date_initial_commit"),
                "test": r.get(file)
            }

            # Se l'autore del commit corrente è lo stesso dell'autore del commit precedente, aggiunge il commit alla lista dei commit
            if r.get("author") == author:
                c_list.append(commit)

            # Se l'autore è diverso
            else:
                c_list.sort(key=lambda x: (x["date"])) # Ordina la lista dei commit per 'author' in ordine alfabetico e poi per 'date' in ordine cronologico
                c_dict[author] = c_list # Aggiunge la lista dei commit per l'autore corrente al dizionario dei commit
                
                c_list = [] # Resetta la lista dei commit
                author = r.get("author")    # Aggiorna l'autore del commit
                c_list.append(commit)       # Aggiunge il commit corrente alla nuova lista dei commit per il nuovo autore
            
        # Se è la prima iterazione
        else:
            # Ottiene l'autore del commit
            author = r.get("author")

            # Crea un dizionario per il commit corrente e lo aggiunge alla lista dei commit
            commit = {
                "date": r.get("date"),
                "date_initial_commit": r.get("date_initial_commit"),
                "test": r.get(file)
            }

            c_list.append(commit)
            
            i += 1

    c_dict_sorted = sorted(c_dict.items(), key=lambda x: x[0])  # Ordina il dizionario dei commit per autore in ordine alfabetico trasformandolo in una lista
    c_dict = dict(c_dict_sorted)  # Converte la lista ordinata in un dizionario

    
    commits_prima_di_passa_dinamico = []    # Lista per tenere traccia del numero di commit prima del commit che passa il check dinamico per autore
    commits_prima_di_passa_statico = []     # Lista per tenere traccia del numero di commit prima del commit che passa il check statico per autore
    tf_passa_dinamico = []  # Lista per tenere traccia delle differenze di tempo tra il primo commit e il primo commit che passa il check dinamico per autore
    tf_passa_statico = []   # Lista per tenere traccia delle differenze di tempo tra il primo commit e il primo commit che passa il check statico per autore

    # Itera attraverso il dizionario dei commit per autore
    for author, items in c_dict.items():
        #print(author)  #DEBUG
        # Ottiene la data del primo commit
        data_primo_commit_string = items[0].get("date_initial_commit")
        data_primo_commit = datetime.strptime(data_primo_commit_string, date_format)

        current_test = ""
        non_passa_dinamico = 0
        non_passa_statico = 0
        passa_tutto = 0
        commit_prima_di_passa_dinamico = 0
        commit_prima_di_passa_statico = 0

        data_passa_dinamico_string = ""
        data_passa_statico_string = ""

        # Itera attraverso la lista dei commit per l'autore corrente
        for item in items:
            #print(item)

            # Se il test corrente è diverso dal test precedente
            if item.get("test") != current_test:
                # Se il commit corrente non passa nessun test incrementa i contatori corrispondenti
                if item.get("test") == "non passa":
                    non_passa_dinamico += 1
                    non_passa_statico += 1
                    commit_prima_di_passa_dinamico += 1
                # Se il commit corrente passa il check dinamico incrementa i contatori corrispondenti e ottiene la data del commit
                elif item.get("test") == "passa dinamico":
                    non_passa_statico += 1
                    commit_prima_di_passa_statico += 1
                    data_passa_dinamico_string = item.get("date")
                # Se il commit corrente passa il check statico incrementa i contatori corrispondenti e ottiene la data del commit
                elif item.get("test") == "passa tutto":
                    passa_tutto += 1
                    data_passa_statico_string = item.get("date")
                
                # Calcola il tempo passato tra il primo commit e il primo commit che passa il check dinamico
                if data_passa_dinamico_string != "":
                    data_passa_dinamico = datetime.strptime(data_passa_dinamico_string, date_format)
                    tf = data_passa_dinamico - data_primo_commit
                    tf_passa_dinamico.append(tf)
                    #print("tempo passa dinamico: ", tf)
                    #print("\n")
                    #print(tf_passa_dinamico)
                    #print("\n")
                    
                # Calcola il tempo passato tra il primo commit e il primo commit che passa il check statico
                if data_passa_statico_string != "":
                    data_passa_statico = datetime.strptime(data_passa_statico_string, date_format)
                    tf = data_passa_statico - data_primo_commit
                    tf_passa_statico.append(tf)
                    #print("tempo passa statico: ", tf)
                    #print("\n")
                    #print(tf_passa_statico)
                    #print("\n")


                current_test = item.get("test") # Aggiorna il test corrente

            # Se il test corrente è uguale al test precedente, incrementa i contatori corrispondenti
            else:
                if item.get("test") == "non passa":
                    commit_prima_di_passa_dinamico += 1
                elif item.get("test") == "passa dinamico":
                    commit_prima_di_passa_statico += 1

        #print("non passa dinamico: ", non_passa_dinamico)
        #print("non passa statico: ", non_passa_statico)
        #print("passa tutto: ", passa_tutto)       
        #print("commit prima di passa dinamico: ", commit_prima_di_passa_dinamico)
        #print("commit prima di passa statico: ", commit_prima_di_passa_statico)       

        commits_prima_di_passa_dinamico.append(commit_prima_di_passa_dinamico)
        commits_prima_di_passa_statico.append(commit_prima_di_passa_statico)

    #print(commits_prima_di_passa_dinamico)
    #print(commits_prima_di_passa_statico)
    
    # Calcola il numero medio di commit prima del primo commit che passa il check dinamico e del primo commit che passa il check statico
    media_commits_prima_di_passa_dinamico = sum(commits_prima_di_passa_dinamico) / len(commits_prima_di_passa_dinamico)
    media_commits_prima_di_passa_statico = sum(commits_prima_di_passa_statico) / len(commits_prima_di_passa_statico)

    #print("media commits prima di passa dinamico: ", media_commits_prima_di_passa_dinamico)
    #print("media commits prima di passa statico: ", media_commits_prima_di_passa_statico)

    # Nel caso in cui per l'esercizio in questione non ci siano commit che passano solo il check dinamico, ma passano direttamente anche il check statico
    # si considera il tempo medio di passaggio del check dinamico uguale a quello del passaggio del check statico
    if tf_passa_dinamico == []:
        tf_passa_dinamico = tf_passa_statico

    #print(tf_passa_dinamico)
    #print(tf_passa_statico)

    # Calcola il tempo medio passato tra il primo commit e il primo commit che passa il check dinamico e il check statico
    total_diff_dinamico = sum(tf_passa_dinamico, timedelta())
    average_time_differences_dinamico = total_diff_dinamico / len(tf_passa_dinamico) if tf_passa_dinamico else timedelta(seconds=0)

    total_diff_statico = sum(tf_passa_statico, timedelta())
    average_time_differences_statico = total_diff_statico / len(tf_passa_statico) if tf_passa_statico else timedelta(seconds=0)

    #print("tempo medio passa dinamico: ", average_time_differences_dinamico)
    #print("tempo medio passa statico: ", average_time_differences_statico)

    # Converte le differenze di tempo in ore
    formatted_time_dinamico = []
    formatted_time_statico = []

    for tf in tf_passa_dinamico:
        # Conversione in timestamp (numero di secondi dall'epoch)
        secondi_totali = tf.total_seconds()

        # Conversione in giorni
        ore_totali = int(secondi_totali / (60 * 60))
        formatted_time_dinamico.append(ore_totali)
        #print(ore_totali)

    for tf in tf_passa_statico:
        # Conversione in timestamp (numero di secondi dall'epoch)
        secondi_totali = tf.total_seconds()

        # Conversione in giorni
        ore_totali = int(secondi_totali / (60 * 60))
        formatted_time_statico.append(ore_totali)
        #print(ore_totali)

    #print(commits_prima_di_passa_dinamico)
    #print(commits_prima_di_passa_statico)
    #print(formatted_time_dinamico)
    #print(formatted_time_statico)

    # Restituisce il numero di commit e il tempo impiegato prima del primo commit che passa il check dinamico e del primo commit che passa il check statico
    return commits_prima_di_passa_dinamico, commits_prima_di_passa_statico, formatted_time_dinamico, formatted_time_statico



def get_slug(title):
    ris = collection.find({"title" : title})   # Risultati della query
    for r in ris:
        slug = r.get("slug")

    return slug



def get_passing(title, file_list):
    ''' Funzione che restituisce il numero di studenti che hanno passato l'esercitazione '''
    ris = collection.find({"title" : title})   # Risultati della query
    for r in ris:
        passing = r.get("passing")

    accepted = collection2.count_documents({"title" : title})   # Numero di studenti che hanno consegnato l'esercitazione

    commits = []
    author = ""
    num = 0

    for file in file_list:
        res = collection4.find({"title": title, "files": {"$regex": file}})   # Risultati della query
        for r in res:
            # Aggiorna la data dell'ultimo commit per lo studente
            if r.get("author") != author:
                author = r.get("author")
                num += 1

        commits.append(num)
        num = 0

    return passing, accepted, commits


if __name__ == "__main__":
    
    # region Inizializzo DB
    # Connessione al client MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Accesso al database (creato se non esiste)
    db = client["tesi2"]

    # Accesso a una collezione (creata se non esiste)
    collection = db["assignments"]
    collection2 = db["repos"]
    collection4 = db["commits2"]
    collection6 = db["commitsCompletati"]
    # endregion

    # region input
    try:
        testo = sys.argv[1] # Nome dell'esercitazione di cui si vogliono ottenere le informazioni ottenuto come argomento da linea di comando
    except IndexError:
        print("Specificare il nome dell'esercitazione di cui si vogliono ottenere le informazioni")
    # endregion

    
    # Crea un nuovo workbook (file Excel)
    wb = Workbook()

    # Seleziona il foglio attivo
    sheet = wb.active

    td = [] # Lista per memorizzare le differenze di tempo per studente
    num_c = [] # Lista per memorizzare il numero di commit per studente
    # Chiama la funzione info_ese per ottenere informazioni sull'esercitazione
    title, nuova_lista = info_ese(testo.capitalize(), collection, collection4, sheet, td, num_c)    # Restituisce il titolo dell'esercitazione e la lista di esercizi nell'esercitazione
    
    slug = get_slug(title)  # Restituisce lo slug dell'esercitazione (es.: esercitazione-1-semafori) utile per la ricerca nel file feedback.md
    
    risultati = []  # Lista per memorizzare i risultati finali dei check per ogni esercizio
    # Chiama la funzione perEs per ottenere informazioni su ogni esercizio
    file_list, risultati = perEs(title, nuova_lista, collection4, sheet, slug, td, num_c)
    
    #   GRAFICO CHECK PER ESERCIZIO A BARRE
    grafici.grafico_check_statici_2(title, risultati)

    partecipanti = [] # Lista per memorizzare il numero di studenti che partecipano all'esercitazione
    passing, accepted, partecipanti = get_passing(title, nuova_lista)

    #print("file_list: ", file_list) 
    #print("risultati_finali: ", risultati)

    commits_prima_di_passa_dinamico = []
    commits_prima_di_passa_statico = []
    tf_passa_dinamico = []
    tf_passa_statico = []
    for file in file_list:
        cd, cs, tf_d, tf_s = count_commits(title, file)
        commits_prima_di_passa_dinamico.append(cd)
        commits_prima_di_passa_statico.append(cs)
        tf_passa_dinamico.append(tf_d)
        tf_passa_statico.append(tf_s)

    #print("commits_prima_di_passa_dinamico: ", commits_prima_di_passa_dinamico)
    #print("commits_prima_di_passa_statico: ", commits_prima_di_passa_statico)
    #print("tf_passa_dinamico: ", tf_passa_dinamico)
    #print("tf_passa_statico: ", tf_passa_statico)

    #grafici.num_commits_prima_di_dinamico(title, file_list, commits_prima_di_passa_dinamico)
    #grafici.num_commits_prima_di_statico(title, file_list, commits_prima_di_passa_statico)
    #grafici.tempo_prima_di_dinamico(title, file_list, tf_passa_dinamico)
    #grafici.tempo_prima_di_statico(title, file_list, tf_passa_statico)

    #   GRAFICO PRODUTTIVITA PER ESERCIZIO E GRAFICO ESERCIZI COMPLETATI
    grafici.box_plot(title, td, file_list, passing, accepted, partecipanti)

    #   GRAFICO COMMIT PER ESERCIZIO
    grafici.box_plot_commit(title, num_c, file_list)

    style_sheet(sheet, len(nuova_lista))

    # Salva il file Excel
    wb.save(testo+'.xlsx')