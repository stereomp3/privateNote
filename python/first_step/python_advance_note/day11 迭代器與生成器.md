## Part 2-1 異常處理

> 對學生管理系統做異常處裡，可以把異常處裡做成一個函式

* 如果系統執行是 A --> B --> C --> D --> E，用一般的try要慢慢回去看誰可以處裡(越近越好)，
	但如果太遠，就會影響效率，這時可以用 raise Exception走快速通道 

  > EX: 
	
	```python
	class Wife:
	    def __init__(self, age)
	    	self.age = age  # 如果是唯讀屬性，要寫成 self.__age = age
	    	
	    @property
	    def age(self):
	    	retun self.__age
	    	
	    @age.setter
	    def age(self, value)
	   		if 20 <= value <= 30:
	        	self.__age = value
	        else:
	            raise Exception("我不要")  # 這邊拋
	
	
	try:
	    shuagner = Wife(40)
	except Exception as e:  # 可以把錯誤放到變量進行操作
	    print(e.arg)  # ('我不要',) 這邊接
	```
	
	**可以自訂義異常**，建創一個類，繼承自Exception，要使用時，只要拋他的名字，接他的名字就好
	
	
	
	>  EX:	
	
	```
	......
	raise AgeRangeError("我不要", 1323, "if 20<=value<=30")
		
	try:
	    shuagner = Wife(40)
	except AgeRangeError as e:  # 可以把錯誤放到變量進行操作，AgeRangeError繼承自Exception
	    print(e.name)  # 我不要   #.他的實例變量 
	    print(e.error_id) # 1323
	    print(e.error_code) # if 20<=value<=30
	
	錯誤種類多了再用自訂義類，一般用Exception就好了
	Exception也可以傳多個訊息，不過要用 e.args，傳出來是元組
	```



exercise01




## Part 2-2 迭代

> 迭代定義: 每一次對過程的重複稱為一次 "迭代"，而每一次迭代得到的結果會作為下一次迭代的初始值。

```python
EX: 循環獲取容器中的元素
```

### 對象可以for的條件是什麼? 

1. 被for的物件具有__iter__方法 (在python)
2. 對象可以獲取迭代器 (大多語言)



> for 原理3步驟:

```python
# 1. 獲取迭代對象
list01 = [1,2,3,4,5,65,7]
iterator = list01.__iter__()
while True:
	try:
        # 2. 獲取下一個元素
        item = iterator.__next__()
		print(item)
    # 3. 如果沒有元素，則捕獲異常，停止循環
    except StopIteration:
    	break
```



exercise02



## Part 2-3 迭代器

> 迭代器定義: 可以被__next()__函數調用並返回下一個值得對象

* 製作迭代器:

```python
class 迭代器類名:
def __next__(self):
    if 沒有元素:
    raise StopIteration
    return 元素
```

#### 迭代器作用: 
* 使用者只需通過一種方式，便可簡潔明瞭的獲取聚合對象中各種元素，而無須了解其構造
* 迭代器 設計模式 --> 隔離



#### 迭代自訂義對象(改父函式裡面的__iter__， 再使用一個字定義迭代器返回值給__iter__接收)

```python
程式代碼在demo03，使用自訂義的函式複寫
這代碼可以推導而來，資料傳遞，錯誤回傳...  # exercise03~04


for i in range(9999999) 寫一次，調一次，回傳一次，走過的都刪掉，只留現在的，不會撐爆內存
```


```python
迭代也可以不用再另外寫一個函式用 __next__方法回傳，而是使用下列方法直接寫在__iter__裡面
def __iter__(self):
# print("準備")
# yield self.__skills[0]
# print("準備")
# yield self.__skills[1]
# print("準備")
# yield self.__skills[2]  # 寫死的代碼
##  yield 等於是把函式切一刀(這裡被切成4部分，最後一部分是用來return StopIteration)

for item in self.__skill: # 活代碼
    print("準備")
    yield item    	

##  yield 以前的代碼，放到__next__方法中
##  yield 以後的數據，作為__next方法的返回值
```



