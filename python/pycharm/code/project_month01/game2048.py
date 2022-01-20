"""
    2048核心算法
        降維思想
"""
# def number_move(item):
#     for n in range(item + 1, len(list_merge)):
#         list_merge[item], list_merge[n] = list_merge[n], list_merge[item]
#
#
# def zero_to_end():
#     """
#         零元素移到列尾
#     :return:
#     """
#     for i in range(len(list_merge) - 1):
#         for y in range(i + 1, len(list_merge)):
#             if list_merge[i] == 0:
#                 number_move(i)
# def merge_element():
#     zero_to_end()
#     for number in range(len(list_merge) - 1):
#         if list_merge[number] == list_merge[number + 1]:
#             list_merge[number] += list_merge[number + 1]
#             list_merge[number + 1] = 0
#     zero_to_end()
# def map_merge():
#     map_temp = []
#     global map
#     for line in map:
#         global list_merge
#         list_merge = line
#         merge()
#         map_temp.append(list_merge)
#     map = map_temp
# def map_merge_right():
#     map_temp = []
#     global map
#     for line in map:
#         global list_merge
#         list_merge = line[::-1]
#         merge()
#         map_temp.append(list_merge[::-1])
#     map = map_temp

# 1. 定義函數，將list_merge中的零元素移動到末尾
# [2,0,0,2] --> [2,2,0,0]
# [4,0,4,0] --> [4,4,0,0]
list_merge = [2, 2, 2, 2]


def zero_to_end():
    """
        零元素移到列尾
        思路:從後向前一次判斷，如果是零元素則刪除後追加0
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# zero_to_end()
# print(list_merge)


# 2. 定義函數，將list_merge中的元素進行合併(相鄰且相同)
# [2,0,0,2] --> [2,2,0,0] --> [4,0,0,0]
# [4,0,4,0] --> [4,4,0,0] --> [8,0,0,0]
# [2,2,2,2] --> [4,4,0,0]

def merge():
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# merge()
# print(list_merge)

map = [
    [2, 0, 0, 2],
    [2, 4, 4, 2],
    [0, 4, 2, 0],
    [2, 0, 2, 0],
]


# 3. 定義函數，將二維列表map中的元素向左移

def move_left():
    """
        向左移動
        思路:將每行(一維列表)賦值給全局變量list_merge
                在通過merge函數操作數據
    """
    global list_merge
    for line in map:
        list_merge = line
        merge()


# move_left()
# print(map)


# 4.定義函數，將二維列表map中的元素向右移
# 提示: 用切片反轉

def move_right():
    """
        向右移動
        思路:將每行(反向切片)賦值給全局變量list_merge
                在通過merge函數操作數據
                再對list_merge(反向切片)
    """
    global list_merge
    for line in map:
        # 因為切片，所以創建了新列表
        list_merge = line[::-1]
        merge()  # 操作的是新列表
        line[::-1] = list_merge  # 賦值時反者放，不創建新列表


# move_right()
# print(map)


def square_matrix_transpose(matrix):
    for i in range(len(matrix) - 1):
        for y in range(i + 1, len(matrix)):
            matrix[i][y], matrix[y][i] = matrix[y][i], matrix[i][y]


# 5. 定義函數，將二維列表map中的元素向上移
def move_up():
    """
        思想:方陣轉置
            調用向左移動
            方陣轉置
    """
    square_matrix_transpose(map)
    move_left()
    square_matrix_transpose(map)


# 6. 定義函數，將二維列表map中的元素向下移
def move_down():
    """
        思想:方陣轉置
            調用向右移動
            方陣轉置
    """
    square_matrix_transpose(map)
    move_right()
    square_matrix_transpose(map)
