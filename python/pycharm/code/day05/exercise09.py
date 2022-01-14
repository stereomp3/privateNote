"""
    定義函數，根據小時、分鐘、秒計算總秒數
    要求:
        根據小時、分鐘、秒
        根據小時、分鐘
        根據分鐘、秒
        根據分鐘
"""


def get_total_second(hours=0, minutes=0, seconds=0):
    return hours * 60 * 60 + minutes * 60 + seconds


print(get_total_second(1, 2, 3))
print(get_total_second(1, 2))
print(get_total_second(minutes=2, seconds=3))
print(get_total_second(minutes=2))
