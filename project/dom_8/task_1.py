# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import json
import os
import pickle
from pathlib import Path


#
#
# def json_pickle(file_folder):
#     for i in os.listdir(file_folder):
#         if i.endswith('.json'):
#             with (open(i.replace('.json', '.pickle'), 'wb') as f_pickle,
#                   open(i) as f_json):
#                 pickle.dump(f_json.read(), f_pickle)
#
#
# if __name__ == '__main__':
#     json_pickle(Path.cwd())


def search_files(ext: str = '.json', dir_: str = '.') -> None:
    """
    Поиск файлов по расширению в текущей директории,
    Кодирование файлов байты и сохранение и в pickle.
    ext: расширение искомых файлов"""
    files = (file for file in os.listdir(dir_) if file.endswith('.json'))

    for file in files:
        name, _ = os.path.splitext(file)
        with (
            open(file, 'r') as r_file,
            open(name + '.pickle', 'wb') as w_file
        ):
            data = r_file.read()
            pickle.dump(file=w_file, obj=data)


if __name__ == '__main__':
    search_files(Path.cwd())
