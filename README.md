# python_labs

## Лабораторная работа 1

### Задание 1

```python
  name = input("Имя: ")
  years = int(input("Возраст: "))
  next_year = years + 1
  print(f"Привет, {name}! Через год тебе будет {next_year}.")
```

![ex1!](/images/lab1/ex1.png)

### Задание 2

```python
  num1 = float(input("a: ")) 
  num2 = float(input("b: ")) 
  summ = num1 + num2 
  avg = (num1 + num2) / 2 
  print(f"sum={summ:.2f}; avg={avg:.2f}") 
```

![ex2!](/images/lab1/ex2.png)

### Задание 3

```python
  price = float(input())
  discount = float(input()) 
  vat = float(input()) 
  base = price*(1-discount/100)
  vat_amount = base*(vat/100) 
  total = base + vat_amount 
  print(f"База после скидки: {base:.2f} ₽") 
  print(f"НДС: {vat_amount:.2f} ₽") 
  print(f"Итого: {total:.2f} ₽") 
```

![ex3!](/images/lab1/ex3.png)

### Задание 4

```python
  m = int(input("Минуты: "))
  hours = m // 60 
  minutes = m % 60 
  print(f"{hours}:{minutes:02d}") 
```

![ex4!](/images/lab1/ex4.png)

### Задание 5

```python
user_name = input(' ').split()
name = ' '.join(user_name)
print(f"ФИО: {name}")
print('Инициалы: {}{}{}'.format(user_name[0][0], user_name[1][0], user_name[2][0]))
print(f"Длина (символов): {len(name)}")
```

![ex5!](/images/lab1/ex5.png)

## Лабораторная работа 2

### Задание 1 — arrays.py

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return 'ValueError'
    return min(nums), max(nums)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    result = []
    for element in mat:
        if isinstance(element, (list, tuple)):
            result.extend(element)
        else:
            return 'TypeError'
    
    return result

if __name__ == "__main__":
    print("Тестирование min_max:")

    result = min_max([3, -1, 5, 5, 0])
    print(f"[3, -1, 5, 5, 0] - {result}")
    
    result = min_max([42])
    print(f"[42] - {result}")
    
    result = min_max([-5, -2, -9])
    print(f"[-5, -2, -9] - {result}")
    
    result = min_max([])
    print(f"[] - {result}")
    
    result = min_max([1.5, 2, 2.0, -3.1])
    print(f"[1.5, 2, 2.0, -3.1] - {result}")
    

    print("\nТестирование unique_sorted:")
    
    result = unique_sorted([3, 1, 2, 1, 3])
    print(f"[3, 1, 2, 1, 3] - {result}")
    
    result = unique_sorted([])
    print(f"[] - {result}")
    
    result = unique_sorted([-1, -1, 0, 2, 2])
    print(f"[-1, -1, 0, 2, 2] - {result}")
    
    result = unique_sorted([1.0, 1, 2.5, 2.5, 0])
    print(f"[1.0, 1, 2.5, 2.5, 0] - {result}")
    

    print("\nТестирование flatten:")
    
    result = flatten([[1, 2], [3, 4]])
    print(f"[[1, 2], [3, 4]] - {result}")

    result = flatten(([1, 2], (3, 4, 5)))
    print(f"([1, 2], (3, 4, 5)) - {result}")
    
    result = flatten([[1], [], [2, 3]])
    print(f"[[1], [], [2, 3]] - {result}")
    
    result = flatten([[1, 2], "ab"])
    print(f"[[1, 2], 'ab'] - {result}")
```
![arrays!](/images/lab2/arrays.png)

### Задание B — matrix.py

```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
            return 'ValueError'
    return [[mat[i][j] for i in range(len(mat))] for j in range(num_cols)]

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
            return 'ValueError'
    return [sum(row) for row in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
           return 'ValueError'
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(num_cols)]

