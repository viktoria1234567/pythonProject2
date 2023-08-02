# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.

import json
import os
from functools import wraps
from random import randint
from typing import Callable


def secret_dec(func: Callable) -> [[int, int], None]:
    @wraps(func)
    def wrapper(*args):
        if not args[0] in range(1, 101) or not args[1] in range(1, 11):
            return func(randint(1, 100), randint(1, 10))
        return func(*args)

    return wrapper


def repeat_runs(count: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return decorator


def fun_log(func: Callable) -> Callable[..., None]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        res_dict = {}
        name = f'{func.__name__}.json'
        if os.path.exists(name):
            with open(name, encoding='utf-8') as json_f:
                if json_f.read():
                    json_f.seek(0)
                    res_dict = json.load(json_f)
        with open(name, "w", encoding='utf-8') as json_f:
            res_dict[str(args)] = args
            res_dict.update(**kwargs)
            res_dict[f"func: {args}"] = func(*args, **kwargs)
            json.dump(res_dict, json_f, indent=2, ensure_ascii=False)

    return wrapper


@repeat_runs(count=2)
@secret_dec
@fun_log
def secret_two_str(num: int, count: int):
    secret = randint(1, num)
    print(f'Угадайте число от 1 до {num}. У вас {count} попыток.')
    for attempt in range(count):
        guess = int(input(f"Попытка №{attempt + 1}: "))
        if guess < secret:
            print("Загаданное число больше")
        elif guess > secret:
            print("Загаданное число меньше")
        else:
            print("Угадали")
            return "Win"
    return "Lost"


if __name__ == '__main__':
    secret_two_str(420, 60)
