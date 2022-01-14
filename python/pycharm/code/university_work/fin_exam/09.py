data = [0, 1, 2, 3, 4, 5, 6]


def inorder(i):  # 中序
    if (i >= 7):
        return;
    else:
        inorder(i * 2 + 1)
        inorder(i * 2 + 2)
        print(data[i], end=' ')



inorder(0)
print('\n')
