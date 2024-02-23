
## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-0608dfdf2b1c9a0806b9330b7caa639b6def4a20/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-0608dfdf2b1c9a0806b9330b7caa639b6def4a20/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-amezak1-0608dfdf2b1c9a0806b9330b7caa639b6def4a20/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-amezak1-0608dfdf2b1c9a0806b9330b7caa639b6def4a20/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-amezak1-0608dfdf2b1c9a0806b9330b7caa639b6def4a20/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-1472b2a935c4995b35a61b8b8a8804f38619cf76/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-1472b2a935c4995b35a61b8b8a8804f38619cf76/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-1472b2a935c4995b35a61b8b8a8804f38619cf76/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (buffer.c) :warning:


<i>Il codice dei lettori non è corretto. Per svolgere l'esercizio, è necessario applicare l'algoritmo visto a lezione, basato sui semafori 'MUTEXL' e 'SYNCH', e la variabile condivisa 'NUM_LETTORI'.
</i>
(codice errore: esercitazione-1-semafori-amezak1-1472b2a935c4995b35a61b8b8a8804f38619cf76.lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa..test.lettori-algoritmo-non-corretto)


```
void leggi_buffer(buffer * b, int sem_id, int *val_1, int *val_2) {

    printf("[%d] Inizio lettura\n", getpid());

    /* TBD: Inizio lettura */
    Wait_Sem(sem_id, 0);
    b -> num_lettori++;
    if(b->num_lettori == 1)  Wait_Sem(sem_id, 1);
    Signal_Sem(sem_id, 0);
    printf("[%d] Lettura in corso: val1=%d, val2=%d\n", getpid(), b->val_1, b->val_2);

    sleep(1);

    *val_1 = b->val_1;
    *val_2 = b->val_2;


    printf("[%d] Fine lettura\n", getpid());

    /* TBD: Fine lettura */
    Wait_Sem(sem_id, 0);
    b -> num_lettori--;
    if(b -> num_lettori == 0)  Signal_Sem(sem_id, 1);
    Signal_Sem(sem_id, 0);
}

```



esercitazione-1-semafori-amezak1-1472b2a935c4995b35a61b8b8a8804f38619cf76/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-amezak1-1472b2a935c4995b35a61b8b8a8804f38619cf76/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-14fd4afcb417e08120f1419dd4c0be57efcb8ce0/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-14fd4afcb417e08120f1419dd4c0be57efcb8ce0/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-14fd4afcb417e08120f1419dd4c0be57efcb8ce0/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-14fd4afcb417e08120f1419dd4c0be57efcb8ce0/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-amezak1-14fd4afcb417e08120f1419dd4c0be57efcb8ce0/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-4f9a2c62fc7a5c5914fd751cda8ebb2bcbf542b6/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-4f9a2c62fc7a5c5914fd751cda8ebb2bcbf542b6/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-4f9a2c62fc7a5c5914fd751cda8ebb2bcbf542b6/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-4f9a2c62fc7a5c5914fd751cda8ebb2bcbf542b6/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-4f9a2c62fc7a5c5914fd751cda8ebb2bcbf542b6/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-ae24976d2774885c8bb645e629dd65389be27a8b/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-ae24976d2774885c8bb645e629dd65389be27a8b/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-ae24976d2774885c8bb645e629dd65389be27a8b/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-amezak1-ae24976d2774885c8bb645e629dd65389be27a8b/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-amezak1-ae24976d2774885c8bb645e629dd65389be27a8b/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-amezak1-fec6b801ab0bd181f234701c45e978ae1b2942b1/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-amezak1-fec6b801ab0bd181f234701c45e978ae1b2942b1/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-amezak1-fec6b801ab0bd181f234701c45e978ae1b2942b1/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-amezak1-fec6b801ab0bd181f234701c45e978ae1b2942b1/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-amezak1-fec6b801ab0bd181f234701c45e978ae1b2942b1/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Beccio-san-0be26f37fdeaa5853b38b52ff9013b0b164a2bb6/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Beccio-san-0be26f37fdeaa5853b38b52ff9013b0b164a2bb6/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: È necessario deallocare le risorse IPC al termine della esecuzione :warning:
esercitazione-1-semafori-Beccio-san-0be26f37fdeaa5853b38b52ff9013b0b164a2bb6/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Beccio-san-0be26f37fdeaa5853b38b52ff9013b0b164a2bb6/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: È necessario deallocare le risorse IPC al termine della esecuzione :warning:
esercitazione-1-semafori-Beccio-san-0be26f37fdeaa5853b38b52ff9013b0b164a2bb6/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Beccio-san-527f7e60093a0a52a417147b4b9d8b5e4fc36745/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Beccio-san-527f7e60093a0a52a417147b4b9d8b5e4fc36745/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Beccio-san-527f7e60093a0a52a417147b4b9d8b5e4fc36745/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Beccio-san-527f7e60093a0a52a417147b4b9d8b5e4fc36745/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Beccio-san-527f7e60093a0a52a417147b4b9d8b5e4fc36745/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Beccio-san-64e56a268e49b56bf6130ad20c1df0fe0181b9a1/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Beccio-san-64e56a268e49b56bf6130ad20c1df0fe0181b9a1/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Beccio-san-64e56a268e49b56bf6130ad20c1df0fe0181b9a1/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Beccio-san-64e56a268e49b56bf6130ad20c1df0fe0181b9a1/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Beccio-san-64e56a268e49b56bf6130ad20c1df0fe0181b9a1/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Beccio-san-6fd57855f4f16fcdb8e4b58bb76560f4252f979d/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Beccio-san-6fd57855f4f16fcdb8e4b58bb76560f4252f979d/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Beccio-san-6fd57855f4f16fcdb8e4b58bb76560f4252f979d/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Beccio-san-6fd57855f4f16fcdb8e4b58bb76560f4252f979d/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Beccio-san-6fd57855f4f16fcdb8e4b58bb76560f4252f979d/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-1c499a482e09d50c798337cc3f0450fea3181ca6/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-1c499a482e09d50c798337cc3f0450fea3181ca6/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-1c499a482e09d50c798337cc3f0450fea3181ca6/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-1c499a482e09d50c798337cc3f0450fea3181ca6/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-1c499a482e09d50c798337cc3f0450fea3181ca6/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-2f70e3a6566382d218312fd10079d7a3549b1d90/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-2f70e3a6566382d218312fd10079d7a3549b1d90/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: È necessario deallocare le risorse IPC al termine della esecuzione :warning:
esercitazione-1-semafori-CarmineAprea-2f70e3a6566382d218312fd10079d7a3549b1d90/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-2f70e3a6566382d218312fd10079d7a3549b1d90/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-2f70e3a6566382d218312fd10079d7a3549b1d90/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-7842854c899dd47392da892e55fa1eb62f8cff5b/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-7842854c899dd47392da892e55fa1eb62f8cff5b/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-7842854c899dd47392da892e55fa1eb62f8cff5b/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-7842854c899dd47392da892e55fa1eb62f8cff5b/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-7842854c899dd47392da892e55fa1eb62f8cff5b/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-8aa4af6b9d5d969ce00b76963aab9cd7dcf6eb85/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-8aa4af6b9d5d969ce00b76963aab9cd7dcf6eb85/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main-produttore.c) :warning:


<i>Nei processi figli, non è necessario indicare i permessi in semget(), poiché i permessi sono stati già assegnati al momento della creazione della risorsa da parte del processo padre. È sufficiente passare 0 come terzo parametro.
</i>
(codice errore: esercitazione-1-semafori-CarmineAprea-8aa4af6b9d5d969ce00b76963aab9cd7dcf6eb85.coppia_di_buffer..test.permessi-semget-non-necessari)


```
    sem_id = semget(ftok(".",'c'), 2, 0664);

```



esercitazione-1-semafori-CarmineAprea-8aa4af6b9d5d969ce00b76963aab9cd7dcf6eb85/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-8aa4af6b9d5d969ce00b76963aab9cd7dcf6eb85/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-8aa4af6b9d5d969ce00b76963aab9cd7dcf6eb85/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-9c685c12360984cfdf908e7ed38365829fe385d4/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-9c685c12360984cfdf908e7ed38365829fe385d4/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-9c685c12360984cfdf908e7ed38365829fe385d4/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-9c685c12360984cfdf908e7ed38365829fe385d4/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-9c685c12360984cfdf908e7ed38365829fe385d4/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-a66ac83c576ec0b09e8fc7c1ceed2fe8f7b4a32b/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-a66ac83c576ec0b09e8fc7c1ceed2fe8f7b4a32b/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-a66ac83c576ec0b09e8fc7c1ceed2fe8f7b4a32b/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-a66ac83c576ec0b09e8fc7c1ceed2fe8f7b4a32b/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-1-semafori-CarmineAprea-a66ac83c576ec0b09e8fc7c1ceed2fe8f7b4a32b/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-prod-cons.c) :warning:


<i>Errato utilizzo dei semafori. È necessario che il produttore effettui Wait_Sem() sul semaforo SPAZIO_DISPONIBILE, e Signal_Sem() sul semaforo MESSAGGIO_DISPONIBILE.
</i>
(codice errore: esercitazione-1-semafori-CarmineAprea-d092e5f0b4225ad36d790f82d165ec0f91e3f334.calcolo_parallelo_su_un_vettore_condiviso..test.uso-semafori-produttore)


```
int inizializza_semafori()
{
    int sem_id = semget (IPC_PRIVATE, 2, IPC_CREAT|0664);
                  /* TBD: usare semget() per allocare un vettore,
                  *      con una coppia di semafori */

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    semctl(sem_id,0,SETVAL,0);
    semctl(sem_id,1,SETVAL,1);
    /* TBD: inizializzare i semafori */

    return sem_id;
}

void figlio(int *vettore,
            int *buffer,
            int sem_id,
            int elemento_iniziale,
            int qta_elementi)
{

    printf("[FIGLIO] Ricerca del minimo: elementi da %d a %d\n", elemento_iniziale, elemento_iniziale + qta_elementi - 1);

    /* TBD: aggiungere dentro questa funzione delle chiamate a
     *      Wait_Sem() e Signal_Sem() per realizzare lo schema
     *      produttore-consumatore con buffer singolo */

    int minimo = INT_MAX;

    for (int i = elemento_iniziale; i < elemento_iniziale + qta_elementi; i++)
    {
        if (vettore[i] < minimo)
        {

            minimo = vettore[i];
        }
    }

    printf("[FIGLIO] Il minimo locale è %d\n", minimo);
     
     Wait_Sem(sem_id,0);
    *buffer = minimo;
    Signal_Sem(sem_id,1);
}

```



<i>Errato utilizzo dei semafori. È necessario che il consumatore effettui Wait_Sem() sul semaforo MESSAGGIO_DISPONIBILE, e Signal_Sem() sul semaforo SPAZIO_DISPONIBILE.
</i>
(codice errore: esercitazione-1-semafori-CarmineAprea-d092e5f0b4225ad36d790f82d165ec0f91e3f334.calcolo_parallelo_su_un_vettore_condiviso..test.uso-semafori-consumatore)


```
int inizializza_semafori()
{
    int sem_id = semget (IPC_PRIVATE, 2, IPC_CREAT|0664);
                  /* TBD: usare semget() per allocare un vettore,
                  *      con una coppia di semafori */

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    semctl(sem_id,0,SETVAL,0);
    semctl(sem_id,1,SETVAL,1);
    /* TBD: inizializzare i semafori */

    return sem_id;
}

void figlio(int *vettore,
            int *buffer,
            int sem_id,
            int elemento_iniziale,
            int qta_elementi)
{

    printf("[FIGLIO] Ricerca del minimo: elementi da %d a %d\n", elemento_iniziale, elemento_iniziale + qta_elementi - 1);

    /* TBD: aggiungere dentro questa funzione delle chiamate a
     *      Wait_Sem() e Signal_Sem() per realizzare lo schema
     *      produttore-consumatore con buffer singolo */

    int minimo = INT_MAX;

    for (int i = elemento_iniziale; i < elemento_iniziale + qta_elementi; i++)
    {
        if (vettore[i] < minimo)
        {

            minimo = vettore[i];
        }
    }

    printf("[FIGLIO] Il minimo locale è %d\n", minimo);
     
     Wait_Sem(sem_id,0);
    *buffer = minimo;
    Signal_Sem(sem_id,1);
}

void padre(int *buffer,
           int sem_id)
{

     /* TBD: aggiungere dentro questa funzione delle chiamate a
     *      Wait_Sem() e Signal_Sem() per realizzare lo schema
     *      produttore-consumatore con buffer singolo */

    int minimo = INT_MAX;

    for (int i = 0; i < 10; i++)
    {
        Wait_Sem(sem_id,1);
        if( *buffer < minimo ) {

            minimo = *buffer;
        }
        Signal_Sem(sem_id,0);
        
    }

    /* Attesa terminazione processi figli */
     for (int i=0;i<10;i++){
        wait(NULL);
     }
    /* TBD: Utilizzare wait() per attendere la terminazione dei 10 figli */
    

    /* Risultato finale */

    printf("[PADRE] Il valore minimo assoluto è: %d\n", minimo);
}

```



esercitazione-1-semafori-CarmineAprea-d092e5f0b4225ad36d790f82d165ec0f91e3f334/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-d092e5f0b4225ad36d790f82d165ec0f91e3f334/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-d092e5f0b4225ad36d790f82d165ec0f91e3f334/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-d092e5f0b4225ad36d790f82d165ec0f91e3f334/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-d092e5f0b4225ad36d790f82d165ec0f91e3f334/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-e590b735706188f95b0c311bab699d4a2fc14c6c/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-CarmineAprea-e590b735706188f95b0c311bab699d4a2fc14c6c/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-e590b735706188f95b0c311bab699d4a2fc14c6c/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-e590b735706188f95b0c311bab699d4a2fc14c6c/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-CarmineAprea-e590b735706188f95b0c311bab699d4a2fc14c6c/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-gaetanor-d2bee91348c536a64c8182994ff9f5e5693d1b94/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-gaetanor-d2bee91348c536a64c8182994ff9f5e5693d1b94/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-gaetanor-d2bee91348c536a64c8182994ff9f5e5693d1b94/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-gaetanor-d2bee91348c536a64c8182994ff9f5e5693d1b94/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-gaetanor-d2bee91348c536a64c8182994ff9f5e5693d1b94/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-prod-cons.c) :warning:


<i>Inizializzazione dei semafori mancante o errata. Controllare che la funzione semctl() sia stata utilizzata correttamente.
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-032515146bac90f8d38a5d09abfe779eb60f2695.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semafori-errata)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'd');

    /* TBD: usare semget() per allocare un vettore,
                  *      con una coppia di semafori */
    int sem_id = semget(sem_key, 2, IPC_CREAT | 0664);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    /* TBD: inizializzare i semafori */
    semctl(sem_id, 1, SETVAL, 1);
    semctl(sem_id, 0, SETVAL, 0);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-032515146bac90f8d38a5d09abfe779eb60f2695/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-mutua-esclusione.c) :warning:


<i>La inizializzazione del semaforo con semctl() è errata o mancante. Controllare l'utilizzo corretto di semctl().
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-032515146bac90f8d38a5d09abfe779eb60f2695.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semaforo-mancante)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'c');
    /* TBD: usare semget() per allocare un vettore,
                  *      con un singolo semaforo "mutex" */
    int sem_id = semget(sem_key, 1, IPC_CREAT | 0644);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valore iniziale: 1 (mutua esclusione) */

    /* TBD: inizializzare il mutex */
    semctl(sem_id, 0, SETVAL, 1);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-032515146bac90f8d38a5d09abfe779eb60f2695/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-032515146bac90f8d38a5d09abfe779eb60f2695/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-032515146bac90f8d38a5d09abfe779eb60f2695/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-032515146bac90f8d38a5d09abfe779eb60f2695/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-1d8f55b34532d7a7cee68dbcc8c410a93996a1e0/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-1d8f55b34532d7a7cee68dbcc8c410a93996a1e0/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-1d8f55b34532d7a7cee68dbcc8c410a93996a1e0/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-1d8f55b34532d7a7cee68dbcc8c410a93996a1e0/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-1d8f55b34532d7a7cee68dbcc8c410a93996a1e0/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-prod-cons.c) :warning:


<i>Inizializzazione dei semafori mancante o errata. Controllare che la funzione semctl() sia stata utilizzata correttamente.
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-2d6d857a60344abd502d9d4a52f75425cb1f7bdd.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semafori-errata)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'b');

    /* TBD: usare semget() per allocare un vettore,
                  *      con una coppia di semafori */
    int sem_id = semget(sem_key, 2, IPC_CREAT | 0664);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    /* TBD: inizializzare i semafori */
    semctl(sem_id, 1, SETVAL, 1);
    semctl(sem_id, 0, SETVAL, 0);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-2d6d857a60344abd502d9d4a52f75425cb1f7bdd/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-mutua-esclusione.c) :warning:


<i>La inizializzazione del semaforo con semctl() è errata o mancante. Controllare l'utilizzo corretto di semctl().
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-2d6d857a60344abd502d9d4a52f75425cb1f7bdd.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semaforo-mancante)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'c');
    /* TBD: usare semget() per allocare un vettore,
                  *      con un singolo semaforo "mutex" */
    int sem_id = semget(sem_key, 1, IPC_CREAT | 0644);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valore iniziale: 1 (mutua esclusione) */

    /* TBD: inizializzare il mutex */
    semctl(sem_id, 0, SETVAL, 1);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-2d6d857a60344abd502d9d4a52f75425cb1f7bdd/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-2d6d857a60344abd502d9d4a52f75425cb1f7bdd/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-2d6d857a60344abd502d9d4a52f75425cb1f7bdd/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-2d6d857a60344abd502d9d4a52f75425cb1f7bdd/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-prod-cons.c) :warning:


<i>Inizializzazione dei semafori mancante o errata. Controllare che la funzione semctl() sia stata utilizzata correttamente.
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-35e13d395575db4c69b523c39f7a944f35314c39.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semafori-errata)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'd');

    /* TBD: usare semget() per allocare un vettore,
                  *      con una coppia di semafori */
    int sem_id = semget(sem_key, 2, IPC_CREAT | 0664);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    /* TBD: inizializzare i semafori */
    semctl(sem_id, 1, SETVAL, 1);
    semctl(sem_id, 0, SETVAL, 0);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-35e13d395575db4c69b523c39f7a944f35314c39/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-mutua-esclusione.c) :warning:


<i>La inizializzazione del semaforo con semctl() è errata o mancante. Controllare l'utilizzo corretto di semctl().
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-35e13d395575db4c69b523c39f7a944f35314c39.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semaforo-mancante)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'c');
    /* TBD: usare semget() per allocare un vettore,
                  *      con un singolo semaforo "mutex" */
    int sem_id = semget(sem_key, 1, IPC_CREAT | 0644);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valore iniziale: 1 (mutua esclusione) */

    /* TBD: inizializzare il mutex */
    semctl(sem_id, 0, SETVAL, 1);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-35e13d395575db4c69b523c39f7a944f35314c39/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-35e13d395575db4c69b523c39f7a944f35314c39/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-35e13d395575db4c69b523c39f7a944f35314c39/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-35e13d395575db4c69b523c39f7a944f35314c39/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-prod-cons.c) :warning:


<i>Inizializzazione dei semafori mancante o errata. Controllare che la funzione semctl() sia stata utilizzata correttamente.
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-471f7a24768d42063f048328843fd50cefe0fd30.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semafori-errata)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'b');

    /* TBD: usare semget() per allocare un vettore,
                  *      con una coppia di semafori */
    int sem_id = semget(sem_key, 2, IPC_CREAT | 0664);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    /* TBD: inizializzare i semafori */
    semctl(sem_id, 1, SETVAL, 1);
    semctl(sem_id, 0, SETVAL, 0);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-471f7a24768d42063f048328843fd50cefe0fd30/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-mutua-esclusione.c) :warning:


<i>La inizializzazione del semaforo con semctl() è errata o mancante. Controllare l'utilizzo corretto di semctl().
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-471f7a24768d42063f048328843fd50cefe0fd30.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semaforo-mancante)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'c');
    /* TBD: usare semget() per allocare un vettore,
                  *      con un singolo semaforo "mutex" */
    int sem_id = semget(sem_key, 1, IPC_CREAT | 0644);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valore iniziale: 1 (mutua esclusione) */

    /* TBD: inizializzare il mutex */
    semctl(sem_id, 0, SETVAL, 1);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-471f7a24768d42063f048328843fd50cefe0fd30/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-471f7a24768d42063f048328843fd50cefe0fd30/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-471f7a24768d42063f048328843fd50cefe0fd30/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-471f7a24768d42063f048328843fd50cefe0fd30/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-prod-cons.c) :warning:


<i>Inizializzazione dei semafori mancante o errata. Controllare che la funzione semctl() sia stata utilizzata correttamente.
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-4d030be3b85f5fb4ff0c0f6606899b5bb1d86d39.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semafori-errata)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'b');

    /* TBD: usare semget() per allocare un vettore,
                  *      con una coppia di semafori */
    int sem_id = semget(sem_key, 2, IPC_CREAT | 0664);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    /* TBD: inizializzare i semafori */
    semctl(sem_id, 1, SETVAL, 1);
    semctl(sem_id, 0, SETVAL, 0);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-4d030be3b85f5fb4ff0c0f6606899b5bb1d86d39/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-mutua-esclusione.c) :warning:


<i>La inizializzazione del semaforo con semctl() è errata o mancante. Controllare l'utilizzo corretto di semctl().
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-4d030be3b85f5fb4ff0c0f6606899b5bb1d86d39.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semaforo-mancante)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'c');
    /* TBD: usare semget() per allocare un vettore,
                  *      con un singolo semaforo "mutex" */
    int sem_id = semget(sem_key, 1, IPC_CREAT | 0644);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valore iniziale: 1 (mutua esclusione) */

    /* TBD: inizializzare il mutex */
    semctl(sem_id, 0, SETVAL, 1);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-4d030be3b85f5fb4ff0c0f6606899b5bb1d86d39/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-4d030be3b85f5fb4ff0c0f6606899b5bb1d86d39/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-giuseppe-maglione-4d030be3b85f5fb4ff0c0f6606899b5bb1d86d39/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-4d030be3b85f5fb4ff0c0f6606899b5bb1d86d39/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-prod-cons.c) :warning:


<i>Inizializzazione dei semafori mancante o errata. Controllare che la funzione semctl() sia stata utilizzata correttamente.
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-8ecef15379f2dc2edfaf298304387145552e113f.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semafori-errata)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'b');

    /* TBD: usare semget() per allocare un vettore,
                  *      con una coppia di semafori */
    int sem_id = semget(sem_key, 2, IPC_CREAT | 0644);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    /* TBD: inizializzare i semafori */
    semctl(sem_id, 1, SETVAL, 1);
    semctl(sem_id, 0, SETVAL, 0);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-8ecef15379f2dc2edfaf298304387145552e113f/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-mutua-esclusione.c) :warning:


<i>La inizializzazione del semaforo con semctl() è errata o mancante. Controllare l'utilizzo corretto di semctl().
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-8ecef15379f2dc2edfaf298304387145552e113f.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semaforo-mancante)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'c');
    /* TBD: usare semget() per allocare un vettore,
                  *      con un singolo semaforo "mutex" */
    int sem_id = semget(sem_key, 1, IPC_CREAT | 0644);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valore iniziale: 1 (mutua esclusione) */

    /* TBD: inizializzare il mutex */
    semctl(sem_id, 0, SETVAL, 1);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-8ecef15379f2dc2edfaf298304387145552e113f/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-8ecef15379f2dc2edfaf298304387145552e113f/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-8ecef15379f2dc2edfaf298304387145552e113f/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-8ecef15379f2dc2edfaf298304387145552e113f/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-prod-cons.c) :warning:


<i>Inizializzazione dei semafori mancante o errata. Controllare che la funzione semctl() sia stata utilizzata correttamente.
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-a088893a716b9e3b4ac0d41a66787b1f238fb359.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semafori-errata)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'b');

    /* TBD: usare semget() per allocare un vettore,
                  *      con una coppia di semafori */
    int sem_id = semget(sem_key, 2, IPC_CREAT | 0664);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    /* TBD: inizializzare i semafori */
    semctl(sem_id, 1, SETVAL, 1);
    semctl(sem_id, 0, SETVAL, 0);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-a088893a716b9e3b4ac0d41a66787b1f238fb359/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-mutua-esclusione.c) :warning:


<i>La inizializzazione del semaforo con semctl() è errata o mancante. Controllare l'utilizzo corretto di semctl().
</i>
(codice errore: esercitazione-1-semafori-giuseppe-maglione-a088893a716b9e3b4ac0d41a66787b1f238fb359.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semaforo-mancante)


```
int inizializza_semafori()
{
    key_t sem_key = ftok(".", 'c');
    /* TBD: usare semget() per allocare un vettore,
                  *      con un singolo semaforo "mutex" */
    int sem_id = semget(sem_key, 1, IPC_CREAT | 0644);

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valore iniziale: 1 (mutua esclusione) */

    /* TBD: inizializzare il mutex */
    semctl(sem_id, 0, SETVAL, 1);

    return sem_id;
}

```



esercitazione-1-semafori-giuseppe-maglione-a088893a716b9e3b4ac0d41a66787b1f238fb359/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-a088893a716b9e3b4ac0d41a66787b1f238fb359/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-a088893a716b9e3b4ac0d41a66787b1f238fb359/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-giuseppe-maglione-a088893a716b9e3b4ac0d41a66787b1f238fb359/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-0cf2d065fb964926f3783a7399a2005b1d41828b/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-0cf2d065fb964926f3783a7399a2005b1d41828b/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-0cf2d065fb964926f3783a7399a2005b1d41828b/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-0cf2d065fb964926f3783a7399a2005b1d41828b/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Kekko17-0cf2d065fb964926f3783a7399a2005b1d41828b/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-1aae014738656e301a02b601fc65327a4c261f4d/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-1aae014738656e301a02b601fc65327a4c261f4d/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Kekko17-1aae014738656e301a02b601fc65327a4c261f4d/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Kekko17-1aae014738656e301a02b601fc65327a4c261f4d/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Kekko17-1aae014738656e301a02b601fc65327a4c261f4d/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-632906ba5fe88e38c2d5727968f557a8668f4131/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-632906ba5fe88e38c2d5727968f557a8668f4131/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-632906ba5fe88e38c2d5727968f557a8668f4131/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Kekko17-632906ba5fe88e38c2d5727968f557a8668f4131/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Kekko17-632906ba5fe88e38c2d5727968f557a8668f4131/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-c9da833f3e093c26e91602b83be798b5b646a849/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-c9da833f3e093c26e91602b83be798b5b646a849/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-c9da833f3e093c26e91602b83be798b5b646a849/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-c9da833f3e093c26e91602b83be798b5b646a849/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Kekko17-c9da833f3e093c26e91602b83be798b5b646a849/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-04e9a4de50bbe0e1a934c77abc59fcfab8d18752/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-04e9a4de50bbe0e1a934c77abc59fcfab8d18752/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MariaAnn333-04e9a4de50bbe0e1a934c77abc59fcfab8d18752/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MariaAnn333-04e9a4de50bbe0e1a934c77abc59fcfab8d18752/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MariaAnn333-04e9a4de50bbe0e1a934c77abc59fcfab8d18752/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-12031c96bdcb1f422dc959474ec06c652092c370/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-12031c96bdcb1f422dc959474ec06c652092c370/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-12031c96bdcb1f422dc959474ec06c652092c370/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-12031c96bdcb1f422dc959474ec06c652092c370/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MariaAnn333-12031c96bdcb1f422dc959474ec06c652092c370/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-1541cd311bb5cdcb863e17ca5853c836f12abe0c/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-1541cd311bb5cdcb863e17ca5853c836f12abe0c/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-1541cd311bb5cdcb863e17ca5853c836f12abe0c/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-1541cd311bb5cdcb863e17ca5853c836f12abe0c/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-1541cd311bb5cdcb863e17ca5853c836f12abe0c/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-8489fcfb44d29e66247beb6c15353444212de4a1/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-8489fcfb44d29e66247beb6c15353444212de4a1/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MariaAnn333-8489fcfb44d29e66247beb6c15353444212de4a1/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MariaAnn333-8489fcfb44d29e66247beb6c15353444212de4a1/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MariaAnn333-8489fcfb44d29e66247beb6c15353444212de4a1/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-2292caf249a710a7f8dd9285b06cdb9a49794add/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-2292caf249a710a7f8dd9285b06cdb9a49794add/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-2292caf249a710a7f8dd9285b06cdb9a49794add/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (buffer.c) :warning:


<i>Il codice dei lettori non è corretto. Per svolgere l'esercizio, è necessario applicare l'algoritmo visto a lezione, basato sui semafori 'MUTEXL' e 'SYNCH', e la variabile condivisa 'NUM_LETTORI'.
</i>
(codice errore: esercitazione-1-semafori-MarkCer16-2292caf249a710a7f8dd9285b06cdb9a49794add.lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa..test.lettori-algoritmo-non-corretto)


```
void leggi_buffer(buffer * b, int sem_id, int *val_1, int *val_2) {

    Wait_Sem(sem_id,1);
    Wait_Sem(sem_id,0);
    printf("[%d] Inizio lettura\n", getpid());

    /* TBD: Inizio lettura */

    

    printf("[%d] Lettura in corso: val1=%d, val2=%d\n", getpid(), b->val_1, b->val_2);

    sleep(1);

    *val_1 = b->val_1;
    *val_2 = b->val_2;


    printf("[%d] Fine lettura\n", getpid());

    Signal_Sem(sem_id,1);
    Signal_Sem(sem_id,0);

    /* TBD: Fine lettura */
}

```



esercitazione-1-semafori-MarkCer16-2292caf249a710a7f8dd9285b06cdb9a49794add/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MarkCer16-2292caf249a710a7f8dd9285b06cdb9a49794add/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-29e016a2d1aaeb5e535eb32b8174db9bb62028c9/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-29e016a2d1aaeb5e535eb32b8174db9bb62028c9/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-29e016a2d1aaeb5e535eb32b8174db9bb62028c9/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MarkCer16-29e016a2d1aaeb5e535eb32b8174db9bb62028c9/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MarkCer16-29e016a2d1aaeb5e535eb32b8174db9bb62028c9/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-75552ac43edf266fe875dff5cb15a67cde646d41/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-75552ac43edf266fe875dff5cb15a67cde646d41/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-75552ac43edf266fe875dff5cb15a67cde646d41/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-75552ac43edf266fe875dff5cb15a67cde646d41/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-1-semafori-MarkCer16-75552ac43edf266fe875dff5cb15a67cde646d41/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-872358587460a5e05fd4582685028f58dbd19337/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-872358587460a5e05fd4582685028f58dbd19337/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MarkCer16-872358587460a5e05fd4582685028f58dbd19337/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MarkCer16-872358587460a5e05fd4582685028f58dbd19337/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MarkCer16-872358587460a5e05fd4582685028f58dbd19337/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-8a597a8e6270888c1487cef41ba074d84a903795/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-8a597a8e6270888c1487cef41ba074d84a903795/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-8a597a8e6270888c1487cef41ba074d84a903795/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (buffer.c) :warning:


