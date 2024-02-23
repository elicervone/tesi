# tesi
per ogni esercitazione
	- numero di studenti
	- numero di commit (totale, medio per studente)
	- numero di commit falliti/corretti
	- numero di linee di codice di ogni commit (totale, medio per studente)

1) efficacia test statici
	- quanti commit passano la compilazione, passano l'esecuzione, ma non i check statici
	- quante volte ogni studente prova a fare commit
 
2) produttività dello studente
	- quanto tempo trascorre fra il primo clone (data creazione pull request) e primo commit, e
	poi al primo commit che funziona (per 1° esercizio, poi il 2° etc.)
 
3) quanto sono efficaci i check statici
	- verificare manualmente gli svolgimenti e capire se ci sono stati in cui i check NON hanno
	trovato un problema (a campione, da fare più avanti)

	- per ogni progetto
	per ogni commit del progetto
		copiare in .test una versione dello script senza analisi statica (commenta la linea static_analsys)
		concludiamo se il programma passa i check dinamici
		copiare in .test la versione originale dello script (con static_analysis)
		concludiamo se il programma passa anche i check statici
 
4) feedback è utile agli studenti?
	- sondaggio, oppure segnalazioni dagli studenti (da fare più avanti)


https://docs.github.com/en/rest/overview/endpoints-available-for-github-app-user-access-tokens?apiVersion=2022-11-28



Puoi spiegare anche nella Introduzione che si sono analizzati i dati relativi allo svolgimento di esercizi per il corso di Sistemi Operativi presso Federico II nella sede di San Giovanni
 
pag. 20 -> spiegare prima i check dinamici e poi statici.
 
Per i check dinamici, dire più semplicemente che viene innanzitutto compilato e eseguito il programma, per verificare che non vi siano problemi di compilazione o di esecuzione (es. terminazione anomala del programma, stallo del programma); viene poi controllato l'output del programma per verificare che sia coerente con le richieste (es. un produttore deve prima inserire un dato in un buffer, e poi un consumatore deve prelevare lo stesso dato dal buffer).
 
Per i check statici, dire che vengono fatti controlli più approfonditi che non sarebbero rilevabili guardando solamente l'output del programma, come ad esempio bug di race condition o di gestione del ciclo di vita delle risorse. Inoltre, possono essere fatte delle verifiche su pratiche di cattiva programmazione (anti-pattern) che non impediscono l'esecuzione ma ne peggiorano la qualità. Puoi specificare che i check statici sono eseguiti solo se i check dinamici non rilevano errori.
 
Figura 3.5: è possibile includere anche il numero totale di studenti che partecipano alla esercitazione (hanno creato il repository) o all'esercizio (hanno fatto almeno 1 commit, anche se non hanno necessariamente completato correttamente i check). Puoi inserire una coppia di barre per ogni esercitazione/esercizio
 
Figura 3.6: si riferisce all'insieme di tutti i commit di tutti gli esercitazioni/esercizi? Puoi fare un grafico separando le esercitazioni ed esercizi? Puoi convertirlo in grafico a barre, e includere 3 categorie: nessun check passato, solo check dinamici passati (no statici), tutti check passati (include dinamici e statici)
 
Per ogni esercizione/esercizio, potresti graficare con un boxplot il numero medio di commit che passa tra il primo commit in assoluto, e il primo commit che passa il check dinamico? e poi contare il numero di commit tra il primo commit che passa il check dinamico e il primo commit che passa i check statici?
 
Per i grafici del punto di prima, puoi contare anche il tempo trascorso tra i commit? sempre con un boxplot.
 
In una appendice della tesi, pls riporta tutti i grafici e tabelle per tutte le esercitazioni ed esercizi. Pls salva su github i dati grezzi che hai usato per generare i grafici