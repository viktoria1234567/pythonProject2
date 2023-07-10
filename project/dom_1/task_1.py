# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

hexadecimal_system: int = 16
number: int = int(input('Введите целое число: '))


def transfer_to_the_system(num: int, system: int) -> str:
    result: str = ''
    while num != 0:
        mod: str = str(num % system)
        result: str = mod + result
        num //= system
    return result


transfer: str = transfer_to_the_system(number, hexadecimal_system)
print(f'Результат - {transfer}')

print(f'Правильный ответ - {hex(number)[2:]}')
