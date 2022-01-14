"""
    方陣轉置([]T)
    這題重要的是推導過程
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
for i in range(len(list01) - 1):  # range(3) --> 0, 1, 2  3只有一個16不用自己交換自己
    for y in range(i + 1, len(list01)):
        list01[i][y], list01[y][i] = list01[y][i], list01[i][y]

# list01[0][1], list01[1][0]
# list01[0][2], list01[2][0]
# list01[0][3], list01[3][0]
#
# list01[1][2], list01[2][1]
# list01[1][3], list01[3][1]
#
# list01[2][3], list01[3][2]
for line in list01:
    for item in line:
        print(item, end="\t")
    print()
