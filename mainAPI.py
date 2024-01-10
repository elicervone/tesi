from time import sleep
import requests, pymongo
import controlli
import code_scanning

def getInfoAssignments(collection, headers):
    '''Funzione che ottiene le informazioni di tutte le assegnazioni accettate in una classroom specifica'''
    
    # URL dell'API di GitHub Classroom per ottenere le assegnazioni accettate in una classroom specifica
    url = 'https://api.github.com/classrooms/193019/assignments'

    # Richiesta GET all'endpoint per ottenere le assegnazioni accettate
    response = requests.get(url, headers=headers)

    # Controlla la risposta
    if response.status_code // 100 == 2:
        accepted_assignments = response.json()
        esercitazione = {}  # Dizionario che conterrà i dati di ogni esercitazione

        for assignment in accepted_assignments:

            id = assignment["id"]
            accepted = assignment["accepted"]   # Numero di studenti che hanno accettato l'esercitazione
            submissions = assignment["submissions"]  # Numero di studenti che hanno consegnato l'esercitazione
            passing = assignment["passing"] # Numero di studenti che hanno superato l'esrcitazione
            
            # Se l'esercitazione non è già presente nel DB, la inserisce (Non inserisce l'Esercitazione 0 - Uso di Git)
            if not controlli.controlloAssignment(id, accepted, submissions, passing, collection) and "GIT" not in assignment['title']:
                # Crea il dizionario con i dati dell'esercitazione
                esercitazione = {
                    "id": id,
                    "title": assignment["title"],
                    "slug": assignment["slug"],
                    "accepted": accepted,
                    "submissions": submissions,
                    "passing": passing,
                }
                
                # Inserisce l'esercitazione nel DB
                ins = collection.insert_one(esercitazione)
                #print(ins)  #DEBUG

    else:
        print(f"Errore: {response.status_code} - {response.text}")


def getRepos(collection2, assignments, headers):
    '''Funzione che ottiene i nomi dei repository di ogni studente'''

    for assignment in assignments:
        # ID dell'esercitazione specifica che si desidera ottenere
        assignment_id = assignment.split("-")[1]
        assignment_title = assignment.split("-")[0]

        # URL dell'API di GitHub Classroom per ottenere informazioni su un'esercitazione specifica
        url = f'https://api.github.com/assignments/{assignment_id}/grades'

        # Richiesta GET per ottenere informazioni sull'esercitazione specifica
        response = requests.get(url, headers=headers)
        repository = {} # Dizionario che conterrà i dati di ogni repository
        
        # Controlla la risposta
        if response.status_code // 100 == 2:
            assignment_info = response.json()

            for assignment in assignment_info:
                repo = assignment.get("student_repository_name")    # Nome del repository dello studente

                # Se il repository non è già presente nel DB, lo inserisce
                if not controlli.controlloRepo(repo, collection2):
                    # Crea il dizionario con i dati del repository
                    repository = {
                        "title" : assignment_title, 
                        "repo" : assignment.get("student_repository_name"), 
                        "username" : assignment.get("github_username")
                    }

                    # Inserisce il repository nel DB
                    ins = collection2.insert_one(repository)
                    #print(ins)  #DEBUG
        else:
            print(f"Errore: {response.status_code} - {response.text}")


def numCommit(headers, collection4, repository):
    ''' Funzione che ottiene informazioni sui commit per ogni repository '''
    i=1 #DEBUG
    commit = {} # Dizionario che conterrà i dati di ogni commit
    for repo in repository:
        
        # region GET
        owner = "so-unina-sangiovanni"
        
        # Nome della repository specifica per cui si desidera ottenere informazioni sui relativi commit
        split_result = repo.split("-")
        rep = "-".join(split_result[1:])
        #print(rep)  #DEBUG

        # URL dell'API di GitHub Classroom per ottenere informazioni su una repository specifica
        url = f'https://api.github.com/repos/{owner}/{rep}/commits'

        # Richiesta GET per ottenere informazioni sull'esercitazione specifica
        response = requests.get(url, headers=headers)
        #endregion

        # Controlla la risposta
        if response.status_code // 100 == 2:
            contributors_activity = response.json()

            for con in contributors_activity:
                # Se le informazioni sul commit sono presenti
                if con and con.get("committer") and con.get("commit") and con.get("commit").get("tree"):
                    author_login = con.get("committer").get("login")
                    commit_date = con.get("commit").get("author").get("date")
                    sha = con.get("sha")

                    # Se le informazioni sul commit non sono già presenti nel DB e se il commit non è effettuato dal bot, le inserisce
                    if author_login and commit_date and sha and author_login!="web-flow" and not controlli.controlloCommit(sha, collection4):
                        commit = {
                            "title": repo.split("-")[0],
                            "author": author_login,
                            "date": commit_date,
                            "sha": sha,
                            "repo" : rep
                        }

                        # Inserisce il commit nel DB
                        ins = collection4.insert_one(commit)
                        #print(ins)  #DEBUG
                        print(i)  #DEBUG
                        i += 1  #DEBUG
        else:
            print(f"Errore: {response.status_code} - {response.text}")


