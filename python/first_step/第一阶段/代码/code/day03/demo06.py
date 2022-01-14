"""
    容器通用操作
        以字符串为例
"""
# + : 拼接
name = "悟空"
print(id(name))
# 不可变:字符串在拼接后，产生新对象，替换name存储的地址.
name += "八戒"
print(id(name))
print(name)

# *: 重复
name = "唐僧"
name *= 3
print(name)

# 成员运算
print("大圣" in "我叫齐天大圣")
print("大圣" not in "我叫齐天大圣")

# 索引
message = "我是花果山水帘洞的齐天大圣"
print(message[0])
# 倒数第二个字符
print(message[-2])
# 正数第三个字符
print(message[2])
# print(message[20])# 索引不能超过范围

# 切片
print(message[2:5:1])
print(message[:5])
print(message[:5:2])
print(message[:])
print(message[::-1])# 圣大天齐的洞帘水山果花是我
print(message[2:-8])
print(message[2:-8:-1])# 空
print(message[2:2])# 空
print(message[2:100])# 越界不报错



