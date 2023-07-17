# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

from typing import Any, Dict, Union

def build_arg(**kwargs: Any) -> Dict[Union[int, float, str, tuple, frozenset], str]:
    arg_dict: Dict[Union[int, str, tuple, frozenset], str] = {}
    for key, value in kwargs.items():
        if not isinstance(value, (int, float, str, tuple, frozenset)):
            value = str(value)
        arg_dict[value] = key
    return arg_dict
result = build_arg(a=10, b=20, c=30.5, d='hello', e=[1,2,3], f={1: 11, 2: 22})
print(result)