def lineePerCommit(headers, collection4, commits):
    i = 1   #DEBUG
    for c in commits:
        # Dettagli del repository e del commit
        owner = "so-unina-sangiovanni"
        commit_sha = c.split("-")[1]    # Identificatore univoco del commit

        # Nome della repository specifica per cui si desidera ottenere informazioni sui relativi commit
        split_result = c.split("-")
        repo = "-".join(split_result[2:])
        #print(repo) #DEBUG

        # URL dell'API di GitHub Classroom per ottenere informazioni su un commit specifico
        url = f'https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}'

        # Richiesta GET per ottenere i dettagli del commit
        response = requests.get(url, headers=headers)

        # Controlla la risposta
        if response.status_code // 100 == 2:
            commit_details = response.json()
            
            # Ottiene i dettagli delle modifiche per ciascun file nel commit
            files = commit_details['files']

            aggiunte = 0
            rimosse = 0
            
            # Ottiene il numero di linee aggiunte e rimosse per ciascun file nel commit
            for file in files:
                aggiunte += file.get('additions')
                rimosse += file.get('deletions')

            # Aggiorna il documento nel DB, in base allo sha del commit utilizzato come filtro  
            filtro = {"sha" : commit_sha}
            collection4.update_one(filtro, {"$set": {"aggiunte": aggiunte, "rimozioni" : rimosse}})
            
            print(i)    #DEBUG
            i+=1    #DEBUG
        else:
            print(f"Errore: {response.status_code} - {response.text}")


def produttivita(collection4, headers, repository):
    ''' Funzione che ottiene la data del clone per ogni repository '''

    i=1 #DEBUG
    for repo in repository:
        
        # region GET
        owner = "so-unina-sangiovanni"
        # Nome della repository specifica per cui si desidera ottenere informazioni sui relativi commit
        split_result = repo.split("-")
        rep = "-".join(split_result[1:])
        #print(rep) #DEBUG

        # URL dell'API di GitHub Classroom per ottenere informazioni su una repository specifica
        url = f'https://api.github.com/repos/{owner}/{rep}/commits'

        # Richiesta GET per ottenere informazioni sulla repository specifica
        response = requests.get(url, headers=headers)
        #endregion

        # Controlla la risposta
        if response.status_code // 100 == 2:
            contributors_activity = response.json()

            for con in contributors_activity:
                # Se le informazioni sul commit sono presenti
                if con and con.get("committer") and con.get("commit") and con.get("commit").get("author"):
                    author = con.get("commit").get("committer").get("name") # Nome dell'autore del commit
                    commit_date = con.get("commit").get("author").get("date")   # Data del commit
                    tree_sha = con.get("sha")   # Identificatore univoco del commit
                    url = con.get("url")    # URL dell'API di GitHub per ottenere i dettagli del commit
                    message = con.get("commit").get("message")  # Messaggio del commit
                    
                    # Se il commit è effettuato dal bot ed è 'Initial commit' (coincide con il clone della repository da parte dello studente), 
                    # inserisce le informazioni nel DB
                    if author and commit_date and tree_sha and author=="GitHub" and message == "Initial commit":
                        # Aggiorna il documento nel DB, aggiungendo la data del clone della repository, 
                        # in base alla repository in cui è effettuato il commit, utilizzata come filtro,
                        # così che sia possibile ottenere la data del clone per ogni repository
                        filtro = {"repo" : rep}
                        collection4.update_many(filtro, {"$set": {"date_initial_commit": commit_date}})
                        print(i)    #DEBUG
                        i += 1  #DEBUG
        else:
            print(f"Errore: {response.status_code} - {response.text}")