if __name__ == "__main__":
    print("Тестирование transpose:")
    result = transpose([[1, 2, 3]])
    print(f"[[1, 2, 3]] - {result}")

    result = transpose([[1], [2], [3]])
    print(f"[[1], [2], [3]] - {result}")

    result = transpose([[1, 2], [3, 4]])
    print(f"[[1, 2], [3, 4]] - {result}")
    
    result = transpose([])
    print(f"[] - {result}")

    result = transpose([[1, 2], [3]])
    print(f"[[1, 2], [3]] - {result}")
    

    print("\nТестирование row_sums:")

    result = row_sums([[1, 2, 3], [4, 5, 6]])
    print(f"[[1, 2, 3], [4, 5, 6]] - {result}")
    
    result = row_sums([[-1, 1], [10, -10]])
    print(f"[[-1, 1], [10, -10]] - {result}")
    
    result = row_sums([[0, 0], [0, 0]])
    print(f"[[0, 0], [0, 0]] - {result}")
    
    result = row_sums([[1, 2], [3]])
    print(f"[[1, 2], [3]] - {result}")
    

    print("\nТестирование col_sums:")

    result = col_sums([[1, 2, 3], [4, 5, 6]])
    print(f"[[1, 2, 3], [4, 5, 6]] - {result}")

    result = col_sums([[-1, 1], [10, -10]])
    print(f"[[-1, 1], [10, -10]] - {result}")

    result = col_sums([[0, 0], [0, 0]])
    print(f"[[0, 0], [0, 0]] - {result}")

    result = col_sums([[1, 2], [3]])
    print(f"[[1, 2], [3]] - {result}")
```
![matrix!](/images/lab2/matrix.png)

### Задание C — tuples.py

```python
def info(fio: str, group: str, gpa: float) -> tuple:
    if not isinstance(fio, str):
        return "TypeError: fio должно быть строкой"
    if not isinstance(group, str):
        return "TypeError: group должно быть строкой"
    if not isinstance(gpa, (float, int)):
        return "TypeError: gpa должно быть числом"
    
    if not fio.strip():
        return "ValueError: ФИО не может быть пустым"
    if not group.strip():
        return "ValueError: Группа не может быть пустой"
    if gpa < 0:
        return "ValueError: GPA не может быть отрицательным"

    parts = [x.capitalize() for x in fio.strip().split() if x]
    
    if len(parts) < 2:
        return "ValueError: ФИО должно содержать фамилию и имя"

    last_name = parts[0]
    first_initial = parts[1][0].upper() + "."
    
    if len(parts) > 2:
        second_initial = parts[2][0].upper() + "."
    else:
        second_initial = ""
    
    formatted_gpa = f"{gpa:.2f}"
    return (f"{last_name} {first_initial}{second_initial}", group, formatted_gpa)

def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    processed_data = info(fio, group, gpa)
    
    if isinstance(processed_data, str):
        return processed_data
    
    result = f"{processed_data[0]}, гр. {processed_data[1]}, GPA {processed_data[2]}"
    return result

# Тест-кейсы
if __name__ == "__main__":
    print('Тестируем функцию:')
    test_cases = [
        ("Иванов Иван Иванович", "BIVT-25", 4.6),
        ("Петров Пётр", "IKBO-12", 5.0),
        ("Петров Пётр Петрович", "IKBO-12", 5.0),
        ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
    ]
    for i, test_case in enumerate(test_cases, 1):
        result = format_record(test_case)
        print(f"{test_case} - {result}")
    
    print('\nТестируем ошибки:')
    error_cases = [
        ("", "GROUP", 4.0),
        ("Иванов", "", 4.0),
        ("Иванов", "GROUP", -1.0),
        (123, "GROUP", 4.0),
        ("Толькофамилия", "GROUP", 4.0),
    ]
    for i, error_case in enumerate(error_cases, 1):
        result = format_record(error_case)
        print(f"{error_case} - {result}")
