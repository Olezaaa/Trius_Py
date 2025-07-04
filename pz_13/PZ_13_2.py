#В двумерном списке элементы столбца N (N задать с клавиатуры) увеличить в два раза.

import random
rows = 3
cols = 3
matrix = [[random.randint(1, 10) for j in range(cols)] for i in range(rows)]
print("Изначальная матрица: ")
for row in matrix:
    print(row)
number = int(input("Введите номер столбца для увеличения в два раза: "))
#увеличение элементов столбца в два раза
matrix = list(map(lambda row, idx: [elem * 2 if idx == number - 1 else elem for idx, elem in enumerate(row)], matrix, range(len(matrix))))
#for i in range(len(matrix)):
#    matrix[i][number - 1] *= 2
print("Изменённая матрица: ")
for row in matrix:
    print(row)