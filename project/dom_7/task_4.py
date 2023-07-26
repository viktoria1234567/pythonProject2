# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# gринимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


import os

def group_rename(desired_name, num_digits, source_ext, target_ext, name_range=None):
    files = [f.split(source_ext)[0] for f in os.listdir('.')
             if os.path.isfile(f) and f.endswith(source_ext)]

    if not files:
        print('Таких файлов нет')
        return

    for i, file in enumerate(files, 1):
        if name_range:
            start, end = name_range
            base_name = file[start -1:end]
            new_name = base_name + desired_name + f"{i:0{num_digits}}" + target_ext
            os.rename(f'{file}{source_ext}', new_name)
            print(f'Переименован {file} в {new_name}')

group_rename('-new', 6, '.txt', '.doc', name_range=[3,6])