## Лабораторная работа 9

### Задание A. Реализовать класс Group

#### group.py

``` python
import csv
from pathlib import Path
from typing import List, Dict, Any
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from models_copy import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path("data/lab_9") / storage_path # Создаем полный путь к файлу в data/lab_9
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        self.path.parent.mkdir(parents=True, exist_ok=True) # Создаем папку data/lab_9 если её нет
        
        if not self.path.exists():
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writeheader()
    
    def _read_all(self) -> List[Dict[str, Any]]: # Прочитать все строки из CSV
        rows = []
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['gpa'] = float(row['gpa'])
                rows.append(row)
        return rows
    
    def _write_all(self, rows: List[Dict[str, Any]]): # Записать все строки в CSV
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(rows)
    
    def list(self) -> List[Student]: # Вернуть всех студентов в виде списка Student
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                student = Student.from_dict(row)
                students.append(student)
            except ValueError as e:
                print(f"Ошибка валидации студента {row['fio']}: {e}")
        return students
    
    def add(self, student: Student): # Добавить нового студента в CSV
        try:
            validated_student = Student(
                fio=student.fio,
                birthdate=student.birthdate,
                group=student.group,
                gpa=student.gpa
            )
        except ValueError as e:
            raise ValueError(f"Некорректные данные студента: {e}")
        
        with open(self.path, 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writerow(validated_student.to_dict())
    
    def find(self, substr: str) -> List[Student]: # Найти студентов по подстроке в fio
        students = self.list()
        return [student for student in students if substr.lower() in student.fio.lower()]
    
    def remove(self, fio: str): # Удалить запись(и) с данным fio
        rows = self._read_all()
        updated_rows = [row for row in rows if row['fio'] != fio]
        
        if len(updated_rows) == len(rows):
            raise ValueError(f"Студент с ФИО '{fio}' не найден")
        
        self._write_all(updated_rows)
    
    def update(self, fio: str, **fields): # Обновить поля существующего студента
        rows = self._read_all()
        updated = False
        
        for row in rows:
            if row['fio'] == fio:
                for field, value in fields.items():
                    if field in ['fio', 'birthdate', 'group', 'gpa']:
                        row[field] = value
                updated = True
                try:
                    Student.from_dict(row)
                except ValueError as e:
                    raise ValueError(f"Некорректные данные после обновления: {e}")
        
        if not updated:
            raise ValueError(f"Студент с ФИО '{fio}' не найден")
        
        self._write_all(rows)
    
    def stats(self) -> Dict[str, Any]: # Статистика по группе
        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": 0,
                "max_gpa": 0,
                "avg_gpa": 0,
                "groups": {},
                "top_5_students": []
            }
        
        gpas = [student.gpa for student in students]
        groups_stats = {}
        for student in students:
            groups_stats[student.group] = groups_stats.get(student.group, 0) + 1
        
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        top_5 = [{"fio": s.fio, "gpa": s.gpa} for s in sorted_students[:5]]
        
        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": round(sum(gpas) / len(gpas), 2),
            "groups": groups_stats,
            "top_5_students": top_5
        }
    
    def exists(self, fio: str) -> bool: # Проверить существует ли студент с таким ФИО
        students = self.list()
        return any(student.fio == fio for student in students)

    def is_empty(self) -> bool: # Проверить пуст ли файл (только заголовок)
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return len(list(reader)) == 0
    
if __name__ == "__main__":

    group = Group("students.csv") # Создаем группу

    if group.is_empty(): # Добавляем студентов
        students_to_add = [
            Student("Иванов Иван", "2000-05-15", "БИВТ-21-1", 4.5),
            Student("Петрова Анна", "2001-12-03", "БИВТ-21-2", 3.8),
            Student("Сидоров Алексей", "1999-08-22", "БИВТ-21-1", 4.2),
            Student("Козлова Мария", "2002-03-10", "БИВТ-21-3", 4.8),
            Student("Новиков Дмитрий", "2000-11-25", "БИВТ-21-2", 3.5),
            Student("Иванова Ольга", "2001-07-14", "БИВТ-21-1", 4.9)
        ]
        
        for student in students_to_add:
            group.add(student)
            print(f"    Добавлен: {student.fio}")
    else:
        print("Файл уже содержит данные")
    
    # Тестируем методы
    print("Все студенты:")
    for student in group.list():
        print(f"  {student}")
    
    print("\nПоиск по 'Иванов':")
    for student in group.find("Иванов"):
        print(f"  {student}")
    
    print("\nСтатистика:")
    stats = group.stats()
    for key, value in stats.items():
        if key == "top_5_students":
            print(f"  {key}:")
            for student in value:
                print(f"    {student['fio']} - GPA: {student['gpa']}")
        else:
            print(f"  {key}: {value}")
```

![terminal!](/images/lab9/terminal.png)

#### До запуска

![before_menu!](/images/lab9/before_menu.png)

#### После запуска

![after_menu!](/images/lab9/after_menu.png)

#### students.csv

![students_csv!](/images/lab9/students_csv.png)

``` python
    # Обновление студента
    group.update("Иванов Иван", gpa=4.7, group="БИВТ-21-2")
    print(f"\nПосле обновления Иванова: {group.find('Иванов Иван')[0]}")
```

![update!](/images/lab9/update.png)

#### students.csv (после обновления)

![students_update!](/images/lab9/students_update.png)

``` python
    # Удаление студента
    group.remove("Новиков Дмитрий")
    print(f"\nПосле удаления Новикова, всего студентов: {len(group.list())}")
```

![remove!](/images/lab9/remove.png)

#### students.csv (после удаления)

![students_remove!](/images/lab9/students_remove.png)