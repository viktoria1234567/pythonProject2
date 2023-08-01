# ------------------------------------------- 4 -----------------------------
# Прочитайте созданный в прошлом задании
# csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл,
# где каждая строка csv файла представлена
# как отдельный json словарь. Имя исходного и конечного
# файлов передавайте как аргументы функции.

import csv
import json
from pathlib import Path


def csv2json(from_file: Path, to_file: Path) -> None:
    json_list = []
    with open(from_file, 'r', newline='', encoding='utf-8') as f:
        csv_write = csv.reader(f, dialect='excel-tab')
        for i, line in enumerate(csv_write):
            json_dict = {}
            if i == 0:
                continue
            else:
                level, id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = f"{int(id):010}"
                json_dict['name'] = name.title()
                json_dict['hash'] = hash(f"{json_dict['name']}{json_dict['id']}")
                json_list.append(json_dict)

    with open(to_file, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, indent=2)


if __name__ == '__main__':
    csv2json(Path('users.csv'), Path('new_users.json'))
