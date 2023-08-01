# Напишите функцию, которая сохраняет
# созданный в прошлом задании файл в формате CSV.

import csv
import json
from pathlib import Path


def json2csv(file: Path) -> None:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    rows = []
    for level, value in data.items():
        for id, name in value.items():
            rows.append({'level': int(level), 'id': int(id), 'name': name})

    with open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(rows)


if __name__ == '__main__':
    json2csv(Path('users.json'))