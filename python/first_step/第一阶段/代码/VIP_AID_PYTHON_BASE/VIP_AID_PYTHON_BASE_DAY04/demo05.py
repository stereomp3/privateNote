"""
    字典dict
"""
# 1. 创建
dict01 = {}
dict02 = dict()

dict01 = {101: "a", 102: "b", 103: "c"}
dict02 = dict([(101,"a"),(102,"b")])


# 2. 添加
dict01[104] = "d"

# 3. 修改
dict01[104] = "e"

# 4. 查找
# key
print(dict01[102])
if 106 in dict01:
    print(dict01[106])

# 循环
for key in dict01:
    print(key)

for value in dict01.values():
    print(value)

for item in dict01.items():
    print(item)

for k,v in dict01.items():
    print(k)
    print(v)



