## Лабораторная работа 10

## Теория

**Стек** (англ. stack - «стопка») - абстрактный тип данных, упорядоченный набор элементов. Добавление новых элементов и удаление существующих происходит с одного конца, называемого вершиной стека.

- **Операции:**
  - `push(x)` — положить элемент сверху;
  - `pop()` — снять верхний элемент;
  - `peek()` — посмотреть верхний, не снимая.

- **Типичные применения:**
  - история действий (undo/redo);
  - обход графа/дерева в глубину (DFS);
  - парсинг выражений, проверка скобок.

---

**Очередь (Queue)** — это структура данных, которая работает по принципу FIFO (First In, First Out): «первый пришёл — первый вышел». Элементы добавляются в конец очереди и извлекаются из начала. 

- **Операции:**
  - `enqueue(x)` — добавить в конец;
  - `dequeue()` — взять элемент из начала;
  - `peek()` — посмотреть первый элемент, не удаляя.

- **Типичные применения:**
  - обработка задач по очереди (job queue);
  - обход графа/дерева в ширину (BFS);
  - буферы (сетевые, файловые, очереди сообщений).

- **В Python:**
  - обычный `list` **плохо подходит** для реализации очереди:
    - удаление с начала `pop(0)` — это `O(n)` (все элементы сдвигаются);
  - `collections.deque` даёт `O(1)` операции по краям:
    - `append` / `appendleft` — `O(1)`;
    - `pop` / `popleft` — `O(1)`.

---

**Односвязный список (Singly Linked List)** — это линейная и однонаправленная структура данных, в которой данные сохраняются на узлах, и каждый узел связан ссылкой со своим следующим узлом.

- **Структура:**
  - состоит из узлов `Node`;
  - каждый узел хранит:
    - `value` — значение элемента;
    - `next` — ссылку на следующий узел или `None` (если это последний).

- **Основные идеи:**
  - элементы не хранятся подряд в памяти, как в массиве;
  - каждый элемент знает только «следующего соседа».

- **Плюсы:**
  - вставка/удаление в **начало** списка за `O(1)`:
    - если есть ссылка на голову (`head`), достаточно перенаправить одну ссылку;
  - при удалении из середины **не нужно сдвигать** остальные элементы:
    - достаточно обновить ссылки узлов;
  - удобно использовать как базовый строительный блок для других структур
    (например, для очередей, стеков, хеш-таблиц с цепочками).

- **Минусы:**
  - доступ по индексу `i` — `O(n)`:
    - чтобы добраться до позиции `i`, нужно пройти `i` шагов от головы;
  - нет быстрого доступа к предыдущему элементу:
    - чтобы удалить узел, нужно знать его предыдущий узел → часто нужен дополнительный проход.

---

**Двусвязный список (Doubly Linked List)** — это структура данных, в которой каждый элемент (узел) содержит указатели на предыдущий и следующий элементы списка.

- **Основные идеи:**
  - можно двигаться как вперёд, так и назад по цепочке узлов;
  - удобно хранить ссылки на оба конца: `head` и `tail`.

- **Плюсы по сравнению с односвязным:**
  - удаление узла по ссылке на него — `O(1)`:
    - достаточно «вытащить» его, перенастроив `prev.next` и `next.prev`;
    - не нужно искать предыдущий узел линейным проходом;
  - эффективен для структур, где часто нужно удалять/добавлять элементы
    в середине, имея на них прямые ссылки (например, реализация LRU-кэша);
  - можно легко идти в обе стороны:
    - прямой и обратный обход списка.

- **Минусы:**
  - узел занимает больше памяти:
    - нужно хранить две ссылки (`prev`, `next`);
  - код более сложный:
    - легко забыть обновить одну из ссылок и «сломать» структуру;
  - сложнее отлаживать.

## Практика

### A. Реализовать `Stack` и `Queue` (`src/lab10/structures.py`)

#### structures.py

