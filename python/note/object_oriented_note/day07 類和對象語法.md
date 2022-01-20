## Part 2-1 實例成員
> **實例變量(self.實例變量)，代表是所有對象共通的變量，都要有**



> 可以在類的外面創建實例變量(python可以但其他語言不行)，建議不要用， 不建議 EX:

```python
class Wife:
    pass

ak = Wife()
ak.name = "阿珂" # 建創實例變量
print(ak.name) # 讀取實例變量 
```

```python
__雙下滑線定義的都是系統定義__
???.__dict__可以把裡面實例變量拿出來 
```



* 實例方法

```python
# 定義 :  def 方法名稱(self, 參數列表) # 函數
      	  方法體

# 調用 :  對象地址.實例方法名(參數列表)
  	  不建議通過類名訪問實例方法
```


## Part 2-2 類成員

* **類變量 : 大家的數據(在函數外，類裡面)**
    * 特點 : 
    
      * 存在優先對象
    
        * 隨類的加載而創建
        * 只有一份，被所有對象共有



> 實例變量(杯子，大家都用自己的)，類變量(飲水機，大家共用一台) --> 屬於面相對象
> 全局變量，局部變量 --> 屬於面相過程

> 一個類的內存只有一個地方

> **類方法: 大家的行為**

```python
說明:
-- 至少有一個形參，第一個形參用於綁定類，一般命名為"cls"
-- 使用@classmethod修飾目的是調用類方法時可以隱式傳遞類(自動傳參-->cls-->Class名)
-- 類方法中不能訪問實例成員，實例方法中可以訪問類成員(飲水機不能用你的杯子，你的杯子可以用飲水機)

作用:
-- 操作類變量，表示大家的行為
```

> exercise01~02


## Part 2-3 靜態方法

> **靜態方法既 "不訪問實例成員也不訪問類成員" ，通常做為類中獨立的工具函數，表達一個歸屬感就是不用self在裡面獨立功能的函式**

* 靜態方法:

```python
語法:
1) 定義:
	@staticmethod
	def 方法名稱(參數列表)
	    方法體

2) 調用: 
	類名.方法名(參數列表)
	不建議通過對象訪問靜態方法

說明:
-- 使用@staticmethod修式的目的是該方法不需要隱式傳參數(不會自動傳參)
```

> **exercise03 !!重要技術!!，列表的元素查詢**




## Part 2-4 封裝

> **從數據角度講封裝 : 將一些基本數據類型複合成一個自定義類型(Class)**

	優勢:
	    將數據與對數據的操作相關聯
	    代碼可讀性更高

>  **從行為角度講封裝 : 向類外提供必要功能，隱藏時線的細節**

```python
* 私有成員:
    * 作用: 無須向類外提供的成員，可以通過私有化進行屏蔽
    * 作法: 命名使用雙下劃線開頭
    * 本質: 障眼法，實際也可以訪問
		私有成員的名稱被修改為: __成員名 --> _類型__成員名，(_類型__成員名，可以直接訪問，駭客)
		可以通過__dict__屬性或dir函數查看

1. 私有化實例變量 (__age)
2. 提供兩個公開的讀寫方法 
    class Wife:
	def __init__(self, name="", age=0):
	    self.name = name
	    set_age(age)

	def get_age(self):
	    return __age

	def set_age(self, value):
	    if 20<=value<=30
		__age = value
	    else:
		raise Exception("我不要")  # 讓系統報錯

	# 把__init__裡面的放入self.set_age(age)讓數據可讀取，但修改有限制
	// 上面的方法是其他語言常用的策略，python會用另一種方法
```



## Part 2-5 封裝-屬性

> **用屬性保護數據 : **

```python
1. 建創實例變量 (self.age = age)
2. 提供兩個公開的讀寫方法 
3. 創建類變量存儲property
	# 類變量  # porperty 作用: 攔截
	age = property(fget, fset)
```

> **標準保護方法: 保護實例變量 --> 攔截**

```python
1. 建創實例變量 (self.age = age)
2. 提供兩個公開的讀寫方法 
3. 使用@property修飾讀取方法
   使用@屬性名.setter修改寫入方法
	    class Wife:
	def __init__(self, name="", age=0):
	    self.name = name
	    self.__age = age

	@property  # 建創property對象，自動綁定下面方法(讀取)
	def age(self):  # 名字要跟綁定對象一樣
	    return self.__age

	@age.setter  # 自動綁訂下面方法(寫入)
	def age(self, value):
	    if 20<=value<=30
		self.__age = value
	    else:
		raise Exception("我不要")  # 讓系統報錯
```

> exercise04



## Part 2-6 屬性相關觀念

* 屬性@property(@是裝飾器的一種寫法，之後會講)
  * 作用:
    * 公開的實例變量，缺少邏輯驗證。私有的實例變量與公開的方法相結合
    * 有使調用者的操作略顯複染。而屬性可以將兩個方法的使用方式向操作變量一樣方便。

* 屬性定義:

  ```python
  @property 
  	def 屬性名(self):
  	    return self.__屬性名
  ```

  ```python
  @屬性名.setter
  def 屬性名(self, value)
      self.__age = value
  ```

  

* 屬性說明:
  * 通常公開的屬性(讀,寫)，保護一個私有變量。
  * @property負責讀取，@屬性名.setter負責寫入
  * 唯寫屬性: 屬性名 = property(None, 寫入方法名)
  * 唯獨直接用上面定義寫，在刪掉setter



## review

```python
class MyClass:
    # 類成員:類
    total_count = 0

    @classmethod
    def print_total_count(cls):
        print(cls.total_count)

    # 實例成員:對象
    def __init__(self, name=""):
        self.name = name

    def print_self(self):
        print(self.name)

    # 靜態方法：類
    @staticmethod
    def tools():
        print("獨立的功能")
```



```python
c01 = MyClass()
c01.name = "xx"
c01.print_self()
MyClass.print_total_count()
MyClass.tools()
```

