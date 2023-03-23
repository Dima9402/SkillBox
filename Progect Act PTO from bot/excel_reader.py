import openpyxl

def read_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    num_rows = len(data)
    num_cols = len(data[0])
    # подсчёт количества строк и столбцов
    headers = data[0]  # Выводит первую строку
    #response = f"Документ: {file_name}\n\n"
    response = f"|{'|'.join(headers)}|\n"  # заголовок
    response += f"\nКоличество строк: {num_rows}"

    return response

