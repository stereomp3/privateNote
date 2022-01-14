import numpy as np


def pivot(list01):
    last = list(list01[0][:-2])  # 取到資料的倒數第二個
    jnum = last.index(max(last))  # 轉入編號
    m = []
    for i in range(bn):
        if list01[i][jnum] == 0:
            m.append(0.)
        else:
            m.append(list01[i][-1] / list01[i][jnum])
    inum = m.index(min([x for x in m[1:] if x != 0]))  # 轉出下標
    s[inum - 1] = jnum
    r = list01[inum][jnum]
    list01[inum] /= r
    for i in [x for x in range(bn) if x != inum]:
        r = list01[i][jnum]
        list01[i] -= r * list01[inum]


def solve(list01):
    flag = True
    while flag:
        print(list(d[0][:-1]))
        if max(list(d[0][:-1])) <= 0:  # 直至所有係數小於等於0
            flag = False
        else:
            pivot(list01)


def printSol():
    for i in range(cn - 1):
        if i in s:
            print(d)
            print(d[s.index(i) + 1])
            print(s.index(i))
            print(i)
            print("x" + str(i) + "=%.2f" % d[s.index(i) + 1][-1])
        else:
            print("x" + str(i) + "=0.00")
    print("objective is %.2f" % (-d[0][-1]))


# 呼叫
d = np.loadtxt("data02.txt", dtype=float)
print(d)

(bn, cn) = d.shape  # row column
print(d.shape)

s = list(range(cn - bn, cn - 1))  # 基變數列表

list01 = [[5, 7, 0, 0, 0],
          [1, 2, 1, 0, 100],
          [4, 3, 0, 1, 250]]

list02 = [["5.   7.   0.   0.   0."],
          ["1.   2.   1.   0. 100."],
          ["4.   3.   0.   1. 250."]]

#print(type(d)) #<class 'numpy.ndarray'>
#print(type(list01)) # <class 'list'>
solve(list01 )

printSol()
