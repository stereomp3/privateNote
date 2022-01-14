"""
    异常处理
"""


def div_apple(apple_count):
    person_count = int(input("请输入人数："))# ValueError
    result = apple_count / person_count# ZeroDivisionError
    print("每个人分%d个苹果" % result)


# 写法1：根据不同的错误,做出不同的逻辑处理
# try:
#     div_apple(10)
# except ValueError:
#     print("输入的必须是整数")
# except ZeroDivisionError:
#     print("输入的不能是零")

# 写法2：不同的错误,相同的处理逻辑
# try:
#     div_apple(10)
# # except Exception:
# except:
#     print("出错喽")

# # 写法3：如果没有出错,可以单独定义逻辑.
# try:
#     div_apple(10)
# except:
#     print("出错喽")
# else:
#     print("没有错误")

# 写法4：如果没有出错,可以单独定义逻辑.
try:
    div_apple(10)
finally:
    print("无论是否错误,一定执行的逻辑")


