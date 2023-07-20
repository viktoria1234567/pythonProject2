# Создайте функцию генератор чисел Фибоначчи


def fibonachi(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b



number = 10
fibonacho_list = list(fibonachi(number))
print(fibonacho_list)
