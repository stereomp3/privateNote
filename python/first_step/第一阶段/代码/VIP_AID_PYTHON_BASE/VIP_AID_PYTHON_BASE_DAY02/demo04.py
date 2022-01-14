"""
    选择语句
    练习:exercise07.py  ~ exercise11.py
"""
sex = input("请输入性别：")
# sex  变量 等于 "男"
if sex == "男":
    print("您好，先生！")
# 否则如果
elif sex == "女":
    print("您好，女士！")
else:
    print("性别未知")

# 调试：让程序中断，逐语句执行。
# 目的：审查程序执行流程
#      查看执行过程中变量的取值
# 步骤：
# 1. 添加断点
# 2. 调试运行Debug
# 3. F7 逐语句执行
# 4. Ctrl + F2 停止调试

