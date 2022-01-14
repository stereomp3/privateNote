"""
定义方阵转置函数
for c in range(len(list01)-1):
    for r in range(c+1, len(list01)):
       list01[r][c],list01[c][r] = list01[c][r] ,list01[r][c]
"""
# def square_matrix_tranpose(matrix):
#     for c in range(len(matrix) - 1):
#         for r in range(c + 1, len(matrix)):
#             matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
#     return matrix
#
# list01 = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16],
# ]
# print(square_matrix_tranpose(list01))

def square_matrix_tranpose(matrix):
    for c in range(len(matrix) - 1):
        for r in range(c + 1, len(matrix)):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

square_matrix_tranpose(list01)
print(list01)