``` python
from collections import deque
from typing import Any, Optional

class Stack: # Структура данных 'Стек' (LIFO - Last In First Out)
    def __init__(self): # Инициализация пустого стека
        self._data = []
    
    def push(self, item: Any) -> None: # Добавить элемент на вершину стека
        self._data.append(item) # item: Элемент для добавления
    
    def pop(self) -> Any: # Снять верхний элемент стека и вернуть его
        if self.is_empty(): # IndexError: Если стек пуст
            raise IndexError("Невозможно извлечь элемент: стек пуст")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]: # Вернуть верхний элемент без удаления
        if self.is_empty():
            return None # Верхний элемент стека или None если стек пуст
        return self._data[-1]
    
    def is_empty(self) -> bool: # Проверить пуст ли стек
        return len(self._data) == 0 # True если стек пуст, иначе False
    
    def __len__(self) -> int: # Количество элементов в стеке
        return len(self._data) # Количество элементов
    
    def __str__(self) -> str: # Строковое представление стека
        return f"Stack({self._data})"
    
    def __repr__(self) -> str:
        return str(self)

class Queue: # Структура данных 'Очередь' (FIFO - First In First Out)    
    def __init__(self): # Инициализация пустой очереди
        self._data = deque()
    
    def enqueue(self, item: Any) -> None: # Добавить элемент в конец очереди
        self._data.append(item) # item: Элемент для добавления
    
    def dequeue(self) -> Any: # Взять элемент из начала очереди
        if self.is_empty():
            raise IndexError("Невозможно извлечь элемент: очередь пуста") # IndexError: Если очередь пуста
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]: # Вернуть первый элемент без удаления
        if self.is_empty():
            return None # Первый элемент очереди или None если очередь пуста
        return self._data[0]
    
    def is_empty(self) -> bool: # Проверить пуста ли очередь
        return len(self._data) == 0 # True если очередь пуста, иначе False
    
    def __len__(self) -> int: # Количество элементов в очереди
        return len(self._data) # Количество элементов
    
    def __str__(self) -> str: # Строковое представление очереди
        return f"Queue({list(self._data)})"
    
    def __repr__(self) -> str:
        return str(self)
```

### B. Реализовать `SinglyLinkedList` (`src/lab10/linked_list.py`)

#### linked_list.py

``` python
from typing import Any, Optional, Iterator

class Node: # Узел односвязного списка
    def __init__(self, value: Any, next_node: Optional['Node'] = None): # Инициализация узла
        self.value = value # value: Значение узла
        self.next = next_node # next_node: Ссылка на следующий узел
    
    def __str__(self) -> str: # Строковое представление узла
        return f"[{self.value}]"
    
    def __repr__(self) -> str:
        return str(self)

class SinglyLinkedList: # Односвязный список
    def __init__(self): # Инициализация пустого списка
        self.head = None
        self.tail = None # Для ускорения операций с концом списка
        self._size = 0
    
    def append(self, value: Any) -> None: # Добавить элемент в конец списка
        new_node = Node(value) # value: Значение для добавления
        
        if self.head is None: # Если список пуст
            self.head = new_node
            self.tail = new_node
        else: # Если в списке уже есть элементы
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None: # Добавить элемент в начало списка
        new_node = Node(value, self.head) # value: Значение для добавления
        self.head = new_node
        
        if self.tail is None: # Если список был пуст
            self.tail = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None: # Вставить элемент по указанному индексу
                                                    # idx: Индекс для вставки (0 <= idx <= len(list))
                                                    # value: Значение для вставки
        if idx < 0 or idx > self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size}]") # IndexError: Если индекс вне допустимого диапазона
        
        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        
        # Вставка в середину списка
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        new_node = Node(value, current.next)
        current.next = new_node
        self._size += 1
    
    def remove(self, value: Any) -> bool: # Удалить первое вхождение значения
                                          # value: Значение для удаления
        if self.head is None: # True если элемент был найден и удален, иначе False
            return False
        
        # Если нужно удалить первый элемент
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:  # Если список стал пустым
                self.tail = None
            self._size -= 1
            return True
        
        # Поиск элемента для удаления
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
        if current.next is None: # Элемент не найден
            return False
        
        # Удаление найденного элемента
        if current.next == self.tail: # Если удаляем последний элемент
            self.tail = current
        
        current.next = current.next.next
        self._size -= 1
        return True
    
    def remove_at(self, idx: int) -> Any: # Удалить элемент по индексу
                                          # idx: Индекс элемента для удаления
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size})") # IndexError: Если индекс вне допустимого диапазона
        
        if idx == 0: # Удаление первого элемента
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return value
        
        # Удаление из середины или конца
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        value = current.next.value
        
        if current.next == self.tail: # Если удаляем последний элемент
            self.tail = current
        
        current.next = current.next.next
        self._size -= 1
        return value
    
    def get(self, idx: int) -> Any: # Получить элемент по индексу
                                    # idx: Индекс элемента
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size})") # IndexError: Если индекс вне допустимого диапазона
        
        current = self.head
        for _ in range(idx):
            current = current.next
        
        return current.value
    
    def __iter__(self) -> Iterator[Any]: # Итератор по значениям списка
                                         # Значения списка в порядке от головы к хвосту
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int: # Количество элементов в списке
        return self._size
    
    def __str__(self) -> str: # Красивое строковое представление списка
        if self.head is None:
            return "None"
        
        parts = []
        current = self.head
        while current is not None:
            parts.append(str(current))
            current = current.next

        return " -> ".join(parts) + " -> None"
    
    def __repr__(self) -> str: # Формальное строковое представление списка
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def is_empty(self) -> bool: # Проверить пуст ли список
        return self._size == 0 # True если список пуст, иначе False
    
if __name__ == "__main__":
   # Пример использования
   lst = SinglyLinkedList()
   lst.append(1)
   lst.append(2)
   lst.prepend(0)
   lst.insert(2, 1.5)
   lst.remove_at(3)
   print(lst)
```

![terminal!](/images/lab10/terminal.png)