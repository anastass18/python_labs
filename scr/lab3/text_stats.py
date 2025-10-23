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