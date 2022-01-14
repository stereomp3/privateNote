"""
    在不改變原有功能的定義與調用情況下 (func01, func02)
    為其增加新功能 (print_execute_time)
        打印執行時間:函數執行後 - 函數執行前

"""
import time


def print_execute_time(func):
    def wrapper(*args, **kwargs):
        pre = time.time()
        result = func(*args, **kwargs)
        now = time.time()
        print(now-pre)
        return result


    return wrapper


@print_execute_time
def func01():
    sum_value = 0
    for i in range(100):
        sum_value += i
    return sum_value


@print_execute_time
def func02(n):
    sum_value = 0
    for i in range(n):
        sum_value += i
    return sum_value


print(func01())
print(func02(10000))
