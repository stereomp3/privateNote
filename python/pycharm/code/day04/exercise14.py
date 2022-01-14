"""
    打印二維列表第四行第三列元素。
    從左到右打印二維列表第二行所有元素。
    從上到下打印二為列表第一列所有元素。
    將二為列表按照表格狀輸出到終端。
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
print(list01[3][2])

# for i in range(len(list01[1])):
#     print(list01[1][i])
for item in list01[1]:
    print(item)

for i in range(len(list01)):
    print(list01[i][0])

# for i in range(len(list01)):
#     for y in range(len(list01[i])):
#         print(list01[i][y], end="\t")
#     print()
for line in list01:
    for item in line:
        print(item, end="\t")
    print()

