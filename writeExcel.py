def write_to_sheet(sheet, testo1, param1, testo2, param2, testo3, param3, testo4, param4, current_row):
    ''' Funzione che scrive le informazioni sul foglio di lavoro '''

    sheet[f"A{current_row}"] = testo1
    sheet[f"B{current_row}"] = param1

    if testo2 is not None:
        current_row += 1
        sheet[f"A{current_row}"] = testo2
        sheet[f"B{current_row}"] = param2

    if testo3 is not None:
        current_row += 1
        sheet[f"A{current_row}"] = testo3
        sheet[f"B{current_row}"] = param3
        
    if testo4 is not None:
        current_row += 1
        sheet[f"A{current_row}"] = testo4
        sheet[f"B{current_row}"] = param4

    return current_row+1


