from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side

import openpyxl
from matplotlib import pyplot as plt
from io import BytesIO

def style_sheet(sheet, num):
    ''' Funzione che crea lo stile del foglio Excel '''

    current_row = 14

    sheet.column_dimensions['A'].width = 75
    sheet.row_dimensions[1].height = 18
    sheet.column_dimensions['B'].width = 10
    

    sheet["A1"].fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
    sheet["A1"].font = Font(name='Arial', size=14, bold=True)
    sheet["A1"].border = Border(left=Side(border_style="thick", color="000000"),
                                right=Side(border_style="thick", color="000000"),
                                top=Side(border_style="thick", color="000000"),
                                bottom=Side(border_style="thick", color="000000"))

    for i in range(1, num+1):
        sheet.row_dimensions[current_row].height = 18
        sheet[f"A{current_row}"].fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
        sheet[f"A{current_row}"].font = Font(name='Arial', size=12, bold=True)
        sheet[f"A{current_row}"].border = Border(left=Side(border_style="thick", color="000000"),
                                                    right=Side(border_style="thick", color="000000"),
                                                    top=Side(border_style="thick", color="000000"),
                                                    bottom=Side(border_style="thick", color="000000"))
        current_row += 7




def grafico(title, authors, sheet):
    ''' Funzione che crea un grafico a barre con i dati passati come argomento '''

    # Creazione del grafico utilizzando matplotlib
    plt.subplots(figsize=(15, 4))  # Imposta le dimensioni della figura (larghezza, altezza)
    plt.subplots_adjust(bottom=0.55, left=0.1)  # Regola lo spazio inferiore per le etichette sull'asse x

    plt.bar(range(len(authors)), list(authors.values()), align='center')
    plt.xticks(range(len(authors)), list(authors.keys()), rotation='vertical')
    plt.xlabel('Studenti')
    plt.ylabel('Numero di commit')
    plt.title(f'Numero di commit per studente - {title}')

    # Salva il grafico in un buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Inserimento del grafico nel file Excel
    img = openpyxl.drawing.image.Image(buffer)
    sheet.add_image(img, 'D2')  # Inserisci l'immagine nella cella D2 (puoi scegliere la posizione desiderata)


