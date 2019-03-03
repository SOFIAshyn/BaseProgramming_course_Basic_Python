#
# Sofiia Petryshyn 07.01.2018
#
# Problem 19
# Задано натуральне n. Розв’язати задачу про n ферзів,
# використовуючи пошук з поверненнями (backtracking).
# Виконати програму для n=3, n=4 і n=5.
# (Дані розв'язки подано у файлі 'results_3_4_5.txt')
#
# Користувач може обрати кількість ферзів(королев) при запуску програми
#


def chooseQueenPosition(row, col):
    """
    (int, int) -> list

    Recursive function that return all previous
    positions of queens on the board
    >>> chooseQueenPosition(0, 4)
    [[]]
    """
    if row <= 0:
        return [[]]
    else:
        return addQueen(row - 1, col, chooseQueenPosition(row - 1, col))


def addQueen(row, col, lst_prev_pos):
    """
    (int, int, list) -> list

    Return list with added position of new queen
    >>> addQueen(0, 4, [])
    []
    """
    all_pos = []
    for pos in lst_prev_pos:
        for column in range(col):
            if free_hash(row, column, pos):
                all_pos.append(pos + [column])
    return all_pos


def free_hash(row, column, lst_prev):
    """
    (int, int, list) -> bool

    Return False if there is no problem with
    position of the queen and True otherwise
    >>> free_hash(0, 0, [])
    True
    """
    for i in range(row):
        if column == lst_prev[i] or column + row == i + lst_prev[i] or \
                column - row == lst_prev[i] - i:
            return False
    return True


def print_result(lst_all_combinations, n, path=0):
    """
    (list, int, int) -> None

    Print all combinations in console or file
    >>> print_result([], 1, 0)

    """
    main_text = "On the board of {} size you can put {} queens in {} ways\n" \
        .format(n, n, len(lst_all_combinations))
    file = open("queen_res.txt", "a")
    if path == 0:
        print(main_text)
    else:
        file = open("queen_res.txt", "w+")
        file.write(main_text)
        if len(lst_all_combinations) != 0:
            file.write("1 - positions of queen, 0 - empty spaces\n")
    for lst in lst_all_combinations:
        temp_board = clean_board(n)
        for i in range(n):
            temp_board[i][lst[i]] = 1
        if path == 0:
            for row in temp_board:
                print(row)
            print("_" * len(str(temp_board[0])))
        elif path == 1:
            for row in temp_board:
                file.write(str(row) + '\n')
            file.write("_" * len(str(temp_board[0])) + '\n')
    file.close()


def save_to_file(lst_all_combinations, n):
    """
    (list, int) -> None

    If user want to save file function calls other function
    >>> save_to_file([], 1)

    """
    to_file = input("Do you want to save result to file?\n'1' means YES,\t\
anything else means NO. ---> answer: ")
    if to_file.isdigit() and int(to_file) == 1:
        print_result(lst_all_combinations, n, 1)
    else:
        print("END.")
    return None


def clean_board(n):
    """
    (int) -> list

    Return list of zeros of size n
    >>> clean_board(1)
    [[0]]
    """
    board = []
    for i in range(n):
        board.append([])

    for i in range(n):
        board[i] += list(map(int, '0' * n))
    return board


def main():
    """
    () -> None

    Main function that calls other functions
    >>> main()

    """
    n = input("Enter a number of queens: ")
    while n.isdigit() is False:
        n = input("Enter a number of queens: ")
    n = int(n)

    lst_all_combinations = chooseQueenPosition(n, n)
    print_result(lst_all_combinations, n, 0)
    save_to_file(lst_all_combinations, n)


if __name__ == "__main__":
    main()
