# from selenium import webdriver

# # 使用 Chrome 的 WebDriver
# browser = webdriver.Chrome()

# # 開啟 Google 首頁
# browser.get('http://www.9800.com.tw/lotto38/statistics.html')
# a = browser.find_elements_by_xpath("//tbody[2]/tr/td[@style='color:#FF0000; font-weight:bold']")
# L=[]
# l=[]
# x=0
# for i in a:
#     l.append(i.text)
#     x+=1
#     if x==6:
#         x=0
#         L.append(l)
#         l=[]

# for i in L:
#     print(i)
# browser.close()



# def count_each_char_1(string):
#     res = {}
#     for i in string:
#         if i not in res:
#             res[i] = 1
#         else:
#             res[i] += 1
#     return res
 
# print(count_each_char_1('aenabsascd'))


# from selenium import webdriver

# # 使用 Chrome 的 WebDriver
# browser = webdriver.Chrome()

# # 開啟 Google 首頁
# browser.get('http://www.9800.com.tw/lotto38/statistics.html')
# a = browser.find_elements_by_xpath("//tbody[2]/tr/td[@style='color:#FF0000; font-weight:bold']")
# x=""
# for i in a:
#     x=x+i.text+','

# print(x.split(","))


x = ['05', '07', '10', '23', '28', '30', '02', '18', '20', '28', '31', '32', '06', '08', '16', '27', '28', '38', '04', '14', '18', '32', '35', '38', '02', '08', '10', '24', '37', '38', '07', '11', '15', '23', '31', '34', '02', '06', '13', '16', '26', '28', '08', '16', '19', '29', '34', '35', '04', '10', '11', '17', '18', '24', '01', '04', '13', '14', '31', '38', '07', '15', '21', '22', '29', '36', '19', '20', '27', '29', '31', '37', '01', '07', '09', '11', '12', '15', '04', '05', '10', '19', '29', '31', '12', '19', '20', '26', '27', '34', '10', '14', '22', '23', '32', '35', '10', '11', '23', '25', '30', '37', '01', '03', '04', '07', '26', '28', '06', '10', '23', '29', '35', '38', '10', '22', '28', '32', '34', '36', '']
x.pop()
res = {}
for i in x:
    if i not in res:
        res[i] = 1
    else:
        res[i] += 1
# print(res)
x=0
for k,b in res.items():
    res[k]=round(b/120,3)

l=[]
L=[]
for k,b in res.items():
    x+=b
    l.append(k)
    L.append(b)
import numpy as np
import pandas as pd
L[2]=L[2]-0.0010000000000006
ironman = np.random.choice(l, size=10000000, p=L)
valueCount = pd.Series(ironman).value_counts()
print(L)
print(valueCount)

# import random
# A=[10	,22,	28	,32,	34,	36]
# B=[6,	10,	23,	29,	35,	38]

# C=[1,2,3,4,5,7,8,9,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,30,31,33,37]
# print(random.sample(C, 6))
