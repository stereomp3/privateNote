"""
    古代的秤一斤有16两，请在终端中获取两，计算是几斤零几两。
    输入：100
    输出：6斤零4两
"""
liang_weight = int(input("请输入量："))
jin = liang_weight // 16
liang = liang_weight % 16
print(str(jin) + "斤零" + str(liang) + "两")
