"""
    在不改變原有功能的定義與調用情況下(進入後台、刪除訂單)，
    為其增加新功能(驗證權限)
"""


def verify_permissions(func):  # 裝飾器
    def wrapper(*args, **kwargs):  # 合成tuple
        # 新
        print("驗證權限")
        # 舊
        return func(*args, **kwargs)  # 拆 tuple

    return wrapper


@verify_permissions  # enter_background = verify_permissions(enter_background)
def enter_background():
    print("進入後台")


@verify_permissions  # delete_order = verify_permissions(delete_order)
def delete_order():
    print("刪除訂單")


# enter_background = verify_permissions(enter_background)
# delete_order = verify_permissions(delete_order)
enter_background()
delete_order()
