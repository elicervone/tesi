#!/bin/bash

destination_folder='/home/so/Desktop/commits'

if [ -d "$destination_folder" ]; then
    # Enter the destination_folder
    cd "$destination_folder"
    echo "Cartella di destinazione trovata"
else
    echo "La cartella di destinazione non esiste."
    exit 1
fi

# Save the names of all elements in a file
ls -a > "/home/so/Desktop/commits/elements.txt"

if [ $? -ne 0 ]; then
    echo "Errore durante l'esecuzione di ls."
    exit 1
else
    echo "File elements.txt creato correttamente."
fi



while IFS= read -r FOLDER; do
    # Entro in repositories e vedo tutte le repositories degli studenti
    if [ "$FOLDER" != "elements.txt" ] && [ "$FOLDER" != "." ] && [ "$FOLDER" != ".." ]; then
        echo "$FOLDER"

        # Entro nelle singole repositories e vedo tutte le cartelle all'interno
        find "$FOLDER" -type d -name '*' -print -prune | while IFS= read -r SUBDIRECTORY; do

            for SOTTODIRECTORY in "$FOLDER"/*; do
                #echo "$SOTTODIRECTORY"

                # Entro nelle singole cartelle degli esercizi e vedo tutti i file all'interno
                find "$SOTTODIRECTORY" -type d -name '*' -print -prune | while IFS= read -r SUBSUBDIRECTORY; do
                    #echo "$SUBSUBDIRECTORY"
                    
                    find "$SUBSUBDIRECTORY/.test" -type f -name '*.sh' -print | while IFS= read -r SCRIPT; do
                        # Stampa il file .sh in esecuzione
                        echo "$SCRIPT"

                        # Esegui il test statico/dinamico
                        bash "$SCRIPT"
                        if [ $? -eq 0 ]; then
                            echo "Test statico/dinamico superato per $SCRIPT"
                        else
                            echo "Test statico/dinamico fallito per $SCRIPT"
                        fi
                        echo "$SUBSUBDIRECTORY" >> /tmp/feedback.md

                    done

                done
            done
        done

    fi
done < "/home/so/Desktop/commits/elements.txt"
