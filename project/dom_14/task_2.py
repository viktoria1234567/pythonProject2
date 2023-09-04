# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

# Пользователь вводит данные
# Сдейлайте проверку данных и переобразуйте в один из вариантов:
# -целое положителдьное число
# -ыещественное положительное или отрицательное число
# -строку в нижнем решистре, если есть заглавные
# -строку в верхнем регистре

def transform_data(data):
    if data.isdecimal():
        result = int(data)
    elif data.replace('.', '', 1).isdecimal():
        result = float(data)
    elif data[0] == "-" and data.replace('-', '', 1).replace('.', '', 1).isdecimal():
        result = float(data)
    elif data != data.lower():
        result = data.lower()
    else:
        result = data.upper()

    return result


data = input("Введите данные")
result = transform_data(data)
print(f'{result =}')


# doctest

def transform_data(data):
    """
    This function transforms input data based on certain conditions.
    Args:
        data (str): the input data to be transformed.
    Returns:
        int, float, str: The transformed data.
    >>> transform_data("42")
    42

    >>> transform_data("3.14")
    3.14

    >>> transform_data("-7")
    -7

    >>> transform_data("Hello Word")
    'hello world'
    """
    if data.isdecimal():
        result = int(data)
    elif data.replace('.', '', 1).isdecimal():
        result = float(data)
    elif data[0] == "-" and data.replace('-', '', 1).replace('.', '', 1).isdecimal():
        result = float(data)
    elif data != data.lower():
        result = data.lower()
    else:
        result = data.upper()

    return result


# unittest

import unittest


class TestTransformData(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(transform_data("42"), 42)

    def test_float(self):
        self.assertEqual(transform_data("3.14"), 3.14)

    def test_negative(self):
        self.assertEqual(transform_data("-7"), -7)

    def test_lower_string(self):
        self.assertEqual(transform_data("Hello World"), 'hello world')


if __name__ == "__main__":
    unittest.main()

# pytest

import pytest
from spam_2 import transform_data


@pytest.fixture
def integer_input():
    return "42"


@pytest.fixture
def float_input():
    return "3.14"


@pytest.fixture
def negative_input():
    return "-7"


@pytest.fixture
def lower_string_input():
    return "Hello World"


def test_transform_integer(integer_input):
    result = transform_data(integer_input)
    assert result == 42


def test_transform_float(float_input):
    result = transform_data(float_input)
    assert result == 3.14


def test_transform_negative(negative_input):
    result = transform_data(negative_input)
    assert result == -7


def test_transform_lower(lower_string_input):
    result = transform_data(lower_string_input)
    assert result == 'hello world'
