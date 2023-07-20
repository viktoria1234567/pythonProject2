# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

name = ['Вика', 'Катя']
bet = [1000, 2000]
bonus = ['10.25%', '9.50%']

def generate_bonus(names, bets, bonuses):
    return{name: bet * float(bonus.rstrip('%')) / 100 for name, bet, bonus in zip(names, bets, bonuses)}

dict_count = generate_bonus(name, bet, bonus)
print(dict_count)