```
![tuples!](/images/lab2/tuples.png)

## Лабораторная работа 3

### Задание A — `src/lib/text.py`

```python
import re
import unicodedata

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    result = text
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'Е') # замена ё/е, Ё/Е
    if casefold:
        result = result.casefold() # нижний регистр
    result = ''.join(char if not unicodedata.category(char).startswith('C') or char == '\n' else ' ' for char in result) # замена управляющих символов на пробелы
    result = re.sub(r'\s+', ' ', result) # склеивание повторяющихся пробелов
    return result.strip() # удаление пробелов в начале и в конце

def tokenize(text: str) -> list[str]:
    pattern = r'\w+(?:-\w+)*' # выражение для поиска слов
    tokens = re.findall(pattern, text) # поиск совпадений с патерном
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1 # увеличение счетчика для текущего токена (если токена нет в словаре - get вернет 0)
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), 
                         key=lambda x: (-x[1], x[0])) # сортировка словаря по убыванию частоты (при равенстве - по алфавиту)
    return sorted_items[:n] # возвращаем переменные n элементов

# Тестирование функций
if __name__ == "__main__":
    print("Тестирование normalize:")
    
    result = normalize("ПрИвЕт\nМИр\t")
    print(f"'ПрИвЕт\\nМИр\\t' -> '{result}'")
    
    result = normalize("ёжик, Ёлка", yo2e=True)
    print(f"'ёжик, Ёлка' -> '{result}'")
    
    result = normalize("Hello\r\nWorld")
    print(f"'Hello\\r\\nWorld' -> '{result}'")
    
    result = normalize("  двойные   пробелы  ")
    print(f"'  двойные   пробелы  ' -> '{result}'")
    
    print("\nТестирование tokenize:")
    
    result = tokenize("привет мир")
    print(f"'привет мир' -> {result}")
    
    result = tokenize("hello,world!!!")
    print(f"'hello,world!!!' -> {result}")
    
    result = tokenize("по-настоящему круто")
    print(f"'по-настоящему круто' -> {result}")
    
    result = tokenize("2025 год")
    print(f"'2025 год' -> {result}")
    
    result = tokenize("emoji 😀 не слово")
    print(f"'emoji 😀 не слово' -> {result}")
    
    print("\nТестирование count_freq + top_n:")
    
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)
    top = top_n(freq, 2)
    print(f"{tokens} -> {freq} -> {top}")
    
    tokens = ["bb", "aa", "bb", "aa", "cc"]
    freq = count_freq(tokens)
    top = top_n(freq, 2)
    print(f"{tokens} -> {freq} -> {top}")
```
![text!](/images/lab3/text.png)

## Задание B — `src/text_stats.py` (скрипт со stdin)

```python
from scr.lib.text import normalize, tokenize, count_freq, top_n

def text_stats(text, beautiful=False):
    words = tokenize(normalize(text)) # разбитие на слова
    
    print(f'Всего слов: {len(words)}') # количество  всех слов
    print(f'Уникальных слов: {len(set(words))}') # количество уникальных слов
    print('Топ-5:')
    
    top_words = top_n(count_freq(words), 5) # нахождение топ-5 популярных слов
    
    if beautiful:
        max_length = max(len(word) for word, count in top_words) # нахождение длины самого длинного слова
        
        print(f"{'слово':<{max_length}} | частота") # заголовок таблицы
        print("-" * max_length + "-|----------")
        
        for word, count in top_words:
            print(f"{word:<{max_length}} | {count}")  # вывод каждого слова с его частотой
    else:
        for word, count in top_words: # вывод не ввиде таблицы
            print(f"{word}:{count}")

text_stats("Привет мир привет всем", beautiful=True)
```
![text_stats!](/images/lab3/text_stats.png)

## Лабораторная работа 4

### Задание A — модуль `src/lab04/io_txt_csv.py`

``` python
from pathlib import Path # импортируем класс Path из модуля pathlib для удобной работы с путями файлов
import csv # импортируем модуль для работы с CSV файлами (формат табличных данных)
import os # импортируем модуль для работы с операционной системой (файлы, папки, пути)
from typing import Iterable, Sequence # импортируем типы данных для аннотаций (подсказки для программиста)
                                      # Iterable - любой объект, по которому можно пройтись в цикле
                                      # Sequence - любой объект с последовательностью элементов (список, кортеж и тд)