def perEsercizio(headers, collection4, commits):
    ''' Funzione che ottiene i nomi dei file modificati per ogni commit '''

    i = 1   #DEBUG
    for c in commits:

        # Dettagli del repository e del commit
        owner = "so-unina-sangiovanni"
        commit_sha = c.split("-")[1]    # Identificatore univoco del commit

        # Nome della repository specifica per cui si desidera ottenere informazioni sui relativi commit
        split_result = c.split("-")
        repo = "-".join(split_result[2:])
        #print(repo) #DEBUG

        # URL dell'API di GitHub Classroom per ottenere informazioni su un commit specifico
        url = f'https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}'

        # Richiesta GET per ottenere i dettagli del commit
        response = requests.get(url, headers=headers)

        # Controlla la risposta
        if response.status_code // 100 == 2:
            commit_details = response.json()
            
            # Ottiene i dettagli delle modifiche per ciascun file nel commit
            files = commit_details['files']
        
            files_list = [] # Lista che conterrà i nomi dei file modificati per ogni commit
            
            for file in files:
                files_list.append(file.get("filename"))
                

            # Aggiorna il documento nel DB, aggiungendo i file modificati per ogni commit, in base allo sha del commit utilizzato come filtro
            filtro = {"sha" : commit_sha}
            collection4.update_one(filtro, {"$set": {"files": files_list}})

            print(i)    #DEBUG
            i+=1    #DEBUG
        else:
            print(f"Errore: {response.status_code} - {response.text}")


def punteggio(headers, collection4, commits):
    ''' Funzione che ottiene il punteggio di ogni commit '''

    i = 1
    for c in commits:

        # Dettagli del repository e del commit
        owner = "so-unina-sangiovanni"
        commit_sha = c.split("-")[1]    # Identificatore univoco del commit

        # Nome della repository specifica per cui si desidera ottenere informazioni sui relativi commit
        split_result = c.split("-")
        repo = "-".join(split_result[2:])
        #print(repo) #DEBUG

        # URL dell'API di GitHub Classroom per ottenere informazioni su un commit specifico
        url = f'https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}/check-runs'

        # Fai la richiesta GET per ottenere i dettagli del commit
        response = requests.get(url, headers=headers)

        # Controlla la risposta
        if response.status_code // 100 == 2:
            commit_details = response.json()
            
            # Se il campo 'check_runs' è presente nella risposta, ottiene il punteggio del commit
            if "check_runs" in commit_details:
                for check_run in commit_details["check_runs"]:
                    print(i)    #DEBUG
                    i += 1  #DEBUG

                    # Se il campo 'output' è presente nella risposta, ottiene il punteggio del commit
                    if "output" in check_run and "Autograding" in check_run['name'] and check_run['pull_requests'] != []:

                        output = check_run["output"]    # Punteggio del commit

                        #author_info = check_run['pull_requests'][0]["head"]["repo"]["name"]    #DEBUG
                        #print(author_info)  #DEBUG
                        #print(output)   #DEBUG
                        
                        # Aggiorna il documento nel DB, aggiungendo il punteggio del commit, in base allo sha del commit utilizzato come filtro
                        filtro = {"sha" : commit_sha}
                        collection4.update_one(filtro, {"$set": {"points": output["text"]}})

                    else:
                        print("Campo 'output' non trovato per questa check run")
            else:
                print("Campo 'check_runs' non trovato nella risposta")
            
        else:
            print(f"Errore: {response.status_code} - {response.text}")
    
        # Esegue la sleep ogni cento iterazioni per non superare il limite massimo di richieste all'API
        if i % 100 == 0:
            sleep(60)


