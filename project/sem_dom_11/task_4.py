# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


class Rectangle:
    """Документация архива данных """
    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.area > other.area

    def __ge__(self, other):
        return self.area <= other.area

    def __lt__(self, other):
        return self.area < other.area

    def __le__(self, other):
        return self.area >= other.area


first_rectangle = Rectangle(1, 9)
second_rectangle = Rectangle(5, 13)

a = first_rectangle.area()
b = second_rectangle.area()

print(f'{a == b = }')
print(f'{a != b = }')
print(f'{a > b = }')
print(f'{a < b = }')
print(f'{a >= b = }')
print(f'{a <= b = }')

print({help(Rectangle)})