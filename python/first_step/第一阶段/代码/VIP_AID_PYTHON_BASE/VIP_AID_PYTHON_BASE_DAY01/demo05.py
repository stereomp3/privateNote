"""
    运算符
        算数运算符

        增强运算符
    练习:exercise04.py
    练习:exercise05.py
    练习:exercise06.py
"""
# 1. 算数运算+ - * / //  %  **
number01 = 5
number02 = 2
print(number01 / number02)  # 除到余数为零的商  2.5
print(number01 // number02)  # 除到整数商 2
print(number01 % number02)  # 获取余数 1
print(number01 ** number02)  # 幂运算 25

# 2. 增强运算+= -= *= /= //=  %=  **=
# number01 = number01 + 10
# 变量 与 其他数据运算后的结果，又赋值给了自身
number01 += 10
