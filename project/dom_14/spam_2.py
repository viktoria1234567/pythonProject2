# Пользователь вводит данные
# Сдейлайте проверку данных и переобразуйте в один из вариантов:
# -целое положителдьное число
# -ыещественное положительное или отрицательное число
# -строку в нижнем решистре, если есть заглавные
# -строку в верхнем регистре


def transform_data(data):
    if data.isdecimal():
        result = int(data)
    elif data.replace('.', '', 1).isdecimal():
        result = float(data)
    elif data[0] == "-" and data.replace('-', '', 1).replace('.', '', 1).isdecimal():
        result = float(data)
    elif data != data.lower():
        result = data.lower()
    else:
        result = data.upper()

    return result

data = input("Введите данные")
result = transform_data(data)
print(f'{result =}')

