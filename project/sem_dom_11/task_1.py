"""
Создайте класс Моя Строка, где:
    будут доступны все возможности str
    дополнительно хранятся имя автора строки и время создания (time.time)
"""

import datetime


class MyStr(str):
    """Документация архива данных """
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time_create = datetime.datetime.today()
        print(f'Создал класс {cls}')
        return instance


n = MyStr("dffsdg dsfg", "Vasy")
print(n.time_create)

print({help(MyStr)})