from matplotlib import pyplot as plt
import numpy as np

def grafico_commits(title, authors):
    ''' Funzione che crea un grafico per media e deviazione standard del numero di commit '''

    # Creazione del grafico utilizzando matplotlib
    plt.subplots(figsize=(15, 4))  # Imposta le dimensioni della figura (larghezza, altezza)
    plt.subplots_adjust(bottom=0.55, left=0.1)  # Regola lo spazio inferiore per le etichette sull'asse x

    mean_commits = 0
    std_commits = 0

    bars = None

    # Creazione del primo grafico con la media
    if isinstance(authors, list):
        mean_commits = np.mean(authors)

        bars=plt.bar(range(len(authors)), authors, color='blue', alpha=0.7, label=f'Numero di commit')
        plt.xticks([])  # Imposta l'asse x senza etichette numeriche o ticks

    elif isinstance(authors, dict):
        # Calcola media e deviazione standard
        mean_commits = np.mean(list(authors.values()))

        bars=plt.bar(range(len(authors)), authors.values(), color='blue', alpha=0.7, label=f'Numero di commit')
        plt.xticks([])  # Imposta l'asse x senza etichette numeriche o ticks

    plt.axhline(mean_commits, color='red', linestyle='dashed', linewidth=2, label='Media')
    plt.xlabel('Studenti')
    plt.ylabel('Numero di commit')
    plt.title(f'Numero di commit medio per studente - {title}')
    plt.legend()

    # Aggiungi il valore della media sopra la barra corrispondente
    for bar, mean in zip(bars, [mean_commits]):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height()+10, f'Media: {mean:.2f}', ha='center', va='bottom')

    plt.show()

    # Chiudi la figura corrente
    plt.close()


    # Creazione del secondo grafico con la deviazione standard
    if isinstance(authors, list):
        std_commits = np.std(authors)

        bars=plt.bar(range(len(authors)), authors, color='blue', alpha=0.7, label=f'Numero di commit')
        plt.xticks([])  # Imposta l'asse x senza etichette numeriche o ticks
        plt.errorbar(range(len(authors)), authors, yerr=std_commits, fmt='o', color='green', ecolor='orange', capthick=2, label='Deviazione Standard') 

    elif isinstance(authors, dict):
        std_commits = np.std(list(authors.values()))

        bars=plt.bar(range(len(authors)), authors.values(), color='blue', alpha=0.7, label=f'Numero di commit')
        plt.xticks([])  # Imposta l'asse x senza etichette numeriche o ticks
        plt.errorbar(range(len(authors)), authors.values(), yerr=std_commits, fmt='o', color='green', ecolor='orange', capthick=2, label='Deviazione Standard')

    plt.xlabel('Studenti')
    plt.ylabel('Numero di commit')
    plt.title(f'Numero di commit con deviazione standard - {title}')
    plt.legend()

    # Aggiungi il valore della deviazione standard sopra la barra corrispondente
    for bar, std_value in zip(bars, [std_commits]):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height()+10, f'Dev. Std.: {std_value:.2f}', ha='center', va='bottom')


    plt.show()

    # Chiudi la figura corrente
    plt.close()


def grafico_codice(title, authors):
    ''' Funzione che crea un grafico per media del numero di righe di codice aggiunte e rimosse '''
    
    indexes = np.arange(len(authors)) # x
    width = 0.3 # larghezza delle barre

    # Estrai dati per il grafico
    aggiunte_values = [author['aggiunte'] for author in authors.values()] # y1
    rimozioni_values = [author['rimozioni'] for author in authors.values()] # y2

    # Calcola media e deviazione standard
    mean_agg = np.mean(aggiunte_values)
    mean_rim = np.std(rimozioni_values)

    # Creazione del grafico combinato
    bars1=plt.bar(indexes, aggiunte_values, color='blue', alpha=0.7, label='Aggiunte', width=width)
    bars2=plt.bar(indexes+width, rimozioni_values, color='red', alpha=0.7, label='Rimozioni', width=width)

    plt.axhline(mean_agg, color='green', linestyle='dashed', linewidth=2, label='Media Aggiunte')
    plt.axhline(mean_rim, color='black', linestyle='dashed', linewidth=2, label='Media Rimozioni')

    # Aggiungi il valore della media sopra la barra corrispondente
    for bar, mean in zip(bars1, [mean_agg]):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height()+150, f'Media Aggiunte: {mean:.2f}', ha='left', va='bottom')

    # Aggiungi il valore della media sopra la barra corrispondente
    for bar, mean in zip(bars2, [mean_rim]):
        plt.text(bar.get_x() + bar.get_width() / 2 - 0.3, bar.get_height()+150, f'Media Rimozioni: {mean:.2f}', ha='left', va='bottom')

    # Titolo del grafico combinato
    plt.title(f'Grafico Combinato: Aggiunte e Rimozioni per Autore - {title}')
    plt.xlabel('Studenti')
    plt.ylabel('Numero di righe modificate')
    plt.xticks([])  # Imposta l'asse x senza etichette numeriche o ticks
    plt.legend()

    # Visualizza il grafico
    plt.show()


