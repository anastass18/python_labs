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
# if __name__ == "__main__":
#     print("Тестирование normalize:")
    
#     result = normalize("ПрИвЕт\nМИр\t")
#     print(f"'ПрИвЕт\\nМИр\\t' -> '{result}'")
    
#     result = normalize("ёжик, Ёлка", yo2e=True)
#     print(f"'ёжик, Ёлка' -> '{result}'")
    
#     result = normalize("Hello\r\nWorld")
#     print(f"'Hello\\r\\nWorld' -> '{result}'")
    
#     result = normalize("  двойные   пробелы  ")
#     print(f"'  двойные   пробелы  ' -> '{result}'")
    
#     print("\nТестирование tokenize:")
    
#     result = tokenize("привет мир")
#     print(f"'привет мир' -> {result}")
    
#     result = tokenize("hello,world!!!")
#     print(f"'hello,world!!!' -> {result}")
    
#     result = tokenize("по-настоящему круто")
#     print(f"'по-настоящему круто' -> {result}")
    
#     result = tokenize("2025 год")
#     print(f"'2025 год' -> {result}")
    
#     result = tokenize("emoji 😀 не слово")
#     print(f"'emoji 😀 не слово' -> {result}")
    
#     print("\nТестирование count_freq + top_n:")
    
#     tokens = ["a", "b", "a", "c", "b", "a"]
#     freq = count_freq(tokens)
#     top = top_n(freq, 2)
#     print(f"{tokens} -> {freq} -> {top}")
    
#     tokens = ["bb", "aa", "bb", "aa", "cc"]
#     freq = count_freq(tokens)
#     top = top_n(freq, 2)
#     print(f"{tokens} -> {freq} -> {top}")