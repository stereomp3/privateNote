"""
    在不改变原有功能的定义与调用情况下(进入后台、删除订单),
    为其增加新功能(验证权限).
"""
def verify_permissions(func):
    def wrapper(*args, **kwargs):  # 合
        # 新功能
        print("验证权限")
        # 旧功能
        return func(*args, **kwargs)  # 拆

    return wrapper

@verify_permissions
def enter_background():
    print("进入后台")

@verify_permissions
def delete_order():
    print("删除订单")

# enter_background = verify_permissions(enter_background)
# delete_order = verify_permissions(delete_order)

enter_background()
delete_order()