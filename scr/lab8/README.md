## Лабораторная работа 8

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

##### p.s Требовался красивый вывод, ну я и решила сделать его красивым, со смайликами 😁