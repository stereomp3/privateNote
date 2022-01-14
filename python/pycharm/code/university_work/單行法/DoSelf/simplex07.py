list001 = [[1, 2, 1, 0, 0, 100],
           [4, 3, 0, 1, 0, 250],
           [-5, -7, 0, 0, 1, 0]]  # 最後求出解 max

list011 = [[4, 1, -1, 0, 0, 8],
           [5, 2, 0, -1, 0, 1],
           [3, 7, 0, 0, -1, 0]]  # 最後求出解 min

list002 = [[2, 1, 2, 1, 0, 0, 0, 1],
           [2, 2, 1, 0, 1, 0, 0, 1],
           [0, 2, 1, 0, 0, 1, 0, 1],
           [-1, -1, -1, 0, 0, 0, 1, 0]]  # 最後求出解

list003 = [[2, 2, 0, -1, 0, 0, 0, 1],
           [1, 2, 2, 0, -1, 0, 0, 1],
           [1, 1, 1, 0, 0, -1, 0, 1],
           [-1, -1, -1, 0, 0, 0, -1, 0]]  # 最後求出解

list012 = [
    [1, 2, 100],
    [4, 3, 250],
    [-5, -7, 0]  # target
]
list013 = [
    [4, 5, 4, 2],
    [7, 8, 3, 44],
    [5, 4, 5, 5],
    [-7, -5, -2, 0]
]

list014 = [
    [4, 3, 12],
    [2, 1, 4],
    [1, 2, 4],
    [2, 1, 0]
]

dict00 = {}
record_dict = {}  # 用在檢查


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
        print(len(list01))
    else:
        identity_list = identity_matrix(len(list01), reverse=True)
    print(identity_list)
    for r in range(len(list01)):
        for c in range(len(identity_list[r])):
            list01[r].insert(len(list01[r]) - 1, identity_list[r][c])  # 從後面插入
    for i in list01:
        print(i)


def find_column(list01):
    columnMin = 0

    # 找陣列最下面的最小值，放入columnMin裡面
    for i in range((len(list01[0]) - 2)):  # 在一開始的x裡面找最小，不包含加進來的x  #這裡不一定要用0，只是求列的長度
        if check_column(list01, i) == -1:
            print("pass")
        elif list01[len(list01) - 1][columnMin] >= list01[len(list01) - 1][i]:
            columnMin = i
    return columnMin


def find_row(list01, columnMin):
    rowMin = 0

    if check_point(list01) == -1:  # 這裡知道了行、列，就可以開始比對
        return -1
    # 找陣列尾元素除columnMin裡面的元素最小值，用那行進行高斯消去法
    for i in range(len(list01) - 1):
        '''if list01[i][columnMin] == 0:
            return -1  # 跳出迴圈'''
        if list01[i][columnMin] != 0:
            if list01[rowMin][len(list01[0]) - 1] / list01[rowMin][columnMin] >= list01[i][len(list01[0]) - 1] / \
                    list01[i][
                        columnMin] >= 0 and i >= 1:
                rowMin = i
    print("columnMin:" + str(columnMin))
    print("rowMin:" + str(rowMin))

    return rowMin


def gaussian_elimination(list01, columnMin, rowMin):
    # 高斯消去法(Gaussian Elimination)
    # 把列元素除到1
    row_min = list01[rowMin][columnMin]
    for y in range(len(list01[0])):
        list01[rowMin][y] /= row_min
    # 進行消去
    for i in range(len(list01)):
        if i != rowMin:
            mu = list01[i][columnMin] / list01[rowMin][columnMin]  # 把要乘的丟過去

            for y in range(len(list01[i])):
                list01[i][y] = list01[i][y] - list01[rowMin][
                    y] * mu  # 對每一列進行減，把rowMin那一行變成都是0﹐除了list01[rowMin][columnMin]s


def check_point(list01):
    flag = True

    for i in range(len(list01[0]) - 2):  # 最後兩個個可以為負(Answer)
        if list01[len(list01) - 1][i] < 0:
            flag = False

    if checker(list01) == -1 and flag:  # 高斯消去結束點
        print("break")
        return -1


def checker(list01):
    checksum = 0
    is0 = 0  # 計算0
    is1 = 0  # 計算1

    for column in range(len(list01[0])):
        dict00["x" + str(column)] = list01[len(list01) - 1][column]  # 把最後一行加入字典
        if dict00["x" + str(column)] == 0:

            checksum += 1
            temp = 0
            for j in range(len(list01)):  # 最後一列的那一欄，全部由1個1、多個0組成，而且全部符合就break
                if list01[j][column] == 0:
                    temp += 1
                if abs(list01[j][column]) == 1:
                    is1 += 1
                    record_dict["x" + str(column)] = j  # 用來定位，最後算出x值要看這個
                if temp >= len(list01) - 1:
                    is0 += 1
    if checksum == is0 and checksum == is1 and is0 != 0:
        return -1


def check_column(list01, column):  # 用來幫助一開始的尋找最小行
    checksum = 0
    is0 = 0  # 計算0
    is1 = 0  # 計算1

    checksum += 1
    temp = 0
    for j in range(len(list01)):  # 最後一列的那一欄，全部由1個1、多個0組成
        if list01[j][column] == 0:
            temp += 1
        if abs(list01[j][column]) == 1:
            is1 += 1
        if temp >= len(list01) - 1:
            is0 += 1
    if checksum == is0 and checksum == is1 and is0 != 0:
        return -1


def simplex_method(list01):
    prelist = 0
    while find_row(list01, find_column(list01)) != -1:
        gaussian_elimination(list01, find_column(list01), find_row(list01, find_column(list01)))

        if list01[len(list01) - 1][len(list01[0]) - 1] == prelist:
            return gaussian_elimination(list01, find_column(list01), find_row(list01, find_column(list01)))
        else:
            prelist = list01[len(list01) - 1][len(list01[0]) - 1]

        for i in list01:
            print(i)


def print_a(list01):
    anwser = 0
    for column in range(len(dict00)):
        if dict00["x" + str(column)] == 0:
            anwser = list01[record_dict["x" + str(column)]][len(list01[0]) - 1] / \
                     list01[record_dict["x" + str(column)]][column]
        else:
            anwser = 0
        print("x" + str(column) + " = " + str(anwser))  # 求x值

    anwser = list01[len(list01) - 1][len(list01[0]) - 1] / list01[len(list01) - 1][len(list01[0]) - 2]
    print("z = " + str(anwser))


merge_matrix(list012)
simplex_method(list012)
print("=============================================================================================================")
print(list012)
print(dict00)
print_a(list012)
