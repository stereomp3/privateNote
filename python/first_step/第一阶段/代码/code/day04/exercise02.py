"""
    将英文单词翻转。
    输入：How are you
    输出：you are How
"""
message = "How are you"
list_temp = message.split(" ")
result = " ".join(list_temp[::-1])
print(result)