list001 = [[1, 2, 1, 0, 0, 100],
           [4, 3, 0, 1, 0, 250],
           [-5, -7, 0, 0, 1, 0]]  # 最後求出解 max

list011 = [[4, 1, -1, 0, 0, 8],
           [5, 2, 0, -1, 0, 1],
           [3, 7, 0, 0, 1, 0]]  # 最後求出解 min

list002 = [[2, 1, 2, 1, 0, 0, 0, 1],
           [2, 2, 1, 0, 1, 0, 0, 1],
           [0, 2, 1, 0, 0, 1, 0, 1],
           [-1, -1, -1, 0, 0, 0, 1, 0]]  # 最後求出解

list003 = [[2, 2, 0, -1, 0, 0, 0, 1],
           [1, 2, 2, 0, -1, 0, 0, 1],
           [1, 1, 1, 0, 0, -1, 0, 1],
           [-1, -1, -1, 0, 0, 0, 1, 0]]  # 最後求出解

dict01 = {}
'''
# print(DoubleListHelper.get_elements(list01, Vector2(1, 0), Vector2.get_right(), 3))


# rowMin和columnMin 在下面會改變
rowMin = 0
columnMin = 1

MaxRow = len(list01) - 1  # 2   0~2
MaxColumn = len(list01[0]) - 1  # 4    0~4

register = 0


# 找陣列最下面的最小值，放入columnMin裡面
for i in range(len(list01[MaxRow])):  # 這裡不一定要用MaxRow，只是求列的長度
    if register > list01[MaxRow][i]:
        columnMin = i
    register = list01[MaxRow][i]

print(columnMin)

# 找陣列尾元素除columnMin裡面的元素最小值，用那行進行高斯消去法
for i in range(len(list01) - 1):
    if register > list01[i][MaxColumn] / list01[i][columnMin] >= 0 and i >= 1:
        rowMin = i
    register = list01[i][MaxColumn] / list01[i][columnMin]

print(rowMin)

# 高斯消去法(Gaussian Elimination)
for i in range(len(list01)):
    if i != rowMin:
        mu = list01[i][columnMin] / list01[rowMin][columnMin]  # 把要乘的丟過去
        for y in range(len(list01[i])):
            list01[i][y] = list01[i][y] - list01[rowMin][y] * mu  # 對每一列進行減，把rowMin那一行變成都是0﹐除了list01[rowMin][columnMin]

print(list01)'''


def find_column(list01):
    columnMin = 0
    # 找陣列最下面的最小值，放入columnMin裡面
    for i in range((len(list01[0]) - 2) // 2):  # 在一開始的x裡面找最小，不包含加進來的x  #這裡不一定要用0，只是求列的長度
        if list01[len(list01) - 1][columnMin] > list01[len(list01) - 1][i]:
            columnMin = i
    return columnMin


def find_row(list01, columnMin):
    rowMin = 0

    checksum = 0
    flag = True
    is0 = 0  # 計算0
    is1 = 0  # 計算1
    for i in range(len(list01[0]) - 1):  # 最後一個可以為負(Answer)
        if list01[len(list01) - 1][i] < 0:
            flag = False

    for column in range(len(list01[0])):
        dict01["x" + str(column)] = list01[len(list01) - 1][column]  # 把最後一行加入字典
        if dict01["x" + str(column)] == 0 and flag:  # flag 為 True(最下面一行全部大於等於0)，才會執行跳出
            checksum += 1
            temp = 0
            for j in range(len(list01)):  # 最後一列的那一欄，全部由1個1、多個0組成，而且全部符合就break
                # print("list01"+"["+str(j)+"]"+"["+str(column)+"]"+":"+str(list01[j][column]))
                if list01[j][column] == 0:
                    temp += 1
                if abs(list01[j][column]) == 1:
                    is1 += 1
                if temp >= len(list01) - 1:
                    is0 += 1
    if checksum == is0 and checksum == is1 and is0 != 0:
        print("break:" + str(is0))
        for i in list01:
            print(i)
        return -1

    # 找陣列尾元素除columnMin裡面的元素最小值，用那行進行高斯消去法
    for i in range(len(list01) - 1):
        '''if list01[i][columnMin] == 0:
            return -1  # 跳出迴圈'''
        if list01[rowMin][columnMin] != 0:
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


'''
col = find_column(list01)
row = find_row(list01, col)
gaussian_elimination(list01, col, row)'''


def simplex_method(list01):
    while find_row(list01, find_column(list01)) != -1:
        gaussian_elimination(list01, find_column(list01), find_row(list01, find_column(list01)))
        for i in list01:
            print(i)


simplex_method(list011)
print(list011)
print(dict01)

'''
last = list(list01[0][:-2])  # 取到資料的倒數第二個
jnum = last.index(max(last))  # 轉入編號
inum = m.index(min([x for x in m[1:] if x != 0]))  # 轉出下標
r = list01[inum][jnum]
    list01[inum] /= r
    for i in [x for x in range(bn) if x != inum]:
        r = list01[i][jnum]
        list01[i] -= r * list01[inum]
'''
