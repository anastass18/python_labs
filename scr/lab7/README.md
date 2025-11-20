## Лабораторная работа 7

### A. Тесты для src/lib/text.py

``` python
import unittest
import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # добавляем корневую папку в путь Python

from scr.lib.text import normalize, tokenize, count_freq, top_n # импортируем из корневой папки


class TestText:
    @pytest.mark.parametrize(
        "input_text, expected",
        [
            ("Hello world", "hello world"),
            (" PYTHON  Programming  ", "python programming"),
            ("Test123", "test123"),
            ("", ""),
            ("  ", ""),
            ("Hello!!??", "hello!!??"),
            ("Привет Мир", "привет мир"),
            ("café", "café"),
        ],
    )
    def test_normalize(self, input_text, expected):
        assert normalize(input_text) == expected

    @pytest.mark.parametrize(
        "input_text, expected",
        [
            ("привет мир", ["привет", "мир"]),
            ("hello,world!!!", ["hello", "world"]),
            ("по-настоящему круто", ["по-настоящему", "круто"]),
            ("2025 год", ["2025", "год"]),
            ("emoji 😀 не слово", ["emoji", "не", "слово"]),
            ("", []),  # пустая строка
            ("   ", []),  # только пробелы
            ("!!!@@@###", []),  # только спецсимволы
            ("раз два.три,четыре!пять?", ["раз", "два", "три", "четыре", "пять"]),
            ("цифры123 и символы!", ["цифры123", "и", "символы"]),
            ("'кавычки' \"двойные\"", ["кавычки", "двойные"]),
        ],
    )
    def test_tokenize(self, input_text, expected):
        assert tokenize(input_text) == expected

    @pytest.mark.parametrize(
        "tokens, expected",
        [
            (["hello", "world", "hello"], {"hello": 2, "world": 1}),
            (["a", "b", "a", "c", "c"], {"a": 2, "b": 1, "c": 2}),
            ([], {}),  # пустой список
            (["x"], {"x": 1}),  # один элемент
            (["a", "a", "a"], {"a": 3}),  # все одинаковые
            (["1", "2", "3"], {"1": 1, "2": 1, "3": 1}),  # все разные
        ],
    )
    def test_count_freq(self, tokens, expected):
        assert count_freq(tokens) == expected

    @pytest.mark.parametrize(
        "freq, n, expected",
        [
            ({"hello": 2, "world": 1}, 1, [("hello", 2)]),
            ({"a": 5, "b": 5, "c": 3}, 2, [("a", 5), ("b", 5)]),  # ничья
            ({"x": 1}, 1, [("x", 1)]),  # один элемент
            ({}, 5, []),  # пустой словарь
            ({"a": 10, "b": 10, "c": 10}, 2, [("a", 10), ("b", 10)]),  # все одинаковые
            ({"z": 1, "y": 2, "x": 3}, 2, [("x", 3), ("y", 2)]),  # проверка порядка
        ],
    )
    def test_top_n(self, freq, n, expected):
        assert top_n(freq, n) == expected
```

![test_text!](/images/lab7/test_text.png) 

![test_text2!](/images/lab7/test_text2.png)

### B. Тесты для src/lab05/json_csv.py

``` python
import pytest
import csv, json
from pathlib import Path
from scr.lab5.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    scr = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    scr.write_text(json.dumps(data, ensure_ascii = False, indent = 2), encoding = "utf-8")
    json_to_csv(str(scr), str(dst))
    with dst.open(encoding = "utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    scr = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    data = [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]
    with open(scr, "w", newline = "", encoding = "utf-8") as f:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(data)
    csv_to_json(str(scr), str(dst))
    with dst.open(encoding = "utf-8") as f:
        rows = json.load(f)
    assert len(rows) == 2


@pytest.mark.parametrize(
    "function, input_file, error",
    [
        (json_to_csv, "people.json", ValueError),
    ],
)
def test_json_to_csv(function, input_file, error, tmp_path: Path):
    file_path = tmp_path / input_file
    file_path.write_text("Error???", encoding = "utf-8")
    dst = tmp_path / "people.csv"
    f = json_to_csv if function is json_to_csv else csv_to_json
    with pytest.raises(error):
        f(str(file_path), str(dst))
```

![json_csv_test!](/images/lab7/json_csv_test.png)

### C. Стиль кода (```black```)

![black!](/images/lab7/black.png)
