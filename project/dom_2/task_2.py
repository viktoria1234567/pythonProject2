# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.


from fractions import Fraction
def calculator_fraction(fraction_1, fraction_2):
    num_1, denom_1 = map(int, fraction_1.split('/'))
    num_2, denom_2 = map(int, fraction_2.split('/'))

    num_add = num_1 * denom_2 + num_2 * denom_1
    num_mult = num_1 * num_2

    denom_common = denom_1 * denom_2

    gcd_add = greatest_common_divisor(num_add, denom_common)
    gcd_mult = greatest_common_divisor(num_mult, denom_common)

    addition = f'{num_add // gcd_add} / {denom_common // gcd_add}'
    multiplication = f'{num_mult // gcd_mult} / {denom_common // gcd_mult}'
    return addition, multiplication

def greatest_common_divisor(a , b):
     while b != 0:
         a, b = b, a % b
     return a

f_1 = input('Введите дробь: ')
f_2 = input('Введите дробь: ')

add, mult = calculator_fraction(f_1, f_2)
print("Сумма дробей:", add)
print("Произведение дробей:", mult)


f1 = Fraction(f_1)
f2 = Fraction(f_2)

print('Сумма дробей: ', f1 + f2)
print('Произведение дробей:', f1 * f2)
