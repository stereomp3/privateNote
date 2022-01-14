"""
    定義函數計數器，統計函數被調用的次數
"""
counter = 0


def fun01():
    global counter
    counter += 1


fun01()
fun01()
fun01()
fun01()
print("fun01()執行次數是:" + str(counter))
