def is_painted(row, column, k):
    for i in range(k):
        for j in range(k):
            if row == column and row == k // 2:
                return False
            if row == column or k - column - 1 == row:
                return True
            if row == k // 2 and column == k // 2 - 1 or row == k // 2 and column == k // 2 + 1:
                return True
            if column == k // 2 and row == k // 2 - 1 or column == k // 2 and row == k // 2 + 1:
                return True
            else:
                return False


def draw_snowflake(k):
    res = []
    for i in range(k):
        for j in range(k):
            if is_painted(i, j, k) == True:
                res.append([i, j])
                print ("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    return None


draw_snowflake(5)
