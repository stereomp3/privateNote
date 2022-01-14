import random
Var = random.randint(1,1000)
print(Var)
underNumber = 1
TopNumber = 1000
Inumber = int(input("請輸入數字:"))

while Inumber != Var:
    # if i <= a:  
    #     # print(str(i)+"<="+str(a))
    #     print("{}<={}".format(i,a,i))
    if Var < Inumber:
        TopNumber = Inumber
    elif Var > Inumber:
        underNumber = Inumber
        

    print("{}<{}<{}".format(underNumber ,Var , TopNumber))
    Inumber = int(input("請輸入數字:"))


print("對")

    