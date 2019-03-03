# def QueenPosition(row, col):
#     """
#     (int, int) -> bool
#     """
#     if row <= 0:
#         return [[]]
#     else:
#         return addQueen(row, col, QueenPosition(row - 1, col))
#
#
# def addQueen(prev_row, col, prev_positions):
#     all_cols = []
#     for prev_one in prev_positions:
#         for new_col in range(col):
#             if check_position(prev_row, new_col, prev_one):
#                 all_cols.append(prev_one + [new_col])
#     return all_cols
#
#
# def check_position(prev_row, col, prev_one):
#     for row in range(prev_row):
#         if prev_one[row] == prv

def queenproblem(rows, cols):
    if rows <= 0:
        return [[]]  # порожня дошка є розв'язком для випадку без ферзів
    else:
        return add_queen(rows - 1, cols, queenproblem(rows - 1, cols))


# Переглянути всі комбінації для часткового розв'язку,
# для яких можна додати ферзя в «new_row».
# Якщо відсутні конфлікти з частковим розв'язком,
# тоді знайдено новий розв'язок для додаткового рядка.
def add_queen(new_row, cols, known_solutions):
    new_solutions = []
    for solution in known_solutions:
        # спробувати розмістити ферзя в кожну комірку додаткового рядка
        for new_column in range(cols):
            # print('Спроба: %s в рядку %s' % (new_column, new_row))
            if no_conflict(new_row, new_column, solution):
                # відсутні конфлікти, цей варіант є розв'язком
                new_solutions.append(solution + [new_column])
                print("asdfyuio;  ", new_solutions, "  ghj\n")
    return new_solutions


# Перевіряє, чи можна поставити ферзя в комірку «new_column»/«new_row» так,
# аби не ставити під удар вже розміщенні ферзі
def no_conflict(new_row, new_column, solution):
    # Переконатись, що новий ферзь не знаходиться на одній колонці або діагоналі
    for row in range(new_row):
        if solution[row] == new_column or solution[row] + row == new_column + new_row or solution[row] - row == new_column - new_row:
            return False
    return True


def work_with_Queen(n):
    """
    (int) ->
    """
    board = []
    for i in range(n):
        board.append([])

    for i in range(n):
        board[i] += list(map(int, '0' * n))
    print(queenproblem(n, n))


def main():
    """
    () -> None
    """
    n = input("Enter a number of queens: ")
    while n.isdigit() == False:
        n = input("Enter a number of queens: ")
    n = int(n)

    work_with_Queen(n)


if __name__ == "__main__":
    main()

#
# positions = []
#     for row in range(n):
#         if row == n:
#             return True
#         for col in range(n):
#             for i in range(len(positions)):
#                 if row == positions[i][0] or col == positions[i][1] or row - col == -1 or row + col == 3:
#                     break
#                 positions.append((row, col))


# all_positions = [] # (0, 0)
# for previous_one in prev_positions:
#     for temp_col in range(col):
#         for pidrow in range(row):
#             if not ( prev_positions[pidrow] == col or row - temp_col == row - col or temp_col + row == row + col):
#                 all_positions.append(previous_one + [(row, temp_col)])
