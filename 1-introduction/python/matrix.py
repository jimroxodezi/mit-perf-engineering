import time, random


MATRIX_SIZE = 1024
# COLUMN_SIZE = 1024

A = [[random.random() for row in range(MATRIX_SIZE)] for column in range(MATRIX_SIZE)]
B = [[random.random() for row in range(MATRIX_SIZE)] for column in range(MATRIX_SIZE)]

C = [[0 for row in range(MATRIX_SIZE)] for colunm in range(MATRIX_SIZE)]

start = time.time()
for i in range(MATRIX_SIZE):
    for j in range(MATRIX_SIZE):
        for k in range(MATRIX_SIZE):
            C[i][j] = A[i][k] * B[j][k]
end = time.time()


print(end-start)
# print(B)
# print(C)