<i>Il codice dei lettori non è corretto. Per svolgere l'esercizio, è necessario applicare l'algoritmo visto a lezione, basato sui semafori 'MUTEXL' e 'SYNCH', e la variabile condivisa 'NUM_LETTORI'.
</i>
(codice errore: esercitazione-1-semafori-MarkCer16-8a597a8e6270888c1487cef41ba074d84a903795.lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa..test.lettori-algoritmo-non-corretto)


```
void leggi_buffer(buffer * b, int sem_id, int *val_1, int *val_2) {

    Wait_Sem(sem_id,1);
    Wait_Sem(sem_id,0);
    printf("[%d] Inizio lettura\n", getpid());

    /* TBD: Inizio lettura */

    

    printf("[%d] Lettura in corso: val1=%d, val2=%d\n", getpid(), b->val_1, b->val_2);

    sleep(1);

    *val_1 = b->val_1;
    *val_2 = b->val_2;


    printf("[%d] Fine lettura\n", getpid());

    Signal_Sem(sem_id,1);
    Signal_Sem(sem_id,0);

    /* TBD: Fine lettura */
}

```



esercitazione-1-semafori-MarkCer16-8a597a8e6270888c1487cef41ba074d84a903795/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-1-semafori-MarkCer16-8a597a8e6270888c1487cef41ba074d84a903795/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-b1cf24740c83a01a51ca0d2148afe5f2c2ad3c1e/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-b1cf24740c83a01a51ca0d2148afe5f2c2ad3c1e/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-b1cf24740c83a01a51ca0d2148afe5f2c2ad3c1e/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-b1cf24740c83a01a51ca0d2148afe5f2c2ad3c1e/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-b1cf24740c83a01a51ca0d2148afe5f2c2ad3c1e/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-b4256b6f194679c7a6d5c89bee2574f36d5355ff/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-b4256b6f194679c7a6d5c89bee2574f36d5355ff/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-b4256b6f194679c7a6d5c89bee2574f36d5355ff/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (buffer.c) :warning:


<i>Il codice dei lettori non è corretto. Per svolgere l'esercizio, è necessario applicare l'algoritmo visto a lezione, basato sui semafori 'MUTEXL' e 'SYNCH', e la variabile condivisa 'NUM_LETTORI'.
</i>
(codice errore: esercitazione-1-semafori-MarkCer16-b4256b6f194679c7a6d5c89bee2574f36d5355ff.lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa..test.lettori-algoritmo-non-corretto)


```
void leggi_buffer(buffer * b, int sem_id, int *val_1, int *val_2) {

    Wait_Sem(sem_id,1);
    Wait_Sem(sem_id,0);
    printf("[%d] Inizio lettura\n", getpid());

    /* TBD: Inizio lettura */

    

    printf("[%d] Lettura in corso: val1=%d, val2=%d\n", getpid(), b->val_1, b->val_2);

    sleep(1);

    *val_1 = b->val_1;
    *val_2 = b->val_2;


    printf("[%d] Fine lettura\n", getpid());

    Signal_Sem(sem_id,1);
    Signal_Sem(sem_id,0);

    /* TBD: Fine lettura */
}

```



esercitazione-1-semafori-MarkCer16-b4256b6f194679c7a6d5c89bee2574f36d5355ff/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-1-semafori-MarkCer16-b4256b6f194679c7a6d5c89bee2574f36d5355ff/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-bf6c6f5c982038c23f31d2aa9d9b7a86547eca77/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-bf6c6f5c982038c23f31d2aa9d9b7a86547eca77/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-MarkCer16-bf6c6f5c982038c23f31d2aa9d9b7a86547eca77/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (buffer.c) :warning:


<i>Il codice dei lettori non è corretto. Per svolgere l'esercizio, è necessario applicare l'algoritmo visto a lezione, basato sui semafori 'MUTEXL' e 'SYNCH', e la variabile condivisa 'NUM_LETTORI'.
</i>
(codice errore: esercitazione-1-semafori-MarkCer16-bf6c6f5c982038c23f31d2aa9d9b7a86547eca77.lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa..test.lettori-algoritmo-non-corretto)


```
void leggi_buffer(buffer * b, int sem_id, int *val_1, int *val_2) {

    Wait_Sem(sem_id,1);
    Wait_Sem(sem_id,0);
    printf("[%d] Inizio lettura\n", getpid());

    /* TBD: Inizio lettura */

    

    printf("[%d] Lettura in corso: val1=%d, val2=%d\n", getpid(), b->val_1, b->val_2);

    sleep(1);

    *val_1 = b->val_1;
    *val_2 = b->val_2;


    printf("[%d] Fine lettura\n", getpid());

    Signal_Sem(sem_id,1);
    Signal_Sem(sem_id,0);

    /* TBD: Fine lettura */
}

```



esercitazione-1-semafori-MarkCer16-bf6c6f5c982038c23f31d2aa9d9b7a86547eca77/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-MarkCer16-bf6c6f5c982038c23f31d2aa9d9b7a86547eca77/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-666ffed69d89fa6f6e5f1c51ca89c43c543914e2/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-666ffed69d89fa6f6e5f1c51ca89c43c543914e2/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-666ffed69d89fa6f6e5f1c51ca89c43c543914e2/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-1-semafori-martamodio-666ffed69d89fa6f6e5f1c51ca89c43c543914e2/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-martamodio-666ffed69d89fa6f6e5f1c51ca89c43c543914e2/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-715a5c419391322df0cb4a0e531de1e6433665c8/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-715a5c419391322df0cb4a0e531de1e6433665c8/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-715a5c419391322df0cb4a0e531de1e6433665c8/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-1-semafori-martamodio-715a5c419391322df0cb4a0e531de1e6433665c8/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-715a5c419391322df0cb4a0e531de1e6433665c8/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-9f52edec7b7aedc5612d67ecbf1dcc6d12e748aa/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-9f52edec7b7aedc5612d67ecbf1dcc6d12e748aa/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-9f52edec7b7aedc5612d67ecbf1dcc6d12e748aa/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-1-semafori-martamodio-9f52edec7b7aedc5612d67ecbf1dcc6d12e748aa/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-1-semafori-martamodio-9f52edec7b7aedc5612d67ecbf1dcc6d12e748aa/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-9f8eb81102b5a58465a54a6744ef1fc6a6accee9/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-9f8eb81102b5a58465a54a6744ef1fc6a6accee9/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-9f8eb81102b5a58465a54a6744ef1fc6a6accee9/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-martamodio-9f8eb81102b5a58465a54a6744ef1fc6a6accee9/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-martamodio-9f8eb81102b5a58465a54a6744ef1fc6a6accee9/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-b852709c74fd40a201ced25dec1af12ad99badec/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-b852709c74fd40a201ced25dec1af12ad99badec/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-b852709c74fd40a201ced25dec1af12ad99badec/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-1-semafori-martamodio-b852709c74fd40a201ced25dec1af12ad99badec/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-b852709c74fd40a201ced25dec1af12ad99badec/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-c5afd867bd0e35f3d2632ccb35d29545922fd40a/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-c5afd867bd0e35f3d2632ccb35d29545922fd40a/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-martamodio-c5afd867bd0e35f3d2632ccb35d29545922fd40a/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-martamodio-c5afd867bd0e35f3d2632ccb35d29545922fd40a/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-martamodio-c5afd867bd0e35f3d2632ccb35d29545922fd40a/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-f96811f74a10ad53d18f3293b950007fddce82e6/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-f96811f74a10ad53d18f3293b950007fddce82e6/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-f96811f74a10ad53d18f3293b950007fddce82e6/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-f96811f74a10ad53d18f3293b950007fddce82e6/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-martamodio-f96811f74a10ad53d18f3293b950007fddce82e6/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-prod-cons.c) :warning:


<i>Inizializzazione dei semafori mancante o errata. Controllare che la funzione semctl() sia stata utilizzata correttamente.
</i>
(codice errore: esercitazione-1-semafori-Yperr-71eb2f187c3452155d867099b0679d302fd45b57.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semafori-errata)


```
int inizializza_semafori()
{
    key_t chiave_SEM = IPC_PRIVATE;
    int sem_id = semget(chiave_SEM, 2, IPC_CREAT | 0664);
    //FATTO            /* TBD: usare semget() per allocare un vettore,
                      /*      con una coppia di semafori */

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    semctl(sem_id, 1, SETVAL, 1);
    semctl(sem_id, 0, SETVAL, 0);

    /* TBD: inizializzare i semafori */
    //FATT0

    return sem_id;
}

```



esercitazione-1-semafori-Yperr-71eb2f187c3452155d867099b0679d302fd45b57/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-mutua-esclusione.c) :warning:


<i>La inizializzazione del semaforo con semctl() è errata o mancante. Controllare l'utilizzo corretto di semctl().
</i>
(codice errore: esercitazione-1-semafori-Yperr-71eb2f187c3452155d867099b0679d302fd45b57.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semaforo-mancante)


```
int inizializza_semafori()
{
    key_t chiave_SEM_mutex;
    int sem_id = semget(chiave_SEM_mutex, 1, IPC_CREAT | 0664); 
    //Fatto            /* TBD: usare semget() per allocare un vettore,
                    /*      con un singolo semaforo "mutex" */

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valore iniziale: 1 (mutua esclusione) */
    semctl(sem_id, 0, SETVAL, 1);
    //FATTO   /* TBD: inizializzare il mutex */

    return sem_id;
}

```



esercitazione-1-semafori-Yperr-71eb2f187c3452155d867099b0679d302fd45b57/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Yperr-71eb2f187c3452155d867099b0679d302fd45b57/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Yperr-71eb2f187c3452155d867099b0679d302fd45b57/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Yperr-71eb2f187c3452155d867099b0679d302fd45b57/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Yperr-7963d3cc2b3fa82365f2cb7075334d3527587e55/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Yperr-7963d3cc2b3fa82365f2cb7075334d3527587e55/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Yperr-7963d3cc2b3fa82365f2cb7075334d3527587e55/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Yperr-7963d3cc2b3fa82365f2cb7075334d3527587e55/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Yperr-7963d3cc2b3fa82365f2cb7075334d3527587e55/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-prod-cons.c) :warning:


<i>Inizializzazione dei semafori mancante o errata. Controllare che la funzione semctl() sia stata utilizzata correttamente.
</i>
(codice errore: esercitazione-1-semafori-Yperr-bdb377a0ddc648c588b43772224a02d8bef5fb4e.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semafori-errata)


```
int inizializza_semafori()
{
    key_t chiave_SEM = IPC_PRIVATE;
    int sem_id = semget(chiave_SEM, 2, IPC_CREAT | 0664);
    //FATTO            /* TBD: usare semget() per allocare un vettore,
                      /*      con una coppia di semafori */

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    semctl(sem_id, 1, SETVAL, 1);
    semctl(sem_id, 0, SETVAL, 0);

    /* TBD: inizializzare i semafori */
    //FATT0

    return sem_id;
}

```



esercitazione-1-semafori-Yperr-bdb377a0ddc648c588b43772224a02d8bef5fb4e/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-mutua-esclusione.c) :warning:


<i>La inizializzazione del semaforo con semctl() è errata o mancante. Controllare l'utilizzo corretto di semctl().
</i>
(codice errore: esercitazione-1-semafori-Yperr-bdb377a0ddc648c588b43772224a02d8bef5fb4e.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semaforo-mancante)


```
int inizializza_semafori()
{
    key_t chiave_SEM_mutex;
    int sem_id = semget(chiave_SEM_mutex, 1, IPC_CREAT | 0664); 
    //Fatto            /* TBD: usare semget() per allocare un vettore,
                    /*      con un singolo semaforo "mutex" */

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valore iniziale: 1 (mutua esclusione) */
    semctl(sem_id, 0, SETVAL, 1);
    //FATTO   /* TBD: inizializzare il mutex */

    return sem_id;
}

```



esercitazione-1-semafori-Yperr-bdb377a0ddc648c588b43772224a02d8bef5fb4e/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Yperr-bdb377a0ddc648c588b43772224a02d8bef5fb4e/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Yperr-bdb377a0ddc648c588b43772224a02d8bef5fb4e/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Yperr-bdb377a0ddc648c588b43772224a02d8bef5fb4e/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-prod-cons.c) :warning:


<i>Inizializzazione dei semafori mancante o errata. Controllare che la funzione semctl() sia stata utilizzata correttamente.
</i>
(codice errore: esercitazione-1-semafori-Yperr-bdee92bd9bd83ff6b3047329f6b5b6b1569f0faf.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semafori-errata)


```
int inizializza_semafori()
{
    key_t chiave_SEM = IPC_PRIVATE;
    int sem_id = semget(chiave_SEM, 2, IPC_CREAT | 0664);
    //FATTO            /* TBD: usare semget() per allocare un vettore,
                      /*      con una coppia di semafori */

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    semctl(sem_id, 1, SETVAL, 1);
    semctl(sem_id, 0, SETVAL, 0);

    /* TBD: inizializzare i semafori */
    //FATT0

    return sem_id;
}

```



esercitazione-1-semafori-Yperr-bdee92bd9bd83ff6b3047329f6b5b6b1569f0faf/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-mutua-esclusione.c) :warning:


<i>La inizializzazione del semaforo con semctl() è errata o mancante. Controllare l'utilizzo corretto di semctl().
</i>
(codice errore: esercitazione-1-semafori-Yperr-bdee92bd9bd83ff6b3047329f6b5b6b1569f0faf.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semaforo-mancante)


```
int inizializza_semafori()
{
    key_t chiave_SEM_mutex;
    int sem_id = semget(chiave_SEM_mutex, 1, IPC_CREAT | 0664); 
    //Fatto            /* TBD: usare semget() per allocare un vettore,
                    /*      con un singolo semaforo "mutex" */

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valore iniziale: 1 (mutua esclusione) */
    semctl(sem_id, 0, SETVAL, 1);
    //FATTO   /* TBD: inizializzare il mutex */

    return sem_id;
}

```



esercitazione-1-semafori-Yperr-bdee92bd9bd83ff6b3047329f6b5b6b1569f0faf/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Yperr-bdee92bd9bd83ff6b3047329f6b5b6b1569f0faf/coppia_di_buffer

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Yperr-bdee92bd9bd83ff6b3047329f6b5b6b1569f0faf/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Yperr-bdee92bd9bd83ff6b3047329f6b5b6b1569f0faf/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio calcolo parallelo su vettore condiviso, con produttore-consumatore

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-prod-cons.c) :warning:


<i>Inizializzazione dei semafori mancante o errata. Controllare che la funzione semctl() sia stata utilizzata correttamente.
</i>
(codice errore: esercitazione-1-semafori-Yperr-d6d3c0036d56467b766a272e3a769584fa12cc2f.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semafori-errata)


```
int inizializza_semafori()
{
    key_t chiave_SEM = IPC_PRIVATE;
    int sem_id = semget(chiave_SEM, 2, IPC_CREAT | 0664);
    //FATTO            /* TBD: usare semget() per allocare un vettore,
                      /*      con una coppia di semafori */

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valori iniziali: 0 (messaggio disponibile), 1 (spazio disponibile) */

    semctl(sem_id, 1, SETVAL, 1);
    semctl(sem_id, 0, SETVAL, 0);

    /* TBD: inizializzare i semafori */
    //FATT0

    return sem_id;
}

```



esercitazione-1-semafori-Yperr-d6d3c0036d56467b766a272e3a769584fa12cc2f/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio calcolo parallelo su vettore condiviso, con mutua esclusione

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (processi-mutua-esclusione.c) :warning:


<i>La inizializzazione del semaforo con semctl() è errata o mancante. Controllare l'utilizzo corretto di semctl().
</i>
(codice errore: esercitazione-1-semafori-Yperr-d6d3c0036d56467b766a272e3a769584fa12cc2f.calcolo_parallelo_su_un_vettore_condiviso..test.inizializzazione-semaforo-mancante)


```
int inizializza_semafori()
{
    key_t chiave_SEM_mutex;
    int sem_id = semget(chiave_SEM_mutex, 1, IPC_CREAT | 0664); 
    //Fatto            /* TBD: usare semget() per allocare un vettore,
                    /*      con un singolo semaforo "mutex" */

    if (sem_id < 0)
    {
        perror("Impossibile creare il semaforo per la mutua esclusione");
        exit(1);
    }

    /* Valore iniziale: 1 (mutua esclusione) */
    semctl(sem_id, 0, SETVAL, 1);
    //FATTO   /* TBD: inizializzare il mutex */

    return sem_id;
}

```



esercitazione-1-semafori-Yperr-d6d3c0036d56467b766a272e3a769584fa12cc2f/calcolo_parallelo_su_un_vettore_condiviso

## Esercizio coppia di buffer

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Yperr-d6d3c0036d56467b766a272e3a769584fa12cc2f/coppia_di_buffer

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-1-semafori-Yperr-d6d3c0036d56467b766a272e3a769584fa12cc2f/lettori-scrittori_con_semafori_su_una_coppia_di_valori_condivisa

## Esercizio simulazione disco, con semafori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-1-semafori-Yperr-d6d3c0036d56467b766a272e3a769584fa12cc2f/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-alicecapolongo-143b9be12d7b1067a0b2519de444e06a6873125a/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-alicecapolongo-143b9be12d7b1067a0b2519de444e06a6873125a/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-alicecapolongo-143b9be12d7b1067a0b2519de444e06a6873125a/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-alicecapolongo-143b9be12d7b1067a0b2519de444e06a6873125a/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-alicecapolongo-bf577a949150f121642d96adfb4806d3058f54d0/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-alicecapolongo-bf577a949150f121642d96adfb4806d3058f54d0/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-alicecapolongo-bf577a949150f121642d96adfb4806d3058f54d0/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-alicecapolongo-bf577a949150f121642d96adfb4806d3058f54d0/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-alicecapolongo-d6aca37c5f7220d966d0e641e5f505cc7044be94/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-alicecapolongo-d6aca37c5f7220d966d0e641e5f505cc7044be94/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-alicecapolongo-d6aca37c5f7220d966d0e641e5f505cc7044be94/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-alicecapolongo-d6aca37c5f7220d966d0e641e5f505cc7044be94/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-alicecapolongo-e4c3e6d7b810e324e8579e33875950e0cf31ce4b/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-alicecapolongo-e4c3e6d7b810e324e8579e33875950e0cf31ce4b/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-alicecapolongo-e4c3e6d7b810e324e8579e33875950e0cf31ce4b/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-alicecapolongo-e4c3e6d7b810e324e8579e33875950e0cf31ce4b/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-38cb1661c19affe82e5bc403c10c3c94688f6d06/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-amezak1-38cb1661c19affe82e5bc403c10c3c94688f6d06/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-amezak1-38cb1661c19affe82e5bc403c10c3c94688f6d06/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-38cb1661c19affe82e5bc403c10c3c94688f6d06/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-725beb10796b57b42af67422961059fe5d731432/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-725beb10796b57b42af67422961059fe5d731432/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto delle produzioni e delle consumazioni :warning:
esercitazione-2-monitor-amezak1-725beb10796b57b42af67422961059fe5d731432/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-725beb10796b57b42af67422961059fe5d731432/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-aefbe290fcd5ff15221b80bb4567348293bb72e8/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-aefbe290fcd5ff15221b80bb4567348293bb72e8/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-amezak1-aefbe290fcd5ff15221b80bb4567348293bb72e8/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-aefbe290fcd5ff15221b80bb4567348293bb72e8/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-af57e6766cb4583977cb4e2b9b437f76f0ca8de5/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-amezak1-af57e6766cb4583977cb4e2b9b437f76f0ca8de5/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-amezak1-af57e6766cb4583977cb4e2b9b437f76f0ca8de5/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-amezak1-af57e6766cb4583977cb4e2b9b437f76f0ca8de5/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-c50842968a92defffbda561782c2581fbc80a6b5/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-c50842968a92defffbda561782c2581fbc80a6b5/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-c50842968a92defffbda561782c2581fbc80a6b5/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-amezak1-c50842968a92defffbda561782c2581fbc80a6b5/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-annxj-264674ff472b8841a550b105f3f8f6a4cc00216e/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-annxj-264674ff472b8841a550b105f3f8f6a4cc00216e/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-annxj-264674ff472b8841a550b105f3f8f6a4cc00216e/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-annxj-264674ff472b8841a550b105f3f8f6a4cc00216e/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-annxj-3954f505d9a6f552f665facc76c30d97b9e933ed/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-annxj-3954f505d9a6f552f665facc76c30d97b9e933ed/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-annxj-3954f505d9a6f552f665facc76c30d97b9e933ed/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-annxj-3954f505d9a6f552f665facc76c30d97b9e933ed/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-annxj-49168b7ca98a475d327b5e0a6102352a028c00e4/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (prodcons.c) :warning:


<i>La funzione signal_condition va chiamata due volte nel consumatore, perché sono fatte due consumazioni.
</i>
(codice errore: esercitazione-2-monitor-annxj-49168b7ca98a475d327b5e0a6102352a028c00e4.prelievi_multipli..test.signal-due-volte)


```
void consuma(ProdCons * p, int* val_1, int* val_2) {

    /* Ingresso nel monitor */
    enter_monitor(&(p->m));

    printf("[%d] Ingresso consumatore\n", getpid());

    if(p->totale_elementi < 2){ // se non ci sono almeno 2 elementi disponibili nel vettore

        wait_condition(&(p->m), 1); // si sospende il consumatore
    } 

    *val_1 = p->vettore[p->coda];
    p->coda = (p->coda + 1) % 10;
    p->totale_elementi--;

    printf("[%d] Prima consumazione: val_1=%d\n", getpid(), *val_1);

    *val_2 = p->vettore[p->coda];
    p->coda = (p->coda + 1) % 10;
    p->totale_elementi--;

    printf("[%d] Seconda consumazione: val_2=%d\n", getpid(), *val_2);

    /* Effettuare signal_condition() per svegliare 2 produttori 
     * (si sono appena liberati 2 buffer nel vettore) */
    
    signal_condition(&(p->m), 0);

    printf("[%d] Uscita consumatore\n", getpid());

    leave_monitor(&(p->m)); /* Uscita dal monitor */
}

```



esercitazione-2-monitor-annxj-49168b7ca98a475d327b5e0a6102352a028c00e4/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-annxj-49168b7ca98a475d327b5e0a6102352a028c00e4/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-annxj-49168b7ca98a475d327b5e0a6102352a028c00e4/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-annxj-687a35df99c887d909b3c89702bc0bb05ceafdec/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-annxj-687a35df99c887d909b3c89702bc0bb05ceafdec/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-annxj-687a35df99c887d909b3c89702bc0bb05ceafdec/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-annxj-687a35df99c887d909b3c89702bc0bb05ceafdec/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-annxj-b58826acba598b86ea8934d2b587d95b509db06d/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-annxj-b58826acba598b86ea8934d2b587d95b509db06d/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-annxj-b58826acba598b86ea8934d2b587d95b509db06d/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-annxj-b58826acba598b86ea8934d2b587d95b509db06d/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Furbizio-66b58b02eeea71d4fe992b1f4b7c025ad5a750e4/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Furbizio-66b58b02eeea71d4fe992b1f4b7c025ad5a750e4/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Furbizio-66b58b02eeea71d4fe992b1f4b7c025ad5a750e4/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Furbizio-66b58b02eeea71d4fe992b1f4b7c025ad5a750e4/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Furbizio-6e1b66b996485890394770439343d6e18cd46806/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Furbizio-6e1b66b996485890394770439343d6e18cd46806/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Furbizio-6e1b66b996485890394770439343d6e18cd46806/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Furbizio-6e1b66b996485890394770439343d6e18cd46806/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Furbizio-70f2437b058b00c04a6978b06041c4a3ff36d16d/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Furbizio-70f2437b058b00c04a6978b06041c4a3ff36d16d/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Furbizio-70f2437b058b00c04a6978b06041c4a3ff36d16d/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Furbizio-70f2437b058b00c04a6978b06041c4a3ff36d16d/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Furbizio-997e85f3361478741f025b6108b12a8b9d231eb0/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Furbizio-997e85f3361478741f025b6108b12a8b9d231eb0/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Furbizio-997e85f3361478741f025b6108b12a8b9d231eb0/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Furbizio-997e85f3361478741f025b6108b12a8b9d231eb0/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-gabriele-brancale-f3be64244eb64c316eb70c3e13f4fb61c4401701/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-gabriele-brancale-f3be64244eb64c316eb70c3e13f4fb61c4401701/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-gabriele-brancale-f3be64244eb64c316eb70c3e13f4fb61c4401701/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-gabriele-brancale-f3be64244eb64c316eb70c3e13f4fb61c4401701/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-67de004e1c3f0d8199267e09d4966d8ebc8f5f72/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-67de004e1c3f0d8199267e09d4966d8ebc8f5f72/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-GiuseppeFus-67de004e1c3f0d8199267e09d4966d8ebc8f5f72/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-GiuseppeFus-67de004e1c3f0d8199267e09d4966d8ebc8f5f72/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-793c31b42b2ae119e89d333a1bd939ac6889ce78/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-793c31b42b2ae119e89d333a1bd939ac6889ce78/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-793c31b42b2ae119e89d333a1bd939ac6889ce78/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-GiuseppeFus-793c31b42b2ae119e89d333a1bd939ac6889ce78/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-8f7bcc01a790926315ccd7d32593acbff6f56a69/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: È necessario deallocare le risorse IPC al termine della esecuzione :warning:
esercitazione-2-monitor-GiuseppeFus-8f7bcc01a790926315ccd7d32593acbff6f56a69/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-GiuseppeFus-8f7bcc01a790926315ccd7d32593acbff6f56a69/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-GiuseppeFus-8f7bcc01a790926315ccd7d32593acbff6f56a69/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-9ca0e938feabdb17b4415557a09f3315486d5516/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-9ca0e938feabdb17b4415557a09f3315486d5516/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-9ca0e938feabdb17b4415557a09f3315486d5516/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-9ca0e938feabdb17b4415557a09f3315486d5516/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-c2dd773c9d9806a05ab3e6432e99fb3756b99384/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-2-monitor-GiuseppeFus-c2dd773c9d9806a05ab3e6432e99fb3756b99384/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-GiuseppeFus-c2dd773c9d9806a05ab3e6432e99fb3756b99384/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-GiuseppeFus-c2dd773c9d9806a05ab3e6432e99fb3756b99384/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-ee0a3798e6c3e18b55db9a6dbd53556cb2a74c82/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-2-monitor-GiuseppeFus-ee0a3798e6c3e18b55db9a6dbd53556cb2a74c82/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-GiuseppeFus-ee0a3798e6c3e18b55db9a6dbd53556cb2a74c82/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-GiuseppeFus-ee0a3798e6c3e18b55db9a6dbd53556cb2a74c82/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-GiuseppeFus-f65383aeae153909f413b2ec1c86013f4faf3bb9/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-GiuseppeFus-f65383aeae153909f413b2ec1c86013f4faf3bb9/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-GiuseppeFus-f65383aeae153909f413b2ec1c86013f4faf3bb9/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-GiuseppeFus-f65383aeae153909f413b2ec1c86013f4faf3bb9/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-1179d64286caa19735d5330e3aed24c2f6a4ffab/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-1179d64286caa19735d5330e3aed24c2f6a4ffab/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-1179d64286caa19735d5330e3aed24c2f6a4ffab/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-1179d64286caa19735d5330e3aed24c2f6a4ffab/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-2523c413b4addf80ad3ff3205778251849f64c6d/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-2523c413b4addf80ad3ff3205778251849f64c6d/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (procedure.c) :warning:


<i>Controllare l'inizializazione delle variabili. Assicurarsi di aver inizializzato TUTTE le variabili della struttura. Le variabile che si consiglia di inizializzare sono: testa, coda, count, num_produttori_alta_prio.
</i>
(codice errore: esercitazione-2-monitor-P0l1702-2523c413b4addf80ad3ff3205778251849f64c6d.produttore-consumatore_con_priorita..test.inizializzazione-struct-priority-prod-cons)


```
void inizializza_prod_cons(PriorityProdCons *p)
{

	/* TBD: Inizializzare le variabili della struttura (testa, coda, ...) */
	p->testa = 0;
	p->coda = 0;
	p->count = 0;
	/* TBD: Inizializzare il sotto-oggetto "Monitor", chiamando init_monitor(...).
			Scegliere accuratamente il numero di variabili condition */
	init_monitor(&(p->m), 3);
}

```



esercitazione-2-monitor-P0l1702-2523c413b4addf80ad3ff3205778251849f64c6d/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-2-monitor-P0l1702-2523c413b4addf80ad3ff3205778251849f64c6d/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-3f20a4cb65d42f1c02b2b796baba7e958bf42d7c/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-3f20a4cb65d42f1c02b2b796baba7e958bf42d7c/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-P0l1702-3f20a4cb65d42f1c02b2b796baba7e958bf42d7c/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-3f20a4cb65d42f1c02b2b796baba7e958bf42d7c/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-P0l1702-6eae1a91968d66c49e97b692ca9b8f8a11fbe8b5/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-6eae1a91968d66c49e97b692ca9b8f8a11fbe8b5/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-P0l1702-6eae1a91968d66c49e97b692ca9b8f8a11fbe8b5/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-6eae1a91968d66c49e97b692ca9b8f8a11fbe8b5/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-a088eceed10269e1bf275339371878390ab35c16/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-a088eceed10269e1bf275339371878390ab35c16/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (procedure.c) :warning:


<i>Controllare l'inizializazione delle variabili. Assicurarsi di aver inizializzato TUTTE le variabili della struttura. Le variabile che si consiglia di inizializzare sono: testa, coda, count, num_produttori_alta_prio.
</i>
(codice errore: esercitazione-2-monitor-P0l1702-a088eceed10269e1bf275339371878390ab35c16.produttore-consumatore_con_priorita..test.inizializzazione-struct-priority-prod-cons)


```
void inizializza_prod_cons(PriorityProdCons *p)
{

	/* TBD: Inizializzare le variabili della struttura (testa, coda, ...) */
	p->testa = 0;
	p->coda = 0;
	p->count = 0;
	/* TBD: Inizializzare il sotto-oggetto "Monitor", chiamando init_monitor(...).
			Scegliere accuratamente il numero di variabili condition */
	init_monitor(&(p->m), 3);
}

```



<i>È un monitor signal and continue, è necessario un ciclo
</i>
(codice errore: esercitazione-2-monitor-P0l1702-a088eceed10269e1bf275339371878390ab35c16.produttore-consumatore_con_priorita..test.monitor-signal-continue-ciclo)


```
	enter_monitor(&(p->m));

	/* TBD: Effettuare l'ingresso nel monitor */

	printf("Produttore tipo 1 con pid %d accede al monitor\n", getpid());

	/* TBD: Sospendere qui il processo se il vettore di buffer è pieno */
	if (p->count == 3)
	{
		wait_condition(&(p->m), 0);
	}

	// Produzione

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 1 con pid %d ha prodotto %d\n", getpid(), value);

	/* TBD: Effettuare la signal_condition per i consumatori in attesa */
	signal_condition(&(p->m), 2);

	/* TBD: Uscire dal monitor */
	leave_monitor(&(p->m));

```



<i>È un monitor signal and continue, è necessario un ciclo
</i>
(codice errore: esercitazione-2-monitor-P0l1702-a088eceed10269e1bf275339371878390ab35c16.produttore-consumatore_con_priorita..test.monitor-signal-continue-ciclo)


