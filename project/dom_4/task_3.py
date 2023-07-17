# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

account: int = 50000
count: int = 0
result = '\nВыберите операцию:\n'\
         "\n1.Снятие"\
         '\n2.Пополнение'\
         '\n3.Выйти\n'
num_operation = 0
all_operations = []
while num_operation != 3:
    def replenishment(account: int) -> int:
        sum: int = int(input('Введите сумму снятия: '))
        сommission = sum * 0.015
        if sum % 50 == 0:
            if account > sum:
                if 30 < сommission < 600:
                    account = account - sum - сommission
                elif сommission < 30:
                    account = account - sum - 30
                else:
                    account = account - sum - 600
                all_operations.append(f'Снятие - {sum}')
            else:
                print('Недостаточно средств')
        else:
            print('Введите корректный номинал')
        return account


    def withdrawal(account: int) -> int:
        sum: int = int(input('Введите сумму пополнения: '))
        if sum % 50 == 0:
            account = account + sum
            all_operations.append(f'Пополнение - {sum}')
        else:
            print('Введите корректный номинал')
        return account



    num_operation = int(input(result))
    print(f'Вы выбрали - {num_operation}')
    count = count + 1
    if count % 3 == 0:
        account = account + (account * 0.03)
    if account > 5000000:
        account = account - (account * 0.1)
    if int(num_operation) == 1:
        account = replenishment(account)
        print(f'Остаток на счете - {account}')
        print(all_operations)
        continue
    if int(num_operation) == 2:
        account = withdrawal(account)
        print(f'Остаток на счете - {account}')
        print(all_operations)

print('Операции окончены')