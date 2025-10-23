## Лабораторная работа 2

### Задание 1 — arrays.py

**min_max** - находит минимальное и максимальное значение в списке чисел

**Что делает:**

- Принимает список чисел
- Если список пустой - возвращает строку 'ValueError'
- Возвращает кортеж из минимального и максимального значения

---

**unique_sorted** - возвращает отсортированный список уникальных значений

**Что делает:**

- `set(nums)` - преобразует список в множество, удаляя дубликаты
- `sorted()` - сортирует уникальные значения по возрастанию
- Возвращает отсортированный список без повторений

---

**flatten** - помещает вложенные списки/кортежи в один плоский список

**Что делает:**

- Принимает список, содержащий списки или кортежи
- Последовательно добавляет элементы всех вложенных списков в один результирующий список
- Если встречает элемент, который не список и не кортеж - возвращает 'TypeError'

---

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

**transpose** - строки становятся столбцами, столбцы - строками

**Что делает:**

- Проверяет пустую матрицу, возвращает пустой список
- Берет длину первой строки матрицы как образец и ожидает, что все остальные строки будут иметь такую же длину
- Создает новую матрицу, где `mat[i][j]` становится `result[j][i]`

---

**row_sums** - вычисление сумм элементов по строкам матрицы

**Что делает:**

- Проверяет прямоугольность матрицы
- Для каждой строки вычисляет сумму её элементов
- Возвращает список сумм по строкам

---

**col_sums** - вычисление сумм элементов по столбцам матрицы

**Что делает:**

- Проверяет прямоугольность матрицы
- Для каждого столбца `j` суммирует элементы `mat[i][j]` по всем строкам `i`
- Возвращает список сумм по столбцам

---

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

**info** - проверка и преобразование входной информации о студенте в корректный и стандартизированный формат

**Что делает:**

- Проверка типов данных:
  - Проверяет что ФИО - строка, группа - строка, GPA - число
  - При ошибке возвращает строку с сообщением
  - Проверяет что ФИО и группа не пустые (после удаления пробелов)
  - Проверяет что GPA не отрицательный
  - `fio.strip().split()` - удаляет пробелы и разбивает на слова
  - `if x` - убирает пустые строки
  - `x.capitalize()` - делает первую букву заглавной
  - Проверяет что в ФИО минимум 2 слова (фамилия и имя)
  - Формирует фамилию и инициалы
  - Возвращает кортеж с обработанными данными

---

**format_record** - форматирование данных студента в итоговую строку

**Что делает:**

- Получает исходные данные и передает их в функцию `info`
- Проверяет: если info вернула строку - значит произошла ошибка
- Если данные корректны - формирует итоговую строку:
  - `processed_data[0]` - ФИО с инициалами
  - `processed_data[1]` - группа
  - `processed_data[2]` - GPA

---

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
