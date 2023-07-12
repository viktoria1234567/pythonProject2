# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

items = ['Привет', 7, 8, 'Пока', 8, 'Привет']
unique = set()

for i in items:
    if items.count(i) > 1:
        unique.add(i)

print(unique)