def read_text(path: str | Path, encoding: str = "utf-8") -> str: # объявляем функцию для чтения текстовых файлов
                                                                 # path: str | Path - принимает путь как строку или объект Path
                                                                 # encoding: str = "utf-8" - кодировка файла (по умолчанию utf-8)
                                                                 # -> str - функция возвращает строку (текст из файла)
    try:
        p = Path(path) # создаем объект Path из переданного пути
        return p.read_text(encoding=encoding) # читаем весь текст из файла в указанной кодировке и возвращаем его
    except FileNotFoundError: # ошибка "Файл не найден"
        return "Такого файла не существует" # возвращаем сообщение об ошибке вместо текста файла
    except UnicodeDecodeError: # ошибка неправильной кодировки
        return "Не удалось изменить кодировку" # возвращаем сообщение об ошибке кодировки

def write_csv(rows: Iterable[Sequence], path: str | Path,  # функция для записи данных в CSV-файл
              header: tuple[str, ...] | None = None) -> None: # rows: Iterable[Sequence] - данные для записи (список, кортеж и тд)
                                                              # path: str | Path - путь к файлу для записи
                                                              # header: tuple[str, ...] | None = None - заголовок таблицы (может быть None)
                                                              # -> None - функция ничего не возвращает
    p = Path(path) # преобразуем путь в объект Path для удобной работы
    rows = list(rows) # преобразуем переданные данные в обычный список (на случай если передали другой тип итератора)
    
    with p.open("w", newline="", encoding="utf-8") as f: # открываем файл для записи
                                                         # "w" - режим записи (перезаписывает файл)
                                                         # newline="" - для корректной работы с переносами строк в Windows
                                                         # encoding="utf-8" - кодировка файла
                                                         # with - гарантирует закрытие файла после работы
        file_c = csv.writer(f) # создаем объект writer для записи CSV-данных
        if header is not None and rows == []: # проверка: если заголовок указан, но нет данных для записи (если нет, записываем тестовые данные (a,b) в файл)
            file_c.writerow(('a','b'))
        if header is not None: # провека: указан ли заголовок; если нет, записываем заголовок первой строкой в файл
            file_c.writerow(header)
        if rows: # проверяем, есть ли данные для записи
            const = len(rows[0]) # запоминаем длину первой строки (количество столбцов)
            for r in rows: # проверяем все строки на одинаковую длину
                if len(r) != const:
                    raise ValueError("Все строки должны иметь одинаковую длину") # если какая-то строка имеет другое количество элементов, вызываем ошибку - все строки должны быть одинаковой длины
            for r in rows:
                file_c.writerow(r) # после проверки записываем все строки данных в CSV-файл

def ensure_parent_dir(path: str | Path) -> None: # функция для создания родительской директории файла
                                                 # path: str | Path - путь к файлу
                                                 # -> None - функция ничего не возвращает
    p = Path(path) # Преобразуем путь в объект Path
    parent_dir = p.parent # получаем путь к родительской директории (папке, где должен лежать файл)
    parent_dir.mkdir(parents=True, exist_ok=True) # создаем директорию (папку) если её нет
                                                  # parents=True - создает все родительские папки по цепочке
                                                  # exist_ok=True - не вызывает ошибку, если папка уже существует
print(read_text(r"C:\Users\Анастасия\Desktop\python_labs\input.txt"))# Читаем файл input.txt и выводим его содержимое на экран
write_csv([("world","count"),("test",3)], r"C:\Users\Анастасия\Desktop\python_labs\check.csv", header=None) # записываем данные в CSV-файл
                                                                                                            # [("world","count"),("test",3)] - данные: две строки по два значения
                                                                                                            # header=None - записываем без заголовка
