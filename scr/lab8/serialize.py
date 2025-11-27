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
            # Проверяем обязательные поля
            required_fields = ['fio', 'birthdate', 'group', 'gpa']
            for field in required_fields:
                if field not in item:
                    raise ValueError(f"Отсутствует обязательное поле '{field}' в элементе {i}")
            
            # Создаем студента (валидация происходит в __post_init__)
            student = Student.from_dict(item)
            students.append(student)
            
        except ValueError as e:
            raise ValueError(f"Ошибка валидации в элементе {i}: {e}")
        except Exception as e:
            raise ValueError(f"Неожиданная ошибка в элементе {i}: {e}")
    return students