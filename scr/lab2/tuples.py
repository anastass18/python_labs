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
