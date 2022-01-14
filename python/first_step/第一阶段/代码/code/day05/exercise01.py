"""
将下列代码，定义到函数中，打印矩形。
	for r in range(3):
        for c in range(5):
            print("*", end=" ")
        print()
"""


def print_rectangle(r_count,c_count,char):
    for r in range(r_count):
        for c in range(c_count):
            print(char, end=" ")
        print()

print_rectangle(5,3,"*")
print_rectangle(2,7,"#")
