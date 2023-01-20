import time, random


ROW_SIZE = 1024
COLUMN_SIZE = 1024

A = [[random.random() for row in range(ROW_SIZE)] for column in range(COLUMN_SIZE)]
B = [[random.random() for row in range(ROW_SIZE)] for column in range(COLUMN_SIZE)]

C = [[0 for row in range(ROW_SIZE)] for colunm in range(COLUMN_SIZE)]