```
#### Терминал
![terminal!](/images/lab4/terminal.png)

#### input.txt
![input!](/images/lab4/input_file.png)

#### check.csv
![check!](/images/lab4/check_file.png)

### Задание B — скрипт `src/lab04/text_report.py`

``` python
import sys # импортируем встроенный модуль, предоставляет доступ к системным параметрам и функциям
sys.path.append(r'C:\Users\Анастасия\Desktop\python_labs\scr\lib') # доступ к объектам и функциям
from text import * # импортирует все функции из файла text
from io_txt_csv import read_text, write_csv #импортирует конкретные функции 

def stats(text, beautiful=False): # не знаю почему, но эта функция не хотела импортироваться :_)
    words = tokenize(normalize(text))
    print(f'Всего слов: {len(words)}')
    print(f'Уникальных слов: {len(set(words))}')
    print('Топ-5:')
    top_words = top_n(count_freq(words), 5)
    for word, count in top_words:
            print(f"{word}:{count}")

text_from_file = read_text(r'C:\Users\Анастасия\Desktop\python_labs\data\lab_4\input_2.txt') # читаем текст из указанного файла
stats(text_from_file) # вызываем функцию и передаем ей прочитанный текст 
write_csv(top_n(count_freq(tokenize(normalize(text_from_file))), 5), path = r'C:\Users\Анастасия\Desktop\python_labs\data\lab_4\check_2.csv', header= ['word', 'count']) # нормализуем текст, разбиваем на слова, получаем топ-5 слов
```

#### Терминал
![terminal2!](/images/lab4/terminal2.png)

#### input_2.txt
![input2!](/images/lab4/input2.png)

#### check_2.csv
![check2!](/images/lab4/check2.png)

## Лабораторная работа 5

### Задание A — JSON ↔ CSV

``` python
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
```

![people_CSV!](/images/lab5/people_CSV.png)

![PFJ!](/images/lab5/PFJ.png)

![people_JSON!](/images/lab5/people_JSON.png)

![PFC!](/images/lab5/PFC.png)

### Задание B — CSV → XLSX

``` python
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
```

![cities!](/images/lab5/cities.png)

![people_xlsx!](/images/lab5/people_xlsx.png)

## Лабораторная работа 6

### Задание 1

``` python
import  argparse # импортируем библиотеку для обработки аргументов командной строки
from scr.lib.text import * # импортируем все функции из нашего модуля обработки текста

def cat(text, n):
    file = open(text, "r").readlines() # открываем файл и читаем все строки в список
    if not n: # если флаг -n не установлен (простой вывод)
        for i in file:
            print(i.replace("\n", ""))
    else:
        file = enumerate(file) # если флаг -n установлен (вывод с нумерацией)
                         # добавляем номера строкам с помощью enumerate
        for i in file:
            print(i[0],i[1].replace("\n", ""))


def stats(txt,n):
    file = open(txt, "r").read() # читаем весь файл как одну строку
    txt = top_n(count_freq(tokenize(normalize(file))),n) # обрабатываем текст: нормализуем - разбиваем на слова - считаем частоты - берем топ-N
    for a in txt:
        print(a[1],a[0])

parser = argparse.ArgumentParser("CLI‑утилиты лабораторной №6")
subparsers = parser.add_subparsers(dest="command")

# подкоманда cat
cat_parser = subparsers.add_parser("cat",help = "Вывести содержимое файла")
cat_parser.add_argument("--input",required = True)
cat_parser.add_argument("-n", action="store_true",help = "Нумировать строки")

# подкоманда stats
stats_parser = subparsers.add_parser("stats",help = "Частоты слез")
stats_parser.add_argument("--input",required = True)
stats_parser.add_argument("--top",type = int, default = 5)

args = parser.parse_args() # разбираем аргументы командной строки

if args.command == "cat":
    cat(args.input,args.n)

if args.command == "stats":
    stats(args.input,args.top)
```

![list!](/images/lab6/list.png)

![cat!](/images/lab6/cat.png)

![stats!](/images/lab6/stats.png)

### Задание 2

``` python
import argparse
from scr.lab5.csv_xlsx import csv_to_excel
from scr.lab5.json_csv import json_to_csv, csv_to_json

