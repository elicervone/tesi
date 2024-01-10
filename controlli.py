### FUNZIONI UTILIZZATE PER CONTROLLARE SE ALCUNI ELEMENTI SONO GIà PRESENTI NEL DB ###

def controlloAssignment(id, accepted, submissions, passing, collection):
    ''' Funzione che controlla se un assignment è già presente nel DB '''

    query = {"id" : id, "accepted" : accepted, "submissions" : submissions, "passing" : passing}
    ris = collection.find_one(query)

    # Se l'assignment è già presente nel DB, ritorna True
    if ris is not None:
        return True
    else:
        return False

def controlloRepo(repo, collection):
    ''' Funzione che controlla se una repository è già presente nel DB '''
    query = {"repo" : repo}
    ris = collection.find_one(query)

    # Se la repository è già presente nel DB, ritorna True
    if ris is not None:
        return True
    else:
        return False
    
def controlloCommit(sha, collection):
    ''' Funzione che controlla se un commit è già presente nel DB '''

    query = {"sha" : sha}
    ris = collection.find_one(query)

    # Se il commit è già presente nel DB, ritorna True
    if ris is not None:
        return True
    else:
        return False
    

