# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.
from typing import Callable


def count(num: int):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)

        return wrapper

    return deco

@count(num=10)
def print_hello():
    print("Hello")

if __name__ == '__main__':
    print_hello()
