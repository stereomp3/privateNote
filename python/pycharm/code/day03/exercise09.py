"""
    使用index([])和slice([:])做字符串的切割
"""

message = "人生苦短，我用Python"
print(message[0])
print(message[-1])
print(message[0:2])  # 0可以不寫
print(message[-6:])
print(message[len(message)//2])
print(message[::-1])
