"""
    循環輸入身高，如果輸入為空，停止輸入
    打印所有人的身高，打印總數，打印最高最低和平均的身高
"""
list_height = []
while True:
    height = input("請輸入身高:")
    if height == "":
        break
    list_height.append(float(height))

# 打印所有人的身高(矩陣)
print("身高列表"+str(list_height))

# 打印所有人的身高(一行一個)
for item in list_height:
    print(item)

print("總共"+str(len(list_height)))
print("最大身高"+str(max(list_height)))
print("最小身高"+str(min(list_height)))
print("平均身高"+str(sum(list_height)/len(list_height)))

