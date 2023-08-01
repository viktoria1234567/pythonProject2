# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 5 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import os
import csv
import pickle
from pathlib import Path
import json




def conv_to_csv(file_name: Path) -> None:
    with(open(file_name, 'rb') as f_pickle,
         open(f'{file_name.stem}.csv', "w", newline='', encoding='utf-8') as f_csv):
        new_dict = pickle.load(f_pickle)
        j_data = json.loads(new_dict)

        csv_write = csv.writer(f_csv, dialect='excel', delimiter=',')
        csv_write.writerow(j_data.keys())
        n = [str(i).split() for i in j_data.values()]
        csv_write.writerows(n)

if __name__ == '__main__':
    conv_to_csv(Path('users.pickle'))
