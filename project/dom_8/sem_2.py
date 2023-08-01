# Напишите функцию, которая в бесконечном
# цикле запрашивает имя, личный идентификатор
# и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны
# независимо от уровня доступа. При перезапуске функции
# уже записанные в файл данные должны сохраняться.

import json
from pathlib import Path


def set_user(file: Path) -> None:
    unique_id = set()
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for _, value in data.items():
                unique_id.update(value.keys())
    else:
        data = {str(i): {} for i in range(1, 7 + 1)}

    while True:
        name = input('Name: ')
        if not name:
            break
        id = input('ID: ')
        level = input('Level [1, 7]: ')

        if id in unique_id and data[level].get(id) is None:
            continue
        data[level].update({id: name})
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)




if __name__ == '__main__':
    set_user(Path('users.json'))