def grafico_produttivita(title, time_differences):
    ''' Funzione che crea un grafico per la produttività '''
    
    #plt.subplots(figsize=(15, 4))
    mean = np.mean([diff for diff in time_differences])

    bars = plt.bar(range(len(time_differences)), time_differences, color='blue', alpha=0.7, label='Tempo impiegato')

    # Creazione del grafico combinato
    #bars=plt.bar(len(time_differences), time_differences, color='blue', alpha=0.7, label='Tempo impiegato')

    plt.axhline(mean, color='red', linestyle='dashed', linewidth=2, label='Media Tempo Impiegato') 

    # Aggiungi il valore della media sopra la barra corrispondente
    for i, mean in zip(bars, [mean]):
        plt.text(i.get_x() + i.get_width() / 2, i.get_height()+20, f'Media Tempo Impiegato: {mean:.2f}', ha='left', va='bottom')

    # Titolo del grafico combinato
    plt.xticks([])  # Imposta l'asse x senza etichette numeriche o ticks
    plt.title(f'Tempo Impiegato per Studente - {title}')
    plt.xlabel('Studenti')
    plt.ylabel('Tempo impiegato (giorni)')
    plt.legend()

    # Visualizza il grafico
    plt.show()


def grafico_check_statici(title, esercizi):
    ''' Funzione che crea un grafico a torta per i check statici e dinamici '''

    plt.style.use('ggplot')

    labels = ['Commit che non passano i check dinamici', 'Commit che passano i check dinamici ma non quelli statici', 'Commit che passano entrambi i check']
    colors = ['#a22e72', '#A09BE7', '#FFF07C']

    patches, texts, autotexts = plt.pie(esercizi, colors=colors, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')

    # Personalizzazione delle etichette
    for text, autotext in zip(texts, autotexts):
        text.set_fontsize(16)  # Dimensione del font per le etichette
        autotext.set_fontsize(14)  # Dimensione del font per le etichette percentuali


    plt.legend(patches, labels, loc='lower center')

    plt.title(f'Checks - {title}')
    plt.show()


def grafico_check_statici_2(title, risultati):
    ''' Funzione che crea un grafico a barre per i check statici e dinamici '''
    #print(risultati)

    indexes = np.arange(len(risultati)) # x
    width = 0.1 # larghezza delle barre

    non_passa_dinamico = []
    non_passa_statico = []
    passa_tutti = []
    labels = []

    # Estrai dati per il grafico
    for result in risultati:
        non_passa_dinamico.append(result[list(result.keys())[0]][0])
        non_passa_statico.append(result[list(result.keys())[0]][1])
        passa_tutti.append(result[list(result.keys())[0]][2])
        labels.append(list(result.keys())[0])

    #print(non_passa_dinamico , np.mean(non_passa_dinamico))
    #print(non_passa_statico ,np.mean(non_passa_statico))
    #print(passa_tutti ,np.mean(passa_tutti))

    # Creazione del grafico combinato
    bars1=plt.bar(indexes, non_passa_dinamico, color='purple', alpha=0.7, label='Non passa Dinamico', width=width)
    bars2=plt.bar(indexes+width, non_passa_statico, color='#a09be7', alpha=0.7, label='Non passa Statico', width=width)
    bars3=plt.bar(indexes+width*2, passa_tutti, color='orange', alpha=0.7, label='Passa entrambi', width=width)

    # Titolo del grafico combinato
    plt.title(f'Checks - {title}', fontsize=18)
    plt.xticks(indexes+width, labels, fontsize=14)
    plt.ylabel('Numero di commit', fontsize=16)
    plt.legend(fontsize=14)

    # Visualizza il grafico
    plt.show()




def box_plot(title, time_differences, file_list, passing, accepted, partecipanti):
    ''' Funzione che crea un box plot confrontando la produttività degli studenti per esercitazione ed eserizi singoli'''

    file_list = [title] + file_list

    colors = ['#F0A05E', '#861657', '#fff07c', '#568259', "#a09be7"]
    meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='black')

    bp = plt.boxplot(time_differences, labels=file_list, patch_artist=True, showfliers=False, meanprops=meanpointprops, meanline=False, showmeans=True)
    plt.xticks(fontsize=14)

    #region style
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # changing color and linewidth of
    # whiskers
    for whisker in bp['whiskers']:
        whisker.set(color ='#8B008B', linewidth = 1.5, linestyle =":")
    
    # changing color and linewidth of
    # caps
    for cap in bp['caps']:
        cap.set(color ='#8B008B', linewidth = 2)
    
    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color ='red', linewidth = 3)
    
    # changing style of fliers
    for flier in bp['fliers']:
        flier.set(color ='#e7298a', alpha = 0.5)

    plt.title(f"Produttività - {title}", fontsize=18)
    plt.ylabel('Tempo impiegato (giorni)', fontsize=16)

    legend_labels = ['Media', 'Mediana']
    legend_patches = [
        plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='black', markersize=10),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10)
    ]
    #endregion

    plt.legend(legend_patches, legend_labels, loc='upper right', fontsize=14)

    plt.grid(True)

    plt.show()

    
    # A partire dal numero di elementi nella lista time_differences, si calcola il numero di studenti che hanno completato l'esercizio
    td = time_differences[1:]

    print(len(td), len(file_list))

    num_completi = []

    for t in td:
        num_completi.append(len(t))

    num_completi = [passing] + num_completi

    # Creazione del grafico combinato che mostra quanti studenti hanno completato l'esercizio rispetto a quelli che hanno partecipato
    grafico_completati(num_completi, file_list, accepted, partecipanti)


