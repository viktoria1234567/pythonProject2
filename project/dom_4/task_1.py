# Напишите функцию для транспонирования матрицы

matrix = [[5, 4, 3], [2, 4, 6], [4, 7, 9], [8, 1, 3]]
for res_1 in matrix:
    print(res_1)
trans_result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for a in range(len(matrix)):
    for b in range(len(matrix[0])):
        trans_result[b][a] = matrix[a][b]

print("The transpose of matrix A is: ")
for res in trans_result:
    print(res)
