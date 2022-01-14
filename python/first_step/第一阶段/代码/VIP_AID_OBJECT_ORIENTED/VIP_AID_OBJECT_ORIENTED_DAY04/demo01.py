"""
    继承 - 行为
        财产：钱不用孩子挣,但是可以花.
        皇位：江山不用太子打,但是可以坐.
        代码：子类不用写,但是可以直接用.
"""


class Person:
    def say(self):
        print("说话")


class Student(Person):
    def study(self):
        print("学习")
        super().say()


class Teacher(Person):
    def teach(self):
        print("教学")


p01 = Person()
# 父类对象,只能访问父类成员
p01.say()

s01 = Student()
# 子类对象,可以访问父类成员和本类成员
s01.say()
s01.study()

t01 = Teacher()
# 不能访问兄弟类成员
# t01.study()


# 内置函数
# isinstance   对象  是一种  类型
# 人对象 是一种 人类型
print(isinstance(p01, Person))  # True
# 学生对象 是一种 人类型
print(isinstance(s01, Person))  # True
# 老师对象 是一种 学生类型
print(isinstance(t01, Student))  # False
# 人对象 是一种 老师类型
print(isinstance(p01, Teacher))  # False

# issubclass   类型  是一种  类型
# 人类型 是一种 人类型
print(issubclass(Person, Person))  # True
# # 学生类型 是一种 人类型
print(issubclass(Student, Person))  # True
# # 老师类型 是一种 学生类型
print(issubclass(Teacher, Student))  # False
# # 人类型 是一种 老师类型
print(issubclass(Person, Teacher))  # False


# type 对象  是  类型
# 人对象 是 人类型
print(type(p01) == Person)  # True
# 学生对象 是 人类型
print(type(s01) == Person)  # False
# 老师对象 是 学生类型
print(type(t01) == Student)  # False
# 人对象 是 老师类型
print(type(p01) == Teacher)  # False