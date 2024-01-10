I file necessari per ottenere informazioni riguardanti i check statici sono *mainAPI* e *code_scanning*. La funzione che si occupa di ottenere le informazioni è *codeScanningInfo*. Si trova in un file separato rispetto alle altre funzioni perché ancora non funziona correttamente.
In generale, il file *mainAPI* si occupa di ottenere le informazioni riguardanti le esercitaizoni dall'API di GitHub per poi salvarle nel DB. Ogni funzione nel file si occupa di prelevare diversi tipi di informazioni.
Siccome per effettuare le richieste GET si impiega molto tempo (qualche minuto a richiesta, per alcune anche una decina di minuti), visto l'elevato numero di richieste da effettuare, 
ho commentato tutte le funzioni che non ottengono informazioni necessarie per effettuare la GET a code scanning.

Per testare anche le altre funzioni basta solo rimuovere il commento. Bisogna fare attenzione al limite massimo di richieste che si possono fare all'API di GitHub, che dovrebbe essere di 1000 richieste all'ora per repository. Alcune funzioni presentano una sleep per evitare di superare il limite massimo di richieste. Altre non hanno la sleep al loro interno per non rallentare troppo il programma. Per questo motivo e per evitare che il programma impieghi troppo tempo ad eseguire tutte le richieste, se si desidera testare anche le altre funzioni potrebbe essere utile commentare funzioni che restituiscono informazioni che sono già state salvate nel DB. In ogni caso, il programma presenta dei controlli per evitare di salvare più volte le stesse informazioni nel DB.

Le varie funzioni dovrebbero stampare il numero di richiesta che si sta effettuando. Questo è utile per capire se il programma si è bloccato o meno. A volte può capitare che per qualche secondo non venga stampato nulla perché la richiesta è ancora in corso. In questo caso basta aspettare qualche secondo e dovrebbe riprendere a stampare il numero della richiesta.

Il file *mainDB* si occupa di elaborare le informazioni salvate precedentemente nel DB per conoscere l'andamento delle esercitazioni. Non è necessaria per ottenere le informazioni da code scanning. In ogni caso, se si desidera testare anche le funzioni presenti in questo file, bisogna eseguire prima il file *mainAPI* per salvare le informazioni nel DB e poi eseguire il file *mainDB* per elaborare le informazioni. Se il file *mainAPI* è già stato eseguito, bisogna solo eseguire il file *mainDB* poiché in questo caso le informazioni sono già presenti nel DB e non è quindi necessario recuperarle nuovamente dall'API soprattutto per evitare di perdere molto tempo con le varie richiesete GET.

Per eseguire il file *mainDB* bisogna specificare l'esercitazione per la quale si desidera ottenere le informazioni: 
    - semafori -> esercitazione 1
    - monitor -> esercitazione 2
    - threads -> esercitazione 3
    - messaggi -> esercitazione 4
    - server -> esercitazione 5

Quando si esegue il file *mainDB*, non viene stampato nulla a video, ma viene creato direttamente il file excel con le informazioni utili. Il file viene salvato nella cartella del progetto. Il nome del file è "esercitazione.xlsx" dove "esercitazione" è il nome dell'esercitazione specificato come argomento quando si esegue il file *mainDB*.

Per quanto riguarda i check statici e code scanning:

L'endpoint verso cui effettuare la richiesta GET è https://api.github.com/repos/{owner}/{repo}/code-scanning/alerts

Non so ancora come usare le informazioni ottenute da code scanning perché non ho avuto modo di capire quali sono, per via dell'errore 403. Per ora ho solo stampato il contenuto della risposta per capire quali informazioni sono disponibili. In ogni caso, dal sito di GitHub ho trovato che: "Code scanning is a feature that you use to analyze the code in a GitHub repository to find security vulnerabilities and coding errors. Any problems identified by the analysis are shown in GitHub. [...] If code scanning finds a potential vulnerability or error in your code, GitHub displays an alert in the repository. After you fix the code that triggered the alert, GitHub closes the alert."


# Errore che ottengo quando provo ad usare code scanning:
Errore: 403 - {"message":"Advanced Security must be enabled for this repository to use code scanning.", 
"documentation_url":"https://docs.github.com/rest/code-scanning/code-scanning#list-code-scanning-alerts-for-a-repository"}