def box_plot_commit(title, num_commits, file_list):
    ''' Funzione che crea un box plot confrontando il numero di commit degli studenti per esercitazione ed eserizi singoli'''
    file_list = [title] + file_list

    colors = ['#F0A05E', '#861657', '#fff07c', '#568259', "#a09be7"]
    meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='black')

    bp = plt.boxplot(num_commits, labels=file_list, patch_artist=True, showfliers=False, meanprops=meanpointprops, meanline=False, showmeans=True)
    plt.xticks(fontsize=14)

    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # changing color and linewidth of
    # whiskers
    for whisker in bp['whiskers']:
        whisker.set(color ='#8B008B', linewidth = 1.5, linestyle =":")
    
    # changing color and linewidth of
    # caps
    for cap in bp['caps']:
        cap.set(color ='#8B008B', linewidth = 2)
    
    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color ='red', linewidth = 3)
    
    # changing style of fliers
    for flier in bp['fliers']:
        flier.set(color ='#e7298a', alpha = 0.5)

    plt.title(f"Numero di commit per studente - {title}", fontsize=18)
    plt.ylabel('Numero di commit', fontsize=16)
    
    legend_labels = ['Media', 'Mediana']
    legend_patches = [
        plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='black', markersize=10),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10)
    ]

    plt.legend(legend_patches, legend_labels, loc='upper right', fontsize=14)

    plt.grid(True)

    plt.show()


