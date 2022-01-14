"""
    定義父類
        動物(行為:吃)
    定義子類
        狗(行為:跑)
        鳥(行為:飛)
    體會isinstance/issubclass/type
"""


class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def run(self):
        print("跑")


class Bird(Animal):
    def fly(self):
        print("飛")


d01 = Dog()
d01.eat()
print(isinstance(d01, Animal))
print(issubclass(Dog, Animal))
print(type(d01) == Animal)