```
	enter_monitor(&(p->m));

	printf("Produttore tipo 2 con pid %d accede al monitor\n", getpid());

	/* TBD: Sospendere qui il processo nei seguenti due possibili casi:
	 *      1) Il vettore di buffer è pieno; oppure
	 *      2) Un produttore ad alta priorità è già sospeso in attesa.
	 *         Si suggerisce di usare queue_condition() oppure una variabile
	 *         intera "num_lettori_alta_priorita", vedi suggerimenti nel
	 *         commento della funzione consuma().
	 */
	if (p->count == 3 || queue_condition(&(p->m), 0) > 0)
	{
		wait_condition(&(p->m), 1);
	}

	// Produzione

	value = 13 + (rand() % 12);

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 2 con pid %d ha prodotto %d\n", getpid(), value);

	/* TBD: Effettuare la signal_condition per i consumatori in attesa */
	signal_condition(&(p->m), 2);
	leave_monitor(&(p->m));

```



<i>È un monitor signal and continue, è necessario un ciclo
</i>
(codice errore: esercitazione-2-monitor-P0l1702-a088eceed10269e1bf275339371878390ab35c16.produttore-consumatore_con_priorita..test.monitor-signal-continue-ciclo)


```
	enter_monitor(&(p->m));

	printf("Consumatore con pid %d accede al monitor\n", getpid());

	/* TBD: Sospendere qui il processo se il vettore di buffer è vuoto */
	if (p->count == 0)
	{
		wait_condition(&(p->m), 2);
	}

	// Consumazione

	value = p->buffer[p->coda];
	p->coda = (p->coda + 1) % 3;
	p->count--;

	printf("Consumatore con pid %d ha consumato %d\n", getpid(), value);

	if (queue_condition(&(p->m), 0) > 0)
	{
		signal_condition(&(p->m), 0);
	}
	else if (queue_condition(&(p->m), 1) > 0)
	{
		signal_condition(&(p->m), 1);
	}

	/* TBD: Effettuare la signal_condition per attivare un produttore.
	 *      Si attivi un produttore di priorità alta se presente, altrimenti,
	 *      si attivi un produttore di priorità bassa.
	 *
	 * 		Per determinare se ci sono produttori ad alta priorità in attesa,
	 * 		si introduca una variabile "num_lettori_alta_priorita", che i produttori
	 *      incrementano subito prima di fare wait_condition(), e che decrementano
	 * 		subito dopo aver eseguito wait_condition().
	 *
	 * 		In alternativa, utilizzare la funzione "queue_condition()".
	 */

	/* TBD: Uscire dal monitor */
	leave_monitor(&(p->m));

```



esercitazione-2-monitor-P0l1702-a088eceed10269e1bf275339371878390ab35c16/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-a088eceed10269e1bf275339371878390ab35c16/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-P0l1702-c25d98600ef1c2f3b2894b75ca9ab20cf64d74d5/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-P0l1702-c25d98600ef1c2f3b2894b75ca9ab20cf64d74d5/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-P0l1702-c25d98600ef1c2f3b2894b75ca9ab20cf64d74d5/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-P0l1702-c25d98600ef1c2f3b2894b75ca9ab20cf64d74d5/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-PietroViolante-82b23ba9b7b80a063eb257fb63a27bdd0fc2d672/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-PietroViolante-82b23ba9b7b80a063eb257fb63a27bdd0fc2d672/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-PietroViolante-82b23ba9b7b80a063eb257fb63a27bdd0fc2d672/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-PietroViolante-82b23ba9b7b80a063eb257fb63a27bdd0fc2d672/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-PietroViolante-d1c9f0122e94b973422ad07168a3c3636726879e/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-PietroViolante-d1c9f0122e94b973422ad07168a3c3636726879e/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-PietroViolante-d1c9f0122e94b973422ad07168a3c3636726879e/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-PietroViolante-d1c9f0122e94b973422ad07168a3c3636726879e/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Simonesorrentino-98797be9f2d6500f849e1d86f21c2955ba54e3ee/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Simonesorrentino-98797be9f2d6500f849e1d86f21c2955ba54e3ee/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Simonesorrentino-98797be9f2d6500f849e1d86f21c2955ba54e3ee/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Simonesorrentino-98797be9f2d6500f849e1d86f21c2955ba54e3ee/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Z3R0M3M-06e9ddde50f79d42be41838e9c680e5c32929221/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Z3R0M3M-06e9ddde50f79d42be41838e9c680e5c32929221/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Z3R0M3M-06e9ddde50f79d42be41838e9c680e5c32929221/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Z3R0M3M-06e9ddde50f79d42be41838e9c680e5c32929221/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Z3R0M3M-90f3c9032c6b667b3bf00c637cc252321ab309de/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Z3R0M3M-90f3c9032c6b667b3bf00c637cc252321ab309de/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Z3R0M3M-90f3c9032c6b667b3bf00c637cc252321ab309de/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Z3R0M3M-90f3c9032c6b667b3bf00c637cc252321ab309de/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Z3R0M3M-a9e80e4853b3358ded48ba862322080619558970/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (prodcons.c) :warning:


<i>Nel costrutto IF la condizione è TOT_ELEMENTI < 2. In questo esercizio, nella funzione consuma(), bisogna effettuare una Wait su MESSAGGIO_DISPONIBILE solo se il numero totale di elementi è < 2.
</i>
(codice errore: esercitazione-2-monitor-Z3R0M3M-a9e80e4853b3358ded48ba862322080619558970.prelievi_multipli..test.if-then-minore-uguale-consuma)


```
void consuma(ProdCons * p, int* val_1, int* val_2) {

    /* TBD: Ingresso nel monitor */
    enter_monitor(&p->m);

    printf("[%d] Ingresso consumatore\n", getpid());

    /* TBD: Sospendere qui il consumatore se non ci sono
     *      *almeno* 2 elementi disponibili nel vettore
     */
    if (p->totale_elementi > 10 - 2)
        wait_condition(&p->m, 1);

    
    *val_1 = p->vettore[p->coda];
    p->coda = (p->coda + 1) % 10;
    p->totale_elementi--;

    printf("[%d] Prima consumazione: val_1=%d\n", getpid(), *val_1);



    *val_2 = p->vettore[p->coda];
    p->coda = (p->coda + 1) % 10;
    p->totale_elementi--;

    printf("[%d] Seconda consumazione: val_2=%d\n", getpid(), *val_2);


    /* TBD: Effettuare signal_condition() per svegliare 2 produttori 
     *      (si sono appena liberati 2 buffer nel vettore)
     */
    signal_condition(&p->m, 0);
    signal_condition(&p->m, 0);


    printf("[%d] Uscita consumatore\n", getpid());

    /* TBD: Uscita dal monitor */
    leave_monitor(&p->m);
}

```



<i>nel costrutto IF della funzione produci() serve >= 2. In questo esercizio, nella funzione produci(), bisogna effettuare una Signal su MESSAGGIO_DISPONIBILE solo se il numero totale di elementi è >= 2. 
</i>
(codice errore: esercitazione-2-monitor-Z3R0M3M-a9e80e4853b3358ded48ba862322080619558970.prelievi_multipli..test.if-then-maggiore-uguale-produci)


```
void produci(ProdCons * p, int val) {

    /* TBD: Ingresso nel monitor */
    enter_monitor(&p->m);

    printf("[%d] Ingresso produttore\n", getpid());

    /* TBD: Sospendere qui il produttore se il vettore è già pieno */
    if (p->totale_elementi == 10)
        wait_condition(&p->m, 0);

    p->vettore[p->testa] = val;
    p->testa = (p->testa + 1) % 10;
    p->totale_elementi++;

    printf("[%d] Produzione: val=%d\n", getpid(), val);

    
    /* TBD: Svegliare un consumatore *solo se* sono disponibili almeno 2 messaggi. 
     *      Poiché è richiesto di utilizzare la semantica di Hoare, il consumatore
     *      sarà attivato immediatamente al momento della signal_condition().
     */

    if (p->totale_elementi <= 10 - 2)
        signal_condition(&p->m, 1);

    printf("[%d] Uscita produttore\n", getpid());

    /* TBD: Uscita dal monitor */
    leave_monitor(&p->m);
}

```



esercitazione-2-monitor-Z3R0M3M-a9e80e4853b3358ded48ba862322080619558970/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Z3R0M3M-a9e80e4853b3358ded48ba862322080619558970/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Z3R0M3M-a9e80e4853b3358ded48ba862322080619558970/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Z3R0M3M-e1da59ccd0061ccc8fc9f8468186b75b289bd5d6/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Z3R0M3M-e1da59ccd0061ccc8fc9f8468186b75b289bd5d6/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-2-monitor-Z3R0M3M-e1da59ccd0061ccc8fc9f8468186b75b289bd5d6/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Z3R0M3M-e1da59ccd0061ccc8fc9f8468186b75b289bd5d6/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Z3R0M3M-ffa47a4eddf076df81c2afb3eb71c2e2449f7ace/lettori-scrittori_con_monitor_e_processi

## Esercizio prelievi multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Z3R0M3M-ffa47a4eddf076df81c2afb3eb71c2e2449f7ace/prelievi_multipli

## Esercizio produttore-consumatore con priorità, con processi

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Z3R0M3M-ffa47a4eddf076df81c2afb3eb71c2e2449f7ace/produttore-consumatore_con_priorita

## Esercizio simulazione disco, con monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-2-monitor-Z3R0M3M-ffa47a4eddf076df81c2afb3eb71c2e2449f7ace/simulazione_di_un_disco_con_un_vettore_circolare

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-annalisaa99-1ec80270ecc7b6d039de3124571e0ea097afb5b4.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-annalisaa99-1ec80270ecc7b6d039de3124571e0ea097afb5b4/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-annalisaa99-1ec80270ecc7b6d039de3124571e0ea097afb5b4/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-annalisaa99-1ec80270ecc7b6d039de3124571e0ea097afb5b4/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-3-threads-annalisaa99-32add3c1d079fe3d07febf1b30c148bf48949c55/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-annalisaa99-32add3c1d079fe3d07febf1b30c148bf48949c55/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-annalisaa99-32add3c1d079fe3d07febf1b30c148bf48949c55/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-annalisaa99-34de9cfbab24ba6593d55f7919d4e5ec7f25b0cc/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-annalisaa99-34de9cfbab24ba6593d55f7919d4e5ec7f25b0cc/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-annalisaa99-34de9cfbab24ba6593d55f7919d4e5ec7f25b0cc/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-3-threads-annalisaa99-88e972627205522eeb4b0000305062482a712f25/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-annalisaa99-88e972627205522eeb4b0000305062482a712f25/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-annalisaa99-88e972627205522eeb4b0000305062482a712f25/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-annalisaa99-b23b35a2a4a325efc96710d4e2264e5882b9d439/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-annalisaa99-b23b35a2a4a325efc96710d4e2264e5882b9d439/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-annalisaa99-b23b35a2a4a325efc96710d4e2264e5882b9d439/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-annalisaa99-f1c4fabcfa764033f90eab26326232f1ee501b64.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-annalisaa99-f1c4fabcfa764033f90eab26326232f1ee501b64/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-annalisaa99-f1c4fabcfa764033f90eab26326232f1ee501b64/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-annalisaa99-f1c4fabcfa764033f90eab26326232f1ee501b64/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-3-threads-annalisaa99-f418a3a467f8a61337771c0edd972d4dbe45ad5b/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-annalisaa99-f418a3a467f8a61337771c0edd972d4dbe45ad5b/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-annalisaa99-f418a3a467f8a61337771c0edd972d4dbe45ad5b/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-cirofrattini-67b64ace851c2752dbf91f97605871f650da20f3.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-cirofrattini-67b64ace851c2752dbf91f97605871f650da20f3/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-cirofrattini-67b64ace851c2752dbf91f97605871f650da20f3/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto delle produzioni e delle consumazioni :warning:
esercitazione-3-threads-cirofrattini-67b64ace851c2752dbf91f97605871f650da20f3/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (procedure.c) :warning:


<i>Quando termina una scrittura, è necessario risvegliare tutti gli eventuali thread lettori in attesa. Sono consentite due soluzioni. 1) prima della lettura, il lettore chiama cond_signal() per risvegliare un ulteriore lettore; oppure 2) lo scrittore risveglia simultaneamente tutti i lettori sospesi chiamando cond_broadcast()
</i>
(codice errore: esercitazione-3-threads-cirofrattini-694cdd4a379ee59f33bfd78c1baa1870606e0e12.lettori-scrittori_su_piu_oggetti_monitor..test.missing-signal-readers)


```
int leggi_stazione(struct monitor* m){

	/* TBD: Implementare qui lo schema dei lettori-scrittori con starvation di entrambi.
	 * 
	 * 		Utilizzare una variabile "num_cv_lettori" per contare il numero
	 * 		di lettori in attesa sulla variabile condition (da affiancare in aggiunta
	 * 		alla variabile "num_lettori" dell'algoritmo).
	 * 
	 * 		La variabile "num_cv_lettori" deve essere incrementata subito prima
	 * 		di wait_cond(), e decrementata subito dopo di wait_cond().
	 */
    pthread_mutex_lock(&(m->mutex));

	while(m->num_scrittori == 1){
		m->num_cv_lettori++;
		pthread_cond_wait(&(m->lettura), &(m->mutex));
		m->num_cv_lettori--;
	}

    m->num_lettori++;

	pthread_mutex_unlock(&(m->mutex));
	
	// LETTURA
	int ris=m->stazione;

	pthread_mutex_lock(&(m->mutex));
    
	m->num_lettori--;

	if(m->num_cv_lettori > 0){
		pthread_cond_signal(&(m->lettura));
	}
	else if(m->num_cv_scrittori > 0){
		pthread_cond_signal(&(m->scrittura));
	}

	pthread_mutex_unlock(&(m->mutex));
	
	return ris;
}

```



esercitazione-3-threads-cirofrattini-694cdd4a379ee59f33bfd78c1baa1870606e0e12/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-694cdd4a379ee59f33bfd78c1baa1870606e0e12/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-694cdd4a379ee59f33bfd78c1baa1870606e0e12/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-858d33d568c08b1b042121ede6ed0936d5438bf2/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-858d33d568c08b1b042121ede6ed0936d5438bf2/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto delle produzioni e delle consumazioni :warning:
esercitazione-3-threads-cirofrattini-858d33d568c08b1b042121ede6ed0936d5438bf2/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-cirofrattini-90cbd7e5d0f07a2884b9c0a05000bda0054edba7.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-cirofrattini-90cbd7e5d0f07a2884b9c0a05000bda0054edba7/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-90cbd7e5d0f07a2884b9c0a05000bda0054edba7/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto delle produzioni e delle consumazioni :warning:
esercitazione-3-threads-cirofrattini-90cbd7e5d0f07a2884b9c0a05000bda0054edba7/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-af38d26eb80c67f650de97d782a54df39315dbe9/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-af38d26eb80c67f650de97d782a54df39315dbe9/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-af38d26eb80c67f650de97d782a54df39315dbe9/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-cee92a650f9e1fdebe54704d8e5eb9eba2939e5a/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-cee92a650f9e1fdebe54704d8e5eb9eba2939e5a/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto delle produzioni e delle consumazioni :warning:
esercitazione-3-threads-cirofrattini-cee92a650f9e1fdebe54704d8e5eb9eba2939e5a/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-f3f4b24ade617acf5201f58e5ee84822a808bd9a/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-f3f4b24ade617acf5201f58e5ee84822a808bd9a/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-f3f4b24ade617acf5201f58e5ee84822a808bd9a/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (prodcons.c) :warning:


<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */
	int testa;
	int coda;
	int count;
	int num_prod_ap_incoda;
	int num_prod_bp_incoda;
	pthread_mutex_t mutex;
	pthread_cond_t cv_prod_ap;
	pthread_cond_t cv_prod_bp;
	pthread_cond_t cv_cons;
    
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif

void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
	p->coda = 0;
	p->testa = 0;
	p->num_prod_ap_incoda = 0;
	p->num_prod_bp_incoda = 0;
	p->count = 0;
    pthread_cond_init(&p->cv_cons, NULL);
    pthread_cond_init(&p->cv_prod_ap, NULL);
	pthread_cond_init(&p->cv_prod_bp, NULL);
	pthread_mutex_init(&p->mutex, NULL);
}



void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_mutex_destroy(&p->mutex);
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_ap);
	pthread_cond_destroy(&p->cv_prod_bp);
	free(p);
}



void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3){
		p->num_prod_ap_incoda++;
		pthread_cond_wait(&p->cv_prod_ap, &p->mutex);
		p->num_prod_ap_incoda--;
	}

	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
    pthread_mutex_unlock(&p->mutex);
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3 || p->num_prod_ap_incoda > 0){
		p->num_prod_bp_incoda++;
		pthread_cond_wait(&p->cv_prod_bp, &p->mutex);
		p->num_prod_bp_incoda--;
	}


	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 2 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
	pthread_mutex_unlock(&p->mutex);
}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}


	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->count--;

	printf("Consumatore ha consumato %d\n", value);

	if(p->num_prod_ap_incoda > 0){
		pthread_cond_signal(&p->cv_prod_ap);
	}
	else /*if(p->num_prod_bp_incoda > 0)*/{
		pthread_cond_signal(&p->cv_prod_bp);
	}
    pthread_mutex_unlock(&p->mutex);

}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <stdlib.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */
	int testa;
	int coda;
	int count;
	int num_prod_ap_incoda;
	int num_prod_bp_incoda;
	pthread_mutex_t mutex;
	pthread_cond_t cv_prod_ap;
	pthread_cond_t cv_prod_bp;
	pthread_cond_t cv_cons;
    
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif

void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
	p->coda = 0;
	p->testa = 0;
	p->num_prod_ap_incoda = 0;
	p->num_prod_bp_incoda = 0;
	p->count = 0;
    pthread_cond_init(&p->cv_cons, NULL);
    pthread_cond_init(&p->cv_prod_ap, NULL);
	pthread_cond_init(&p->cv_prod_bp, NULL);
	pthread_mutex_init(&p->mutex, NULL);
}



void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_mutex_destroy(&p->mutex);
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_ap);
	pthread_cond_destroy(&p->cv_prod_bp);
	free(p);
}



void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3){
		p->num_prod_ap_incoda++;
		pthread_cond_wait(&p->cv_prod_ap, &p->mutex);
		p->num_prod_ap_incoda--;
	}

	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
    pthread_mutex_unlock(&p->mutex);
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3 || p->num_prod_ap_incoda > 0){
		p->num_prod_bp_incoda++;
		pthread_cond_wait(&p->cv_prod_bp, &p->mutex);
		p->num_prod_bp_incoda--;
	}


	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 2 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
	pthread_mutex_unlock(&p->mutex);
}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}


	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->count--;

	printf("Consumatore ha consumato %d\n", value);

	if(p->num_prod_ap_incoda > 0){
		pthread_cond_signal(&p->cv_prod_ap);
	}
	else /*if(p->num_prod_bp_incoda > 0)*/{
		pthread_cond_signal(&p->cv_prod_bp);
	}
    pthread_mutex_unlock(&p->mutex);

}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */
	int testa;
	int coda;
	int count;
	int num_prod_ap_incoda;
	int num_prod_bp_incoda;
	pthread_mutex_t mutex;
	pthread_cond_t cv_prod_ap;
	pthread_cond_t cv_prod_bp;
	pthread_cond_t cv_cons;
    
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif

void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
	p->coda = 0;
	p->testa = 0;
	p->num_prod_ap_incoda = 0;
	p->num_prod_bp_incoda = 0;
	p->count = 0;
    pthread_cond_init(&p->cv_cons, NULL);
    pthread_cond_init(&p->cv_prod_ap, NULL);
	pthread_cond_init(&p->cv_prod_bp, NULL);
	pthread_mutex_init(&p->mutex, NULL);
}



void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_mutex_destroy(&p->mutex);
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_ap);
	pthread_cond_destroy(&p->cv_prod_bp);
	free(p);
}



void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3){
		p->num_prod_ap_incoda++;
		pthread_cond_wait(&p->cv_prod_ap, &p->mutex);
		p->num_prod_ap_incoda--;
	}

	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
    pthread_mutex_unlock(&p->mutex);
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3 || p->num_prod_ap_incoda > 0){
		p->num_prod_bp_incoda++;
		pthread_cond_wait(&p->cv_prod_bp, &p->mutex);
		p->num_prod_bp_incoda--;
	}


	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 2 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
	pthread_mutex_unlock(&p->mutex);
}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}


	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->count--;

	printf("Consumatore ha consumato %d\n", value);

	if(p->num_prod_ap_incoda > 0){
		pthread_cond_signal(&p->cv_prod_ap);
	}
	else /*if(p->num_prod_bp_incoda > 0)*/{
		pthread_cond_signal(&p->cv_prod_bp);
	}
    pthread_mutex_unlock(&p->mutex);

}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <sys/types.h>
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */
	int testa;
	int coda;
	int count;
	int num_prod_ap_incoda;
	int num_prod_bp_incoda;
	pthread_mutex_t mutex;
	pthread_cond_t cv_prod_ap;
	pthread_cond_t cv_prod_bp;
	pthread_cond_t cv_cons;
    
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif

void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
	p->coda = 0;
	p->testa = 0;
	p->num_prod_ap_incoda = 0;
	p->num_prod_bp_incoda = 0;
	p->count = 0;
    pthread_cond_init(&p->cv_cons, NULL);
    pthread_cond_init(&p->cv_prod_ap, NULL);
	pthread_cond_init(&p->cv_prod_bp, NULL);
	pthread_mutex_init(&p->mutex, NULL);
}



void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_mutex_destroy(&p->mutex);
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_ap);
	pthread_cond_destroy(&p->cv_prod_bp);
	free(p);
}



void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3){
		p->num_prod_ap_incoda++;
		pthread_cond_wait(&p->cv_prod_ap, &p->mutex);
		p->num_prod_ap_incoda--;
	}

	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
    pthread_mutex_unlock(&p->mutex);
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3 || p->num_prod_ap_incoda > 0){
		p->num_prod_bp_incoda++;
		pthread_cond_wait(&p->cv_prod_bp, &p->mutex);
		p->num_prod_bp_incoda--;
	}


	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 2 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
	pthread_mutex_unlock(&p->mutex);
}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}


	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->count--;

	printf("Consumatore ha consumato %d\n", value);

	if(p->num_prod_ap_incoda > 0){
		pthread_cond_signal(&p->cv_prod_ap);
	}
	else /*if(p->num_prod_bp_incoda > 0)*/{
		pthread_cond_signal(&p->cv_prod_bp);
	}
    pthread_mutex_unlock(&p->mutex);

}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */
	int testa;
	int coda;
	int count;
	int num_prod_ap_incoda;
	int num_prod_bp_incoda;
	pthread_mutex_t mutex;
	pthread_cond_t cv_prod_ap;
	pthread_cond_t cv_prod_bp;
	pthread_cond_t cv_cons;
    
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif

void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
	p->coda = 0;
	p->testa = 0;
	p->num_prod_ap_incoda = 0;
	p->num_prod_bp_incoda = 0;
	p->count = 0;
    pthread_cond_init(&p->cv_cons, NULL);
    pthread_cond_init(&p->cv_prod_ap, NULL);
	pthread_cond_init(&p->cv_prod_bp, NULL);
	pthread_mutex_init(&p->mutex, NULL);
}



void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_mutex_destroy(&p->mutex);
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_ap);
	pthread_cond_destroy(&p->cv_prod_bp);
	free(p);
}



void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3){
		p->num_prod_ap_incoda++;
		pthread_cond_wait(&p->cv_prod_ap, &p->mutex);
		p->num_prod_ap_incoda--;
	}

	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
    pthread_mutex_unlock(&p->mutex);
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3 || p->num_prod_ap_incoda > 0){
		p->num_prod_bp_incoda++;
		pthread_cond_wait(&p->cv_prod_bp, &p->mutex);
		p->num_prod_bp_incoda--;
	}


	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 2 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
	pthread_mutex_unlock(&p->mutex);
}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}


	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->count--;

	printf("Consumatore ha consumato %d\n", value);

	if(p->num_prod_ap_incoda > 0){
		pthread_cond_signal(&p->cv_prod_ap);
	}
	else /*if(p->num_prod_bp_incoda > 0)*/{
		pthread_cond_signal(&p->cv_prod_bp);
	}
    pthread_mutex_unlock(&p->mutex);

}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
	p->coda = 0;
	p->testa = 0;
	p->num_prod_ap_incoda = 0;
	p->num_prod_bp_incoda = 0;
	p->count = 0;
    pthread_cond_init(&p->cv_cons, NULL);
    pthread_cond_init(&p->cv_prod_ap, NULL);
	pthread_cond_init(&p->cv_prod_bp, NULL);
	pthread_mutex_init(&p->mutex, NULL);
}



void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_mutex_destroy(&p->mutex);
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_ap);
	pthread_cond_destroy(&p->cv_prod_bp);
	free(p);
}



void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3){
		p->num_prod_ap_incoda++;
		pthread_cond_wait(&p->cv_prod_ap, &p->mutex);
		p->num_prod_ap_incoda--;
	}

	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
    pthread_mutex_unlock(&p->mutex);
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3 || p->num_prod_ap_incoda > 0){
		p->num_prod_bp_incoda++;
		pthread_cond_wait(&p->cv_prod_bp, &p->mutex);
		p->num_prod_bp_incoda--;
	}


	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 2 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
	pthread_mutex_unlock(&p->mutex);
}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}


	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->count--;

	printf("Consumatore ha consumato %d\n", value);

	if(p->num_prod_ap_incoda > 0){
		pthread_cond_signal(&p->cv_prod_ap);
	}
	else /*if(p->num_prod_bp_incoda > 0)*/{
		pthread_cond_signal(&p->cv_prod_bp);
	}
    pthread_mutex_unlock(&p->mutex);

}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_mutex_destroy(&p->mutex);
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_ap);
	pthread_cond_destroy(&p->cv_prod_bp);
	free(p);
}



void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3){
		p->num_prod_ap_incoda++;
		pthread_cond_wait(&p->cv_prod_ap, &p->mutex);
		p->num_prod_ap_incoda--;
	}

	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
    pthread_mutex_unlock(&p->mutex);
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3 || p->num_prod_ap_incoda > 0){
		p->num_prod_bp_incoda++;
		pthread_cond_wait(&p->cv_prod_bp, &p->mutex);
		p->num_prod_bp_incoda--;
	}


	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 2 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
	pthread_mutex_unlock(&p->mutex);
}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}


	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->count--;

	printf("Consumatore ha consumato %d\n", value);

	if(p->num_prod_ap_incoda > 0){
		pthread_cond_signal(&p->cv_prod_ap);
	}
	else /*if(p->num_prod_bp_incoda > 0)*/{
		pthread_cond_signal(&p->cv_prod_bp);
	}
    pthread_mutex_unlock(&p->mutex);

}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3){
		p->num_prod_ap_incoda++;
		pthread_cond_wait(&p->cv_prod_ap, &p->mutex);
		p->num_prod_ap_incoda--;
	}

	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
    pthread_mutex_unlock(&p->mutex);
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3 || p->num_prod_ap_incoda > 0){
		p->num_prod_bp_incoda++;
		pthread_cond_wait(&p->cv_prod_bp, &p->mutex);
		p->num_prod_bp_incoda--;
	}


	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 2 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
	pthread_mutex_unlock(&p->mutex);
}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}


	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->count--;

	printf("Consumatore ha consumato %d\n", value);

	if(p->num_prod_ap_incoda > 0){
		pthread_cond_signal(&p->cv_prod_ap);
	}
	else /*if(p->num_prod_bp_incoda > 0)*/{
		pthread_cond_signal(&p->cv_prod_bp);
	}
    pthread_mutex_unlock(&p->mutex);

}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 3 || p->num_prod_ap_incoda > 0){
		p->num_prod_bp_incoda++;
		pthread_cond_wait(&p->cv_prod_bp, &p->mutex);
		p->num_prod_bp_incoda--;
	}


	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->count++;

	printf("Produttore tipo 2 ha prodotto %d\n", value);

	pthread_cond_signal(&p->cv_cons);
	pthread_mutex_unlock(&p->mutex);
}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}


	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->count--;

	printf("Consumatore ha consumato %d\n", value);

	if(p->num_prod_ap_incoda > 0){
		pthread_cond_signal(&p->cv_prod_ap);
	}
	else /*if(p->num_prod_bp_incoda > 0)*/{
		pthread_cond_signal(&p->cv_prod_bp);
	}
    pthread_mutex_unlock(&p->mutex);

}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */
	pthread_mutex_lock(&p->mutex);
	while(p->count == 0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}


	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->count--;

	printf("Consumatore ha consumato %d\n", value);

	if(p->num_prod_ap_incoda > 0){
		pthread_cond_signal(&p->cv_prod_ap);
	}
	else /*if(p->num_prod_bp_incoda > 0)*/{
		pthread_cond_signal(&p->cv_prod_bp);
	}
    pthread_mutex_unlock(&p->mutex);

}

