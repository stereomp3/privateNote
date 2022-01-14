"""
    自定義排序算法，對列表進行升序排列。
    思路:
        依次取出元素，與後面進行比較
        發現更小的，則交換
    輸入: [2, 8, 6, 1]
    輸出: [1, 2, 6, 8]
"""
number_input = input("請輸入數字:")
list_number = list(number_input)
for i in range(len(list_number)-1):  # 沒有-1就 是最後的一個跟自己比，沒意義
    for j in range(i+1, len(list_number)):
        if int(list_number[j]) < int(list_number[i]):
            list_number[j], list_number[i] = list_number[i], list_number[j]

for i in list_number:
    print(i, end="")

