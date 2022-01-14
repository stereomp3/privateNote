"""
    方陣轉置([]T)，用函數做
"""


def transpose_matrix(matrix):
    for i in range(len(matrix) - 1):
        for y in range(i + 1, len(matrix)):
            matrix[i][y], matrix[y][i] = matrix[y][i], matrix[i][y]


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
transpose_matrix(list01)
for line in list01:
    for item in line:
        print(item, end="\t")
    print()
