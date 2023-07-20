# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_file(way):
    dir_way, full_file = way.rsplit('/', 1)
    name, file_ext = full_file.split('.', 1)

    return dir_way, name, file_ext

file_way = '/home/user/documents/example.txt'
directory, filename, file_extension = split_file(file_way)
print(directory)
print(filename)
print(file_extension)





