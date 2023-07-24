# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

import itertools
import random


def are_queens_attacking_each_other(queens_positions):
    for i in range(len(queens_positions)):
        for j in range(i + 1, len(queens_positions)):
            row1, col1 = queens_positions[i]
            row2, col2 = queens_positions[j]

            if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
                return False
    return True


def generate_successful_arrangements():
    successful_args = []
    all_permutations = list(itertools.permutations(range(1, 9)))
    random.shuffle(all_permutations)
    for permutation in all_permutations:
        queens_positions = [(i + 1, permutation[1]) for i in range(8)]
        if are_queens_attacking_each_other(queens_positions):
            successful_args.append(queens_positions)
            if len(successful_args) == 4:
                break

    return successful_args


successful_arrangaments = generate_successful_arrangements()
for i, arrangement in enumerate(successful_arrangaments, 1):
    print(f'Расстановка {i}: {arrangement}')
