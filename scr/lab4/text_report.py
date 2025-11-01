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