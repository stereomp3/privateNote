"""
    將英文單字翻轉
    Input: How are you
    Output: you are How
"""
message = "How are you"
list_message = message.split(" ")
# list_message[0], list_message[2] = list_message[2], list_message[0]
result = " ".join(list_message[::-1])
print(result)

