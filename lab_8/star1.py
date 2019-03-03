def is_painted(row, column, k):
    for i in range(k):
        for j in range(k):
            if row == column or k - column -1 == row or row == k //2 or column == k//2:
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
    print(res)
    return None

draw_snowflake(8)
