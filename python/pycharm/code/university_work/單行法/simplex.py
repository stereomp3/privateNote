import numpy as np


def pivot():
    l = list(d[0][:-2]) # 取到資料的倒數第二個
    #print(l)
    jnum = l.index(max(l))  # 轉入編號
    m = []
    for i in range(bn):
        if d[i][jnum] == 0:
            m.append(0.)
        else:
            m.append(d[i][-1] / d[i][jnum])
    #print(m)
    inum = m.index(min([x for x in m[1:] if x != 0]))  # 轉出下標
    s[inum - 1] = jnum
    r = d[inum][jnum]
    d[inum] /= r
    for i in [x for x in range(bn) if x != inum]:
        r = d[i][jnum]
        d[i] -= r * d[inum]


def solve():
    flag = True
    while flag:
        print(list(d[0][:-1]))
        if max(list(d[0][:-1])) <= 0:  # 直至所有係數小於等於0
            flag = False
        else:
            pivot()


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
d = np.loadtxt("data05.txt", dtype=float)
print(d)
(bn, cn) = d.shape # row column
print(d.shape)

s = list(range(cn - bn, cn - 1))  # 基變數列表


solve()

printSol()


