import requests

def codeScanningInfo(token, repos):
        
    i = 1   #DEBUG
    for repo in repos:

        owner = "so-unina-sangiovanni"
        # Nome della repository specifica per cui si desidera ottenere informazioni sui relativi commit
        split_result = repo.split("-")
        rep = "-".join(split_result[1:])
        #print(rep) #DEBUG

        url = f'https://api.github.com/repos/{owner}/{rep}/code-scanning/alerts'    # Endpoint per ottenere le informazioni da code scanning

        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json, application/vnd.github.vixen-preview+json'
        }

        # Fai la richiesta GET per ottenere i dettagli del commit
        response = requests.get(url, headers=headers)

        # Controlla la risposta
        if response.status_code // 100 == 2:
            code_scan = response.json()
            
            for c in code_scan:
                print(i)    #DEBUG
                i += 1    #DEBUG

                print(c)    # Stampo il contenuto del code scan per sapere quali informazioni sono disponibili      

        else:
            print(f"Errore: {response.status_code} - {response.text}")
            
