"""
    重写:覆盖
        子类具有和父类名称相同的方法
        调用子类对象时,执行子类方法。(父类方法被覆盖，不执行)
"""


# 对象 --> 字符串
# __str__
class Wife(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 对象 --> 字符串(没有限制)
    def __str__(self):
        return "奴家%s今年%d岁啦" % (self.name, self.age)

    # 对象 --> 字符串(python语法)
    def __repr__(self):
        return "Wife('%s', %d)"% (self.name, self.age)


w01 = Wife("双儿", 22)
# print(w01)
content = w01.__str__()
print(content)

code = w01.__repr__()
print(code)

# eval：将字符串作为python代码执行
print(eval("1+2*3"))
# print(eval(input()))

# 克隆对象
w02 = eval(w01.__repr__())
w01.age = 26
print(w02.atk)