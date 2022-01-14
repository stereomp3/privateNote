# 画出下列代码内存图：
teacher_of_month01 = "qtx"
teacher_of_month01 = "QTX"
teacher_of_month02 = "lz"
teacher_of_month03 = teacher_of_month02
teacher_of_month02 = "lzmly"
print(teacher_of_month03)

del teacher_of_month01
