def warshall(mat):
    n = len(mat)
    for k in range(n):
        for i in range(n):
            if i != k and mat[i][k] == 1:
                for j in range(n):
                    mat[i][j] = mat[i][j] or mat[k][j]
        for i in mat:
            print(i)
        print("___________")
    return mat


matrix = [[1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 1, 0, 1]]
for i in matrix:
    print(i)
print('\n')
mat = warshall(matrix)
for i in mat:
    print(i)