parser = argparse.ArgumentParser("CLI‑утилиты лабораторной №6")
subparsers = parser.add_subparsers(dest="command")

json2csv_parser = subparsers.add_parser("json2csv",help = "Первевести json в csv")
json2csv_parser.add_argument("--in",required=True,dest='input')
json2csv_parser.add_argument("--out",required=True)

csv2json_parser = subparsers.add_parser("csv2json",help = "Перевести csv в json")
csv2json_parser.add_argument("--in",required=True,dest='input')
csv2json_parser.add_argument("--out",required=True)

csv2xlsx_parser = subparsers.add_parser("csv2xlsx",help = "Первевести csv в xlsx")
csv2xlsx_parser.add_argument("--in",required=True,dest='input')
csv2xlsx_parser.add_argument("--out",required=True)

args = parser.parse_args()

if args.command == "json2csv":
    json_to_csv(args.input,args.out)

if args.command == "csv2json":
    csv_to_json(args.input,args.out)

if args.command == "csv2xlsx":
    csv_to_excel(args.input,args.out)
```

![comands!](/images/lab6/comands.png)

```
python -m scr.lab6.cli_convert csv2xlsx --in "data/samples/cities.csv" --out "data/out/people.xlsx"
```

![tablichka!](/images/lab5/people_xlsx.png)

```
python -m scr.lab6.cli_convert json2csv --in "data/samples/people.json" --out "data/out/people_from_json.csv"
```

![PFJ!](/images/lab5/PFJ.png)

```
python -m scr.lab6.cli_convert csv2json --in "data/samples/people.csv" --out "data/out/people_from_csv.json"
```

![PFC!](/images/lab5/PFC.png) 


## Лабораторная работа 7

### A. Тесты для src/lib/text.py

``` python
import unittest
import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # добавляем корневую папку в путь Python

from scr.lib.text import normalize, tokenize, count_freq, top_n # импортируем из корневой папки


class TestText:
    @pytest.mark.parametrize(
        "input_text, expected",
        [
            ("привет\nмир\t", "привет мир"),
            ("ёжик, Ёлка", "ежик, елка"),
            ("hello\r\nworld", "hello world"),
            ("  двойные   пробелы  ", "двойные пробелы"),
        ],
    )
    def test_normalize(self, input_text, expected):
        assert normalize(input_text) == expected

    @pytest.mark.parametrize(
        "input_text, expected",
        [
            ("привет мир", ["привет", "мир"]),
            ("hello,world!!!", ["hello", "world"]),
            ("по-настоящему круто", ["по-настоящему", "круто"]),
            ("2025 год", ["2025", "год"]),
            ("emoji 😀 не слово", ["emoji", "не", "слово"]),
            ("", []),  # пустая строка
            ("   ", []),  # только пробелы
            ("!!!@@@###", []),  # только спецсимволы
            ("раз два.три,четыре!пять?", ["раз", "два", "три", "четыре", "пять"]),
            ("цифры123 и символы!", ["цифры123", "и", "символы"]),
            ("'кавычки' \"двойные\"", ["кавычки", "двойные"]),
        ],
    )
    def test_tokenize(self, input_text, expected):
        assert tokenize(input_text) == expected

    @pytest.mark.parametrize(
        "tokens, expected",
        [
            (["hello", "world", "hello"], {"hello": 2, "world": 1}),
            (["a", "b", "a", "c", "c"], {"a": 2, "b": 1, "c": 2}),
            ([], {}),  # пустой список
            (["x"], {"x": 1}),  # один элемент
            (["a", "a", "a"], {"a": 3}),  # все одинаковые
            (["1", "2", "3"], {"1": 1, "2": 1, "3": 1}),  # все разные
        ],
    )
    def test_count_freq(self, tokens, expected):
        assert count_freq(tokens) == expected

    @pytest.mark.parametrize(
        "freq, n, expected",
        [
            ({"hello": 2, "world": 1}, 1, [("hello", 2)]),
            ({"a": 5, "b": 5, "c": 3}, 2, [("a", 5), ("b", 5)]),  # ничья
            ({"x": 1}, 1, [("x", 1)]),  # один элемент
            ({}, 5, []),  # пустой словарь
            ({"a": 10, "b": 10, "c": 10}, 2, [("a", 10), ("b", 10)]),  # все одинаковые
            ({"z": 1, "y": 2, "x": 3}, 2, [("x", 3), ("y", 2)]),  # проверка порядка
        ],
    )
    def test_top_n(self, freq, n, expected):
        assert top_n(freq, n) == expected
