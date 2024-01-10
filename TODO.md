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