```



esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-cirofrattini-f642e2bd62f4a1774985f2af33549c3fbfaf89a4/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-emanueleascolese-0ae8d47801a68997a63e94da609c6c812781aaf1/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-emanueleascolese-0ae8d47801a68997a63e94da609c6c812781aaf1/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-emanueleascolese-0ae8d47801a68997a63e94da609c6c812781aaf1/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-emanueleascolese-1763c6e38fd3ee5d9421cabc71288fd5fbc7d52b/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-emanueleascolese-1763c6e38fd3ee5d9421cabc71288fd5fbc7d52b/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-emanueleascolese-1763c6e38fd3ee5d9421cabc71288fd5fbc7d52b/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-emanueleascolese-cdcd96fa6117abd67347ad745fb0fb12fb4b122b/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-emanueleascolese-cdcd96fa6117abd67347ad745fb0fb12fb4b122b/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-emanueleascolese-cdcd96fa6117abd67347ad745fb0fb12fb4b122b/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-GiuseppeGuarino-0393cf530f70e1d55e6b8217205d7c9a1f79e99b.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-GiuseppeGuarino-0393cf530f70e1d55e6b8217205d7c9a1f79e99b/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-GiuseppeGuarino-0393cf530f70e1d55e6b8217205d7c9a1f79e99b/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-GiuseppeGuarino-0393cf530f70e1d55e6b8217205d7c9a1f79e99b/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-GiuseppeGuarino-18f8d6def6b6a4cb410f1242581f1076e18bf41f/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-GiuseppeGuarino-18f8d6def6b6a4cb410f1242581f1076e18bf41f/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-GiuseppeGuarino-18f8d6def6b6a4cb410f1242581f1076e18bf41f/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-GiuseppeGuarino-2ff5094f690bb99d1a60098eee216b258685c1d7/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-GiuseppeGuarino-2ff5094f690bb99d1a60098eee216b258685c1d7/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-GiuseppeGuarino-2ff5094f690bb99d1a60098eee216b258685c1d7/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-GiuseppeGuarino-cbec4365e4fa6931ddd4b75d01d0aa9d9e32d654/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-GiuseppeGuarino-cbec4365e4fa6931ddd4b75d01d0aa9d9e32d654/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-GiuseppeGuarino-cbec4365e4fa6931ddd4b75d01d0aa9d9e32d654/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-GiuseppeGuarino-fdea0c48ce401f6f9b75c4d78127aec99587391f.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-GiuseppeGuarino-fdea0c48ce401f6f9b75c4d78127aec99587391f/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-GiuseppeGuarino-fdea0c48ce401f6f9b75c4d78127aec99587391f/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-GiuseppeGuarino-fdea0c48ce401f6f9b75c4d78127aec99587391f/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-MarkCer16-2fbd98d65ed4b2f7370e8daa8a82542f652c66f0.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-MarkCer16-2fbd98d65ed4b2f7370e8daa8a82542f652c66f0/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-MarkCer16-2fbd98d65ed4b2f7370e8daa8a82542f652c66f0/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-MarkCer16-2fbd98d65ed4b2f7370e8daa8a82542f652c66f0/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-MarkCer16-50c444f1465aac8a61a184a2decd315528ef558e/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-MarkCer16-50c444f1465aac8a61a184a2decd315528ef558e/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-MarkCer16-50c444f1465aac8a61a184a2decd315528ef558e/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (procedure.c) :warning:


<i>Quando termina una scrittura, è necessario risvegliare tutti gli eventuali thread lettori in attesa. Sono consentite due soluzioni. 1) prima della lettura, il lettore chiama cond_signal() per risvegliare un ulteriore lettore; oppure 2) lo scrittore risveglia simultaneamente tutti i lettori sospesi chiamando cond_broadcast()
</i>
(codice errore: esercitazione-3-threads-MarkCer16-5ea661a79850c6f141eb57ae9f2875ae9f472fac.lettori-scrittori_su_piu_oggetti_monitor..test.missing-signal-readers)


```
int leggi_stazione(struct monitor* m){

	/* TBD: Implementare qui lo schema dei lettori-scrittori con starvation di entrambi.
	 *
	 * 		Utilizzare una variabile "num_cv_lettori" per contare il numero
	 * 		di lettori in attesa sulla variabile condition (da affiancare in aggiunta
	 * 		alla variabile "num_lettori" dell'algoritmo).
	 *
	 * 		La variabile "num_cv_lettori" deve essere incrementata subito prima
	 * 		di wait_cond(), e decrementata subito dopo di wait_cond().
	 */
	pthread_mutex_lock(&m->mutex);
	while(m->num_scrittori>0||m->num_lettori>0){
		m->num_cv_lettori++;
		pthread_cond_wait(&m->ok_viaggiatori,&m->mutex);
		m->num_cv_lettori--;
	}
	m->num_lettori++;
	pthread_mutex_unlock(&m->mutex);


	// LETTURA
	int ris=m->stazione;
	printf("Lettura: stazione=%d\n", ris);
	m->num_lettori--;
	pthread_mutex_lock(&m->mutex);

	pthread_cond_signal(&m->ok_viaggiatori);
	if(m->num_lettori==0){
		pthread_cond_signal(&m->ok_capitreno);
	}

	pthread_mutex_unlock(&m->mutex);
	return ris;
}

```



esercitazione-3-threads-MarkCer16-5ea661a79850c6f141eb57ae9f2875ae9f472fac/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-MarkCer16-5ea661a79850c6f141eb57ae9f2875ae9f472fac/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-MarkCer16-5ea661a79850c6f141eb57ae9f2875ae9f472fac/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (procedure.c) :warning:


<i>In questo esercizio si raccomanda di utilizzare l'algoritmo con starvation di entrambi (sia lettori sia scrittori). Per realizzare questo algoritmo, è necessario che la scrittura sia effettuata uscendo dal monitor (ossia, liberando temporaneamente la sezione critica del monitor, e riacquisendola subito dopo la scrittura). Questo consente ad eventuali altri scrittori di porsi in attesa su una variabile condition, e di potergli dare la priorità quando lo scrittore deve risvegliare un altro thread.
</i>
(codice errore: esercitazione-3-threads-MarkCer16-6fa0b763f541034f939d682a339a62d975a15285.lettori-scrittori_su_piu_oggetti_monitor..test.writing-inside-monitor)


```
void scrivi_stazione(struct monitor* m, int stazione){

	/* TBD: Implementare qui lo schema dei lettori-scrittori con starvation di entrambi.
	 *
	 * 		Utilizzare una variabile "num_cv_scrittori" per contare il numero
	 * 		di scrittori in attesa sulla variabile condition (da affiancare in aggiunta
	 * 		alla variabile "num_scrittori" dell'algoritmo).
	 *
	 * 		La variabile "num_cv_scrittori" deve essere incrementata subito prima
	 * 		di wait_cond(), e decrementata subito dopo di wait_cond().
	 */
	pthread_mutex_lock(&m->mutex);
	while(m->num_scrittori>0||m->num_lettori>0){
		m->num_cv_scrittori++;
		pthread_cond_wait(&m->ok_capitreno,&m->mutex);
		m->num_cv_scrittori--;		
	}
	m->num_scrittori++;
	
	

	// SCRITTURA
	m->stazione=stazione;
	printf("Scrittura: stazione=%d\n", stazione);
	m->num_scrittori--;

	if(m->num_cv_scrittori>0){
		pthread_cond_signal(&m->ok_capitreno);
	}
	else if(m->num_cv_lettori>0){
		//pthread_cond_signal(&m->ok_viaggiatori);
		pthread_cond_broadcast(&m->ok_viaggiatori);
	}

	
	pthread_mutex_unlock(&m->mutex);

}

```



<i>Quando termina una scrittura, è necessario risvegliare tutti gli eventuali thread lettori in attesa. Sono consentite due soluzioni. 1) prima della lettura, il lettore chiama cond_signal() per risvegliare un ulteriore lettore; oppure 2) lo scrittore risveglia simultaneamente tutti i lettori sospesi chiamando cond_broadcast()
</i>
(codice errore: esercitazione-3-threads-MarkCer16-6fa0b763f541034f939d682a339a62d975a15285.lettori-scrittori_su_piu_oggetti_monitor..test.missing-signal-readers)


```
int leggi_stazione(struct monitor* m){

	/* TBD: Implementare qui lo schema dei lettori-scrittori con starvation di entrambi.
	 *
	 * 		Utilizzare una variabile "num_cv_lettori" per contare il numero
	 * 		di lettori in attesa sulla variabile condition (da affiancare in aggiunta
	 * 		alla variabile "num_lettori" dell'algoritmo).
	 *
	 * 		La variabile "num_cv_lettori" deve essere incrementata subito prima
	 * 		di wait_cond(), e decrementata subito dopo di wait_cond().
	 */
	pthread_mutex_lock(&m->mutex);
	while(m->num_scrittori>0||m->num_lettori>0){
		m->num_cv_lettori++;
		pthread_cond_wait(&m->ok_viaggiatori,&m->mutex);
		m->num_cv_lettori--;
	}
	m->num_lettori++;



	// LETTURA
	int ris=m->stazione;
	printf("Lettura: stazione=%d\n", ris);
	m->num_lettori--;

	pthread_cond_signal(&m->ok_viaggiatori);
	if(m->num_lettori==0){
		pthread_cond_signal(&m->ok_capitreno);
	}

	pthread_mutex_unlock(&m->mutex);
	return ris;
}

```



<i>È necessario che la lettura sia effettuata uscendo dal monitor (ossia, liberando temporaneamente la sezione critica del monitor, e riacquisendola subito dopo la lettura). Questo consente a più lettori di poter leggere contemporaneamente il buffer.
</i>
(codice errore: esercitazione-3-threads-MarkCer16-6fa0b763f541034f939d682a339a62d975a15285.lettori-scrittori_su_piu_oggetti_monitor..test.reading-inside-monitor)


```
int leggi_stazione(struct monitor* m){

	/* TBD: Implementare qui lo schema dei lettori-scrittori con starvation di entrambi.
	 *
	 * 		Utilizzare una variabile "num_cv_lettori" per contare il numero
	 * 		di lettori in attesa sulla variabile condition (da affiancare in aggiunta
	 * 		alla variabile "num_lettori" dell'algoritmo).
	 *
	 * 		La variabile "num_cv_lettori" deve essere incrementata subito prima
	 * 		di wait_cond(), e decrementata subito dopo di wait_cond().
	 */
	pthread_mutex_lock(&m->mutex);
	while(m->num_scrittori>0||m->num_lettori>0){
		m->num_cv_lettori++;
		pthread_cond_wait(&m->ok_viaggiatori,&m->mutex);
		m->num_cv_lettori--;
	}
	m->num_lettori++;



	// LETTURA
	int ris=m->stazione;
	printf("Lettura: stazione=%d\n", ris);
	m->num_lettori--;

	pthread_cond_signal(&m->ok_viaggiatori);
	if(m->num_lettori==0){
		pthread_cond_signal(&m->ok_capitreno);
	}

	pthread_mutex_unlock(&m->mutex);
	return ris;
}

```



esercitazione-3-threads-MarkCer16-6fa0b763f541034f939d682a339a62d975a15285/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-MarkCer16-6fa0b763f541034f939d682a339a62d975a15285/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-MarkCer16-6fa0b763f541034f939d682a339a62d975a15285/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-MarkCer16-d741c76a8c8cec1d18f8ffcb5afd917922b95200.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-MarkCer16-d741c76a8c8cec1d18f8ffcb5afd917922b95200/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-MarkCer16-d741c76a8c8cec1d18f8ffcb5afd917922b95200/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto delle produzioni e delle consumazioni :warning:
esercitazione-3-threads-MarkCer16-d741c76a8c8cec1d18f8ffcb5afd917922b95200/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-MarkCer16-e856c82f1094507de7060f97503e43a624752e3e/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-MarkCer16-e856c82f1094507de7060f97503e43a624752e3e/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-MarkCer16-e856c82f1094507de7060f97503e43a624752e3e/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (procedure.c) :warning:


<i>In questo esercizio si raccomanda di utilizzare l'algoritmo con starvation di entrambi (sia lettori sia scrittori). Per realizzare questo algoritmo, è necessario che la scrittura sia effettuata uscendo dal monitor (ossia, liberando temporaneamente la sezione critica del monitor, e riacquisendola subito dopo la scrittura). Questo consente ad eventuali altri scrittori di porsi in attesa su una variabile condition, e di potergli dare la priorità quando lo scrittore deve risvegliare un altro thread.
</i>
(codice errore: esercitazione-3-threads-MarkCer16-ed7f68aa04548c311b41d28f4a76894a765c9a38.lettori-scrittori_su_piu_oggetti_monitor..test.writing-inside-monitor)


```
void scrivi_stazione(struct monitor* m, int stazione){

	/* TBD: Implementare qui lo schema dei lettori-scrittori con starvation di entrambi.
	 *
	 * 		Utilizzare una variabile "num_cv_scrittori" per contare il numero
	 * 		di scrittori in attesa sulla variabile condition (da affiancare in aggiunta
	 * 		alla variabile "num_scrittori" dell'algoritmo).
	 *
	 * 		La variabile "num_cv_scrittori" deve essere incrementata subito prima
	 * 		di wait_cond(), e decrementata subito dopo di wait_cond().
	 */
	pthread_mutex_lock(&m->mutex);
	while(m->num_scrittori>0||m->num_lettori>0){
		m->num_cv_scrittori++;
		pthread_cond_wait(&m->ok_capitreno,&m->mutex);
		m->num_cv_scrittori--;		
	}
	m->num_scrittori++;
	
	

	// SCRITTURA
	m->stazione=stazione;
	printf("Scrittura: stazione=%d\n", stazione);
	m->num_scrittori--;

	if(m->num_cv_scrittori>0){
		pthread_cond_signal(&m->ok_capitreno);
	}
	else if(m->num_cv_lettori>0){
		pthread_cond_signal(&m->ok_viaggiatori);
	}

	
	pthread_mutex_unlock(&m->mutex);

}

```



<i>Quando termina una scrittura, è necessario risvegliare tutti gli eventuali thread lettori in attesa. Sono consentite due soluzioni. 1) prima della lettura, il lettore chiama cond_signal() per risvegliare un ulteriore lettore; oppure 2) lo scrittore risveglia simultaneamente tutti i lettori sospesi chiamando cond_broadcast()
</i>
(codice errore: esercitazione-3-threads-MarkCer16-ed7f68aa04548c311b41d28f4a76894a765c9a38.lettori-scrittori_su_piu_oggetti_monitor..test.missing-signal-readers)


```
int leggi_stazione(struct monitor* m){

	/* TBD: Implementare qui lo schema dei lettori-scrittori con starvation di entrambi.
	 *
	 * 		Utilizzare una variabile "num_cv_lettori" per contare il numero
	 * 		di lettori in attesa sulla variabile condition (da affiancare in aggiunta
	 * 		alla variabile "num_lettori" dell'algoritmo).
	 *
	 * 		La variabile "num_cv_lettori" deve essere incrementata subito prima
	 * 		di wait_cond(), e decrementata subito dopo di wait_cond().
	 */
	pthread_mutex_lock(&m->mutex);
	while(m->num_scrittori>0||m->num_lettori>0){
		m->num_cv_lettori++;
		pthread_cond_wait(&m->ok_viaggiatori,&m->mutex);
		m->num_cv_lettori--;
	}
	m->num_lettori++;



	// LETTURA
	int ris=m->stazione;
	printf("Lettura: stazione=%d\n", ris);
	m->num_lettori--;

	pthread_cond_signal(&m->ok_viaggiatori);
	if(m->num_lettori==0){
		pthread_cond_signal(&m->ok_capitreno);
	}

	pthread_mutex_unlock(&m->mutex);
	return ris;
}

```



<i>È necessario che la lettura sia effettuata uscendo dal monitor (ossia, liberando temporaneamente la sezione critica del monitor, e riacquisendola subito dopo la lettura). Questo consente a più lettori di poter leggere contemporaneamente il buffer.
</i>
(codice errore: esercitazione-3-threads-MarkCer16-ed7f68aa04548c311b41d28f4a76894a765c9a38.lettori-scrittori_su_piu_oggetti_monitor..test.reading-inside-monitor)


```
int leggi_stazione(struct monitor* m){

	/* TBD: Implementare qui lo schema dei lettori-scrittori con starvation di entrambi.
	 *
	 * 		Utilizzare una variabile "num_cv_lettori" per contare il numero
	 * 		di lettori in attesa sulla variabile condition (da affiancare in aggiunta
	 * 		alla variabile "num_lettori" dell'algoritmo).
	 *
	 * 		La variabile "num_cv_lettori" deve essere incrementata subito prima
	 * 		di wait_cond(), e decrementata subito dopo di wait_cond().
	 */
	pthread_mutex_lock(&m->mutex);
	while(m->num_scrittori>0||m->num_lettori>0){
		m->num_cv_lettori++;
		pthread_cond_wait(&m->ok_viaggiatori,&m->mutex);
		m->num_cv_lettori--;
	}
	m->num_lettori++;



	// LETTURA
	int ris=m->stazione;
	printf("Lettura: stazione=%d\n", ris);
	m->num_lettori--;

	pthread_cond_signal(&m->ok_viaggiatori);
	if(m->num_lettori==0){
		pthread_cond_signal(&m->ok_capitreno);
	}

	pthread_mutex_unlock(&m->mutex);
	return ris;
}

```



esercitazione-3-threads-MarkCer16-ed7f68aa04548c311b41d28f4a76894a765c9a38/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-MarkCer16-ed7f68aa04548c311b41d28f4a76894a765c9a38/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-MarkCer16-ed7f68aa04548c311b41d28f4a76894a765c9a38/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-P0l1702-1e60f6c43d3837fec8a722c858c99d22185fcd07/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-P0l1702-1e60f6c43d3837fec8a722c858c99d22185fcd07/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-P0l1702-1e60f6c43d3837fec8a722c858c99d22185fcd07/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (procedure.c) :warning:


<i>In questo esercizio si raccomanda di utilizzare l'algoritmo con starvation di entrambi (sia lettori sia scrittori). Per realizzare questo algoritmo, è necessario che la scrittura sia effettuata uscendo dal monitor (ossia, liberando temporaneamente la sezione critica del monitor, e riacquisendola subito dopo la scrittura). Questo consente ad eventuali altri scrittori di porsi in attesa su una variabile condition, e di potergli dare la priorità quando lo scrittore deve risvegliare un altro thread.
</i>
(codice errore: esercitazione-3-threads-P0l1702-8674de407c198b58f95101f13d79b3901004741b.lettori-scrittori_su_piu_oggetti_monitor..test.writing-inside-monitor)


```
void scrivi_stazione(struct monitor *m, int stazione)
{

	/* TBD: Implementare qui lo schema dei lettori-scrittori con starvation di entrambi.
	 *
	 * 		Utilizzare una variabile "num_cv_scrittori" per contare il numero
	 * 		di scrittori in attesa sulla variabile condition (da affiancare in aggiunta
	 * 		alla variabile "num_scrittori" dell'algoritmo).
	 *
	 * 		La variabile "num_cv_scrittori" deve essere incrementata subito prima
	 * 		di wait_cond(), e decrementata subito dopo di wait_cond().
	 */
	pthread_mutex_lock(&(m->mutex));
	while (m->occupato == 1)
	{
		m->coda_scrittori++;
		pthread_cond_wait(&(m->scrittori), &(m->mutex));
		m->coda_scrittori--;
	}
	m->occupato = 1;

	// SCRITTURA

	m->stazione = stazione;
	printf("Scrittura: stazione=%d\n", stazione);
	if (m->coda_scrittori > 0)
	{
		pthread_cond_signal(&(m->scrittori));
	}
	else if (m->coda_lettori > 0)
	{
		pthread_cond_signal(&(m->lettori));
	}
	m->occupato = 0;
	pthread_mutex_unlock(&(m->mutex));
}

```



<i>Quando termina una scrittura, è necessario risvegliare tutti gli eventuali thread lettori in attesa. Sono consentite due soluzioni. 1) prima della lettura, il lettore chiama cond_signal() per risvegliare un ulteriore lettore; oppure 2) lo scrittore risveglia simultaneamente tutti i lettori sospesi chiamando cond_broadcast()
</i>
(codice errore: esercitazione-3-threads-P0l1702-8674de407c198b58f95101f13d79b3901004741b.lettori-scrittori_su_piu_oggetti_monitor..test.missing-signal-readers)


```
int leggi_stazione(struct monitor *m)
{

	/* TBD: Implementare qui lo schema dei lettori-scrittori con starvation di entrambi.
	 *
	 * 		Utilizzare una variabile "num_cv_lettori" per contare il numero
	 * 		di lettori in attesa sulla variabile condition (da affiancare in aggiunta
	 * 		alla variabile "num_lettori" dell'algoritmo).
	 *
	 * 		La variabile "num_cv_lettori" deve essere incrementata subito prima
	 * 		di wait_cond(), e decrementata subito dopo di wait_cond().
	 */
	pthread_mutex_lock(&(m->mutex));
	while (m->occupato == 1 && m->num_lettori == 0)
	{
		m->coda_lettori++;
		pthread_cond_wait(&(m->lettori), &(m->mutex));
		m->coda_lettori--;
	}
	m->occupato = 1;
	// LETTURA
	m->num_lettori++;
	pthread_cond_signal(&(m->lettori));
	int ris = m->stazione;
	printf("Lettura: stazione=%d\n", ris);
	m->num_lettori--;
	if (m->num_lettori == 0)
	{
		m->occupato = 0;
		pthread_cond_signal(&(m->scrittori));
	}

	pthread_mutex_unlock(&(m->mutex));
	return ris;
}

```



<i>È necessario che la lettura sia effettuata uscendo dal monitor (ossia, liberando temporaneamente la sezione critica del monitor, e riacquisendola subito dopo la lettura). Questo consente a più lettori di poter leggere contemporaneamente il buffer.
</i>
(codice errore: esercitazione-3-threads-P0l1702-8674de407c198b58f95101f13d79b3901004741b.lettori-scrittori_su_piu_oggetti_monitor..test.reading-inside-monitor)


```
int leggi_stazione(struct monitor *m)
{

	/* TBD: Implementare qui lo schema dei lettori-scrittori con starvation di entrambi.
	 *
	 * 		Utilizzare una variabile "num_cv_lettori" per contare il numero
	 * 		di lettori in attesa sulla variabile condition (da affiancare in aggiunta
	 * 		alla variabile "num_lettori" dell'algoritmo).
	 *
	 * 		La variabile "num_cv_lettori" deve essere incrementata subito prima
	 * 		di wait_cond(), e decrementata subito dopo di wait_cond().
	 */
	pthread_mutex_lock(&(m->mutex));
	while (m->occupato == 1 && m->num_lettori == 0)
	{
		m->coda_lettori++;
		pthread_cond_wait(&(m->lettori), &(m->mutex));
		m->coda_lettori--;
	}
	m->occupato = 1;
	// LETTURA
	m->num_lettori++;
	pthread_cond_signal(&(m->lettori));
	int ris = m->stazione;
	printf("Lettura: stazione=%d\n", ris);
	m->num_lettori--;
	if (m->num_lettori == 0)
	{
		m->occupato = 0;
		pthread_cond_signal(&(m->scrittori));
	}

	pthread_mutex_unlock(&(m->mutex));
	return ris;
}

```



esercitazione-3-threads-P0l1702-8674de407c198b58f95101f13d79b3901004741b/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-P0l1702-8674de407c198b58f95101f13d79b3901004741b/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-P0l1702-8674de407c198b58f95101f13d79b3901004741b/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-P0l1702-930ff61884f2b4fa8e76da03adf8fb5fa23297a1/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-P0l1702-930ff61884f2b4fa8e76da03adf8fb5fa23297a1/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-P0l1702-930ff61884f2b4fa8e76da03adf8fb5fa23297a1/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-P0l1702-cb1d0231c3199e471798cd46b51e8b61b9257ff3.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-P0l1702-cb1d0231c3199e471798cd46b51e8b61b9257ff3/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-P0l1702-cb1d0231c3199e471798cd46b51e8b61b9257ff3/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-P0l1702-cb1d0231c3199e471798cd46b51e8b61b9257ff3/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-PietroViolante-04e7770c7a573ef191c6afacfcfe595ddefc9a54/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-PietroViolante-04e7770c7a573ef191c6afacfcfe595ddefc9a54/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-PietroViolante-04e7770c7a573ef191c6afacfcfe595ddefc9a54/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-PietroViolante-066d568f8e67259cab5f5f9f49efb95e51675906/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-PietroViolante-066d568f8e67259cab5f5f9f49efb95e51675906/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-PietroViolante-066d568f8e67259cab5f5f9f49efb95e51675906/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-PietroViolante-61da2c26eefeded5fbf2f15e776f5e366a266e54/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-PietroViolante-61da2c26eefeded5fbf2f15e776f5e366a266e54/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-PietroViolante-61da2c26eefeded5fbf2f15e776f5e366a266e54/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-PietroViolante-8ddd85eb58d16388acd1185caf10ca771bf54c40/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-PietroViolante-8ddd85eb58d16388acd1185caf10ca771bf54c40/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-PietroViolante-8ddd85eb58d16388acd1185caf10ca771bf54c40/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-ragdolla-0eb367955947a2044b4bfdd238b21de20914c926/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-ragdolla-0eb367955947a2044b4bfdd238b21de20914c926/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-ragdolla-0eb367955947a2044b4bfdd238b21de20914c926/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (prodcons.c) :warning:


<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */

	pthread_mutex_t mutex;
	pthread_cond_t cv_prod_prio1;
	pthread_cond_t cv_prod_prio2;
	pthread_cond_t cv_cons;

	int testa;
	int coda;
	int riemp;
	int threads_prio_1;
	int threads_prio_2;

    
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif


void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
	pthread_mutex_init(&p->mutex, NULL);
	pthread_cond_init(&p->cv_cons, NULL);
	pthread_cond_init(&p->cv_prod_prio1, NULL);
	pthread_cond_init(&p->cv_prod_prio2, NULL);

	p->coda=0;
	p->testa=0;
	p->riemp=0;
	p->threads_prio_1=0;
	p->threads_prio_2=0;

}

void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_prio1);
	pthread_cond_destroy(&p->cv_prod_prio2);
	pthread_mutex_destroy(&p->mutex);

}

void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3){
		p->threads_prio_1++;
		pthread_cond_wait(&p->cv_prod_prio1, &p->mutex);
		p->threads_prio_1--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 1 ha prodotto %d\n", value);


}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */


	/* Produzione */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3 || p->threads_prio_1 > 0){
		p->threads_prio_2++;
		pthread_cond_wait(&p->cv_prod_prio2, &p->mutex);
		p->threads_prio_2--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 2 ha prodotto %d\n", value);


}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}

	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->riemp--;

	if(p->threads_prio_1 > 0){
		pthread_cond_signal(&p->cv_prod_prio1);
	}
	else{
		pthread_cond_signal(&p->cv_prod_prio2);
	}

	pthread_mutex_unlock(&p->mutex);

	printf("Consumatore ha consumato %d\n", value);


}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <stdlib.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */

	pthread_mutex_t mutex;
	pthread_cond_t cv_prod_prio1;
	pthread_cond_t cv_prod_prio2;
	pthread_cond_t cv_cons;

	int testa;
	int coda;
	int riemp;
	int threads_prio_1;
	int threads_prio_2;

    
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif


void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
	pthread_mutex_init(&p->mutex, NULL);
	pthread_cond_init(&p->cv_cons, NULL);
	pthread_cond_init(&p->cv_prod_prio1, NULL);
	pthread_cond_init(&p->cv_prod_prio2, NULL);

	p->coda=0;
	p->testa=0;
	p->riemp=0;
	p->threads_prio_1=0;
	p->threads_prio_2=0;

}

void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_prio1);
	pthread_cond_destroy(&p->cv_prod_prio2);
	pthread_mutex_destroy(&p->mutex);

}

void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3){
		p->threads_prio_1++;
		pthread_cond_wait(&p->cv_prod_prio1, &p->mutex);
		p->threads_prio_1--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 1 ha prodotto %d\n", value);


}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */


	/* Produzione */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3 || p->threads_prio_1 > 0){
		p->threads_prio_2++;
		pthread_cond_wait(&p->cv_prod_prio2, &p->mutex);
		p->threads_prio_2--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 2 ha prodotto %d\n", value);


}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}

	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->riemp--;

	if(p->threads_prio_1 > 0){
		pthread_cond_signal(&p->cv_prod_prio1);
	}
	else{
		pthread_cond_signal(&p->cv_prod_prio2);
	}

	pthread_mutex_unlock(&p->mutex);

	printf("Consumatore ha consumato %d\n", value);


}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */

	pthread_mutex_t mutex;
	pthread_cond_t cv_prod_prio1;
	pthread_cond_t cv_prod_prio2;
	pthread_cond_t cv_cons;

	int testa;
	int coda;
	int riemp;
	int threads_prio_1;
	int threads_prio_2;

    
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif


void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
	pthread_mutex_init(&p->mutex, NULL);
	pthread_cond_init(&p->cv_cons, NULL);
	pthread_cond_init(&p->cv_prod_prio1, NULL);
	pthread_cond_init(&p->cv_prod_prio2, NULL);

	p->coda=0;
	p->testa=0;
	p->riemp=0;
	p->threads_prio_1=0;
	p->threads_prio_2=0;

}

void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_prio1);
	pthread_cond_destroy(&p->cv_prod_prio2);
	pthread_mutex_destroy(&p->mutex);

}

void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3){
		p->threads_prio_1++;
		pthread_cond_wait(&p->cv_prod_prio1, &p->mutex);
		p->threads_prio_1--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 1 ha prodotto %d\n", value);


}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */


	/* Produzione */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3 || p->threads_prio_1 > 0){
		p->threads_prio_2++;
		pthread_cond_wait(&p->cv_prod_prio2, &p->mutex);
		p->threads_prio_2--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 2 ha prodotto %d\n", value);


}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}

	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->riemp--;

	if(p->threads_prio_1 > 0){
		pthread_cond_signal(&p->cv_prod_prio1);
	}
	else{
		pthread_cond_signal(&p->cv_prod_prio2);
	}

	pthread_mutex_unlock(&p->mutex);

	printf("Consumatore ha consumato %d\n", value);


}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <sys/types.h>
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */

	pthread_mutex_t mutex;
	pthread_cond_t cv_prod_prio1;
	pthread_cond_t cv_prod_prio2;
	pthread_cond_t cv_cons;

	int testa;
	int coda;
	int riemp;
	int threads_prio_1;
	int threads_prio_2;

    
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif


void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
	pthread_mutex_init(&p->mutex, NULL);
	pthread_cond_init(&p->cv_cons, NULL);
	pthread_cond_init(&p->cv_prod_prio1, NULL);
	pthread_cond_init(&p->cv_prod_prio2, NULL);

	p->coda=0;
	p->testa=0;
	p->riemp=0;
	p->threads_prio_1=0;
	p->threads_prio_2=0;

}

void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_prio1);
	pthread_cond_destroy(&p->cv_prod_prio2);
	pthread_mutex_destroy(&p->mutex);

}

void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3){
		p->threads_prio_1++;
		pthread_cond_wait(&p->cv_prod_prio1, &p->mutex);
		p->threads_prio_1--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 1 ha prodotto %d\n", value);


}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */


	/* Produzione */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3 || p->threads_prio_1 > 0){
		p->threads_prio_2++;
		pthread_cond_wait(&p->cv_prod_prio2, &p->mutex);
		p->threads_prio_2--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 2 ha prodotto %d\n", value);


}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}

	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->riemp--;

	if(p->threads_prio_1 > 0){
		pthread_cond_signal(&p->cv_prod_prio1);
	}
	else{
		pthread_cond_signal(&p->cv_prod_prio2);
	}

	pthread_mutex_unlock(&p->mutex);

	printf("Consumatore ha consumato %d\n", value);


}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */

	pthread_mutex_t mutex;
	pthread_cond_t cv_prod_prio1;
	pthread_cond_t cv_prod_prio2;
	pthread_cond_t cv_cons;

	int testa;
	int coda;
	int riemp;
	int threads_prio_1;
	int threads_prio_2;

    
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif


void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
	pthread_mutex_init(&p->mutex, NULL);
	pthread_cond_init(&p->cv_cons, NULL);
	pthread_cond_init(&p->cv_prod_prio1, NULL);
	pthread_cond_init(&p->cv_prod_prio2, NULL);

	p->coda=0;
	p->testa=0;
	p->riemp=0;
	p->threads_prio_1=0;
	p->threads_prio_2=0;

}

void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_prio1);
	pthread_cond_destroy(&p->cv_prod_prio2);
	pthread_mutex_destroy(&p->mutex);

}

void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3){
		p->threads_prio_1++;
		pthread_cond_wait(&p->cv_prod_prio1, &p->mutex);
		p->threads_prio_1--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 1 ha prodotto %d\n", value);


}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */


	/* Produzione */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3 || p->threads_prio_1 > 0){
		p->threads_prio_2++;
		pthread_cond_wait(&p->cv_prod_prio2, &p->mutex);
		p->threads_prio_2--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 2 ha prodotto %d\n", value);


}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}

	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->riemp--;

	if(p->threads_prio_1 > 0){
		pthread_cond_signal(&p->cv_prod_prio1);
	}
	else{
		pthread_cond_signal(&p->cv_prod_prio2);
	}

	pthread_mutex_unlock(&p->mutex);

	printf("Consumatore ha consumato %d\n", value);


}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
	pthread_mutex_init(&p->mutex, NULL);
	pthread_cond_init(&p->cv_cons, NULL);
	pthread_cond_init(&p->cv_prod_prio1, NULL);
	pthread_cond_init(&p->cv_prod_prio2, NULL);

	p->coda=0;
	p->testa=0;
	p->riemp=0;
	p->threads_prio_1=0;
	p->threads_prio_2=0;

}

void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_prio1);
	pthread_cond_destroy(&p->cv_prod_prio2);
	pthread_mutex_destroy(&p->mutex);

}

void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3){
		p->threads_prio_1++;
		pthread_cond_wait(&p->cv_prod_prio1, &p->mutex);
		p->threads_prio_1--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 1 ha prodotto %d\n", value);


}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */


	/* Produzione */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3 || p->threads_prio_1 > 0){
		p->threads_prio_2++;
		pthread_cond_wait(&p->cv_prod_prio2, &p->mutex);
		p->threads_prio_2--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 2 ha prodotto %d\n", value);


}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}

	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->riemp--;

	if(p->threads_prio_1 > 0){
		pthread_cond_signal(&p->cv_prod_prio1);
	}
	else{
		pthread_cond_signal(&p->cv_prod_prio2);
	}

	pthread_mutex_unlock(&p->mutex);

	printf("Consumatore ha consumato %d\n", value);


}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
	pthread_cond_destroy(&p->cv_cons);
	pthread_cond_destroy(&p->cv_prod_prio1);
	pthread_cond_destroy(&p->cv_prod_prio2);
	pthread_mutex_destroy(&p->mutex);

}

void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3){
		p->threads_prio_1++;
		pthread_cond_wait(&p->cv_prod_prio1, &p->mutex);
		p->threads_prio_1--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 1 ha prodotto %d\n", value);


}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */


	/* Produzione */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3 || p->threads_prio_1 > 0){
		p->threads_prio_2++;
		pthread_cond_wait(&p->cv_prod_prio2, &p->mutex);
		p->threads_prio_2--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 2 ha prodotto %d\n", value);


}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}

	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->riemp--;

	if(p->threads_prio_1 > 0){
		pthread_cond_signal(&p->cv_prod_prio1);
	}
	else{
		pthread_cond_signal(&p->cv_prod_prio2);
	}

	pthread_mutex_unlock(&p->mutex);

	printf("Consumatore ha consumato %d\n", value);


}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void produci_alta_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3){
		p->threads_prio_1++;
		pthread_cond_wait(&p->cv_prod_prio1, &p->mutex);
		p->threads_prio_1--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 1 ha prodotto %d\n", value);


}




void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */


	/* Produzione */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3 || p->threads_prio_1 > 0){
		p->threads_prio_2++;
		pthread_cond_wait(&p->cv_prod_prio2, &p->mutex);
		p->threads_prio_2--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 2 ha prodotto %d\n", value);


}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}

	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->riemp--;

	if(p->threads_prio_1 > 0){
		pthread_cond_signal(&p->cv_prod_prio1);
	}
	else{
		pthread_cond_signal(&p->cv_prod_prio2);
	}

	pthread_mutex_unlock(&p->mutex);

	printf("Consumatore ha consumato %d\n", value);


}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void produci_bassa_prio(PriorityProdCons* p){

	int value;

	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */


	/* Produzione */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==3 || p->threads_prio_1 > 0){
		p->threads_prio_2++;
		pthread_cond_wait(&p->cv_prod_prio2, &p->mutex);
		p->threads_prio_2--;
	}

	/* Produzione */

	value = rand() % 12;

	p->buffer[p->testa] = value;
	p->testa = (p->testa + 1) % 3;
	p->riemp++;

	pthread_cond_signal(&p->cv_cons);

	pthread_mutex_unlock(&p->mutex);

	printf("Produttore tipo 2 ha prodotto %d\n", value);


}




void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}

	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->riemp--;

	if(p->threads_prio_1 > 0){
		pthread_cond_signal(&p->cv_prod_prio1);
	}
	else{
		pthread_cond_signal(&p->cv_prod_prio2);
	}

	pthread_mutex_unlock(&p->mutex);

	printf("Consumatore ha consumato %d\n", value);


}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void consuma(PriorityProdCons* p){

	int value;

	printf("Consumatore accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */

	pthread_mutex_lock(&p->mutex);

	while(p->riemp==0){
		pthread_cond_wait(&p->cv_cons, &p->mutex);
	}

	/* Consumazione */

	value = p->buffer[p->coda];/* TBD */
	p->coda = (p->coda + 1) % 3;
	p->riemp--;

	if(p->threads_prio_1 > 0){
		pthread_cond_signal(&p->cv_prod_prio1);
	}
	else{
		pthread_cond_signal(&p->cv_prod_prio2);
	}

	pthread_mutex_unlock(&p->mutex);

	printf("Consumatore ha consumato %d\n", value);


}

```



esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-ragdolla-12e05f8c584c74a35c470c0be69841ecd91f45d8/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-ragdolla-4dbb5916ed8a1606a040653de700ad90c6bd17e2.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-ragdolla-4dbb5916ed8a1606a040653de700ad90c6bd17e2/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-ragdolla-4dbb5916ed8a1606a040653de700ad90c6bd17e2/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (stack.c) :warning:


<i>La condizione va controllata all'interno di un ciclo "while". Nei programmi basati su libreria PThreads, il monitor è sempre di tipo signal-and-continue.
</i>
(codice errore: esercitazione-3-threads-ragdolla-4dbb5916ed8a1606a040653de700ad90c6bd17e2.una_struttura_dati_stack_thread-safe..test.using-if)


```
void StackPush(Stack * s, Elem e) {

	/* TBD: Aggiungere la sincronizzazione */

	pthread_mutex_lock(&s->mutex);

	if (s->in_uso == s->dim){
		pthread_cond_wait(&s->cv_scrittori, &s->mutex);
	}

	s->dati[s->testa] = e;
	s->testa++;
	s->in_uso++;

	printf("Inserimento: %d\n", e);

	pthread_cond_signal(&s->cv_lettore);

	pthread_mutex_unlock(&s->mutex);

	


}

```



<i>La condizione va controllata all'interno di un ciclo "while". Nei programmi basati su libreria PThreads, il monitor è sempre di tipo signal-and-continue.
</i>
(codice errore: esercitazione-3-threads-ragdolla-4dbb5916ed8a1606a040653de700ad90c6bd17e2.una_struttura_dati_stack_thread-safe..test.using-if)


```
Elem StackPop(Stack * s) {

	int elemento;

	/* TBD: Aggiungere la sincronizzazione */

	pthread_mutex_lock(&s->mutex);

	if (s->in_uso == 0){
		pthread_cond_wait(&s->cv_lettore, &s->mutex);
	}


	s->testa--;
	elemento = s->dati[s->testa];
	s->in_uso--;

	printf("Prelievo: %d\n", elemento);

	pthread_cond_signal(&s->cv_scrittori);

	pthread_mutex_unlock(&s->mutex);

	return elemento;
}

```



esercitazione-3-threads-ragdolla-4dbb5916ed8a1606a040653de700ad90c6bd17e2/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-ragdolla-565be8a28c1501626c5095aef1fbd3c25575bf6d.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-ragdolla-565be8a28c1501626c5095aef1fbd3c25575bf6d/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-ragdolla-565be8a28c1501626c5095aef1fbd3c25575bf6d/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto delle produzioni e delle consumazioni :warning:
esercitazione-3-threads-ragdolla-565be8a28c1501626c5095aef1fbd3c25575bf6d/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-ragdolla-c52cb30a63e7cedb5d9ba12bc1ec7f300fccd46b.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-ragdolla-c52cb30a63e7cedb5d9ba12bc1ec7f300fccd46b/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-ragdolla-c52cb30a63e7cedb5d9ba12bc1ec7f300fccd46b/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-ragdolla-c52cb30a63e7cedb5d9ba12bc1ec7f300fccd46b/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-ragdolla-dde7326b94179317d3404092e8a9112ae617d5ed/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-ragdolla-dde7326b94179317d3404092e8a9112ae617d5ed/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-ragdolla-dde7326b94179317d3404092e8a9112ae617d5ed/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-valeannu-2408b907d13d22dda347f3c900005df58ff57f4c/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-valeannu-2408b907d13d22dda347f3c900005df58ff57f4c/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-valeannu-2408b907d13d22dda347f3c900005df58ff57f4c/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-valeannu-5f891e3ccf8a69c2650e8173eb69461c5742ad43/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-valeannu-5f891e3ccf8a69c2650e8173eb69461c5742ad43/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-valeannu-5f891e3ccf8a69c2650e8173eb69461c5742ad43/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-valeannu-d788d7cf2e6b397cf72b134880f00b108258f870/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-valeannu-d788d7cf2e6b397cf72b134880f00b108258f870/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-valeannu-d788d7cf2e6b397cf72b134880f00b108258f870/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-Vecchions110-1d21253105cee36a4cf5beef1d8175e4a924aa39.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-Vecchions110-1d21253105cee36a4cf5beef1d8175e4a924aa39/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-3-threads-Vecchions110-1d21253105cee36a4cf5beef1d8175e4a924aa39/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-Vecchions110-1d21253105cee36a4cf5beef1d8175e4a924aa39/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (prodcons.c) :warning:


<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */
	//variabili produttore consumatore con priorità
	int testa;
	int coda;
	int count;
	int threads_prio_1;// thread sospesi alta priorità
	int threads_prio_2;// thrad sospesi bassa priorità
	
	//----
	pthread_mutex_t mutex; // mutex gestione monitor
	pthread_cond_t cons; // per la gestione del consumatore
	pthread_cond_t prod; // per la gestione del prod
        pthread_cond_t prod_prio; // per la gestione del produttore con priorità
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif


void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
    pthread_mutex_init(&(p->mutex),NULL);
    pthread_cond_init(&(p->prod),NULL);
    pthread_cond_init(&(p->cons),NULL);
    pthread_cond_init(&(p->prod_prio),NULL);
    p->testa=0;
    p->coda=0;
    p->count=0;
    p->threads_prio_1=0;
    p->threads_prio_2=0;

}

void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
    pthread_mutex_destroy(&(p->mutex));
    pthread_cond_destroy(&(p->prod));
     pthread_cond_destroy(&(p->prod_prio));
    pthread_cond_destroy(&(p->cons));

}

void produci_alta_prio(PriorityProdCons* p){

	int value;
      pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
     
  
   while(p->count == 3)
   {
	p->threads_prio_1++; // incremento se il produttore con pirorità con trova spazio
	printf("Produttore tipo 1 in attesa \n");
	pthread_cond_wait(&(p->prod_prio),&(p->mutex)); // mettiti in attesa di un consumatore
	printf("Produttore tipo 1 in risveglio \n");
	// qui arrivo nel momento in cui si risveglia 
	p->threads_prio_1--;// ora ho lo spazio ci metto il valore prodotto al suo interno
   }


	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa]=value; // assegna il valore prodotto al buffer
	p->testa=(p->testa+1)%3; // CODA CIRCOLARE
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);
	
	// risveglio un eventuale consumatore in attesa
	pthread_cond_signal(&(p->cons));

 pthread_mutex_unlock(&(p->mutex));
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;
  pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	while(p->count == 3 || p->threads_prio_1)
	{	p->threads_prio_2++; // invremento il numero di produttori sospesi con bassa priorità
		pthread_cond_wait(&(p->prod),&(p->mutex));
		// qui vado solo nel momento in cui si sblocca
		
		p->threads_prio_2--; // decremento il numero di produttori con bassa priorità sospesi	
	}
	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa]=value;
	p->testa=(p->testa+1)%3;
	p->count++; // ho inserito un nuovo valore il conteggio deve aumentare

	printf("Produttore tipo 2 ha prodotto %d\n", value);
	pthread_cond_signal(&(p->cons));

  pthread_mutex_unlock(&(p->mutex)); // uscita dal monitor
}




void consuma(PriorityProdCons* p){

	int value;
        pthread_mutex_lock(&(p->mutex));
	printf("Consumatore accede al monitor\n");

	
    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */


	/* Consumazione */
	while(p->count==0)
	{ 
		pthread_cond_wait(&(p->cons),&(p->mutex));
		// se arrivo qui il consumatore è stato reattivato	
			
	}

	value = p->buffer[p->coda];    /* TBD */
	p->coda=(p->coda+1)%3;
	p->count--;
	printf("Consumatore ha consumato %d\n", value);
	
	// devo risvegliare il produttore ma quale ?
	
	if(p->threads_prio_1>0)
	{
		printf("Consumatore risveglia produttore con priorità\n");
		pthread_cond_signal(&(p->prod_prio));	
	}
	if(p->threads_prio_2>0)
	{
		printf("Consumatore risveglia produttore \n");
		pthread_cond_signal(&(p->prod));
	}

     pthread_mutex_unlock(&(p->mutex));
}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <stdlib.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */
	//variabili produttore consumatore con priorità
	int testa;
	int coda;
	int count;
	int threads_prio_1;// thread sospesi alta priorità
	int threads_prio_2;// thrad sospesi bassa priorità
	
	//----
	pthread_mutex_t mutex; // mutex gestione monitor
	pthread_cond_t cons; // per la gestione del consumatore
	pthread_cond_t prod; // per la gestione del prod
        pthread_cond_t prod_prio; // per la gestione del produttore con priorità
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif


void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
    pthread_mutex_init(&(p->mutex),NULL);
    pthread_cond_init(&(p->prod),NULL);
    pthread_cond_init(&(p->cons),NULL);
    pthread_cond_init(&(p->prod_prio),NULL);
    p->testa=0;
    p->coda=0;
    p->count=0;
    p->threads_prio_1=0;
    p->threads_prio_2=0;

}

void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
    pthread_mutex_destroy(&(p->mutex));
    pthread_cond_destroy(&(p->prod));
     pthread_cond_destroy(&(p->prod_prio));
    pthread_cond_destroy(&(p->cons));

}

void produci_alta_prio(PriorityProdCons* p){

	int value;
      pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
     
  
   while(p->count == 3)
   {
	p->threads_prio_1++; // incremento se il produttore con pirorità con trova spazio
	printf("Produttore tipo 1 in attesa \n");
	pthread_cond_wait(&(p->prod_prio),&(p->mutex)); // mettiti in attesa di un consumatore
	printf("Produttore tipo 1 in risveglio \n");
	// qui arrivo nel momento in cui si risveglia 
	p->threads_prio_1--;// ora ho lo spazio ci metto il valore prodotto al suo interno
   }


	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa]=value; // assegna il valore prodotto al buffer
	p->testa=(p->testa+1)%3; // CODA CIRCOLARE
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);
	
	// risveglio un eventuale consumatore in attesa
	pthread_cond_signal(&(p->cons));

 pthread_mutex_unlock(&(p->mutex));
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;
  pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	while(p->count == 3 || p->threads_prio_1)
	{	p->threads_prio_2++; // invremento il numero di produttori sospesi con bassa priorità
		pthread_cond_wait(&(p->prod),&(p->mutex));
		// qui vado solo nel momento in cui si sblocca
		
		p->threads_prio_2--; // decremento il numero di produttori con bassa priorità sospesi	
	}
	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa]=value;
	p->testa=(p->testa+1)%3;
	p->count++; // ho inserito un nuovo valore il conteggio deve aumentare

	printf("Produttore tipo 2 ha prodotto %d\n", value);
	pthread_cond_signal(&(p->cons));

  pthread_mutex_unlock(&(p->mutex)); // uscita dal monitor
}




void consuma(PriorityProdCons* p){

	int value;
        pthread_mutex_lock(&(p->mutex));
	printf("Consumatore accede al monitor\n");

	
    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */


	/* Consumazione */
	while(p->count==0)
	{ 
		pthread_cond_wait(&(p->cons),&(p->mutex));
		// se arrivo qui il consumatore è stato reattivato	
			
	}

	value = p->buffer[p->coda];    /* TBD */
	p->coda=(p->coda+1)%3;
	p->count--;
	printf("Consumatore ha consumato %d\n", value);
	
	// devo risvegliare il produttore ma quale ?
	
	if(p->threads_prio_1>0)
	{
		printf("Consumatore risveglia produttore con priorità\n");
		pthread_cond_signal(&(p->prod_prio));	
	}
	if(p->threads_prio_2>0)
	{
		printf("Consumatore risveglia produttore \n");
		pthread_cond_signal(&(p->prod));
	}

     pthread_mutex_unlock(&(p->mutex));
}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */
	//variabili produttore consumatore con priorità
	int testa;
	int coda;
	int count;
	int threads_prio_1;// thread sospesi alta priorità
	int threads_prio_2;// thrad sospesi bassa priorità
	
	//----
	pthread_mutex_t mutex; // mutex gestione monitor
	pthread_cond_t cons; // per la gestione del consumatore
	pthread_cond_t prod; // per la gestione del prod
        pthread_cond_t prod_prio; // per la gestione del produttore con priorità
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif


void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
    pthread_mutex_init(&(p->mutex),NULL);
    pthread_cond_init(&(p->prod),NULL);
    pthread_cond_init(&(p->cons),NULL);
    pthread_cond_init(&(p->prod_prio),NULL);
    p->testa=0;
    p->coda=0;
    p->count=0;
    p->threads_prio_1=0;
    p->threads_prio_2=0;

}

void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
    pthread_mutex_destroy(&(p->mutex));
    pthread_cond_destroy(&(p->prod));
     pthread_cond_destroy(&(p->prod_prio));
    pthread_cond_destroy(&(p->cons));

}

void produci_alta_prio(PriorityProdCons* p){

	int value;
      pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
     
  
   while(p->count == 3)
   {
	p->threads_prio_1++; // incremento se il produttore con pirorità con trova spazio
	printf("Produttore tipo 1 in attesa \n");
	pthread_cond_wait(&(p->prod_prio),&(p->mutex)); // mettiti in attesa di un consumatore
	printf("Produttore tipo 1 in risveglio \n");
	// qui arrivo nel momento in cui si risveglia 
	p->threads_prio_1--;// ora ho lo spazio ci metto il valore prodotto al suo interno
   }


	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa]=value; // assegna il valore prodotto al buffer
	p->testa=(p->testa+1)%3; // CODA CIRCOLARE
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);
	
	// risveglio un eventuale consumatore in attesa
	pthread_cond_signal(&(p->cons));

 pthread_mutex_unlock(&(p->mutex));
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;
  pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	while(p->count == 3 || p->threads_prio_1)
	{	p->threads_prio_2++; // invremento il numero di produttori sospesi con bassa priorità
		pthread_cond_wait(&(p->prod),&(p->mutex));
		// qui vado solo nel momento in cui si sblocca
		
		p->threads_prio_2--; // decremento il numero di produttori con bassa priorità sospesi	
	}
	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa]=value;
	p->testa=(p->testa+1)%3;
	p->count++; // ho inserito un nuovo valore il conteggio deve aumentare

	printf("Produttore tipo 2 ha prodotto %d\n", value);
	pthread_cond_signal(&(p->cons));

  pthread_mutex_unlock(&(p->mutex)); // uscita dal monitor
}




void consuma(PriorityProdCons* p){

	int value;
        pthread_mutex_lock(&(p->mutex));
	printf("Consumatore accede al monitor\n");

	
    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */


	/* Consumazione */
	while(p->count==0)
	{ 
		pthread_cond_wait(&(p->cons),&(p->mutex));
		// se arrivo qui il consumatore è stato reattivato	
			
	}

	value = p->buffer[p->coda];    /* TBD */
	p->coda=(p->coda+1)%3;
	p->count--;
	printf("Consumatore ha consumato %d\n", value);
	
	// devo risvegliare il produttore ma quale ?
	
	if(p->threads_prio_1>0)
	{
		printf("Consumatore risveglia produttore con priorità\n");
		pthread_cond_signal(&(p->prod_prio));	
	}
	if(p->threads_prio_2>0)
	{
		printf("Consumatore risveglia produttore \n");
		pthread_cond_signal(&(p->prod));
	}

     pthread_mutex_unlock(&(p->mutex));
}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <sys/types.h>
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */
	//variabili produttore consumatore con priorità
	int testa;
	int coda;
	int count;
	int threads_prio_1;// thread sospesi alta priorità
	int threads_prio_2;// thrad sospesi bassa priorità
	
	//----
	pthread_mutex_t mutex; // mutex gestione monitor
	pthread_cond_t cons; // per la gestione del consumatore
	pthread_cond_t prod; // per la gestione del prod
        pthread_cond_t prod_prio; // per la gestione del produttore con priorità
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif


void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
    pthread_mutex_init(&(p->mutex),NULL);
    pthread_cond_init(&(p->prod),NULL);
    pthread_cond_init(&(p->cons),NULL);
    pthread_cond_init(&(p->prod_prio),NULL);
    p->testa=0;
    p->coda=0;
    p->count=0;
    p->threads_prio_1=0;
    p->threads_prio_2=0;

}

void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
    pthread_mutex_destroy(&(p->mutex));
    pthread_cond_destroy(&(p->prod));
     pthread_cond_destroy(&(p->prod_prio));
    pthread_cond_destroy(&(p->cons));

}

void produci_alta_prio(PriorityProdCons* p){

	int value;
      pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
     
  
   while(p->count == 3)
   {
	p->threads_prio_1++; // incremento se il produttore con pirorità con trova spazio
	printf("Produttore tipo 1 in attesa \n");
	pthread_cond_wait(&(p->prod_prio),&(p->mutex)); // mettiti in attesa di un consumatore
	printf("Produttore tipo 1 in risveglio \n");
	// qui arrivo nel momento in cui si risveglia 
	p->threads_prio_1--;// ora ho lo spazio ci metto il valore prodotto al suo interno
   }


	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa]=value; // assegna il valore prodotto al buffer
	p->testa=(p->testa+1)%3; // CODA CIRCOLARE
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);
	
	// risveglio un eventuale consumatore in attesa
	pthread_cond_signal(&(p->cons));

 pthread_mutex_unlock(&(p->mutex));
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;
  pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	while(p->count == 3 || p->threads_prio_1)
	{	p->threads_prio_2++; // invremento il numero di produttori sospesi con bassa priorità
		pthread_cond_wait(&(p->prod),&(p->mutex));
		// qui vado solo nel momento in cui si sblocca
		
		p->threads_prio_2--; // decremento il numero di produttori con bassa priorità sospesi	
	}
	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa]=value;
	p->testa=(p->testa+1)%3;
	p->count++; // ho inserito un nuovo valore il conteggio deve aumentare

	printf("Produttore tipo 2 ha prodotto %d\n", value);
	pthread_cond_signal(&(p->cons));

  pthread_mutex_unlock(&(p->mutex)); // uscita dal monitor
}




void consuma(PriorityProdCons* p){

	int value;
        pthread_mutex_lock(&(p->mutex));
	printf("Consumatore accede al monitor\n");

	
    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */


	/* Consumazione */
	while(p->count==0)
	{ 
		pthread_cond_wait(&(p->cons),&(p->mutex));
		// se arrivo qui il consumatore è stato reattivato	
			
	}

	value = p->buffer[p->coda];    /* TBD */
	p->coda=(p->coda+1)%3;
	p->count--;
	printf("Consumatore ha consumato %d\n", value);
	
	// devo risvegliare il produttore ma quale ?
	
	if(p->threads_prio_1>0)
	{
		printf("Consumatore risveglia produttore con priorità\n");
		pthread_cond_signal(&(p->prod_prio));	
	}
	if(p->threads_prio_2>0)
	{
		printf("Consumatore risveglia produttore \n");
		pthread_cond_signal(&(p->prod));
	}

     pthread_mutex_unlock(&(p->mutex));
}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
#include <unistd.h>

#ifndef __PROCEDURE_H

#include <pthread.h>


typedef struct{

	int buffer[3];

	/* TBD: Aggiungere ulteriori variabili per la sincronizzazione */
	//variabili produttore consumatore con priorità
	int testa;
	int coda;
	int count;
	int threads_prio_1;// thread sospesi alta priorità
	int threads_prio_2;// thrad sospesi bassa priorità
	
	//----
	pthread_mutex_t mutex; // mutex gestione monitor
	pthread_cond_t cons; // per la gestione del consumatore
	pthread_cond_t prod; // per la gestione del prod
        pthread_cond_t prod_prio; // per la gestione del produttore con priorità
} PriorityProdCons;


void inizializza_prod_cons(PriorityProdCons * p);
void produci_alta_prio(PriorityProdCons * p);
void produci_bassa_prio(PriorityProdCons * p);
void consuma(PriorityProdCons * p);
void rimuovi_prod_cons(PriorityProdCons * p);

#endif


void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
    pthread_mutex_init(&(p->mutex),NULL);
    pthread_cond_init(&(p->prod),NULL);
    pthread_cond_init(&(p->cons),NULL);
    pthread_cond_init(&(p->prod_prio),NULL);
    p->testa=0;
    p->coda=0;
    p->count=0;
    p->threads_prio_1=0;
    p->threads_prio_2=0;

}

void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
    pthread_mutex_destroy(&(p->mutex));
    pthread_cond_destroy(&(p->prod));
     pthread_cond_destroy(&(p->prod_prio));
    pthread_cond_destroy(&(p->cons));

}

void produci_alta_prio(PriorityProdCons* p){

	int value;
      pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
     
  
   while(p->count == 3)
   {
	p->threads_prio_1++; // incremento se il produttore con pirorità con trova spazio
	printf("Produttore tipo 1 in attesa \n");
	pthread_cond_wait(&(p->prod_prio),&(p->mutex)); // mettiti in attesa di un consumatore
	printf("Produttore tipo 1 in risveglio \n");
	// qui arrivo nel momento in cui si risveglia 
	p->threads_prio_1--;// ora ho lo spazio ci metto il valore prodotto al suo interno
   }


	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa]=value; // assegna il valore prodotto al buffer
	p->testa=(p->testa+1)%3; // CODA CIRCOLARE
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);
	
	// risveglio un eventuale consumatore in attesa
	pthread_cond_signal(&(p->cons));

 pthread_mutex_unlock(&(p->mutex));
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;
  pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	while(p->count == 3 || p->threads_prio_1)
	{	p->threads_prio_2++; // invremento il numero di produttori sospesi con bassa priorità
		pthread_cond_wait(&(p->prod),&(p->mutex));
		// qui vado solo nel momento in cui si sblocca
		
		p->threads_prio_2--; // decremento il numero di produttori con bassa priorità sospesi	
	}
	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa]=value;
	p->testa=(p->testa+1)%3;
	p->count++; // ho inserito un nuovo valore il conteggio deve aumentare

	printf("Produttore tipo 2 ha prodotto %d\n", value);
	pthread_cond_signal(&(p->cons));

  pthread_mutex_unlock(&(p->mutex)); // uscita dal monitor
}




void consuma(PriorityProdCons* p){

	int value;
        pthread_mutex_lock(&(p->mutex));
	printf("Consumatore accede al monitor\n");

	
    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */


	/* Consumazione */
	while(p->count==0)
	{ 
		pthread_cond_wait(&(p->cons),&(p->mutex));
		// se arrivo qui il consumatore è stato reattivato	
			
	}

	value = p->buffer[p->coda];    /* TBD */
	p->coda=(p->coda+1)%3;
	p->count--;
	printf("Consumatore ha consumato %d\n", value);
	
	// devo risvegliare il produttore ma quale ?
	
	if(p->threads_prio_1>0)
	{
		printf("Consumatore risveglia produttore con priorità\n");
		pthread_cond_signal(&(p->prod_prio));	
	}
	if(p->threads_prio_2>0)
	{
		printf("Consumatore risveglia produttore \n");
		pthread_cond_signal(&(p->prod));
	}

     pthread_mutex_unlock(&(p->mutex));
}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void inizializza_prod_cons(PriorityProdCons* p){

    /* TBD: Inizializzare tutte le variabili del monitor */
    pthread_mutex_init(&(p->mutex),NULL);
    pthread_cond_init(&(p->prod),NULL);
    pthread_cond_init(&(p->cons),NULL);
    pthread_cond_init(&(p->prod_prio),NULL);
    p->testa=0;
    p->coda=0;
    p->count=0;
    p->threads_prio_1=0;
    p->threads_prio_2=0;

}

void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
    pthread_mutex_destroy(&(p->mutex));
    pthread_cond_destroy(&(p->prod));
     pthread_cond_destroy(&(p->prod_prio));
    pthread_cond_destroy(&(p->cons));

}

void produci_alta_prio(PriorityProdCons* p){

	int value;
      pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
     
  
   while(p->count == 3)
   {
	p->threads_prio_1++; // incremento se il produttore con pirorità con trova spazio
	printf("Produttore tipo 1 in attesa \n");
	pthread_cond_wait(&(p->prod_prio),&(p->mutex)); // mettiti in attesa di un consumatore
	printf("Produttore tipo 1 in risveglio \n");
	// qui arrivo nel momento in cui si risveglia 
	p->threads_prio_1--;// ora ho lo spazio ci metto il valore prodotto al suo interno
   }


	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa]=value; // assegna il valore prodotto al buffer
	p->testa=(p->testa+1)%3; // CODA CIRCOLARE
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);
	
	// risveglio un eventuale consumatore in attesa
	pthread_cond_signal(&(p->cons));

 pthread_mutex_unlock(&(p->mutex));
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;
  pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	while(p->count == 3 || p->threads_prio_1)
	{	p->threads_prio_2++; // invremento il numero di produttori sospesi con bassa priorità
		pthread_cond_wait(&(p->prod),&(p->mutex));
		// qui vado solo nel momento in cui si sblocca
		
		p->threads_prio_2--; // decremento il numero di produttori con bassa priorità sospesi	
	}
	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa]=value;
	p->testa=(p->testa+1)%3;
	p->count++; // ho inserito un nuovo valore il conteggio deve aumentare

	printf("Produttore tipo 2 ha prodotto %d\n", value);
	pthread_cond_signal(&(p->cons));

  pthread_mutex_unlock(&(p->mutex)); // uscita dal monitor
}




void consuma(PriorityProdCons* p){

	int value;
        pthread_mutex_lock(&(p->mutex));
	printf("Consumatore accede al monitor\n");

	
    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */


	/* Consumazione */
	while(p->count==0)
	{ 
		pthread_cond_wait(&(p->cons),&(p->mutex));
		// se arrivo qui il consumatore è stato reattivato	
			
	}

	value = p->buffer[p->coda];    /* TBD */
	p->coda=(p->coda+1)%3;
	p->count--;
	printf("Consumatore ha consumato %d\n", value);
	
	// devo risvegliare il produttore ma quale ?
	
	if(p->threads_prio_1>0)
	{
		printf("Consumatore risveglia produttore con priorità\n");
		pthread_cond_signal(&(p->prod_prio));	
	}
	if(p->threads_prio_2>0)
	{
		printf("Consumatore risveglia produttore \n");
		pthread_cond_signal(&(p->prod));
	}

     pthread_mutex_unlock(&(p->mutex));
}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void rimuovi_prod_cons(PriorityProdCons* p){

    /* TBD: Disattivare mutex e variabili condition */
    pthread_mutex_destroy(&(p->mutex));
    pthread_cond_destroy(&(p->prod));
     pthread_cond_destroy(&(p->prod_prio));
    pthread_cond_destroy(&(p->cons));

}

