list001 = [[1, 2, 1, 0, 0, 100],
           [4, 3, 0, 1, 0, 250],
           [-5, -7, 0, 0, 1, 0]]  # 最後求出解 max

list011 = [[4, 1, -1, 0, 0, 8],
           [5, 2, 0, -1, 0, 1],
           [3, 7, 0, 0, 1, 0]]  # 最後求出解 min

# 下面這兩個都出錯
list002 = [[2, 1, 2, 1, 0, 0, 0, 1],
           [2, 2, 1, 0, 1, 0, 0, 1],
           [0, 2, 1, 0, 0, 1, 0, 1],
           [-1, -1, -1, 0, 0, 0, 1, 0]]  # 最後求出解
list003 = [[2, 2, 0, -1, 0, 0, 0, 1],
           [1, 2, 2, 0, -1, 0, 0, 1],
           [2, 1, 1, 0, 0, -1, 0, 1],
           [-1, -1, -1, 0, 0, 0, 1, 0]]  # 最後求出解

list012 = [
    [1, 2, 100],
    [4, 3, 250],
    [-5, -7, 0]  # target
]
list013 = [
    [4, 5, 4, 2],
    [7, 8, 3, 44],
    [5, 4, 5, 5],
    [7, 5, 2, 0]
]


def identity_matrix(size, reverse=False):
    identity_list = []
    for i in range(size):
        identity_list.append([])
        for j in range(size):
            if i == j:
                if not reverse:
                    identity_list[i].append(1)
                else:
                    identity_list[i].append(-1)
            else:
                identity_list[i].append(0)
    return identity_list


def merge_matrix(list01, m=True):
    """
    bool m: 求最大值還是最小值(True = max, False = min)
    list list01: 線性方程式
    """
    identity_list = []
    if m:
        identity_list = identity_matrix(len(list01))
    else:
        identity_list = identity_matrix(len(list01), reverse=True)

    for r in range(len(list01)):
        for c in range(len(identity_list[r])):
            list01[r].insert(len(list01) - 1, identity_list[r][c])
    print(list01)

def find_column(list01):
    columnMin = 0
    for i in range((len(list01[0]) - 2) // 2):
        if list01[len(list01) - 1][columnMin] >= list01[len(list01) - 1][i]:
            columnMin = i
    return columnMin


def find_row(list01, columnMin):
    rowMin = 0

    is0 = 0
    for i in range(len(list01) - 1):
        if list01[i][columnMin] == 0:
            is0 += 1
            print("is0")
            # return -1  # 跳出迴圈

        elif list01[rowMin][len(list01[0]) - 1] / list01[rowMin][columnMin] >= list01[i][len(list01[0]) - 1] / \
                list01[i][columnMin] >= 0 and i >= 1:
            rowMin = i

        if len(list01) - 2 == is0:
            return -1

    return rowMin


def gaussian_elimination(list01, columnMin, rowMin):
    row_min = list01[rowMin][columnMin]
    for y in range(len(list01[0])):
        list01[rowMin][y] /= row_min
    for i in range(len(list01)):
        if i != rowMin:
            mu = list01[i][columnMin] / list01[rowMin][columnMin]

            for y in range(len(list01[i])):
                list01[i][y] = list01[i][y] - list01[rowMin][
                    y] * mu


def simplex_method(list01):
    count = 0
    while find_row(list01, find_column(list01)) != -1:
        count += 1
        gaussian_elimination(list01, find_column(list01), find_row(list01, find_column(list01)))
    return count


merge_matrix(list001)
print(simplex_method(list001))

for i in list001:
    print(i)
