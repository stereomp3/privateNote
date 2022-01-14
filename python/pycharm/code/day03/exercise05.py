"""
    判斷質數
"""
# while寫法

# number = int(input("請輸入一個整數:"))
#
# count = 2
# prime_number = True
#
# while count < number:
#     if not number % count:
#         prime_number = False
#         break
#     count += 1
#
# if prime_number:
#     print("輸入是質數")
# else:
#     print("輸入非質數")


# for寫法 快 

number = int(input("請輸入一個整數:"))

for i in range(2, number):
    if number % i == 0:
        print("不是質數")
        break
else:
    print("是質數")
