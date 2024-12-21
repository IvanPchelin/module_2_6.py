def get_matrix(n, m, value):
    matrix = []
    for a in range(n):
        matrix.append([])
        for b in range(m):
            matrix[a].append([value])
    print(matrix)
    return matrix
n = int(input('строки матрицы: '))
m = int(input('столбцы матрицы: '))
value = input('значения матрицы: ')
matrix = get_matrix(n, m, value)
if n <= 0:
    print('', n)
elif m <=0:
    print('' ,m)
else:
    print("Вывод на консоль матрицы:")
    for c in matrix:
        print(*c)