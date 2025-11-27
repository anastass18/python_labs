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