## Part 2-1 強化-數據基本運算

做練習exercise01~04



## Part 2-2 bool運算

> bool帶有判斷性質的陳述句，bool轉換Flase的只有沒有數據或是等於0:



* 結果為flase
  * bool(0)、bool(0.0)、bool(None)、bool("")
* 其他的皆為true(bool(" ")也是true)



1. 比較運算符

  * 參與的數據類型: 主要是數值
  * 比較後的結果是: 布林類型

2. 邏輯運算符 (與(and)或(or)非(not))

  * 參與的數據類型: 布林類型
  * 比較後的結果是: 布林類型

  

* 一旦確定結果，後面的代碼不會執行:

> EX:

```python
re = 1 > 1 and input("請輸入:") == "a" //Flase and ?
print(re)

re = 1 > 1 or input("請輸入:") == "a"  //True or ?
print(re) # 已經確定了，後面不會給使用者輸入
```

> output:

```
Flase
True
```





> **這是邏輯運算符的短路邏輯，盡量把複雜的運算放到後面**

exercise01~05



## Part 2-3 選擇語句

* \是折行符，代表裡面是一行，但有誇號就可以當作一句，如果要在python內執行多行代碼要用;分開

```python
a = 1+2+\
    3+\
    4+5+6

a = (1+2+3+
     4+5+6)

a = 1; b = 2
```



* python的縮進是4個空格(Tab)，C的是{}

```python
if sex == "男":
	print("男生")
elif:
    print("女生")
else:
    print("性別未知")
```





* 程序調試
  1. 添加斷點
  2. 調序運行 Debug
  3. F7 逐語句執行
  4. Ctrl + F2 停止調試



exercise06

## Part 2-4 強化-選擇語句

> 範圍大的判斷寫前面，可以強化效能

exercise07~10



## Part 2-5 選擇語句&循環語句

>在if裡面放真值，會自動轉bool

* if 100 就等同於 if bool(100)



* 有值為true，為0或沒值為flase，所以如果是:
  * if var ==  0 #  false 
  * 可以表示成 if not var # var 為 0



* 條件賦值
根據一個條件，為變量進行賦值



```python
if input("請輸入性別:") == "男":
  	sex = 1
else:
	sex = 0
```

> 可以寫成下面一行

```python
sex = 1 if input("請輸入性別:") == "男" else 0
```

> 只能表達if else，不適用其他的





exercise11~14



## Part 2-6 強化-while循環

exercise15~17