```

![test_text!](/images/lab7/test_text.png) 

![test_text2!](/images/lab7/test_text2.png)

### B. Тесты для src/lab05/json_csv.py

``` python
import pytest
import csv, json
from pathlib import Path
from scr.lab5.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    scr = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    scr.write_text(json.dumps(data, ensure_ascii = False, indent = 2), encoding = "utf-8")
    json_to_csv(str(scr), str(dst))
    with dst.open(encoding = "utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    scr = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    data = [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]
    with open(scr, "w", newline = "", encoding = "utf-8") as f:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(data)
    csv_to_json(str(scr), str(dst))
    with dst.open(encoding = "utf-8") as f:
        rows = json.load(f)
    assert len(rows) == 2


@pytest.mark.parametrize(
    "function, input_file, error",
    [
        (json_to_csv, "people.json", ValueError),
    ],
)
def test_json_to_csv(function, input_file, error, tmp_path: Path):
    file_path = tmp_path / input_file
    file_path.write_text("Error???", encoding = "utf-8")
    dst = tmp_path / "people.csv"
    f = json_to_csv if function is json_to_csv else csv_to_json
    with pytest.raises(error):
        f(str(file_path), str(dst))
```

![json_csv_test!](/images/lab7/json_csv_test.png)

### C. Стиль кода (```black```)

![black!](/images/lab7/black.png)

## Лабораторная работа 7

### Задание А, В

#### models.py
``` python
from dataclasses import dataclass
from datetime import datetime, date
from typing import ClassVar

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    __date_format: ClassVar[str] = "%Y-%m-%d" # приватное поле для формата даты
    
    def __post_init__(self): # валидация данных после инициализации
        self._validate_birthdate()
        self._validate_gpa()
    
    def _validate_birthdate(self): # проверка формата даты (YYYY-MM-DD)
        try:
            datetime.strptime(self.birthdate, self.__date_format)
        except ValueError:
            raise ValueError(f"Дата должна быть в формате {self.__date_format}")
    
    def _validate_gpa(self): # проверка диапазона GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError("GPA должен быть в диапазоне от 0 до 5")
    
    def age(self) -> int: # вернуть количество полных лет
        birth_date = datetime.strptime(self.birthdate, self.__date_format).date()
        today = date.today()
        age = today.year - birth_date.year # проверяем, был ли уже день рождения в этом году
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age
    
    def to_dict(self) -> dict: # сериализация в словарь
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, d: dict) -> 'Student': # десериализация из словаря
        return cls(
            fio = d["fio"],
            birthdate = d["birthdate"],
            group = d["group"],
            gpa= d ["gpa"]
        )
    
    def __str__(self): # красивый вывод информации о студенте
        return f"{self.fio}, {self.group}, GPA: {self.gpa:.2f}, возраст: {self.age()} лет"
```

#### serialize.py

``` python
import json
from typing import List
from models import Student

def students_to_json(students: List[Student], path: str): # Сохраняет список студентов в JSON файл
                                                          # students: список объектов Student
                                                          # path: путь к файлу для сохранения
    data = [s.to_dict() for s in students]
    with open(path, 'w', encoding = 'utf-8') as f:
        json.dump(data, f, ensure_ascii = False, indent = 2)