void produci_alta_prio(PriorityProdCons* p){

	int value;
      pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
     
  
   while(p->count == 3)
   {
	p->threads_prio_1++; // incremento se il produttore con pirorità con trova spazio
	printf("Produttore tipo 1 in attesa \n");
	pthread_cond_wait(&(p->prod_prio),&(p->mutex)); // mettiti in attesa di un consumatore
	printf("Produttore tipo 1 in risveglio \n");
	// qui arrivo nel momento in cui si risveglia 
	p->threads_prio_1--;// ora ho lo spazio ci metto il valore prodotto al suo interno
   }


	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa]=value; // assegna il valore prodotto al buffer
	p->testa=(p->testa+1)%3; // CODA CIRCOLARE
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);
	
	// risveglio un eventuale consumatore in attesa
	pthread_cond_signal(&(p->cons));

 pthread_mutex_unlock(&(p->mutex));
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;
  pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	while(p->count == 3 || p->threads_prio_1)
	{	p->threads_prio_2++; // invremento il numero di produttori sospesi con bassa priorità
		pthread_cond_wait(&(p->prod),&(p->mutex));
		// qui vado solo nel momento in cui si sblocca
		
		p->threads_prio_2--; // decremento il numero di produttori con bassa priorità sospesi	
	}
	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa]=value;
	p->testa=(p->testa+1)%3;
	p->count++; // ho inserito un nuovo valore il conteggio deve aumentare

	printf("Produttore tipo 2 ha prodotto %d\n", value);
	pthread_cond_signal(&(p->cons));

  pthread_mutex_unlock(&(p->mutex)); // uscita dal monitor
}




void consuma(PriorityProdCons* p){

	int value;
        pthread_mutex_lock(&(p->mutex));
	printf("Consumatore accede al monitor\n");

	
    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */


	/* Consumazione */
	while(p->count==0)
	{ 
		pthread_cond_wait(&(p->cons),&(p->mutex));
		// se arrivo qui il consumatore è stato reattivato	
			
	}

	value = p->buffer[p->coda];    /* TBD */
	p->coda=(p->coda+1)%3;
	p->count--;
	printf("Consumatore ha consumato %d\n", value);
	
	// devo risvegliare il produttore ma quale ?
	
	if(p->threads_prio_1>0)
	{
		printf("Consumatore risveglia produttore con priorità\n");
		pthread_cond_signal(&(p->prod_prio));	
	}
	if(p->threads_prio_2>0)
	{
		printf("Consumatore risveglia produttore \n");
		pthread_cond_signal(&(p->prod));
	}

     pthread_mutex_unlock(&(p->mutex));
}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void produci_alta_prio(PriorityProdCons* p){

	int value;
      pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 1 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     *
     *      Si introduca nel monitor una variabile "threads_prio_1"
     *      per contare il numero di produttori sospesi ad alta priorità.
     */
     
  
   while(p->count == 3)
   {
	p->threads_prio_1++; // incremento se il produttore con pirorità con trova spazio
	printf("Produttore tipo 1 in attesa \n");
	pthread_cond_wait(&(p->prod_prio),&(p->mutex)); // mettiti in attesa di un consumatore
	printf("Produttore tipo 1 in risveglio \n");
	// qui arrivo nel momento in cui si risveglia 
	p->threads_prio_1--;// ora ho lo spazio ci metto il valore prodotto al suo interno
   }


	/* Produzione */

	value = rand() % 12;
	p->buffer[p->testa]=value; // assegna il valore prodotto al buffer
	p->testa=(p->testa+1)%3; // CODA CIRCOLARE
	p->count++;

	printf("Produttore tipo 1 ha prodotto %d\n", value);
	
	// risveglio un eventuale consumatore in attesa
	pthread_cond_signal(&(p->cons));

 pthread_mutex_unlock(&(p->mutex));
}




void produci_bassa_prio(PriorityProdCons* p){

	int value;
  pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	while(p->count == 3 || p->threads_prio_1)
	{	p->threads_prio_2++; // invremento il numero di produttori sospesi con bassa priorità
		pthread_cond_wait(&(p->prod),&(p->mutex));
		// qui vado solo nel momento in cui si sblocca
		
		p->threads_prio_2--; // decremento il numero di produttori con bassa priorità sospesi	
	}
	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa]=value;
	p->testa=(p->testa+1)%3;
	p->count++; // ho inserito un nuovo valore il conteggio deve aumentare

	printf("Produttore tipo 2 ha prodotto %d\n", value);
	pthread_cond_signal(&(p->cons));

  pthread_mutex_unlock(&(p->mutex)); // uscita dal monitor
}




void consuma(PriorityProdCons* p){

	int value;
        pthread_mutex_lock(&(p->mutex));
	printf("Consumatore accede al monitor\n");

	
    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */


	/* Consumazione */
	while(p->count==0)
	{ 
		pthread_cond_wait(&(p->cons),&(p->mutex));
		// se arrivo qui il consumatore è stato reattivato	
			
	}

	value = p->buffer[p->coda];    /* TBD */
	p->coda=(p->coda+1)%3;
	p->count--;
	printf("Consumatore ha consumato %d\n", value);
	
	// devo risvegliare il produttore ma quale ?
	
	if(p->threads_prio_1>0)
	{
		printf("Consumatore risveglia produttore con priorità\n");
		pthread_cond_signal(&(p->prod_prio));	
	}
	if(p->threads_prio_2>0)
	{
		printf("Consumatore risveglia produttore \n");
		pthread_cond_signal(&(p->prod));
	}

     pthread_mutex_unlock(&(p->mutex));
}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void produci_bassa_prio(PriorityProdCons* p){

	int value;
  pthread_mutex_lock(&(p->mutex));
	printf("Produttore tipo 2 accede al monitor\n");


    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
	 *
	 *      I produttori a bassa priorità devono sospendersi sia nel caso di vettore
	 *      di buffer già pieno, sia nel caso vi siano produttori ad alta priorità già
	 *      in attesa.
     *
     *      Si introduca nel monitor una variabile "threads_prio_2"
     *      per contare il numero di produttori sospesi a bassa priorità.
     */
	while(p->count == 3 || p->threads_prio_1)
	{	p->threads_prio_2++; // invremento il numero di produttori sospesi con bassa priorità
		pthread_cond_wait(&(p->prod),&(p->mutex));
		// qui vado solo nel momento in cui si sblocca
		
		p->threads_prio_2--; // decremento il numero di produttori con bassa priorità sospesi	
	}
	/* Produzione */

	value = 13 + (rand() % 12);
	p->buffer[p->testa]=value;
	p->testa=(p->testa+1)%3;
	p->count++; // ho inserito un nuovo valore il conteggio deve aumentare

	printf("Produttore tipo 2 ha prodotto %d\n", value);
	pthread_cond_signal(&(p->cons));

  pthread_mutex_unlock(&(p->mutex)); // uscita dal monitor
}




void consuma(PriorityProdCons* p){

	int value;
        pthread_mutex_lock(&(p->mutex));
	printf("Consumatore accede al monitor\n");

	
    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */


	/* Consumazione */
	while(p->count==0)
	{ 
		pthread_cond_wait(&(p->cons),&(p->mutex));
		// se arrivo qui il consumatore è stato reattivato	
			
	}

	value = p->buffer[p->coda];    /* TBD */
	p->coda=(p->coda+1)%3;
	p->count--;
	printf("Consumatore ha consumato %d\n", value);
	
	// devo risvegliare il produttore ma quale ?
	
	if(p->threads_prio_1>0)
	{
		printf("Consumatore risveglia produttore con priorità\n");
		pthread_cond_signal(&(p->prod_prio));	
	}
	if(p->threads_prio_2>0)
	{
		printf("Consumatore risveglia produttore \n");
		pthread_cond_signal(&(p->prod));
	}

     pthread_mutex_unlock(&(p->mutex));
}

```



<i>È necessario controllare che il consumatore verifichi la presenza di produttori ad alta priorità in attesa e risvegliare loro. Altrimenti, il consumatore risveglia un produttore a bassa priorità.
</i>
(codice errore: esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb.produttore-consumatore_con_priorita..test.wake-producers-inorder-up)


```
void consuma(PriorityProdCons* p){

	int value;
        pthread_mutex_lock(&(p->mutex));
	printf("Consumatore accede al monitor\n");

	
    /* TBD: Implementare la sincronizzazione secondo lo schema del
     *      produttore-consumatore con vettore di buffer circolare.
     */


	/* Consumazione */
	while(p->count==0)
	{ 
		pthread_cond_wait(&(p->cons),&(p->mutex));
		// se arrivo qui il consumatore è stato reattivato	
			
	}

	value = p->buffer[p->coda];    /* TBD */
	p->coda=(p->coda+1)%3;
	p->count--;
	printf("Consumatore ha consumato %d\n", value);
	
	// devo risvegliare il produttore ma quale ?
	
	if(p->threads_prio_1>0)
	{
		printf("Consumatore risveglia produttore con priorità\n");
		pthread_cond_signal(&(p->prod_prio));	
	}
	if(p->threads_prio_2>0)
	{
		printf("Consumatore risveglia produttore \n");
		pthread_cond_signal(&(p->prod));
	}

     pthread_mutex_unlock(&(p->mutex));
}

```



esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-Vecchions110-4c48d3228e159953e8e2df3a7c1d5e566bf7accb/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-Vecchions110-ed602c4031f4619e91ba4e555f2b9a4e81950026/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-Vecchions110-ed602c4031f4619e91ba4e555f2b9a4e81950026/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-Vecchions110-ed602c4031f4619e91ba4e555f2b9a4e81950026/una_struttura_dati_stack_thread-safe

## Esercizio lettori-scrittori su più oggetti monitor

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>In conclusione al programma è sempre buona norma rilasciare le aree di memoria precedentemente utilizzate e riservate
</i>
(codice errore: esercitazione-3-threads-Vecchions110-ffc781077f8a68167c6b59ce7d865d9b7feb107b.lettori-scrittori_su_piu_oggetti_monitor..test.13-missing-free)


```
int main() {

	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_JOINABLE);

	srand(time(NULL));

	struct monitor* m[4];	// array di 4 oggetti-monitor, per gestire i 4 treni

	pthread_t capo[4];		// 4 capitreno
	pthread_t viagg[10];	// 10 viaggiatori

	int i;

	/* TBD: Allocare 4 istanze di monitor,
	 *		assegnarle all'array m[], e
	 *		inizializzarle con inizializza()
	 */

	// assegno un id ad ogni treno
	m[0]->id_treno=1;
	m[1]->id_treno=2;
	m[2]->id_treno=3;
	m[3]->id_treno=4;


	/* TBD: Avviare 4 thread, facendogli eseguire la funzione Capotreno(),
	 * 	e passando ad ognuno una istanza di monitor diversa m[i]
	 */


	/* TBD: Avviare 10 thread, facendogli eseguire la funzione Viaggiatori(),
	 *      e passando ad ognuno una istanza di monitor diversa, da scegliere
	 *      a caso con "rand() % 4"
	 */


	/* TBD: Effettuare la join con i thread "Capotreno" */

	/* TBD: Effettuare la join con i thread "Viaggiatori" */

	/* TBD: Disattivazione delle 4 istanze di monitor con rimuovi() */

	/* TBD: Deallocazione delle 4 istanze di monitor con free() */


	return 0;
}

```



esercitazione-3-threads-Vecchions110-ffc781077f8a68167c6b59ce7d865d9b7feb107b/lettori-scrittori_su_piu_oggetti_monitor

## Esercizio produttore-consumatore con priorità, con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-Vecchions110-ffc781077f8a68167c6b59ce7d865d9b7feb107b/produttore-consumatore_con_priorita

## Esercizio struttura dati thread-safe

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-3-threads-Vecchions110-ffc781077f8a68167c6b59ce7d865d9b7feb107b/una_struttura_dati_stack_thread-safe

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-4ebfbc118033186f7560337851845aabf0303fcf/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-4ebfbc118033186f7560337851845aabf0303fcf/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-4ebfbc118033186f7560337851845aabf0303fcf/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (server.c) :warning:


<i>È richiesto che ogni server usi una coda msg_id distinta dagli altri server. Usare ftok() non è corretto, perchè se ftok() viene chiamata più volte con gli stessi parametri, si ottiene sempre la stessa chiave e quindi la stessa coda. È sufficiente usare qui IPC_PRIVATE.
</i>
(codice errore: esercitazione-4-messaggi-alicecapolongo-4ebfbc118033186f7560337851845aabf0303fcf.server_sincroni_multipli..test.private_message_queue_server)


```
    key_t msg_key = ftok (".", 'c');/* TBD: Definire una chiave per la coda */

    int msg_id = msgget(msg_key, IPC_CREAT|0644); /* TBD: Ottenere la coda privata del server */

```



esercitazione-4-messaggi-alicecapolongo-4ebfbc118033186f7560337851845aabf0303fcf/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-559e2ae646212e3815e947665a60af69dd4adc9a/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-559e2ae646212e3815e947665a60af69dd4adc9a/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-559e2ae646212e3815e947665a60af69dd4adc9a/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-alicecapolongo-559e2ae646212e3815e947665a60af69dd4adc9a/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-61c0291d046eb06fde989c000a46647826f66aac/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-61c0291d046eb06fde989c000a46647826f66aac/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-61c0291d046eb06fde989c000a46647826f66aac/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-alicecapolongo-61c0291d046eb06fde989c000a46647826f66aac/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-8b35f164dc7104783c9e2b542f29d43da43c4602/grafo_delle_dipendenze

## Esercizio load balancing

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-alicecapolongo-8b35f164dc7104783c9e2b542f29d43da43c4602/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-alicecapolongo-8b35f164dc7104783c9e2b542f29d43da43c4602/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-alicecapolongo-8b35f164dc7104783c9e2b542f29d43da43c4602/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-bd3123d3a7e1756812181d87c29fbd009dff4ade/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-bd3123d3a7e1756812181d87c29fbd009dff4ade/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-bd3123d3a7e1756812181d87c29fbd009dff4ade/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-alicecapolongo-bd3123d3a7e1756812181d87c29fbd009dff4ade/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-be62b769195f69a76d03dee4e0c80cc4cd9d0282/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-be62b769195f69a76d03dee4e0c80cc4cd9d0282/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-be62b769195f69a76d03dee4e0c80cc4cd9d0282/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-be62b769195f69a76d03dee4e0c80cc4cd9d0282/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-c265a92fd21f79ca3a6e817535914cb7f8273131/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-c265a92fd21f79ca3a6e817535914cb7f8273131/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-alicecapolongo-c265a92fd21f79ca3a6e817535914cb7f8273131/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-alicecapolongo-c265a92fd21f79ca3a6e817535914cb7f8273131/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-d22401267de81ae24936fae67cf66beff819bf77/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-d22401267de81ae24936fae67cf66beff819bf77/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-d22401267de81ae24936fae67cf66beff819bf77/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-d22401267de81ae24936fae67cf66beff819bf77/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-alicecapolongo-fced3de69ab1db776ee1c580f9d2e3510141aa51/grafo_delle_dipendenze

## Esercizio load balancing

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-alicecapolongo-fced3de69ab1db776ee1c580f9d2e3510141aa51/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-alicecapolongo-fced3de69ab1db776ee1c580f9d2e3510141aa51/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-alicecapolongo-fced3de69ab1db776ee1c580f9d2e3510141aa51/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-550fc3edc3db448cac47ba4384a2208419ef6707/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-550fc3edc3db448cac47ba4384a2208419ef6707/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>È necessario eliminare le code di messaggio al termine dell'esecuzione utilizzando msgctl() con IPC_RMID.
</i>
(codice errore: esercitazione-4-messaggi-Beccio-san-550fc3edc3db448cac47ba4384a2208419ef6707.registro_distribuito..test.remove_queue)


```
int main() {


    /* TBD: Creare le code di messaggi, e avviare i processi server e registro,
     *      facendogli chiamare le funzioni server() e registro().
     */

    int id_coda_registro_richieste = msgget('a', IPC_CREAT | 0644)/* TBD */;

    if(id_coda_registro_richieste < 0){
        perror("Errore msgget coda richieste");
        exit(1);
    }

    int id_coda_registro_risposte = msgget('b', IPC_CREAT | 0644)/* TBD */;

    if(id_coda_registro_risposte < 0){
        perror("Errore msgget coda risposte");
        exit(1);
    }

    /* TBD: Avviare un processo figlio, e chiamare la funzione:
     *      registro(id_coda_registro_richieste,id_coda_registro_risposte);
     */
    pid_t p = fork();

    if(p < 0){
        perror("Errore fork registro");
        exit(1);
    }
    if(p == 0){
        registro(id_coda_registro_richieste, id_coda_registro_risposte);
        exit(0);
    }

    for (int i = 0; i < 2; i++)
    {
        /* TBD: Avviare un processo figlio, e chiamare la funzione:
         *      server(id_coda_registro_richieste, id_coda_registro_risposte, i);
         */
        
        p = fork();
        
        if(p < 0){
            perror("Errore fork server");
            exit(1);
        }
        if(p == 0){
            server(id_coda_registro_richieste, id_coda_registro_risposte, i+1);
            exit(0);
        }
        
    }


    /* NOTA: Lasciare questa sleep per avviare i client con un ritardo,
     *       in modo da dare il tempo ai server di registrarsi sul processo registro.
     */

    sleep(2);

    for (int i = 0; i < 3; i++)
    {
        /* TBD: Avviare un processo figlio, e chiamare la funzione:
         *      client(id_coda_registro_richieste, id_coda_registro_risposte);
         */

        p = fork();

        if(p < 0){
            perror("Errore fork client");
            exit(1);
        }
        if(p == 0){
            client(id_coda_registro_richieste, id_coda_registro_risposte);
            exit(0);
        }
    }


    /* TBD: Attendere la terminazione dei processi client */
    int status;
    for(int i = 0; i < 3; i++){
        p  = wait(&status);
        if(p < 0){
            perror("Errore wait client");
            exit(1);
        }

        if(WIF4ED(status) && W4STATUS(status)==0){
            printf("Processo client %d terminato correttamente\n", p);
        }
        else
            printf("Processo client %d terminato in modo anomalo\n", p);
    }


    printf("Padre: Invio messaggio 4\n");

    /* TBD: Inviare un messaggio di tipo 4 al registro,
     *      tramite "id_coda_registro_richieste"
     */
    messaggio_registro msg;
    msg.type = 4;
    msgsnd(id_coda_registro_richieste, &msg, sizeof(messaggio_registro)-sizeof(long), 0);

    /* TBD: Attendere la terminazione dei processi server e del processo registro */
    p  = wait(&status);
    if(p < 0){
        perror("Errore wait registro");
        exit(1);
    }

    if(WIF4ED(status) && W4STATUS(status)==0){
        printf("Processo registro %d terminato correttamente\n", p);
    }
    else
        printf("Processo registro %d terminato in modo anomalo\n", p);
    

    for(int i = 0; i < 2; i++){
        p  = wait(&status);
        if(p < 0){
            perror("Errore wait server");
            exit(1);
        }

        if(WIF4ED(status) && W4STATUS(status)==0){
            printf("Processo server %d terminato correttamente\n", p);
        }
        else
            printf("Processo server %d terminato in modo anomalo\n", p);
    }



    /* TBD: Rimuovere le code */
    int ret;
    ret = msgctl(id_coda_registro_richieste, IPC_RMID, NULL);
    if(ret < 0){
        perror("Errore msgctl coda richieste");
        exit(1);
    }
    ret = msgctl(id_coda_registro_risposte, IPC_RMID, NULL);
    if(ret < 0){
        perror("Errore msgctl coda risposte");
        exit(1);
    }
}

```



esercitazione-4-messaggi-Beccio-san-550fc3edc3db448cac47ba4384a2208419ef6707/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-550fc3edc3db448cac47ba4384a2208419ef6707/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-55273704c6faa4b520e87019938c7ecbdd6f9652/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-55273704c6faa4b520e87019938c7ecbdd6f9652/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-Beccio-san-55273704c6faa4b520e87019938c7ecbdd6f9652/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-55273704c6faa4b520e87019938c7ecbdd6f9652/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-699848e9038b5504608d9400c411e3b9a8403407/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-699848e9038b5504608d9400c411e3b9a8403407/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>È necessario eliminare le code di messaggio al termine dell'esecuzione utilizzando msgctl() con IPC_RMID.
</i>
(codice errore: esercitazione-4-messaggi-Beccio-san-699848e9038b5504608d9400c411e3b9a8403407.registro_distribuito..test.remove_queue)


```
int main() {


    /* TBD: Creare le code di messaggi, e avviare i processi server e registro,
     *      facendogli chiamare le funzioni server() e registro().
     */

    int id_coda_registro_richieste = msgget('a', IPC_CREAT | 0644)/* TBD */;

    if(id_coda_registro_richieste < 0){
        perror("Errore msgget coda richieste");
        exit(1);
    }

    int id_coda_registro_risposte = msgget('b', IPC_CREAT | 0644)/* TBD */;

    if(id_coda_registro_risposte < 0){
        perror("Errore msgget coda risposte");
        exit(1);
    }

    /* TBD: Avviare un processo figlio, e chiamare la funzione:
     *      registro(id_coda_registro_richieste,id_coda_registro_risposte);
     */
    pid_t p = fork();

    if(p < 0){
        perror("Errore fork registro");
        exit(1);
    }
    if(p == 0){
        registro(id_coda_registro_richieste, id_coda_registro_risposte);
        exit(0);
    }

    for (int i = 0; i < 2; i++)
    {
        /* TBD: Avviare un processo figlio, e chiamare la funzione:
         *      server(id_coda_registro_richieste, id_coda_registro_risposte, i);
         */
        
        p = fork();
        
        if(p < 0){
            perror("Errore fork server");
            exit(1);
        }
        if(p == 0){
            server(id_coda_registro_richieste, id_coda_registro_risposte, i+1);
            exit(0);
        }
        
    }


    /* NOTA: Lasciare questa sleep per avviare i client con un ritardo,
     *       in modo da dare il tempo ai server di registrarsi sul processo registro.
     */

    sleep(2);

    for (int i = 0; i < 3; i++)
    {
        /* TBD: Avviare un processo figlio, e chiamare la funzione:
         *      client(id_coda_registro_richieste, id_coda_registro_risposte);
         */

        p = fork();

        if(p < 0){
            perror("Errore fork client");
            exit(1);
        }
        if(p == 0){
            client(id_coda_registro_richieste, id_coda_registro_risposte);
            exit(0);
        }
    }


    /* TBD: Attendere la terminazione dei processi client */
    int status;
    for(int i = 0; i < 3; i++){
        p  = wait(&status);
        if(p < 0){
            perror("Errore wait client");
            exit(1);
        }

        if(WIF4ED(status) && W4STATUS(status)==0){
            printf("Processo client %d terminato correttamente\n", p);
        }
        else
            printf("Processo client %d terminato in modo anomalo\n", p);
    }


    printf("Padre: Invio messaggio 4\n");

    /* TBD: Inviare un messaggio di tipo 4 al registro,
     *      tramite "id_coda_registro_richieste"
     */
    messaggio_registro msg;
    msg.type = 4;
    msgsnd(id_coda_registro_richieste, &msg, sizeof(messaggio_registro)-sizeof(long), 0);

    /* TBD: Attendere la terminazione dei processi server e del processo registro */
    p  = wait(&status);
    if(p < 0){
        perror("Errore wait registro");
        exit(1);
    }

    if(WIF4ED(status) && W4STATUS(status)==0){
        printf("Processo registro %d terminato correttamente\n", p);
    }
    else
        printf("Processo registro %d terminato in modo anomalo\n", p);
    

    for(int i = 0; i < 2; i++){
        p  = wait(&status);
        if(p < 0){
            perror("Errore wait server");
            exit(1);
        }

        if(WIF4ED(status) && W4STATUS(status)==0){
            printf("Processo server %d terminato correttamente\n", p);
        }
        else
            printf("Processo server %d terminato in modo anomalo\n", p);
    }



    /* TBD: Rimuovere le code */
    /*int ret;
    ret = */
    msgctl(id_coda_registro_richieste, IPC_RMID, NULL);
    /* if(ret < 0){
        perror("Errore msgctl coda richieste");
        exit(1);
    }
    ret =*/ 
    msgctl(id_coda_registro_risposte, IPC_RMID, NULL);
    /* if(ret < 0){
        perror("Errore msgctl coda risposte");
        exit(1);
    }
    */
}

```



esercitazione-4-messaggi-Beccio-san-699848e9038b5504608d9400c411e3b9a8403407/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-699848e9038b5504608d9400c411e3b9a8403407/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-711343162308cb5e4529b77d2cf986a78fc3d9dc/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-711343162308cb5e4529b77d2cf986a78fc3d9dc/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (main.c) :warning:


<i>È necessario eliminare le code di messaggio al termine dell'esecuzione utilizzando msgctl() con IPC_RMID.
</i>
(codice errore: esercitazione-4-messaggi-Beccio-san-711343162308cb5e4529b77d2cf986a78fc3d9dc.registro_distribuito..test.remove_queue)


```
int main() {


    /* TBD: Creare le code di messaggi, e avviare i processi server e registro,
     *      facendogli chiamare le funzioni server() e registro().
     */

    int id_coda_registro_richieste = msgget('a', IPC_CREAT | 0644)/* TBD */;

    if(id_coda_registro_richieste < 0){
        perror("Errore msgget coda richieste");
        exit(1);
    }

    int id_coda_registro_risposte = msgget('b', IPC_CREAT | 0644)/* TBD */;

    if(id_coda_registro_risposte < 0){
        perror("Errore msgget coda risposte");
        exit(1);
    }

    /* TBD: Avviare un processo figlio, e chiamare la funzione:
     *      registro(id_coda_registro_richieste,id_coda_registro_risposte);
     */
    pid_t p = fork();

    if(p < 0){
        perror("Errore fork registro");
        exit(1);
    }
    if(p == 0){
        registro(id_coda_registro_richieste, id_coda_registro_risposte);
        exit(0);
    }

    for (int i = 0; i < 2; i++)
    {
        /* TBD: Avviare un processo figlio, e chiamare la funzione:
         *      server(id_coda_registro_richieste, id_coda_registro_risposte, i);
         */
        
        p = fork();
        
        if(p < 0){
            perror("Errore fork server");
            exit(1);
        }
        if(p == 0){
            server(id_coda_registro_richieste, id_coda_registro_risposte, i+1);
            exit(0);
        }
        
    }


    /* NOTA: Lasciare questa sleep per avviare i client con un ritardo,
     *       in modo da dare il tempo ai server di registrarsi sul processo registro.
     */

    sleep(2);

    for (int i = 0; i < 3; i++)
    {
        /* TBD: Avviare un processo figlio, e chiamare la funzione:
         *      client(id_coda_registro_richieste, id_coda_registro_risposte);
         */

        p = fork();

        if(p < 0){
            perror("Errore fork client");
            exit(1);
        }
        if(p == 0){
            client(id_coda_registro_richieste, id_coda_registro_risposte);
            exit(0);
        }
    }


    /* TBD: Attendere la terminazione dei processi client */
    int status;
    for(int i = 0; i < 3; i++){
        p  = wait(&status);
        if(p < 0){
            perror("Errore wait client");
            exit(1);
        }

        if(WIF4ED(status) && W4STATUS(status)==0){
            printf("Processo client %d terminato correttamente\n", p);
        }
        else
            printf("Processo client %d terminato in modo anomalo\n", p);
    }


    printf("Padre: Invio messaggio 4\n");

    /* TBD: Inviare un messaggio di tipo 4 al registro,
     *      tramite "id_coda_registro_richieste"
     */
    messaggio_registro msg;
    msg.type = 4;
    msgsnd(id_coda_registro_richieste, &msg, sizeof(messaggio_registro)-sizeof(long), 0);

    /* TBD: Attendere la terminazione dei processi server e del processo registro */
    p  = wait(&status);
    if(p < 0){
        perror("Errore wait registro");
        exit(1);
    }

    if(WIF4ED(status) && W4STATUS(status)==0){
        printf("Processo registro %d terminato correttamente\n", p);
    }
    else
        printf("Processo registro %d terminato in modo anomalo\n", p);
    

    for(int i = 0; i < 2; i++){
        p  = wait(&status);
        if(p < 0){
            perror("Errore wait server");
            exit(1);
        }

        if(WIF4ED(status) && W4STATUS(status)==0){
            printf("Processo server %d terminato correttamente\n", p);
        }
        else
            printf("Processo server %d terminato in modo anomalo\n", p);
    }



    /* TBD: Rimuovere le code */
    int ret;
    ret = msgctl(id_coda_registro_richieste, IPC_RMID, NULL);
    if(ret < 0){
        perror("Errore msgctl coda richieste");
        exit(1);
    }
    ret = msgctl(id_coda_registro_risposte, IPC_RMID, NULL);
    if(ret < 0){
        perror("Errore msgctl coda risposte");
        exit(1);
    }
}

```



esercitazione-4-messaggi-Beccio-san-711343162308cb5e4529b77d2cf986a78fc3d9dc/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-711343162308cb5e4529b77d2cf986a78fc3d9dc/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-7b083fbf29afd2c843b0dbff4abecb26ac81f62f/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-7b083fbf29afd2c843b0dbff4abecb26ac81f62f/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-Beccio-san-7b083fbf29afd2c843b0dbff4abecb26ac81f62f/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-7b083fbf29afd2c843b0dbff4abecb26ac81f62f/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-b19c599114df638561f744b5e58eec123290ff65/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-b19c599114df638561f744b5e58eec123290ff65/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-b19c599114df638561f744b5e58eec123290ff65/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-b19c599114df638561f744b5e58eec123290ff65/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Beccio-san-b7293b8ece3ab6ca20bf5c69423b1bf6c60709d6/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-b7293b8ece3ab6ca20bf5c69423b1bf6c60709d6/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Beccio-san-b7293b8ece3ab6ca20bf5c69423b1bf6c60709d6/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-Beccio-san-b7293b8ece3ab6ca20bf5c69423b1bf6c60709d6/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Beccio-san-cc70ab690fa3eae16e36f11929251668ed66e47c/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-cc70ab690fa3eae16e36f11929251668ed66e47c/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Beccio-san-cc70ab690fa3eae16e36f11929251668ed66e47c/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-cc70ab690fa3eae16e36f11929251668ed66e47c/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-e3d132f737f108f89c08c230890b32f06aac6f52/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-e3d132f737f108f89c08c230890b32f06aac6f52/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-Beccio-san-e3d132f737f108f89c08c230890b32f06aac6f52/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-e3d132f737f108f89c08c230890b32f06aac6f52/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Beccio-san-ea2ce9f4572f8c8e8e16b478467c58fd25aaaea2/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Beccio-san-ea2ce9f4572f8c8e8e16b478467c58fd25aaaea2/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Beccio-san-ea2ce9f4572f8c8e8e16b478467c58fd25aaaea2/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Beccio-san-ea2ce9f4572f8c8e8e16b478467c58fd25aaaea2/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-CarmineAprea-3a6caf4686ef5ebe62a0d8a4318ec3d06be7eb74/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-3a6caf4686ef5ebe62a0d8a4318ec3d06be7eb74/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-3a6caf4686ef5ebe62a0d8a4318ec3d06be7eb74/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-3a6caf4686ef5ebe62a0d8a4318ec3d06be7eb74/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-CarmineAprea-59c488ffbb44093e181437f62bde31945174fd82/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-59c488ffbb44093e181437f62bde31945174fd82/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-CarmineAprea-59c488ffbb44093e181437f62bde31945174fd82/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-CarmineAprea-59c488ffbb44093e181437f62bde31945174fd82/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-CarmineAprea-6f750281c1716281afc4218c1255e3b0ed6dcab1/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-6f750281c1716281afc4218c1255e3b0ed6dcab1/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-CarmineAprea-6f750281c1716281afc4218c1255e3b0ed6dcab1/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-CarmineAprea-6f750281c1716281afc4218c1255e3b0ed6dcab1/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-CarmineAprea-70734de10ecd5f2854ebc9e935827087e533f90c/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-70734de10ecd5f2854ebc9e935827087e533f90c/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-70734de10ecd5f2854ebc9e935827087e533f90c/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-CarmineAprea-70734de10ecd5f2854ebc9e935827087e533f90c/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-CarmineAprea-80de86670cc142aa04dbe1811cca8e47bc15d681/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-80de86670cc142aa04dbe1811cca8e47bc15d681/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-80de86670cc142aa04dbe1811cca8e47bc15d681/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (serversync.c) :warning:


<i>Prima di inviare con msgsnd(), req_msg deve essere riempita con il campo tipo pari al proprio PID, in modo da poter realizzare la ricezione della risposta in modo selettivo (vedi esempio visto a lezione).
</i>
(codice errore: esercitazione-4-messaggi-CarmineAprea-80de86670cc142aa04dbe1811cca8e47bc15d681.server_sincroni_multipli..test.send_sinc_empty_msg)


```
    int ret;

    pid_t pid = getpid();

    REQUEST_TO_SEND richiesta;
    richiesta.type=pid;

    printf("[%d] Client: invio request-to-send\n", pid);

    /* TBD: Inviare il messaggio REQUEST TO SEND, includendo il PID del client nel messaggio */
    

    ret = msgsnd(req_id,&richiesta,sizeof(REQUEST_TO_SEND)-sizeof(long),0);/* TBD */