def esercizi(headers, collection, repository, assignments):
    ''' Funzione che aggiunge ad ogni assignment i nomi dei singoli esercizi '''

    i = 1   #DEBUG
    for repo in repository:

        # Dettagli del repository e del commit
        owner = "so-unina-sangiovanni"

        # Nome della repository specifica per cui si desidera ottenere informazioni sui relativi commit
        split_result = repo.split("-")
        rep = "-".join(split_result[1:])
        #print(rep) #DEBUG

        # URL dell'API di GitHub Classroom per ottenere informazioni su una repository specifica
        url = f'https://api.github.com/repos/{owner}/{rep}/contents'

        # Fai la richiesta GET per ottenere i dettagli del commit
        response = requests.get(url, headers=headers)

        # Controlla la risposta
        if response.status_code // 100 == 2:
            commit_details = response.json()
            
            print(i)    #DEBUG
            i+=1    #DEBUG

            file_list = []  # Lista che conterrà i nomi dei singoli esercizi per ogni esercitazione
            title = ""
            url_es = ""

            for commit in commit_details:
                name = commit["name"]   # Nome del file
                url_es = commit["url"]  # URL dell'esercizio

                # Aggiunge alla lista dei file solo i file che sono esercizi e non README o test
                if "git" not in name and "test" not in name and "README" not in name:
                    file_list.append(name)
                                
            # In base al numero dell'esercitazione presente nell'url, ottiene il titolo dell'esercitazione
            # 1 -> semafori, 2-> monitor, 3-> threads, 4-> messaggi, 5-> server multithread
            if "1" in url_es:
                title = assignments[0].split("-")[0]
            elif "2" in url_es:
                title = assignments[1].split("-")[0] 
            elif "3" in url_es:
                title = assignments[2].split("-")[0]    
            elif "4" in url_es:
                title = assignments[3].split("-")[0]    
            elif "5" in url_es:
                title = assignments[4].split("-")[0]
            
            # Cerca l'esercitazione nel DB in base al titolo usato come filtro
            filtro = {"title" : title}
            #print(url_es)   #DEBUG
            #print(title)    #DEBUG
            found_document = collection.find_one(filtro, {"files": 1})

            # Se l'esercitazione è presente nel DB, aggiorna il documento aggiungendo i nomi degli esercizi
            if found_document is not None:
                # Se il campo 'files' non esiste, aggiorna il documento
                if "files" not in found_document:
                    collection.update_one(filtro, {"$set": {"files": file_list}})
                    file_list=[]    # Dopo l'inserimento svuota la lista dei file
                elif len(found_document["files"]) == 0: # Se il campo 'files' esiste ma è vuoto (se non è stato aggiornato corretamente in precedenza), aggiorna il documento
                    collection.update_one(filtro, {"$set": {"files": file_list}})
                    file_list=[]    # Dopo l'inserimento svuota la lista dei file
                else:
                    print("Il campo 'files' esiste già per questo documento.")   
            #print("\n") #DEBUG
            #print("\n") #DEBUG

        else:
            print(f"Errore: {response.status_code} - {response.text}")
            if 'X-RateLimit-Reset' in response.headers: #DEBUG  perché più di una volta ho superato il limite massimo di richieste all'api 
                reset_time = int(response.headers['X-RateLimit-Reset'])
                print(f"Tempo di reset del rate limit: {reset_time}")
            else:
                print("Header 'X-RateLimit-Reset' non presente nella risposta")

        # Aggiungi una sleep ogni 100 richieste per non superare il limite massimo di richieste all'API
        if i % 100 == 0:
            sleep(60)  # Sleep for 60 seconds



def assignmentID(collection):
    ''' Funzione che restituisce una lista di stringhe contenenti il titolo e l'id di ogni assignment '''
    
    assignments = []

    ris = collection.find({})
    for r in ris:
        query = {"title" : r.get("title"), "id" : str(r.get("id"))} # Ottengo il titolo e l'id di ogni assignment
        a = query.get("title")+"-"+query.get("id")
        assignments.append(a)

    # Restituisce una lista di stringhe contenenti il titolo e l'id di ogni assignment
    return assignments


def repos(collection2):
    ''' Funzione che restituisce una lista di stringhe contenenti il titolo e il nome di ogni repository '''

    repos = []

    ris = collection2.find({})
    for r in ris:
        query = {"title" : r.get("title"), "repo" : r.get("repo")}  # Ottengo il titolo e il nome di ogni repository
        a = query.get("title")+"-"+query.get("repo")
        repos.append(a) 

    # Restituisce una lista di stringhe contenenti il titolo e il nome di ogni repository
    return repos


def getCommits(collection4):
    ''' Funzione che restituisce una lista di stringhe contenenti il titolo, lo sha e la repository di ogni commit '''

    commits = []

    ris = collection4.find({})
    for r in ris:
        query = {"title" : r.get("title"), "sha" : r.get("sha"), "repo" : r.get("repo")}    # Ottengo il titolo, lo sha e la repository di ogni commit
        a = query.get("title")+"-"+query.get("sha")+"-"+query.get("repo")
        commits.append(a)

    # Restituisce una lista di stringhe contenenti il titolo, lo sha e la repository di ogni commit 
    return commits



if __name__ == "__main__":
    
    # region Inizializzo DB
    # Connessione al client MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Accesso al database (creato se non esiste)
    db = client["tesi"]

    # Accesso a una collezione (creata se non esiste)
    collection = db["assignments"]
    collection2 = db["repos"]
    collection4 = db["commits"]
    # endregion
        
    # region token e headers http request 
    token = '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'  # Token di accesso all'API di GitHub (con tutti i permessi possibili)

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    #endregion

    getInfoAssignments(collection, headers) 
    assignments = assignmentID(collection) 

    getRepos(collection2, assignments, headers)
    repository = repos(collection2)

    #numCommit(headers, collection4, repository) 
    #commits = getCommits(collection4)
    
    #lineePerCommit(headers, collection4, commits)
    
    #produttivita(collection4, headers, repository)

    #perEsercizio(headers, collection4, commits)
    
    #punteggio(headers, collection4, commits)

    #esercizi(headers, collection, repository, assignments)


    code_scanning.codeScanningInfo(token, repository)