def students_from_json(path: str) -> List[Student]: # Читает JSON-массив и создаёт список Student с валидацией
                                                    # path: путь к JSON файлу
                                                    # List[Student]: список объектов Student
                                                    # ValueError: если данные в файле невалидны
    try:
        with open(path, 'r', encoding = 'utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {path} не найден")
    except json.JSONDecodeError:
        raise ValueError(f"Файл {path} содержит некорректный JSON")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать массив объектов")
    
    students = []
    for i, item in enumerate(data):
        try:
            required_fields = ['fio', 'birthdate', 'group', 'gpa'] # проверяем обязательные поля
            for field in required_fields:
                if field not in item:
                    raise ValueError(f"Отсутствует обязательное поле '{field}' в элементе {i}")
            student = Student.from_dict(item) # создаем студента (валидация происходит в __post_init__)
            students.append(student)
        except ValueError as e:
            raise ValueError(f"Ошибка валидации в элементе {i}: {e}")
        except Exception as e:
            raise ValueError(f"Неожиданная ошибка в элементе {i}: {e}")
    return students
```

#### main.py

``` python
from models import Student
from serialize import students_to_json, students_from_json
import json
import os

class Config:
    INPUT_FILE = "data/lab_8/students_input.json"
    OUTPUT_FILE = "data/lab_8/students_output.json"

def ensure_input_file():
    if not os.path.exists(Config.INPUT_FILE): # создает students_input.json если его нет
        sample_data = [
            {
                "fio": "Иванов Иван Иванович",
                "birthdate": "2000-05-15",
                "group": "SE-01", 
                "gpa": 4.5
            },
            {
                "fio": "Петрова Анна Сергеевна",
                "birthdate": "2001-12-03",
                "group": "SE-02",
                "gpa": 3.8
            },
            {
                "fio": "Сидоров Алексей Викторович",
                "birthdate": "1999-08-22",
                "group": "SE-01",
                "gpa": 4.2
            },
            {
                "fio": "Козлова Мария Дмитриевна", 
                "birthdate": "2002-03-10",
                "group": "SE-03",
                "gpa": 4.8
            }
        ]
        with open(Config.INPUT_FILE, 'w', encoding = 'utf-8') as f:
            json.dump(sample_data, f, ensure_ascii = False, indent = 2)
        print(f"✅ Создан файл {Config.INPUT_FILE} с тестовыми данными")
    return Config.INPUT_FILE

def main():
    print("🚀 ЗАПУСК ПРОГРАММЫ РАБОТЫ СО СТУДЕНТАМИ")
    print("="*50)
    
    input_file = ensure_input_file() # гарантируем что входной файл существует
    print(f"\n📖 ЧТЕНИЕ ИЗ {input_file}") # читаем данные
    print("-" * 30)

    try:
        students = students_from_json(input_file)
        print(f"✅ Успешно загружено {len(students)} студентов:")
        for i, student in enumerate(students, 1):
            print(f"   {i}. {student}")
    except Exception as e:
        print(f"❌ Ошибка чтения файла: {e}")
        return
    print(f"\n💾 СОХРАНЕНИЕ В {Config.OUTPUT_FILE}") # сохраняем данные
    print("-" * 30)

    try:
        students_to_json(students, Config.OUTPUT_FILE)
        if os.path.exists(Config.OUTPUT_FILE):
            file_size = os.path.getsize(Config.OUTPUT_FILE)
            print(f"✅ Файл {Config.OUTPUT_FILE} успешно создан")
            print(f"   Размер файла: {file_size} байт")
        else:
            print("❌ Ошибка: файл не создан")
            return
    except Exception as e:
        print(f"❌ Ошибка сохранения файла: {e}")
        return

if __name__ == "__main__":
    main()
```

#### До запуска

![before_run!](/images/lab8/before_run.png)

#### После запуска

![after_run!](/images/lab8/after_run.png)

#### Терминал после запуска

![terminal!](/images/lab8/terminal.png)

#### students_input.py

![students_input!](/images/lab8/students_input.png)

#### students_output.py

![students_output!](/images/lab8/students_output.png)