```



esercitazione-4-messaggi-CarmineAprea-80de86670cc142aa04dbe1811cca8e47bc15d681/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-CarmineAprea-89a3cf97820273f7ccdbd68db5b37881dccaaa89/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-89a3cf97820273f7ccdbd68db5b37881dccaaa89/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-89a3cf97820273f7ccdbd68db5b37881dccaaa89/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (serversync.c) :warning:


<i>Prima di inviare con msgsnd(), req_msg deve essere riempita con il campo tipo pari al proprio PID, in modo da poter realizzare la ricezione della risposta in modo selettivo (vedi esempio visto a lezione).
</i>
(codice errore: esercitazione-4-messaggi-CarmineAprea-89a3cf97820273f7ccdbd68db5b37881dccaaa89.server_sincroni_multipli..test.send_sinc_empty_msg)


```
    int ret;

    pid_t pid = getpid();



    printf("[%d] Client: invio request-to-send\n", pid);

    /* TBD: Inviare il messaggio REQUEST TO SEND, includendo il PID del client nel messaggio */
    REQUEST_TO_SEND richiesta;
    richiesta.type=pid;

    ret = msgsnd(req_id,&richiesta,sizeof(REQUEST_TO_SEND)-sizeof(long),0);/* TBD */

```



esercitazione-4-messaggi-CarmineAprea-89a3cf97820273f7ccdbd68db5b37881dccaaa89/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-CarmineAprea-ac13097d4d02865e08cdab3917d117ec805b7e51/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-ac13097d4d02865e08cdab3917d117ec805b7e51/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-ac13097d4d02865e08cdab3917d117ec805b7e51/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-CarmineAprea-ac13097d4d02865e08cdab3917d117ec805b7e51/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-ba2d1f3469891e14a5a4d83fe6010bc7b31a3c8e/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-ba2d1f3469891e14a5a4d83fe6010bc7b31a3c8e/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-ba2d1f3469891e14a5a4d83fe6010bc7b31a3c8e/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-ba2d1f3469891e14a5a4d83fe6010bc7b31a3c8e/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-CarmineAprea-f2c664c8b3167a678d6c871fa1f459fdbc6772cd/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-f2c664c8b3167a678d6c871fa1f459fdbc6772cd/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-CarmineAprea-f2c664c8b3167a678d6c871fa1f459fdbc6772cd/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-CarmineAprea-f2c664c8b3167a678d6c871fa1f459fdbc6772cd/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-criccardoo-1d33be1d66537e25a3ba846290914dd5977e7c84/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-1d33be1d66537e25a3ba846290914dd5977e7c84/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-criccardoo-1d33be1d66537e25a3ba846290914dd5977e7c84/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-1d33be1d66537e25a3ba846290914dd5977e7c84/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-2ea212c518aa88d44f07c94a5b9fa2f201746604/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-2ea212c518aa88d44f07c94a5b9fa2f201746604/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-criccardoo-2ea212c518aa88d44f07c94a5b9fa2f201746604/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-2ea212c518aa88d44f07c94a5b9fa2f201746604/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-criccardoo-41b3bf2173ea866506f6cc2eb35bfa59e8fd9055/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-41b3bf2173ea866506f6cc2eb35bfa59e8fd9055/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-criccardoo-41b3bf2173ea866506f6cc2eb35bfa59e8fd9055/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-criccardoo-41b3bf2173ea866506f6cc2eb35bfa59e8fd9055/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-8a1d4d592e844baa41c9fbaea3dd9952f4f3b34b/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-8a1d4d592e844baa41c9fbaea3dd9952f4f3b34b/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-8a1d4d592e844baa41c9fbaea3dd9952f4f3b34b/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-8a1d4d592e844baa41c9fbaea3dd9952f4f3b34b/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-criccardoo-8e592ae7fa318838f87254d124fc1378a38d614e/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-8e592ae7fa318838f87254d124fc1378a38d614e/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-criccardoo-8e592ae7fa318838f87254d124fc1378a38d614e/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-8e592ae7fa318838f87254d124fc1378a38d614e/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-b8e3c1ed76838fda050b3e0a6e3c22f728be290d/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-b8e3c1ed76838fda050b3e0a6e3c22f728be290d/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-criccardoo-b8e3c1ed76838fda050b3e0a6e3c22f728be290d/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-b8e3c1ed76838fda050b3e0a6e3c22f728be290d/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-criccardoo-c8b7b3563bab1ce20448ff90e1a2c522be46b524/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-c8b7b3563bab1ce20448ff90e1a2c522be46b524/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-criccardoo-c8b7b3563bab1ce20448ff90e1a2c522be46b524/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (server.c) :warning:


<i>È richiesto che ogni server usi una coda msg_id distinta dagli altri server. Usare ftok() non è corretto, perchè se ftok() viene chiamata più volte con gli stessi parametri, si ottiene sempre la stessa chiave e quindi la stessa coda. È sufficiente usare qui IPC_PRIVATE.
</i>
(codice errore: esercitazione-4-messaggi-criccardoo-c8b7b3563bab1ce20448ff90e1a2c522be46b524.server_sincroni_multipli..test.private_message_queue_server)


```
    key_t msg_key = ftok(".",'c');
    /* TBD: Definire una chiave per la coda */;

    int msg_id = msgget(msg_key,IPC_CREAT | 0664);

```



esercitazione-4-messaggi-criccardoo-c8b7b3563bab1ce20448ff90e1a2c522be46b524/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-criccardoo-f424c87f078a547d7a269d3d4e5caa831a42c4f9/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-criccardoo-f424c87f078a547d7a269d3d4e5caa831a42c4f9/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-criccardoo-f424c87f078a547d7a269d3d4e5caa831a42c4f9/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-criccardoo-f424c87f078a547d7a269d3d4e5caa831a42c4f9/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-giuseppe-maglione-235a30e2da88fd58caba8ca4a82d80df59a85764/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-giuseppe-maglione-235a30e2da88fd58caba8ca4a82d80df59a85764/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-giuseppe-maglione-235a30e2da88fd58caba8ca4a82d80df59a85764/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-giuseppe-maglione-235a30e2da88fd58caba8ca4a82d80df59a85764/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-giuseppe-maglione-399357d2293787e74100ec23d03c6904018d2dcd/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-giuseppe-maglione-399357d2293787e74100ec23d03c6904018d2dcd/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-giuseppe-maglione-399357d2293787e74100ec23d03c6904018d2dcd/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-giuseppe-maglione-399357d2293787e74100ec23d03c6904018d2dcd/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-giuseppe-maglione-4ed4d566fdaeafbe8af9bccd409c862075011197/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-giuseppe-maglione-4ed4d566fdaeafbe8af9bccd409c862075011197/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-giuseppe-maglione-4ed4d566fdaeafbe8af9bccd409c862075011197/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-giuseppe-maglione-4ed4d566fdaeafbe8af9bccd409c862075011197/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-giuseppe-maglione-7f13ecc997a13fe5e61addd7be3302adb935e88e/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-giuseppe-maglione-7f13ecc997a13fe5e61addd7be3302adb935e88e/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-giuseppe-maglione-7f13ecc997a13fe5e61addd7be3302adb935e88e/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-giuseppe-maglione-7f13ecc997a13fe5e61addd7be3302adb935e88e/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-giuseppe-maglione-a40f288269ae9601f874a6efa33ab4811165d6cf/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-giuseppe-maglione-a40f288269ae9601f874a6efa33ab4811165d6cf/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-giuseppe-maglione-a40f288269ae9601f874a6efa33ab4811165d6cf/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (server.c) :warning:


<i>È richiesto che ogni server usi una coda msg_id distinta dagli altri server. Usare ftok() non è corretto, perchè se ftok() viene chiamata più volte con gli stessi parametri, si ottiene sempre la stessa chiave e quindi la stessa coda. È sufficiente usare qui IPC_PRIVATE.
</i>
(codice errore: esercitazione-4-messaggi-giuseppe-maglione-a40f288269ae9601f874a6efa33ab4811165d6cf.server_sincroni_multipli..test.private_message_queue_server)


```
    key_t msg_key = ftok(".", 'c');

    /* TBD: Ottenere la coda privata del server */
    int msg_id = msgget(msg_key, IPC_CREAT | 0644);

```



esercitazione-4-messaggi-giuseppe-maglione-a40f288269ae9601f874a6efa33ab4811165d6cf/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-giuseppe-maglione-c99fbbd6b019399cb5832059873cd83fed953be9/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-giuseppe-maglione-c99fbbd6b019399cb5832059873cd83fed953be9/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-giuseppe-maglione-c99fbbd6b019399cb5832059873cd83fed953be9/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-giuseppe-maglione-c99fbbd6b019399cb5832059873cd83fed953be9/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-lorenzoalessandrella-42133d237764c63c348d92680cf1719dbff6c083/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-42133d237764c63c348d92680cf1719dbff6c083/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-lorenzoalessandrella-42133d237764c63c348d92680cf1719dbff6c083/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-lorenzoalessandrella-42133d237764c63c348d92680cf1719dbff6c083/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-4542a76ed794a3cff1de10e95b9dfe0cad7d2c46/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-4542a76ed794a3cff1de10e95b9dfe0cad7d2c46/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-4542a76ed794a3cff1de10e95b9dfe0cad7d2c46/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-lorenzoalessandrella-4542a76ed794a3cff1de10e95b9dfe0cad7d2c46/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-7970ca68ceeab359bd16884807bd4754c38b6a83/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-7970ca68ceeab359bd16884807bd4754c38b6a83/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-7970ca68ceeab359bd16884807bd4754c38b6a83/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (serversync.c) :warning:


<i>Prima di inviare con msgsnd(), req_msg deve essere riempita con il campo tipo pari al proprio PID, in modo da poter realizzare la ricezione della risposta in modo selettivo (vedi esempio visto a lezione).
</i>
(codice errore: esercitazione-4-messaggi-lorenzoalessandrella-7970ca68ceeab359bd16884807bd4754c38b6a83.server_sincroni_multipli..test.send_sinc_empty_msg)


```
    int ret;

    pid_t pid = getpid();

    /* TBD: Inviare il messaggio REQUEST TO SEND */

    struct req_to_send req;
    req.type = pid;

    printf("[%d] Client: invio request-to-send, type=%ld\n", getpid(), req.type /* TBD */);

    ret = msgsnd(req_id, &req, sizeof(struct req_to_send) - sizeof(long), 0); /* TBD */

```



esercitazione-4-messaggi-lorenzoalessandrella-7970ca68ceeab359bd16884807bd4754c38b6a83/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-81ec242eebce83c9789b09c66e5b38b0c7eeb01b/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-81ec242eebce83c9789b09c66e5b38b0c7eeb01b/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-81ec242eebce83c9789b09c66e5b38b0c7eeb01b/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-81ec242eebce83c9789b09c66e5b38b0c7eeb01b/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-lorenzoalessandrella-840934f6b63da40bee02de8ded7a39157a4276f4/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-840934f6b63da40bee02de8ded7a39157a4276f4/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-lorenzoalessandrella-840934f6b63da40bee02de8ded7a39157a4276f4/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-lorenzoalessandrella-840934f6b63da40bee02de8ded7a39157a4276f4/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-lorenzoalessandrella-a82e1ad0eef50bfa35d7dbd9be5a031d37fdccfa/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-a82e1ad0eef50bfa35d7dbd9be5a031d37fdccfa/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-lorenzoalessandrella-a82e1ad0eef50bfa35d7dbd9be5a031d37fdccfa/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-lorenzoalessandrella-a82e1ad0eef50bfa35d7dbd9be5a031d37fdccfa/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-lorenzoalessandrella-c96ad2ab6b3719fa33443e104732b043aacb6bbc/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-c96ad2ab6b3719fa33443e104732b043aacb6bbc/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-lorenzoalessandrella-c96ad2ab6b3719fa33443e104732b043aacb6bbc/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-lorenzoalessandrella-c96ad2ab6b3719fa33443e104732b043aacb6bbc/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-fa85379ffd5a138c482ab74b93d7744a1826e21a/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-lorenzoalessandrella-fa85379ffd5a138c482ab74b93d7744a1826e21a/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-lorenzoalessandrella-fa85379ffd5a138c482ab74b93d7744a1826e21a/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-lorenzoalessandrella-fa85379ffd5a138c482ab74b93d7744a1826e21a/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-075b2a297172d7775a87d2fa1026915f237af77b/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-075b2a297172d7775a87d2fa1026915f237af77b/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-luke-the-coder-075b2a297172d7775a87d2fa1026915f237af77b/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-075b2a297172d7775a87d2fa1026915f237af77b/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-luke-the-coder-15f85fcdc96e39c61a5c981113477f8852834fcb/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-15f85fcdc96e39c61a5c981113477f8852834fcb/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-luke-the-coder-15f85fcdc96e39c61a5c981113477f8852834fcb/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-luke-the-coder-15f85fcdc96e39c61a5c981113477f8852834fcb/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-luke-the-coder-27df285a8549e224083c48fd6c6cbf4f47d6e029/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-27df285a8549e224083c48fd6c6cbf4f47d6e029/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-luke-the-coder-27df285a8549e224083c48fd6c6cbf4f47d6e029/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-luke-the-coder-27df285a8549e224083c48fd6c6cbf4f47d6e029/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-4c321a6a40343086a30787a4224c2d1265593f8c/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-4c321a6a40343086a30787a4224c2d1265593f8c/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-4c321a6a40343086a30787a4224c2d1265593f8c/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-4c321a6a40343086a30787a4224c2d1265593f8c/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-606e32537afb6e9583dfa8e547b4bd574863020e/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-606e32537afb6e9583dfa8e547b4bd574863020e/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-luke-the-coder-606e32537afb6e9583dfa8e547b4bd574863020e/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-606e32537afb6e9583dfa8e547b4bd574863020e/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-9319ab1227214393749fa2271fa9fbf9150ca5ec/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-9319ab1227214393749fa2271fa9fbf9150ca5ec/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: È necessario deallocare le risorse IPC al termine della esecuzione :warning:
esercitazione-4-messaggi-luke-the-coder-9319ab1227214393749fa2271fa9fbf9150ca5ec/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-9319ab1227214393749fa2271fa9fbf9150ca5ec/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-afab1a467d9e8d46125c1b7773aa10287a6752c3/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-afab1a467d9e8d46125c1b7773aa10287a6752c3/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-luke-the-coder-afab1a467d9e8d46125c1b7773aa10287a6752c3/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-afab1a467d9e8d46125c1b7773aa10287a6752c3/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-luke-the-coder-bf70939381ce4d55272bab021541a1effe357cf1/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-bf70939381ce4d55272bab021541a1effe357cf1/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-luke-the-coder-bf70939381ce4d55272bab021541a1effe357cf1/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-luke-the-coder-bf70939381ce4d55272bab021541a1effe357cf1/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-luke-the-coder-d440ee194dfbc858ef321f0bb714a6064f253cc3/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-d440ee194dfbc858ef321f0bb714a6064f253cc3/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-luke-the-coder-d440ee194dfbc858ef321f0bb714a6064f253cc3/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-d440ee194dfbc858ef321f0bb714a6064f253cc3/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-luke-the-coder-e6698af6e2ee2a9d469064ffc2a0fefb3164758e/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-e6698af6e2ee2a9d469064ffc2a0fefb3164758e/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-luke-the-coder-e6698af6e2ee2a9d469064ffc2a0fefb3164758e/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-luke-the-coder-e6698af6e2ee2a9d469064ffc2a0fefb3164758e/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-562e43f203b13a33b664529225d73c0bca5bbc81/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-562e43f203b13a33b664529225d73c0bca5bbc81/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Mashtemah-562e43f203b13a33b664529225d73c0bca5bbc81/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-562e43f203b13a33b664529225d73c0bca5bbc81/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Mashtemah-64de9bc309167bc97e4a579723738ec9feef99f4/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-64de9bc309167bc97e4a579723738ec9feef99f4/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Mashtemah-64de9bc309167bc97e4a579723738ec9feef99f4/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-64de9bc309167bc97e4a579723738ec9feef99f4/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Mashtemah-6d489efddbc1f2401e73c01cc00b02db291cba13/grafo_delle_dipendenze

## Esercizio load balancing

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-Mashtemah-6d489efddbc1f2401e73c01cc00b02db291cba13/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Mashtemah-6d489efddbc1f2401e73c01cc00b02db291cba13/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Mashtemah-6d489efddbc1f2401e73c01cc00b02db291cba13/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Mashtemah-70f1e7c2a1886bdf6e9731872d29ef4bb7334bda/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-70f1e7c2a1886bdf6e9731872d29ef4bb7334bda/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Mashtemah-70f1e7c2a1886bdf6e9731872d29ef4bb7334bda/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (serversync.c) :warning:


<i>L’esercizio prevede che il mittente riceva lo ok-to-send tramite ricezione selettiva, basata sul PID del processo mittente.
</i>
(codice errore: esercitazione-4-messaggi-Mashtemah-70f1e7c2a1886bdf6e9731872d29ef4bb7334bda.server_sincroni_multipli..test.pid_selective_sinc_2)


```
void send_sinc(int ok_id, int req_id, messaggio * msg)
{

    int ret;

    /* TBD: Inviare il messaggio REQUEST TO SEND */

    req_to_send req;

    req.type = getpid();
    req.pid = getpid();

    printf("[%d] Client: invio request-to-send, type=%ld\n", getpid(), req.type/* TBD */);

    ret = msgsnd(req_id, &req, sizeof(req_to_send) - sizeof(long), 0); /* TBD */

    if (ret < 0)
    {
        perror("Errore msgsnd (request-to-send)");
        exit(1);
    }


    /* TBD: Ricevere il messaggio OK TO SEND */

    ok_to_send ok;

    printf("[%d] Client: in attesa di ok-to-send...\n", getpid());

    ret = msgrcv(ok_id, &ok, sizeof(ok_to_send) - sizeof(long), req.pid, 0); /* TBD */

    if (ret < 0)
    {
        perror("Errore msgrcv (ok-to-send)");
        exit(1);
    }

    printf("[%d] Client: ricevuto ok-to-send... type=%ld, id_coda=%d\n", getpid(), ok.type /* TBD */, ok.id /* TBD */);




    /* TBD: Inviare il messaggio al server */

    int id_coda = ok.id; /* TBD */

    printf("[%d] Client: invio messaggio, coda=%d, type=%ld, valore=%d\n", getpid(), id_coda, msg->type, msg->val);

    ret = msgsnd(id_coda, msg, sizeof(messaggio) - sizeof(long), 0); /* TBD */

    if (ret < 0)
    {
        perror("Errore msgsnd (coda messaggi)");
        exit(1);
    }

}

```



esercitazione-4-messaggi-Mashtemah-70f1e7c2a1886bdf6e9731872d29ef4bb7334bda/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-b43cea17f7ccb50728a83e1a0fc0f4b8b3503465/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-b43cea17f7ccb50728a83e1a0fc0f4b8b3503465/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-b43cea17f7ccb50728a83e1a0fc0f4b8b3503465/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-b43cea17f7ccb50728a83e1a0fc0f4b8b3503465/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-ce2b71ff6ebcf56bb3c73663cfda25130f366b04/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-ce2b71ff6ebcf56bb3c73663cfda25130f366b04/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (server.c) :warning:


<i>Quando il server riceve un messaggio di tipo SERVICE, occorre che aggiorni il valore della "risorsa" con il valore ricevuto nel messaggio.
</i>
(codice errore: esercitazione-4-messaggi-Mashtemah-ce2b71ff6ebcf56bb3c73663cfda25130f366b04.registro_distribuito..test.server_status_service)


```
void server(int id_coda_registro_richieste, int id_coda_registro_risposte, int id_server) {

    int risorsa = 0;

    int id_coda_server = msgget(IPC_PRIVATE, IPC_CREAT | 0664); /* TBD */

    printf("Server: Invio messaggio 1 (id_server=%d, id_coda=%d)\n", id_server, id_coda_server);

    /* TBD: Inviare messaggio di 1 al registro,
     *      tramite la coda "id_coda_registro_richieste",
     *      e includere nel messaggio lo ID della
     *      coda privata del server "id_coda_server"
     */

    int ret;

    messaggio_registro msgr;

    msgr.type = 1;
    msgr.id_coda = id_coda_server;
    msgr.id_sever = id_server,

    ret = msgsnd(id_coda_registro_richieste, &msgr, sizeof(messaggio_registro) - sizeof(long), 0);

    if(ret < 0){

        perror("ERRORE MSGSND");
        exit(1);
    }

    while(1) {

        printf("Server: In attesa di messaggi...\n");

        /* TBD: Prelevare un messaggio dalla coda del server */

        messaggio_server msgs;

        ret = msgrcv(id_coda_server, &msgs, sizeof(messaggio_server) - sizeof(long), 0, 0);

        if(ret < 0){

            perror("ERRORE MSGRCV");
            exit(1);
        }

        if(/* TBD: Controllare se il messaggio è di tipo 3 */ msgs.type == 3) {

            int valore = msgs.valore; /* TBD: Estrarre il valore dal messaggio */

            printf("Server: Ricevuto messaggio 3 (id_server=%d, valore=%d)\n", id_server, valore);

            risorsa = valore; /* TBD: Assegnare il valore ricevuto alla risorsa */;
        }
        else if(/* TBD: Controllare se il messaggio è di tipo 4 */ msgs.type == 4) {

            printf("Server: Ricevuto messaggio 4 (id_server=%d)\n", id_server);

            /* TBD: De-allocare la coda del server */

            msgctl(id_coda_server, IPC_RMID, 0);

            printf("Server: Uscita\n");

            /* TBD: Terminare il processo */

            exit(0);
        }
        else {

            printf("Server: Ricevuto messaggio non riconosciuto\n");
        }

    }
}

```



esercitazione-4-messaggi-Mashtemah-ce2b71ff6ebcf56bb3c73663cfda25130f366b04/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-ce2b71ff6ebcf56bb3c73663cfda25130f366b04/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Mashtemah-d8f001829077a079b987dd864958e36cd580dbac/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-d8f001829077a079b987dd864958e36cd580dbac/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Mashtemah-d8f001829077a079b987dd864958e36cd580dbac/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Mashtemah-d8f001829077a079b987dd864958e36cd580dbac/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-e238464c154132f0052121c6b6362eea3bece2f1/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-e238464c154132f0052121c6b6362eea3bece2f1/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Mashtemah-e238464c154132f0052121c6b6362eea3bece2f1/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Mashtemah-e238464c154132f0052121c6b6362eea3bece2f1/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-P0l1702-5b3e1878f76268f56aabd9b70064731eae57cb00/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-P0l1702-5b3e1878f76268f56aabd9b70064731eae57cb00/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-P0l1702-5b3e1878f76268f56aabd9b70064731eae57cb00/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-P0l1702-5b3e1878f76268f56aabd9b70064731eae57cb00/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-P0l1702-a5d1f15a16a162684fc46476b5d80179d0eb0861/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-P0l1702-a5d1f15a16a162684fc46476b5d80179d0eb0861/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-P0l1702-a5d1f15a16a162684fc46476b5d80179d0eb0861/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-P0l1702-a5d1f15a16a162684fc46476b5d80179d0eb0861/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-P0l1702-bbdff3290a4a85a5b83697d022d26a787c0ce250/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-P0l1702-bbdff3290a4a85a5b83697d022d26a787c0ce250/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-P0l1702-bbdff3290a4a85a5b83697d022d26a787c0ce250/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-P0l1702-bbdff3290a4a85a5b83697d022d26a787c0ce250/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-P0l1702-c3c5eeb0da6a754ccb98b81f0538b58d3d11731b/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-P0l1702-c3c5eeb0da6a754ccb98b81f0538b58d3d11731b/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-P0l1702-c3c5eeb0da6a754ccb98b81f0538b58d3d11731b/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-P0l1702-c3c5eeb0da6a754ccb98b81f0538b58d3d11731b/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-P0l1702-db6b6bdc9c3f458b535dd279783745ba1fa99997/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-P0l1702-db6b6bdc9c3f458b535dd279783745ba1fa99997/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-P0l1702-db6b6bdc9c3f458b535dd279783745ba1fa99997/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-P0l1702-db6b6bdc9c3f458b535dd279783745ba1fa99997/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-P0l1702-f57fcba9e384701270f239b7dc2eb879dab86d25/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-P0l1702-f57fcba9e384701270f239b7dc2eb879dab86d25/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-P0l1702-f57fcba9e384701270f239b7dc2eb879dab86d25/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-4-messaggi-P0l1702-f57fcba9e384701270f239b7dc2eb879dab86d25/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Vecchions110-0b172e5cf3d4dfe89150ab819e92934aa64579fe/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-0b172e5cf3d4dfe89150ab819e92934aa64579fe/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Vecchions110-0b172e5cf3d4dfe89150ab819e92934aa64579fe/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-0b172e5cf3d4dfe89150ab819e92934aa64579fe/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-2e13bda3b20f63bae9749c2bfcb1ab2f78a6267f/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-2e13bda3b20f63bae9749c2bfcb1ab2f78a6267f/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Vecchions110-2e13bda3b20f63bae9749c2bfcb1ab2f78a6267f/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-2e13bda3b20f63bae9749c2bfcb1ab2f78a6267f/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-58a8e101ec1feb48fd3d6ed006c75f1500d720ea/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-58a8e101ec1feb48fd3d6ed006c75f1500d720ea/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Vecchions110-58a8e101ec1feb48fd3d6ed006c75f1500d720ea/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-58a8e101ec1feb48fd3d6ed006c75f1500d720ea/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-7ae93e4807e4074cacaac652bc93ea8d02500672/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-7ae93e4807e4074cacaac652bc93ea8d02500672/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non invia correttamente i messaggi :warning:
esercitazione-4-messaggi-Vecchions110-7ae93e4807e4074cacaac652bc93ea8d02500672/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-7ae93e4807e4074cacaac652bc93ea8d02500672/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-92d75d9b91fd086da97c1941b2cadd8d08f304d6/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-92d75d9b91fd086da97c1941b2cadd8d08f304d6/load_balancing

## Esercizio registro distribuito

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-92d75d9b91fd086da97c1941b2cadd8d08f304d6/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-92d75d9b91fd086da97c1941b2cadd8d08f304d6/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-9bf35b8a6be7b48453f08ce4e2c913c183f05049/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-9bf35b8a6be7b48453f08ce4e2c913c183f05049/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (server.c) :warning:


<i>È necessario che i processi server utilizzino code distinte. Se i processi chiamano tutti ftok() con gli stessi parametri, ottengono la stessa chiave e quindi la stessa coda. Il modo suggerito di risolvere l'esercizio è utilizzare IPC_PRIVATE (le code non avranno una chiave, e msgget restituirà uno ID distinto).
</i>
(codice errore: esercitazione-4-messaggi-Vecchions110-9bf35b8a6be7b48453f08ce4e2c913c183f05049.registro_distribuito..test.server_distinct_queues)


```
void server(int id_coda_registro_richieste, int id_coda_registro_risposte, int id_server) {

    int risorsa = 0;

    int id_coda_server = msgget(ftok(".",'c'),IPC_CREAT|0664);/* TBD */
    if(id_coda_server < 0) {
        perror("Server: Errore msgget");
        exit(1);
    }

    printf("Server: Invio messaggio 1 (id_server=%d, id_coda=%d)\n", id_server, id_coda_server);

    /* TBD: Inviare messaggio di 1 al registro,
     *      tramite la coda "id_coda_registro_richieste",
     *      e includere nel messaggio lo ID della
     *      coda privata del server "id_coda_server"
     */
    messaggio_registro msg_r;
    msg_r.type=1;
    msg_r.id_server=id_server; // questo è passato alla funzione
    msg_r.id_coda=id_coda_server;
    int ret=msgsnd(id_coda_registro_richieste,&msg_r,sizeof(messaggio_registro)-sizeof(long),0);
    if(ret<0)
    {
        perror("Problema snd in server id coda");
        exit(1);
    }

    while(1) {

        printf("Server: In attesa di messaggi...\n");

        /* TBD: Prelevare un messaggio dalla coda del server */
        messaggio_server msg_s;
        ret=msgrcv(id_coda_server,&msg_s,sizeof(messaggio_server)-sizeof(long),0,0);
        if(ret<0){
            perror("Problema rcv coda server server");
            exit(1);
        }



        if(msg_s.type==3/* TBD: Controllare se il messaggio è di tipo 3 */) {

            int valore = msg_s.valore;/* TBD: Estrarre il valore dal messaggio */

            printf("Server: Ricevuto messaggio 3 (id_server=%d, valore=%d)\n", id_server, valore);

            risorsa =  msg_s.valore;/* TBD: Assegnare il valore ricevuto alla risorsa */;
        }
        else if(msg_s.type==4/* TBD: Controllare se il messaggio è di tipo 4 */) {

            printf("Server: Ricevuto messaggio 4 (id_server=%d)\n", id_server);

            /* TBD: De-allocare la coda del server */
            msgctl(id_coda_server,IPC_RMID,0);

            printf("Server: Uscita\n");

            /* TBD: Terminare il processo */
            exit(0);
        }
        else {

            printf("Server: Ricevuto messaggio non riconosciuto\n");
        }

    }
}

