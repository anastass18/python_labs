import csv # библиотека для работы с CSV файлами (Comma-Separated Values)
           # отвечает за: чтение и запись табличных данных в текстовом формате
import json # библиотека для работы с JSON форматом (JavaScript Object Notation)
            # отвечает за: преобразование данных Python в JSON и обратно, работу с JSON файлами
import os # библиотека для работы с операционной системой
          # отвечает за: проверку существования файлов, работу с путями, размер файлов

def json_to_csv(json_file_path, csv_file_path):
    if not os.path.exists(json_file_path):
        print("FileNotFoundError") # вывод сообщения об ошибке если файл не найден
        return
    
    if os.path.getsize(json_file_path) == 0:
        print("ValueError") # вывод сообщения об ошибке для пустого файла
        return
    
    with open(json_file_path, 'r', encoding='utf-8') as file: # открытие JSON файла для чтения с указанием кодировки UTF-8 для корректной работы с кириллицей
        data = json.load(file) # загрузка и преобразование JSON данных в объекты Python (списки и словари)
    
    # 'w' - режим записи (перезапись если файл существует)
    # newline='' - предотвращает добавление лишних пустых строк в Windows
    # encoding='utf-8' - кодировка для поддержки русских букв
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file: # открытие CSV файла для записи с указанием параметров:
        columns = data[0].keys() # получение названий колонок из ключей первого элемента списка данных
        writer = csv.DictWriter(file, fieldnames=columns) # создание объекта DictWriter для записи словарей в CSV формат
                                                          # fieldnames=columns - передаем список названий колонок для заголовка
        writer.writeheader()  # запись строки заголовка в CSV файл с названиями колонок
        writer.writerows(data) # запись всех данных из JSON в CSV файл построчно
#    print(f"Успешно преобразован {json_file_path} в {csv_file_path}")

def csv_to_json(csv_file_path, json_file_path):
    if not os.path.exists(csv_file_path):
        print("FileNotFoundError") # сообщение об ошибке если CSV файл не найден
        return
    
    if os.path.getsize(csv_file_path) == 0:
        print("ValueError") # сообщение об ошибке для пустого файла
        return
    
    with open(csv_file_path, 'r', encoding='utf-8') as file: # открытие CSV файла для чтения с кодировкой UTF-8
        reader = csv.DictReader(file) # создание объекта DictReader который автоматически использует первую строку CSV как заголовок и возвращает каждую последующую строку как словарь {заголовок: значение}
        data = list(reader) # преобразование всех строк CSV в список словарей
    
    with open(json_file_path, 'w', encoding='utf-8') as file: # открытие JSON файла для записи
        json.dump(data, file, ensure_ascii=False, indent=4) # Запись данных в JSON файл с параметрами:
                                                            # data - данные для записи (список словарей)
                                                            # file - файловый объект для записи
                                                            # ensure_ascii=False - разрешает запись кириллицы и других не-ASCII символов без экранирования
                                                            # indent=4 - форматирование с отступами (4 пробела) для читаемости
    
#    print(f"Успешно преобразован {csv_file_path} в {json_file_path}")

csv_to_json(
    r"C:\Users\Анастасия\Desktop\python_labs\data\samples\people.csv",
    r"C:\Users\Анастасия\Desktop\python_labs\data\out\people_from_csv.json"
)

json_to_csv(
    r"C:\Users\Анастасия\Desktop\python_labs\data\samples\people.json",
    r"C:\Users\Анастасия\Desktop\python_labs\data\out\people_from_json.csv"
)