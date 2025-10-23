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