def box_plot_produttivita(time_differences):
    ''' Funzione che crea un box plot confrontando la produttività degli studenti per esercitazione ed eserizi singoli'''

    colors = ['#F0A05E', '#861657', '#fff07c', '#568259', "#a09be7"]
    meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='black')
    labels = ["Esercitazione 1\nSemafori", "Esercitazione 2\nMonitor", "Esercitazione 3\nThreads", "Esercitazione 4\nMessaggi", "Esercitazione 5\nServer Multithread"]

    bp = plt.boxplot(time_differences, labels=labels, patch_artist=True, showfliers=False, meanprops=meanpointprops, meanline=False, showmeans=True)
    plt.xticks(fontsize=14)

    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # changing color and linewidth of
    # whiskers
    for whisker in bp['whiskers']:
        whisker.set(color ='#8B008B', linewidth = 1.5, linestyle =":")
    
    # changing color and linewidth of
    # caps
    for cap in bp['caps']:
        cap.set(color ='#8B008B', linewidth = 2)
    
    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color ='red', linewidth = 3)
    
    # changing style of fliers
    for flier in bp['fliers']:
        flier.set(color ='#e7298a', alpha = 0.5)

    plt.title("Produttività per Esercitazione", fontsize=18)
    plt.ylabel('Tempo impiegato (giorni)', fontsize=16)

    legend_labels = ['Media', 'Mediana']
    legend_patches = [
        plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='black', markersize=10),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10)
    ]

    plt.legend(legend_patches, legend_labels, loc='upper right', fontsize=14)

    plt.grid(True)

    plt.show()




def grafico_completati(num_completi, file_list, accepted, partecipanti):
    ''' Funzione che crea un grafico per il numero di studenti che completano gli esercizi rispetto a quelli che partecipano '''

    partecipanti = [accepted] + partecipanti
    print(file_list)
    print(num_completi)
    print(partecipanti)

    for i in range(len(file_list)):
        if file_list[i] == "simulazione disco, con monitor":
            file_list[i] = "simulazione disco"
    
    indexes = np.arange(len(file_list)) # x
    width = 0.3 # larghezza delle barre

    # Creazione del grafico combinato
    bars1=plt.bar(indexes, num_completi, color='purple', alpha=0.7, label='Completati', width=width)
    bars2=plt.bar(indexes+width, partecipanti, color='orange', alpha=0.7, label='Partecipanti', width=width)

    # Titolo del grafico combinato
    plt.title(f'Studenti che completano gli esercizi - {file_list[0]}', fontsize=18)
    plt.ylabel('Numero di studenti', fontsize=16)
    plt.xticks(indexes+width/2, labels=file_list, fontsize=14)
    plt.legend(fontsize=14)

    # Visualizza il grafico
    plt.show()



