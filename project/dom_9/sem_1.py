# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from typing import Callable
from random import randint


def fun_top(num: int, count: int) -> Callable[[], None]:
    def fun_down():
        current_num = randint(1, num)
        for item in range(1, count + 1):
            spam = int(input(f'введите число в дианазоне от 1 до {num} (попытка № {item}): \n'))
            if spam == current_num:
                print('верно')
                break
            elif spam > current_num:
                print('меньше')
            else:
                print('больше')

    return fun_down


if __name__ == '__main__':
    game = fun_top(100, 5)
    game()