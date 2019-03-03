col = int(input())
row = int(input())
for i in range(col):
    for j in range(row):
        if i == 0 or i == (col - 1):
            print("*", end = "")
        else:
            if j == 0 or j == (row - 1):
                print("*", end = "")
            else:
                print(" ", end = "")
    print("\n")