def num_commits_prima_di_dinamico(title, file_list, commits_prima_di_passa_dinamico):
    ''' Funzione che crea un grafico per il numero di commit prima di passare i check statici e dinamici '''

    colors = ['#F0A05E', '#861657', '#fff07c', '#568259', "#a09be7"]
    meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='black')

    bp = plt.boxplot(commits_prima_di_passa_dinamico, labels=file_list, patch_artist=True, showfliers=False, meanprops=meanpointprops, meanline=False, showmeans=True)
    plt.xticks(fontsize=14)

    #region style
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # changing color and linewidth of
    # whiskers
    for whisker in bp['whiskers']:
        whisker.set(color ='#8B008B', linewidth = 1.5, linestyle =":")
    
    # changing color and linewidth of
    # caps
    for cap in bp['caps']:
        cap.set(color ='#8B008B', linewidth = 2)
    
    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color ='red', linewidth = 3)
    
    # changing style of fliers
    for flier in bp['fliers']:
        flier.set(color ='#e7298a', alpha = 0.5)

    legend_labels = ['Media', 'Mediana']
    legend_patches = [
        plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='black', markersize=10),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10)
    ]
    #endregion

    plt.legend(legend_patches, legend_labels, loc='upper right', fontsize=14)

    plt.grid(True)

    # Titolo del grafico combinato
    plt.title(f'Numero di commit prima di passare i check dinamici - {title}', fontsize=18)
    plt.ylabel('Numero di commit', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Visualizza il grafico
    plt.show()


def num_commits_prima_di_statico(title, file_list, commits_prima_di_passa_statico):
    ''' Funzione che crea un grafico per il numero di commit prima di passare i check statici e dinamici '''

    colors = ['#F0A05E', '#861657', '#fff07c', '#568259', "#a09be7"]
    meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='black')

    bp = plt.boxplot(commits_prima_di_passa_statico, labels=file_list, patch_artist=True, showfliers=False, meanprops=meanpointprops, meanline=False, showmeans=True)
    plt.xticks(fontsize=14)

    #region style
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # changing color and linewidth of
    # whiskers
    for whisker in bp['whiskers']:
        whisker.set(color ='#8B008B', linewidth = 1.5, linestyle =":")
    
    # changing color and linewidth of
    # caps
    for cap in bp['caps']:
        cap.set(color ='#8B008B', linewidth = 2)
    
    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color ='red', linewidth = 3)
    
    # changing style of fliers
    for flier in bp['fliers']:
        flier.set(color ='#e7298a', alpha = 0.5)

    legend_labels = ['Media', 'Mediana']
    legend_patches = [
        plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='black', markersize=10),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10)
    ]
    #endregion

    plt.legend(legend_patches, legend_labels, loc='upper right', fontsize=14)

    plt.grid(True)

    # Titolo del grafico combinato
    plt.title(f'Numero di commit prima di passare i check statici - {title}', fontsize=18)
    plt.ylabel('Numero di commit', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Visualizza il grafico
    plt.show()


def tempo_prima_di_dinamico(title, file_list, tf_dinamico):
    ''' Funzione che crea un grafico per il numero di commit prima di passare i check statici e dinamici '''

    colors = ['#F0A05E', '#861657', '#fff07c', '#568259', "#a09be7"]
    meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='black')

    bp = plt.boxplot(tf_dinamico, labels=file_list, patch_artist=True, showfliers=False, meanprops=meanpointprops, meanline=False, showmeans=True)
    plt.xticks(fontsize=14)

    #region style
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # changing color and linewidth of
    # whiskers
    for whisker in bp['whiskers']:
        whisker.set(color ='#8B008B', linewidth = 1.5, linestyle =":")
    
    # changing color and linewidth of
    # caps
    for cap in bp['caps']:
        cap.set(color ='#8B008B', linewidth = 2)
    
    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color ='red', linewidth = 3)
    
    # changing style of fliers
    for flier in bp['fliers']:
        flier.set(color ='#e7298a', alpha = 0.5)

    legend_labels = ['Media', 'Mediana']
    legend_patches = [
        plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='black', markersize=10),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10)
    ]
    #endregion

    plt.legend(legend_patches, legend_labels, loc='upper right', fontsize=14)

    plt.grid(True)

    # Titolo del grafico combinato
    plt.title(f'Tempo impiegato prima di passare i check dinamici - {title}', fontsize=18)
    plt.ylabel('Tempo (ore)', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Visualizza il grafico
    plt.show()


def tempo_prima_di_statico(title, file_list, tf_statico):
    ''' Funzione che crea un grafico per il numero di commit prima di passare i check statici e dinamici '''

    colors = ['#F0A05E', '#861657', '#fff07c', '#568259', "#a09be7"]
    meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='black')

    bp = plt.boxplot(tf_statico, labels=file_list, patch_artist=True, showfliers=False, meanprops=meanpointprops, meanline=False, showmeans=True)
    plt.xticks(fontsize=14)

    #region style
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # changing color and linewidth of
    # whiskers
    for whisker in bp['whiskers']:
        whisker.set(color ='#8B008B', linewidth = 1.5, linestyle =":")
    
    # changing color and linewidth of
    # caps
    for cap in bp['caps']:
        cap.set(color ='#8B008B', linewidth = 2)
    
    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color ='red', linewidth = 3)
    
    # changing style of fliers
    for flier in bp['fliers']:
        flier.set(color ='#e7298a', alpha = 0.5)

    legend_labels = ['Media', 'Mediana']
    legend_patches = [
        plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='black', markersize=10),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10)
    ]
    #endregion

    plt.legend(legend_patches, legend_labels, loc='upper right', fontsize=14)

    plt.grid(True)

    # Titolo del grafico combinato
    plt.title(f'Tempo impiegato prima di passare i check statici - {title}', fontsize=18)
    plt.ylabel('Tempo (ore)', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Visualizza il grafico
    plt.show()

