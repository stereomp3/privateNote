import random

abc = [[], []]
print(len(abc))
print("==============")

a = random.randrange(1, 10, 1)

print(a)

file = open("text" + ".txt", 'r+')
s = file.read(99)
for i in s:
    if i == "\n":
        print("no")
    print(i)


