# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

import csv
import pickle
from pathlib import Path
import os
import json


def get_size(directory):
    total_size = 0
    for dir_path, dir_name, file_name in os.walk(directory):
        for filename in dir_name:
            filepath = os.path.join(dir_path, filename)
            total_size += os.path.getsize(filepath)
    return total_size


def collection(files_path):
    data = []
    for dir_path, dir_name, file_name in os.walk(files_path):
        for name in dir_name:
            little_path = os.path.join(dir_path, name)
            size = get_size(little_path)
            data.append({
                'name': name,
                'type': 'directionary',
                'parent_dorectionary': dir_path,
                'size': size
            })
        for name in file_name:
            filepath = os.path.join(dir_path, name)
            size = os.path.getsize(filepath)
            data.append({
                'name': name,
                'type': 'file',
                'parent_directory': dir_path,
                'size': size
            })
    with(open('directory_data.json', 'w') as json_file,
         open('directory_data.csv', 'w', newline='') as csv_file,
         open('directory_data.pickle', 'wb') as pickle_file):
        json.dump(data, json_file, indent=2)

        filenames = ['name', 'type', 'parent_directory', 'size']
        writer = csv.DictWriter(csv_file, filenames=filenames)
        writer.writeheader()
        writer.writerows(data)

        pickle.dump(data, pickle_file)


if __name__ == '__mane__':
    collection(Path.cwd())
