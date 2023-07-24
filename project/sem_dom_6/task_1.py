# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint



def guess_game(start, stop, attempts) -> bool:
    guess = randint(start, stop)
    for i in range(1, attempts + 1):
        n = int(input(f'Попытка номер {i}, отгадайте число: '))
        if n > guess:
            turn = "Меньше"
        elif n < guess:
            turn = "Больше"
        else:
            print("Победа!")
            return True
        print(turn)
    else:
        return False


if __name__ == '__main__':
    print(guess_game(1, 5, 3))
