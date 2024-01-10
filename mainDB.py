import pymongo, sys
from datetime import datetime, timedelta
from openpyxl import Workbook
from style import *
from writeExcel import *


def info_ese(testo, collection, collection4, sheet):
    ''' Funzione che stampa le informazioni relative all'esercitazione passata come argomento '''
    
    ris = collection.find({})   # Risultati della query
    title = ""

    for r in ris:
        # Ottiene i dati dell'esercitazione
        query = {"Title" : r.get("title"), "Accepted" : str(r.get("accepted")), "Submissions" : str(r.get("submissions")), "Passing" : str(r.get("passing")), "Files" : str(r.get("files"))}

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
    med = media(title, collection4, totale, sheet)  # Numero medio di commit per studente

    agg, rim = lineeCodice(title, collection4)  # Numero medio di righe aggiunte e rimosse per studente

    # Scrive le informazioni riguardo l'esercitazione sul file excel
    current_row = write_to_sheet(sheet, "Numero totale di commit", totale,
                                "Numero di commit medio per studente", med,
                                "Numero medio di righe aggiunte ad ogni commit per studente", agg, 
                                "Numero medio di righe rimosse ad ogni commit per studente", rim, current_row)

    produttivita(title, collection4, sheet, current_row+1)  # Tempo medio impiegato da ogni studente per svolgere l'esercitazione
    
    # Restituisce il titolo dell'esercitazione e la lista dei file dell'esercitazione
    return title, nuova_lista


def media(title, collection4, totale, sheet):
    ''' Funzione che calcola il numero medio di commit per studente '''

    ris = collection4.find({"title" : title})    # Risultati della query
    authors = {}  # Dizionario per tenere traccia dei commit per ogni autore

    for r in ris:
        author = r.get("author")    # Autore del commit

        # Controlla se l'autore è già nel dizionario authors. Se sì, ottiene il numero di commit effettuati dall'autore finora, altrimenti imposta il valore a 0.
        authors[author] = authors.get(author, 0) + 1  # Incrementa il conteggio dei commit per l'autore

    num_authors = len(authors)  # Numero di autori unici

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
    
    # Calcola e restituisce la media delle righe aggiunte e rimosse dividendo il totale delle righe per il numero di autori unici
    return agg_tot/len(authors), rim_tot/len(authors)
    

def produttivita(title, collection4, sheet, current_row):
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

    # Itera attraverso il dizionario dei commit per studente
    for author, commit_info in commit_dates.items():
            last_commit_date = commit_info["last_commit_date"]
            initial_commit_date = commit_info["initial_commit_date"]

            time_difference = last_commit_date - initial_commit_date    # Differenza di tempo tra l'ultimo commit e il clone della repository
            time_differences.append(time_difference)

    # Calcola la somma delle differenze di tempo
    total_diff = sum(time_differences, timedelta())

    # Calcola la media delle differenze di tempo per studente se la lista non è vuota, altrimenti imposta la media a 0
    average_time_differences = total_diff / len(time_differences) if time_differences else timedelta(seconds=0)
    
    # Scrive le informazioni riguardo l'esercitazione sul file excel
    sheet[f"A{current_row}"] = "Tempo impiegato in media da ogni studente per svolgere l'esercitazione"
    sheet[f"B{current_row}"] = formatta_data(average_time_differences)


def perEs(title, file_list, collection4, sheet):
    ''' Funzione che stampa le informazioni relative ad ogni esercizio dell'esercitazione passata come argomento '''

    current_row = 12 # Riparte dalla riga 12 nel file excel

    for f in file_list:
        current_row += 2

        file = f
        sheet[f"A{current_row}"] = file # Scrive il nome dell'esercizio sul file excel
        current_row += 1

        totale = collection4.count_documents({"title" : title, "files": {"$regex": file}})  # Numero totale di commit per l'esercizio

        media = media_perEs(title, file, collection4, totale)  # Numero medio di commit per studente

        agg_tot, rim_tot = linee_codice_perEs(title, file, collection4) # Numero medio di righe aggiunte e rimosse per studente

        # Scrive le informazioni riguardo l'esercizio sul file excel
        current_row = write_to_sheet(sheet, "Numero totale di commit", totale,
                                    "Numero di commit medio per studente", media,
                                    "Numero medio di righe aggiunte ad ogni commit per studente", agg_tot,
                                    "Numero medio di righe rimosse ad ogni commit per studente", rim_tot,
                                    current_row)

        prodPerEs(title, f, collection4, sheet, current_row)    # Tempo medio impiegato da ogni studente per svolgere l'esercizio


def media_perEs(title, file, collection4, totale):
    ''' Funzione che calcola il numero medio di commit per studente per singolo esercizio'''
    
    # Pipeline usata come filtro nella ricerca nel DB (cerca fra i commit quelli relativi all'esercitazione richiesta
    # e quelli per cui il nome del file modificato contiene il nome dell'esercizio al suo interno)
    pipeline = [
        {"$match": {"title": title, "files": {"$regex": file}}},
        {"$group": {"_id": "$author"}},
        {"$group": {"_id": None, "count": {"$sum": 1}}} # Conta il numero di autori unici
    ]

    result = collection4.aggregate(pipeline)    # Risultati della query

    for doc in result:
        num_studenti = doc['count'] # Numero di autori unici

    return totale/num_studenti # Numero medio di commit per studente


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

    # Calcola e restituisce la media delle righe aggiunte e rimosse dividendo il totale delle righe per il numero di autori unici
    return agg_tot/len(authors), rim_tot/len(authors)


def prodPerEs(title, file, collection4, sheet, current_row):
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

    title, nuova_lista = info_ese(testo.capitalize(), collection, collection4, sheet)
    perEs(title, nuova_lista, collection4, sheet)

    style_sheet(sheet, len(nuova_lista))

    # Salva il file Excel
    wb.save(testo+'.xlsx')

    