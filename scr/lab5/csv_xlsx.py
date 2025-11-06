import os # библиотека для работы с операционной системой
          # отвечает за: проверку существования файлов, работу с путями, размер файлов
import csv # библиотека для работы с CSV файлами (Comma-Separated Values)
           # отвечает за: чтение и запись табличных данных в текстовом формате
import sys # библиотека для системных функций
           # отвечает за: взаимодействие с интерпретатором Python, аргументы командной строки, выход из программы
from openpyxl import Workbook # специальная библиотека для работы с Excel файлами
                              # отвечает за: создание, редактирование и сохранение .xlsx файлов

def csv_to_excel(csv_file_path, excel_file_path): #проверка фвйла
    # существует ли файл?
    if not os.path.exists(csv_file_path):
        print("Ошибка: Файл не найден!")
        return
    
    # не пустой ли файл?
    if os.path.getsize(csv_file_path) == 0:
        print("Ошибка: Файл пустой!")
        return
    
    excel_book = Workbook() # создаем новую книгу Excel
    sheet = excel_book.active # выбираем активный лист (первую страницу)
    sheet.title = "Sheet1" # даем название странице
    
    with open(csv_file_path, "r", encoding="utf-8") as csv_file: # открываем CSV файл
        csv_reader = csv.reader(csv_file) # читаем CSV построчно
        for row in csv_reader: # для каждой строки в CSV
            sheet.append(row) # добавляем строку в Excel
    
    for column in sheet.columns: # для каждой колонки в Excel
        longest_text = 0  # длина самого длинного текста
        column_letter = column[0].column_letter # получаем букву колонки (A, B, C...)
        for cell in column: # ищем самую длинную ячейку в колонке
            if cell.value:  # если ячейка не пустая
                text_length = len(str(cell.value))
                if text_length > longest_text:
                    longest_text = text_length
        column_width = max(longest_text + 2, 8) # устанавливаем ширину колонки
                                                                      # минимальная ширина = 8, оптимальная = длина текста + 2
        sheet.column_dimensions[column_letter].width = column_width
    excel_book.save(excel_file_path) # сохраняем Excel файл
#    print(f"Успешно создан файл: {excel_file_path}")

csv_to_excel(r"C:\Users\Анастасия\Desktop\python_labs\data\samples\cities.csv", r"C:\Users\Анастасия\Desktop\python_labs\data\out\people.xlsx")