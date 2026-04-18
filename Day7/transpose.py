mat = [[1,2,3],[4,5,6],[7,8,9]]

transpose = list(map(lambda x: list(map(lambda y: mat[y][x], range(len(mat[0])))), range(len(mat))))

print(transpose)


for i in range(len(mat)):
    for j in range(len(mat[0])):
        transpose[i][j] = mat[j][i]
print(transpose)