# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix:
    _rows: int = None
    _cols: int = None
    _a_matrix: list[list[int, float]] = None

    def __init__(self, a_matrix: list[list[int, float]]):

        self._rows = len(a_matrix)
        self._cols = len(a_matrix[0])
        self._a_matrix = a_matrix

    def __add__(self, other):
        new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(self._cols):
                new_matrix[j][i] = self._a_matrix[j][i] + other._a_matrix[j][i]
        return Matrix(new_matrix)

    def __mul__(self, other):
        new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(self._cols):
                new_matrix[j][i] = self._a_matrix[j][i] * other._a_matrix[j][i]
        return Matrix(new_matrix)

    def __eq__(self, other):
        return self._a_matrix == other._a_matrix

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self._a_matrix]) + '\n'


mtx_a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
mtx_b = Matrix([[10, 11, 12], [4, 5, 6], [1, 2, 3], [7, 8, 9]])
print(f'{mtx_a == mtx_b =}')
print(mtx_a + mtx_b)
print(mtx_a * mtx_b)
