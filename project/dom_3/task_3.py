# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

items = {
    'Рюкзак': 4,
    'Котелок': 8,
    'Палатка': 10
}

massa = 9

def fit_items(items, massa_max):
    box = []
    all_massa = 0
    sort_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    for thing, weight in sort_items:
        if all_massa + weight <= massa_max:
            box.append(thing)
            all_massa += weight
    return box, all_massa

massa_max = 15
backpack, all_massa = fit_items(items, massa_max)
print(backpack)
print(f'Вес рюкзака составил: {all_massa} из {massa_max}')

