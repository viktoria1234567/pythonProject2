# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from random import choices, randint
from string import ascii_lowercase, digits


def make_files(extension: str, min_name: int = 6, max_name: int = 30, min_size: int = 256,
               max_size: int = 4096, count: int = 42) -> None:
    for _ in range(count):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)

def file_generate(**kwargs) -> None:
    for extension, count in kwargs.items():
        make_files(extension=extension, count=count)


if __name__ == '__main__':
    file_generate(bin=2, jpg=1)