```



esercitazione-4-messaggi-Vecchions110-9bf35b8a6be7b48453f08ce4e2c913c183f05049/registro_distribuito

## Esercizio server sincroni multipli

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-9bf35b8a6be7b48453f08ce4e2c913c183f05049/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Vecchions110-ae0e2556e5a9352d6c09b5240fdacce44c9f22ab/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-ae0e2556e5a9352d6c09b5240fdacce44c9f22ab/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Vecchions110-ae0e2556e5a9352d6c09b5240fdacce44c9f22ab/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Vecchions110-ae0e2556e5a9352d6c09b5240fdacce44c9f22ab/server_sincroni_multipli

## Esercizio grafo delle dipendenze

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Vecchions110-e9a650a7a9b6c67ac0beea9e510429149470f893/grafo_delle_dipendenze

## Esercizio load balancing

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-4-messaggi-Vecchions110-e9a650a7a9b6c67ac0beea9e510429149470f893/load_balancing

## Esercizio registro distribuito

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-4-messaggi-Vecchions110-e9a650a7a9b6c67ac0beea9e510429149470f893/registro_distribuito

## Esercizio server sincroni multipli

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (serversync.c) :warning:


<i>L’esercizio prevede che il mittente riceva lo ok-to-send tramite ricezione selettiva, basata sul PID del processo mittente.
</i>
(codice errore: esercitazione-4-messaggi-Vecchions110-e9a650a7a9b6c67ac0beea9e510429149470f893.server_sincroni_multipli..test.pid_selective_sinc_2)


```
void send_sinc(int ok_id, int req_id, messaggio * msg)
{

    int ret;
    

    /* TBD: Inviare il messaggio REQUEST TO SEND */
    // la prima cosa fare è varibile richiesta 
    REQUEST_TO_SEND req_msg; // la spiegazione di dopo ti permette di capire il perchè è stata fatta questa scelta
   

    // aggiunta informazioni provenienti dal readme
    /* Un client deve inizialmente sincronizzarsi con uno dei
       server, mandando prima una richiesta `REQUEST TO SEND`, indicando il
       proprio PID all'interno del messaggio, e attendendo una risposta
       `OK TO SEND` con il proprio PID nel campo "tipo" del messaggio di
        risposta.*/

    req_msg.type=getpid();

    printf("[%d] Client: invio request-to-send, type=%ld\n", getpid(), req_msg.type/* TBD */); // notare che type = &d quindi vuole il type del msg
    // invio il messaggio msg la dimensione deve essere privata del long
    ret = msgsnd(req_id,&req_msg,sizeof(REQUEST_TO_SEND)-sizeof(long),0);/* TBD */ // msg in questo caso è già un puntatore quindi non serve la & commerciale

    if (ret < 0)
    {
        perror("Errore msgsnd (request-to-send)");
        exit(1);
    }


    /* TBD: Ricevere il messaggio OK TO SEND */

     OK_TO_SEND ok_msg; // creazione della variabile richiesta
    // informazioni provenienti dal readme 
    /*Ognuno dei server, al proprio avvio, dovrà creare una ulteriore coda di
    messaggi (ogni server avrà una propria coda di messaggi, creata da esso stesso). 
        Quando un server riceve una `REQUEST TO SEND`, invia una risposta sulla coda
        `OK TO SEND`, indicando il PID del client nel campo "tipo". Inoltre, il server 
        dovrà indicare nel messaggio di risposta lo ID della propria coda, utilizzando 
    un campo aggiuntivo nel messaggio di tipo intero.
    */

    printf("[%d] Client: in attesa di ok-to-send...\n", getpid());

    ret = msgrcv(ok_id,&ok_msg,sizeof(OK_TO_SEND)-sizeof(long),0,0);/* TBD */

    if (ret < 0)
    {
        perror("Errore msgrcv (ok-to-send)");
        exit(1);
    }
    // qui leggendo capisci che oltra il long nel ok to send vuole anche la coda ma lo potevi capire anche dalla spiegazione
    printf("[%d] Client: ricevuto ok-to-send... type=%ld, id_coda=%d\n", getpid(), ok_msg.type/* TBD */, ok_msg.id_coda/* TBD */);




    /* TBD: Inviare il messaggio al server */
    // per inviarlo ho bisgno dell'id della coda del server

    int id_coda =ok_msg.id_coda; /* TBD */

    printf("[%d] Client: invio messaggio, coda=%d, type=%ld, valore=%d\n", getpid(), id_coda, msg->type, msg->val);


    // ora il messaggio deve essere inviato alla cosa msg è già un puntatore il resto è normale richiesta della funzione 
    //vedi esercitazione 9
    ret = msgsnd(id_coda,msg,sizeof(messaggio)-sizeof(long),0);/* TBD */

    if (ret < 0)
    {
        perror("Errore msgsnd (coda messaggi)");
        exit(1);
    }

}

```



esercitazione-4-messaggi-Vecchions110-e9a650a7a9b6c67ac0beea9e510429149470f893/server_sincroni_multipli

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-alicecapolongo-7f5dfb90cecfc3c0273efc295b6b55bd3bc0aec5/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-alicecapolongo-7f5dfb90cecfc3c0273efc295b6b55bd3bc0aec5/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-alicecapolongo-7f5dfb90cecfc3c0273efc295b6b55bd3bc0aec5/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-alicecapolongo-dca0a06506d0632f4bedae28f5913ff352538352/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-alicecapolongo-dca0a06506d0632f4bedae28f5913ff352538352/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-alicecapolongo-dca0a06506d0632f4bedae28f5913ff352538352/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-alicecapolongo-e483c193c09639b4cbd4325c3f8082e9c89bd750/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-alicecapolongo-e483c193c09639b4cbd4325c3f8082e9c89bd750/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-alicecapolongo-e483c193c09639b4cbd4325c3f8082e9c89bd750/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Antonio-Red-13456ad4024ba699a3f7a809547b5c65d96431f5/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Antonio-Red-13456ad4024ba699a3f7a809547b5c65d96431f5/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Antonio-Red-13456ad4024ba699a3f7a809547b5c65d96431f5/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-Antonio-Red-5b8f64bb676032404662f7ad448ff147ff15ba6d/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-Antonio-Red-5b8f64bb676032404662f7ad448ff147ff15ba6d/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Antonio-Red-5b8f64bb676032404662f7ad448ff147ff15ba6d/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Antonio-Red-731fdee72d2fb948433b5e24c8f2023ee34a4463/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-Antonio-Red-731fdee72d2fb948433b5e24c8f2023ee34a4463/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non effettua correttamente l'invio dei messaggi di richiesta e risposta :warning:
esercitazione-5-server-multithread-Antonio-Red-731fdee72d2fb948433b5e24c8f2023ee34a4463/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Antonio-Red-79c0f6baa35ced42cec752ab71350dd9b355aca4/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-Antonio-Red-79c0f6baa35ced42cec752ab71350dd9b355aca4/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Antonio-Red-79c0f6baa35ced42cec752ab71350dd9b355aca4/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-Antonio-Red-dac9e7c70837166cf3008070939b3d0e945d2bed/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-Antonio-Red-dac9e7c70837166cf3008070939b3d0e945d2bed/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non effettua correttamente l'invio dei messaggi di richiesta e risposta :warning:
esercitazione-5-server-multithread-Antonio-Red-dac9e7c70837166cf3008070939b3d0e945d2bed/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Antonio-Red-f1fc1c313628b06cca209e8139db511725af3a25/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-Antonio-Red-f1fc1c313628b06cca209e8139db511725af3a25/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Antonio-Red-f1fc1c313628b06cca209e8139db511725af3a25/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-CarmineAprea-079527bbafbc63029544a52cd4f414f7544e98ff/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-CarmineAprea-079527bbafbc63029544a52cd4f414f7544e98ff/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-CarmineAprea-079527bbafbc63029544a52cd4f414f7544e98ff/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-CarmineAprea-2292edd9a0937ab48249b6acc0591a4c5d90d31b/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-CarmineAprea-2292edd9a0937ab48249b6acc0591a4c5d90d31b/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-CarmineAprea-2292edd9a0937ab48249b6acc0591a4c5d90d31b/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-CarmineAprea-29a395520c0b3f09a4c14dbaac19f5bf9647ab1e/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-CarmineAprea-29a395520c0b3f09a4c14dbaac19f5bf9647ab1e/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-CarmineAprea-29a395520c0b3f09a4c14dbaac19f5bf9647ab1e/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-CarmineAprea-31967b6a72d4e998814bc15c59828ac8dc0bd249/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-CarmineAprea-31967b6a72d4e998814bc15c59828ac8dc0bd249/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-CarmineAprea-31967b6a72d4e998814bc15c59828ac8dc0bd249/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-CarmineAprea-bb62646118da0aa494f1085054660804ef9e6475/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-CarmineAprea-bb62646118da0aa494f1085054660804ef9e6475/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-CarmineAprea-bb62646118da0aa494f1085054660804ef9e6475/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-G1OV4NNI-15afa01734dfcf74861f6ddd66bf35eb026da0e2/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-G1OV4NNI-15afa01734dfcf74861f6ddd66bf35eb026da0e2/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-G1OV4NNI-15afa01734dfcf74861f6ddd66bf35eb026da0e2/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-G1OV4NNI-8fb7c00d682f500a2f307965cc66c16fe095350f/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-G1OV4NNI-8fb7c00d682f500a2f307965cc66c16fe095350f/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-G1OV4NNI-8fb7c00d682f500a2f307965cc66c16fe095350f/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-G1OV4NNI-d2b6b1a4be4c16038d2cbf3101116ee40480962c/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-G1OV4NNI-d2b6b1a4be4c16038d2cbf3101116ee40480962c/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-G1OV4NNI-d2b6b1a4be4c16038d2cbf3101116ee40480962c/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-G1OV4NNI-eba256721aa905f1668e38a2bd95cae767c2b1c4/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-G1OV4NNI-eba256721aa905f1668e38a2bd95cae767c2b1c4/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-G1OV4NNI-eba256721aa905f1668e38a2bd95cae767c2b1c4/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-G1OV4NNI-fa38dad481af4bffcd565c98684eb62655756a4e/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-G1OV4NNI-fa38dad481af4bffcd565c98684eb62655756a4e/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-G1OV4NNI-fa38dad481af4bffcd565c98684eb62655756a4e/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-G1OV4NNI-fbd03e88c4cd4fe5928515207f3b8c7ed1726c25/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-G1OV4NNI-fbd03e88c4cd4fe5928515207f3b8c7ed1726c25/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-G1OV4NNI-fbd03e88c4cd4fe5928515207f3b8c7ed1726c25/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-5c1b14cc14fc818d76b3d5d1140be79bb1fdb715/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-giuseppe-maglione-5c1b14cc14fc818d76b3d5d1140be79bb1fdb715/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-giuseppe-maglione-5c1b14cc14fc818d76b3d5d1140be79bb1fdb715/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-703e304fc725213eebd213e8c7eddc599892fa6c/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-703e304fc725213eebd213e8c7eddc599892fa6c/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (Client.c) :warning:


<i>È richiesto che il client effettui una receive selettiva, utilizzando il PID nel campo tipo dei messaggi di risposta.
</i>
(codice errore: esercitazione-5-server-multithread-giuseppe-maglione-703e304fc725213eebd213e8c7eddc599892fa6c.un_primo_esempio_di_server_multithread..test.receive-selettiva)


```
		ret = msgrcv(id_s, &risp, sizeof(struct msg_risposta)-sizeof(long), pid, 0);

```



esercitazione-5-server-multithread-giuseppe-maglione-703e304fc725213eebd213e8c7eddc599892fa6c/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-9887f5671a9cf804e428f695493215c2a82674c0/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-9887f5671a9cf804e428f695493215c2a82674c0/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-giuseppe-maglione-9887f5671a9cf804e428f695493215c2a82674c0/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-9cfbc0ecc9011ba150e6e32c1aa8fa242982d5d2/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-9cfbc0ecc9011ba150e6e32c1aa8fa242982d5d2/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-9cfbc0ecc9011ba150e6e32c1aa8fa242982d5d2/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-a7006c165d0f379f21dc6f30773649700602570e/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-a7006c165d0f379f21dc6f30773649700602570e/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (Server.c) :warning:


<i>È richiesto che il mutex sia definito e inizializzato fuori dal ciclo while(1){...} del server. Si suggerisce di dichiarare una variabile globale di tipo pthread_mutex_t, e di inizializzarla subito prima del ciclo tramite pthread_mutex_init().
</i>
(codice errore: esercitazione-5-server-multithread-giuseppe-maglione-a7006c165d0f379f21dc6f30773649700602570e.un_primo_esempio_di_server_multithread..test.mutex_initialization)


```
void server(int id_c, int id_s){

	int k;
	int ret;
	struct msg_richiesta ric;
	struct msg* msg;
	struct msg_risposta risp;
	id_coda_risposte = id_s;
	pthread_t thread_id;


	while(1){

		/* TBD: Ricevere un messaggio di richiesta dal client */
	
		/* TBD */
		ret = msgrcv(id_c, &ric, sizeof(struct msg_richiesta)-sizeof(long), 0, 0);

		if(ret < 0) {
			perror("Errore ricezione richiesta server");
			exit(1);
		}

		if( ric.value1/* TBD */ == -1 && ric.value2/* TBD */ == -1){

			/* Il processo esce quando si riceve un messaggio di terminazione,
			   con i valori {-1, -1}
			 */
			
			exit(0);
		}

		/* TBD: Avviare un thread figlio per l'elaborazione del messaggio,
				passandogli una **copia sullo heap** del messaggio ricevuto.
				(ogni thread figlio deve elaborare un messaggio diverso)
		 */
		msg = malloc(sizeof(struct msg));
		msg->m.pid = ric.pid;
		msg->m.value1 = ric.value1;
		msg->m.value2 = ric.value2;
		msg->id_coda = id_coda_risposte;
		msg->type = 1;
		pthread_create(&thread_id, NULL, Prodotto, (void*) msg);

	}

}

```



<i>È richiesto che la struttura dati con i parametri del thread worker venga deallocata dallo heap, utilizzando free().
</i>
(codice errore: esercitazione-5-server-multithread-giuseppe-maglione-a7006c165d0f379f21dc6f30773649700602570e.un_primo_esempio_di_server_multithread..test.no_free_parameters)


```
void server(int id_c, int id_s){

	int k;
	int ret;
	struct msg_richiesta ric;
	struct msg* msg;
	struct msg_risposta risp;
	id_coda_risposte = id_s;
	pthread_t thread_id;


	while(1){

		/* TBD: Ricevere un messaggio di richiesta dal client */
	
		/* TBD */
		ret = msgrcv(id_c, &ric, sizeof(struct msg_richiesta)-sizeof(long), 0, 0);

		if(ret < 0) {
			perror("Errore ricezione richiesta server");
			exit(1);
		}

		if( ric.value1/* TBD */ == -1 && ric.value2/* TBD */ == -1){

			/* Il processo esce quando si riceve un messaggio di terminazione,
			   con i valori {-1, -1}
			 */
			
			exit(0);
		}

		/* TBD: Avviare un thread figlio per l'elaborazione del messaggio,
				passandogli una **copia sullo heap** del messaggio ricevuto.
				(ogni thread figlio deve elaborare un messaggio diverso)
		 */
		msg = malloc(sizeof(struct msg));
		msg->m.pid = ric.pid;
		msg->m.value1 = ric.value1;
		msg->m.value2 = ric.value2;
		msg->id_coda = id_coda_risposte;
		msg->type = 1;
		pthread_create(&thread_id, NULL, Prodotto, (void*) msg);

	}

}



void* Prodotto(void* v){

	int ret;
	struct msg* msg = (struct msg*) v;
	struct msg_risposta risp;
	int id_coda = msg->id_coda;

	int v3 = msg->m.value1 * msg->m.value2; /* TBD: Calcolare il prodotto */


	/* TBD: Inviare il messaggio di risposta al client.
	        
	   IMPORTANTE: In questo esercizio, si richiede che 
	   			   la coda delle risposte sia utilizzata
				   in modo mutuamente esclusivo dai thread
	   			   (la funzione msgsnd() deve essere chiamata
				   all'interno di una sezione critica).
	 */

	risp.res = v3;
	risp.type = msg->m.pid;
	printf("\nSono Prodotto di Server. Invio del calcolo: %d\n\n", v3);  

	/* TBD */
	
	ret = msgsnd(id_coda, &risp, sizeof(struct msg_risposta)-sizeof(long), 0);


	if(ret < 0) {
		perror("Errore invio risposta server");
		exit(1);
	}


	pthread_exit(NULL);
}

```



<i>In questo esercizio, si richiede che la coda delle risposte sia utilizzata in modo mutuamente esclusivo dai thread (la funzione msgsnd() deve essere chiamata all'interno di una sezione critica).
</i>
(codice errore: esercitazione-5-server-multithread-giuseppe-maglione-a7006c165d0f379f21dc6f30773649700602570e.un_primo_esempio_di_server_multithread..test.critical_section)


```
	ret = msgsnd(id_coda, &risp, sizeof(struct msg_risposta)-sizeof(long), 0);

```



esercitazione-5-server-multithread-giuseppe-maglione-a7006c165d0f379f21dc6f30773649700602570e/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-b6ccd7dc7b718ab4e1abd9c41568168a5f65cdc7/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-b6ccd7dc7b718ab4e1abd9c41568168a5f65cdc7/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-giuseppe-maglione-b6ccd7dc7b718ab4e1abd9c41568168a5f65cdc7/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-d6db2f879cf0573b40ec61752dbae142c4d32c9c/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-d6db2f879cf0573b40ec61752dbae142c4d32c9c/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-giuseppe-maglione-d6db2f879cf0573b40ec61752dbae142c4d32c9c/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-lorenzoalessandrella-32dd6362de8840de8817c05c8ea6223163ac5baf/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-lorenzoalessandrella-32dd6362de8840de8817c05c8ea6223163ac5baf/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-lorenzoalessandrella-32dd6362de8840de8817c05c8ea6223163ac5baf/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-lorenzoalessandrella-790f07eebd0f0a01cb063ebfde6c048b0e65e295/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-lorenzoalessandrella-790f07eebd0f0a01cb063ebfde6c048b0e65e295/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-lorenzoalessandrella-790f07eebd0f0a01cb063ebfde6c048b0e65e295/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-lorenzoalessandrella-8d13af54ad54878f9e170e0639d94d188f1e45f4/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-lorenzoalessandrella-8d13af54ad54878f9e170e0639d94d188f1e45f4/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-lorenzoalessandrella-8d13af54ad54878f9e170e0639d94d188f1e45f4/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-lorenzoalessandrella-9d5986f7ffc27a413a16ac57e8328e3a6f7454ca/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-lorenzoalessandrella-9d5986f7ffc27a413a16ac57e8328e3a6f7454ca/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-lorenzoalessandrella-9d5986f7ffc27a413a16ac57e8328e3a6f7454ca/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-lorenzoalessandrella-e9107dec7efd97fab3ebab9088435d2bbca05f57/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-lorenzoalessandrella-e9107dec7efd97fab3ebab9088435d2bbca05f57/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-lorenzoalessandrella-e9107dec7efd97fab3ebab9088435d2bbca05f57/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-MarkCer16-030e9580dce9f90444ccfd33a5a87db499aa63fc/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-MarkCer16-030e9580dce9f90444ccfd33a5a87db499aa63fc/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-MarkCer16-030e9580dce9f90444ccfd33a5a87db499aa63fc/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-MarkCer16-2e2480e9252b03217f3fb1ec42449b8233456c22/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-MarkCer16-2e2480e9252b03217f3fb1ec42449b8233456c22/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-MarkCer16-2e2480e9252b03217f3fb1ec42449b8233456c22/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: È necessario deallocare le risorse IPC al termine della esecuzione :warning:
esercitazione-5-server-multithread-MarkCer16-30f23eef757968591c9f2c4041ad485930d25c81/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-MarkCer16-30f23eef757968591c9f2c4041ad485930d25c81/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-MarkCer16-30f23eef757968591c9f2c4041ad485930d25c81/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-MarkCer16-63c13b31a051479be15db14477c59282ef1aa1a1/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-MarkCer16-63c13b31a051479be15db14477c59282ef1aa1a1/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-MarkCer16-63c13b31a051479be15db14477c59282ef1aa1a1/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-MarkCer16-8fad79ae6bc27e096bf9a4cafec446f2a6b6dcca/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-MarkCer16-8fad79ae6bc27e096bf9a4cafec446f2a6b6dcca/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-MarkCer16-8fad79ae6bc27e096bf9a4cafec446f2a6b6dcca/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-MarkCer16-aab86633ef6ce1fb0efe6654278445f18106fbae/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-MarkCer16-aab86633ef6ce1fb0efe6654278445f18106fbae/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-MarkCer16-aab86633ef6ce1fb0efe6654278445f18106fbae/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: È necessario deallocare le risorse IPC al termine della esecuzione :warning:
esercitazione-5-server-multithread-MarkCer16-bc24cc260fcda706ce9c8a752b2f63d9d423b8e0/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-MarkCer16-bc24cc260fcda706ce9c8a752b2f63d9d423b8e0/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-MarkCer16-bc24cc260fcda706ce9c8a752b2f63d9d423b8e0/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-MarkCer16-dec6fdfaeab23633c99f6581ad2e59450b12a6ed/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-MarkCer16-dec6fdfaeab23633c99f6581ad2e59450b12a6ed/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-MarkCer16-dec6fdfaeab23633c99f6581ad2e59450b12a6ed/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: È necessario deallocare le risorse IPC al termine della esecuzione :warning:
esercitazione-5-server-multithread-MarkCer16-eff9bfeb319a5e00eb4b41fa44d9739a68c750ef/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-MarkCer16-eff9bfeb319a5e00eb4b41fa44d9739a68c750ef/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-MarkCer16-eff9bfeb319a5e00eb4b41fa44d9739a68c750ef/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-08de4c865e9dc040412e5364ad2558fc626bc381/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-martamodio-08de4c865e9dc040412e5364ad2558fc626bc381/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-08de4c865e9dc040412e5364ad2558fc626bc381/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-3c79016b1fb8c5b69b66d3d613f2a647ae11f437/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-martamodio-3c79016b1fb8c5b69b66d3d613f2a647ae11f437/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-3c79016b1fb8c5b69b66d3d613f2a647ae11f437/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto delle produzioni e delle consumazioni :warning:
esercitazione-5-server-multithread-martamodio-45a5e9373159220565d4f725ccb1e8e24593cf18/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-martamodio-45a5e9373159220565d4f725ccb1e8e24593cf18/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-45a5e9373159220565d4f725ccb1e8e24593cf18/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-martamodio-4e5d60ef31cc02a2a16e68eddd71a1b04c1e819a/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-4e5d60ef31cc02a2a16e68eddd71a1b04c1e819a/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-4e5d60ef31cc02a2a16e68eddd71a1b04c1e819a/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-67cb24813eb747317c32ebea7878d255a6e83b39/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-67cb24813eb747317c32ebea7878d255a6e83b39/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-67cb24813eb747317c32ebea7878d255a6e83b39/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-martamodio-67d3ab1fed1d2ec160db810115bde4ea5b392db1/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-martamodio-67d3ab1fed1d2ec160db810115bde4ea5b392db1/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-67d3ab1fed1d2ec160db810115bde4ea5b392db1/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto delle produzioni e delle consumazioni :warning:
esercitazione-5-server-multithread-martamodio-ad6acd49b07a2874fa311917e321d4c611223883/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-martamodio-ad6acd49b07a2874fa311917e321d4c611223883/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-ad6acd49b07a2874fa311917e321d4c611223883/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto delle produzioni e delle consumazioni :warning:
esercitazione-5-server-multithread-martamodio-c7828d5c50a484db1a9d977f6e96f983c418d728/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-martamodio-c7828d5c50a484db1a9d977f6e96f983c418d728/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-martamodio-c7828d5c50a484db1a9d977f6e96f983c418d728/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Mashtemah-2df03e660ff9f66566aa2f054c84f3e59d4ed131/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Mashtemah-2df03e660ff9f66566aa2f054c84f3e59d4ed131/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Mashtemah-2df03e660ff9f66566aa2f054c84f3e59d4ed131/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Mashtemah-7237d73039d12df6da617482701be2a46c61e800/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-Mashtemah-7237d73039d12df6da617482701be2a46c61e800/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Mashtemah-7237d73039d12df6da617482701be2a46c61e800/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-Mashtemah-a5cf23f8732e0a9eca6bd75f98165e7da8c987a3/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-Mashtemah-a5cf23f8732e0a9eca6bd75f98165e7da8c987a3/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Mashtemah-a5cf23f8732e0a9eca6bd75f98165e7da8c987a3/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Mashtemah-a7f27ea7108f820354bf993ce8fb1c876c8ba08f/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Mashtemah-a7f27ea7108f820354bf993ce8fb1c876c8ba08f/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Mashtemah-a7f27ea7108f820354bf993ce8fb1c876c8ba08f/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-Mashtemah-b77c4d5b8425fd4cfea780d793782edec3f1c43b/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-Mashtemah-b77c4d5b8425fd4cfea780d793782edec3f1c43b/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-Mashtemah-b77c4d5b8425fd4cfea780d793782edec3f1c43b/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-Mashtemah-ef84dd3efa0cbdfabd67cb317a65dc5fcdaaaed8/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-Mashtemah-ef84dd3efa0cbdfabd67cb317a65dc5fcdaaaed8/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (Server.c) :warning:


<i>È richiesto che la struttura dati con i parametri del thread worker venga deallocata dallo heap, utilizzando free().
</i>
(codice errore: esercitazione-5-server-multithread-Mashtemah-ef84dd3efa0cbdfabd67cb317a65dc5fcdaaaed8.un_primo_esempio_di_server_multithread..test.no_free_parameters)


```
void server(int id_c, int id_s){

	int k;
	int ret;

	id_coda_risposte = id_s;

	pthread_mutex_init(&mutex, NULL);


	while(1){

		/* TBD: Ricevere un messaggio di richiesta dal client */

		msg_richiesta msgr;
	
		ret = msgrcv(id_c, &msgr, sizeof(msg_richiesta) - sizeof(long), 5, 0); /* TBD */

		if(ret < 0) {
			perror("Errore ricezione richiesta server");
			exit(1);
		}

		if( /* TBD */ msgr.x == -1 && /* TBD */ msgr.y == -1){

			/* Il processo esce quando si riceve un messaggio di terminazione,
			   con i valori {-1, -1}
			 */
			
			exit(0);
		}

		/* TBD: Avviare un thread figlio per l'elaborazione del messaggio,
				passandogli una **copia sullo heap** del messaggio ricevuto.
				(ogni thread figlio deve elaborare un messaggio diverso)
		 */

		msg_richiesta * copia = (msg_richiesta*) malloc(sizeof(msg_richiesta));

		copia->type = msgr.type;
		copia->pid = msgr.pid;
		copia->x = msgr.x;
		copia->y = msgr.y;

		pthread_t thread;

		pthread_create(&thread, NULL, Prodotto, (void*) copia);
	}

}



void* Prodotto(void* v){

	int ret;

	msg_richiesta * copia = (msg_richiesta*) v;

	int v3 = (copia->x) * (copia->y); /* TBD: Calcolare il prodotto */


	/* TBD: Inviare il messaggio di risposta al client.
	        
	   IMPORTANTE: In questo esercizio, si richiede che 
	   			   la coda delle risposte sia utilizzata
				   in modo mutuamente esclusivo dai thread
	   			   (la funzione msgsnd() deve essere chiamata
				   all'interno di una sezione critica).
	 */

	msg_risposta msg;

	msg.type = copia->pid;
	msg.valore = v3;

	pthread_mutex_lock(&mutex);

	printf("\nSono Prodotto di Server. Invio del calcolo: %d\n\n", v3);  

	ret = msgsnd(id_coda_risposte, &msg, sizeof(msg_risposta) - sizeof(long), 0); /* TBD */

	if(ret < 0) {
		perror("Errore invio risposta server");
		exit(1);
	}

	pthread_mutex_unlock(&mutex);

	pthread_exit(NULL);
}

```



esercitazione-5-server-multithread-Mashtemah-ef84dd3efa0cbdfabd67cb317a65dc5fcdaaaed8/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-P0l1702-11a3e38d7f8cae484bb3b09562894586a8648571/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-P0l1702-11a3e38d7f8cae484bb3b09562894586a8648571/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-P0l1702-11a3e38d7f8cae484bb3b09562894586a8648571/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-124b5d73ca638ca6a30087b27c12e377797d1d42/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-P0l1702-124b5d73ca638ca6a30087b27c12e377797d1d42/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-124b5d73ca638ca6a30087b27c12e377797d1d42/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-P0l1702-27e0d7716a87e497ece9bcad3c29269bfab30b55/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-P0l1702-27e0d7716a87e497ece9bcad3c29269bfab30b55/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-27e0d7716a87e497ece9bcad3c29269bfab30b55/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-P0l1702-703efbf1dc266ce655329f245a93e6040d744e1a/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-P0l1702-703efbf1dc266ce655329f245a93e6040d744e1a/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione del programma non termina correttamente :warning:
esercitazione-5-server-multithread-P0l1702-703efbf1dc266ce655329f245a93e6040d744e1a/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-a3471e9bf042d2a0ad60be1210dc12291089d95a/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-a3471e9bf042d2a0ad60be1210dc12291089d95a/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-a3471e9bf042d2a0ad60be1210dc12291089d95a/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-c24a577c02943f4173a9772336b17ab34a94927d/remote_procedure_call

## Esercizio server aggregatore con thread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-c24a577c02943f4173a9772336b17ab34a94927d/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-c24a577c02943f4173a9772336b17ab34a94927d/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-d533bb921aac1425291cb690ffada88e9c9407ca/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Anche se il programma esegue, sono stati riscontrati i seguenti difetti all'interno del codice (aggregatore.c) :warning:


<i>È necessario che i lettori possano leggere contemporaneamente il dato condiviso. Si applichi qui l'algoritmo visto a lezione.
</i>
(codice errore: esercitazione-5-server-multithread-P0l1702-d533bb921aac1425291cb690ffada88e9c9407ca.server_aggregatore_thread..test.reader-writer)


```
    *valore = m->variabile;

```



esercitazione-5-server-multithread-P0l1702-d533bb921aac1425291cb690ffada88e9c9407ca/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-d533bb921aac1425291cb690ffada88e9c9407ca/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-P0l1702-d731edc34dd661615f001f307e002c6f8cdb6268/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-P0l1702-d731edc34dd661615f001f307e002c6f8cdb6268/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-d731edc34dd661615f001f307e002c6f8cdb6268/un_primo_esempio_di_server_multithread

## Esercizio remote procedure call

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: Non è stato possibile compilare il programma :warning:
esercitazione-5-server-multithread-P0l1702-fa0c517512fef2ff076018ab1b12b8feb805afc3/remote_procedure_call

## Esercizio server aggregatore con thread

:x: L'esercizio non è ancora stato svolto correttamente.
:warning: L'esecuzione non rispetta l'ordine corretto dei messaggi e delle letture-scritture :warning:
esercitazione-5-server-multithread-P0l1702-fa0c517512fef2ff076018ab1b12b8feb805afc3/server_aggregatore_thread

## Esercizio primo esempio di server multithread

:white_check_mark: Congratulazioni, l'esercizio compila ed esegue correttamente, e non è stato riscontrato nessuno degli errori frequenti nel codice :tada:
esercitazione-5-server-multithread-P0l1702-fa0c517512fef2ff076018ab1b12b8feb805afc3/un_primo_esempio_di_server_multithread