exercise03~04



## Part 2-4 生成器 

> 大數據時代下，利用惰性操作，讓內存不會佔那麼多

> 生成器:  (我做別人用)



> 思想:

```python
class Generator:
    def __iter__(self):  # 生成器是可迭代對象 (可以參與for)
	return self

    def __next__(self):  # 生成器也是迭代器 **(生成數據)
	...
```



> 定義:

* 含有yield語句的函數，返回值為生成器對象
* 能夠動態(循環一次計算一次返回一次)提供數據的可迭代對象(可以提供數據的迭代器)。



> 建創:

```python
def 函數名():
    ...	
    yield 數據	(切一刀，惰性操作)
    ...	
```



> 調用:

```python
for 變量名 in 函數名():
    語句
```



> 作用:

* 在循環過程中，按照某種算法推算數據，不必建創容器儲存完整的結果
從而節省內存空間。數據量越大，優勢越明顯。

* 以上作用也稱之為延遲操作或惰性操作，通俗的講就是在需要的時候才計算結果，
而不是一次構建出所有結果。  



> **返回結果如果是單個 --> 用return，返回結果如果是多個 --> 用yield**



exercise05



## Part 2-5 生成器相關概念

> 內置生成器:

```python
enumerate() --> 把可迭代對象裡面的 元素 和 順序 組合成一個元組(item)
語法:
    for item in enumerate(可迭代對象):
	語句

    for 索引, 元素 in enumerate(可迭代對象):
	語句

zip() --> 把多組元素壓縮成一個元組，生成員組個數由最小的可迭代對象決定
語法:
    for item in zip(可迭代對象1, 可迭代對象2)
	語句
```



> 生成器表達式:  (做簡單邏輯，我做我用)

* 複習前面的表達式:

  * 列表表達式 

    * `[表達式 for 變量 in 可迭代對象 (可加可不加if...)]`
  * 字典表達式 (這裡的item是字典的索引)
  
    * `{item:表達式 for 變量 in 可迭代對象 (可加可不加if...)} `
  *  集合表達式
   * `{表達式 for 變量 in 可迭代對象 (可加可不加if...)}`
  * 元組沒有表達式，所以留給生成器用，跟上面使用方法基本一樣
  * 生成器表達式
    * `[表達式 for 變量 in 可迭代對象 (可加可不加if...)]`



> 生成器作用:

* 在循環過程中，按照某種算法推算數據，不必創建容器存儲完整的結果，從而節省內存空間。數據量越大，優勢越明顯。



exercise06




## Part 2-6 函數式編程思想

> 函數式編程思想:  讓程序靈活!

```python
# 定義:
	用一系列函數解決問題

# 體現:
* 函數可以賦值給變量，賦值後變量綁定函數。
    (傳到變數的function不能有誇號，有()傳的會是return的值: a=func01   a())

* 允許將函數作為參數傳入另一個函數。
    # 通用
    def func03(func)
	print("func03")
	func()

* 允許函數返回一個函數。
```


```python
# 思想: 跟前面的類差不多概念

# 需求1：定義函数,在列表中查找所有大於50的数字
    def find01():
		for item in list01:
    	    if item > 50:
        	        yield item

# 需求2：定義函数,在列表中查找所有小於10的数字
    def find02():
		for item in list01:
    	    if item < 10:
        	        yield item

# "封装" -- 分
    def condition01(item):
		return item > 50

    def condition02(item):
		return item < 10

# 通用
# "繼承" - 隔
    def find(func):
		for item in list01:
    	    # if item < 10:
    	    # if condition02(item):
    	    if func(item):
        		yield item

# "多態" - 做
    for item in find(condition01):
		print(item)

   for item in find(condition02):
		print(item)
```



> 大道歸一，函數思想與類思想本質是一樣的

