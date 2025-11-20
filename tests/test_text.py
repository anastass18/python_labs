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
