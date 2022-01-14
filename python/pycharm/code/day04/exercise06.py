"""
我無解!
    計算字符串中每個字符出現的次數
    輸入 : abcbdeacb
    輸出 :
        字符a,2次
        字符b,3次
        字符c,2次
        字符d,1次
        字符e,1次
"""
dict01 = {}
str_input = input("輸入字符:")
for i in str_input:
    if i not in dict01:
        dict01[i] = 1
    else:
        dict01[i] += 1

for k, v in dict01.items():
    print("字符'%s',%d次" % (k, v))
