## Part 4-1 繼承-方法

* 繼承: 子類不用寫，但是可以 直接 用

```python
class Person:
    def say("說話")

class Student(Person):
    del study(self)
	print("學習")
	#  self.say() 不建議用，會混淆
	super().say()

class Teather(Person):
     pass

s01 = Student()
s01.say()  # 可以直接用

p01 = Teather
```

> 子類對象可以訪問父類，不能訪問兄弟
>
> 

# 內置函數
```python
isinstance  判斷    對象 是 類型 
print(isinstance(p01,Person))  #               True
print(isinstance(s01,Person))  # 學生屬於人    True
print(isinstance(t01,Student))  # 老師屬於學生 False
print(isinstance(p01,Teacher))  #              False

issubclass  判斷     類型  是  類型  
print(issubclass(Person,Person))  #                      True
print(issubclass(Student,Person))  # 學生類型屬於人類型  True
print(issubclass(Teacher,Student))  # 老師類型是學生類型 False
print(issubclass(Person,Teacher))  #                     False
 
type 判斷   對象   是   類型    
print(type(p01) == Person))  #                       True
```
> !!! 常見錯誤	

```python
print(type(s01) == Person))  # 學生對象是類型        False
print(type(t01) == Student))  # 老師對象是學生類型   False
print(type(p01) == Teacher))  #                      False   
```



> 父類寫共性，子類寫特性

> exercise01


## Part 4-2 繼承-數據

* 如果子類沒有構造函數，直接使用父類構造函數
* 如果子類有構造函數，創建子類，只有調用子類構造函數
* 創建子類對象不會生成父類對象

```python
super().__init__(name) # 如果父類有構造函數就要用super().__init__加入子類構造函數，可以調父類構造函數

class 子類(父類)
	def __init__(self,參數列表)
	    super().__init__(參數列表)
	    self.自身實例變量 = 參數
```

#### 重寫(overwrite)
```python
子類具有和父類名稱相同的方法，調用子類對象時，執行子類方法
				(父類方法被覆蓋，不執行)
	# 對象 --> 字符串
	# EX: __str__: 將對象轉換為字符串(對人有好的(沒有限制))
      __repr__: 將對象轉換為字符串(解釋器可識別的(有限制，須滿足python語法))，搭配eval

class Wife:
    def __init__(self, name="", age=0):
	self.name = name
	self.age = age

    def __str__(self):
	return "奴家%s今年%d歲啦"%(self.name,self.age)

    def __repr__(self):
	return "Wife('%s', %d)"%(self.name,self.age)
```


```python
 w01 = Wife("雙兒", 22)
 content = w01.__str__()  # 父類的__str__ 會讓下面印出來變 --> <__main__.Wife object at 0x00F0B040>
 print(content)   # 加上子類的__str__ 輸出就會變 --> 奴家雙兒今年22歲啦    

 code = w01.__repr__()
 print(code)    # Wife('雙兒', 22)
```

> **每個類都會繼承自object物件，所以__str__就是他其中一個函數**

#### 繼承優缺點
    * 優點
    一種代碼複用的方式
    
    * 缺點
    耦合度高: 複類的變化，直接影響到子類

> exercise02




## Part 4-3 運算符重載

> eval  :將字符串作為python代碼執行

```python
print(eval("1+2*3")) # 7
print(eval(input())) # 容易成為病毒入侵的地方，
		       apple就有明文規定不能讓字符串轉代碼，而android沒有，所以android病毒多

w01 = Wife("雙兒", 22)
```



> **克隆對象**

```python
w02 = eval(w01.__repr__())
w01.age = 26
print(w02.age) # 22
```



> 運算符重載(重寫): 自定義對象用python運算符

```python
exercise03裡面有重寫的運算符
我們呼叫的 +  -  *  / ... 其實都是在叫函式
EX: 
    pos = 1
    dir = 0
    pos + dir  # 這行指的是 pos.__add(dir)
```



> 複合運算符重載 +=  -=  *=  /= ...

```python
exercise04裡面有重寫的複合運算符

複合運算和運算符差在哪裡?
EX:
    
# 運算符會建創 '新' 對象
list01 = [1]
print(id(list01))  # 140195509160072
list01 = list01 + [2]
print(id(list01))  # 140195509160584

# 複合運算是累加(在原有對象基礎上增加)
list01 = [1]
print(id(list01))  # 140195509160072
list01 += [2]
print(id(list01))  # 140195509160072
```



> 比較運算符重載 <  <=  >  >=  ==  !=

```python
exercise05裡面有重寫的比較運算符

sort(list)可以幫物件進行升序排序，內部再循環調用每個元素的__lt__方法  # <
in 的內部也在循環調用每個元素的__eq__方法，預設是比較地址  # ==
list.remove(), list.count() 也是使用__eq__
```

> 運算符重載 主要用兩個 `__str__, __eq__`

> exercise03~05

////////////////////////////////////////////////////////////////////////////////////////////////////////////

## Part 4-4 設計思想

> 面相對象設計原則:

	1. 開閉原則: 允許增加新功能，但是不能修改以前的代碼
	
	2. 依賴倒置: 使用父類，不調用子類 --> 穩定
			子類的功能用重載讓他有個性

* 封裝: 分成多類(分)
* 繼承: 隔離變化(增加新代碼而不修改以前代碼)
* 多態: 子類重寫(做變化點)

> 分隔做


## Part 4-5 強化-設計思想

* 多態

    定義:
    設計角度來說: 父類的同一種動作或行為，在不同的子類上有不同的實現(強調子的特性)
    語法角度來說 --> 重寫

* 封裝: 分
* 繼承: 隔
* 多態: 做

> exercise06

////////////////////////////////////////////////////////////////////////////////////////////////////////////

## Part 4-6 設計原則

> 六大設計原則

    1. 開閉原則 (目標、總的指導思想)
    Open Closed Principle
    對擴展開放，對修改關閉
    增加新功能，不改變原有代碼
    
    2. 類的單一職責 (一個類的定義)
    Single Responsibility Principle
    一個類有且只有一個改變他的原因  --> 不能因為好幾個原因改一個類，只能因為一個原因
    
    3. 依賴導致 (依賴抽象)
    Dependency Inversion Principle
    客戶端代碼(調用的類)盡量依賴抽象(使用父類)。
    抽象不應該依賴細節， 細節應該依賴抽象。
    
    4. 組合復用原則 (復用的最佳實踐)
    Composite Reuse Principle
    如果僅僅為了代碼復用，優先選擇組合復用(設一個對象接收，使用裡面的方法)而非繼承復用。
    組合的耦合性相對低。
    
    繼承 --> 統一變化點     組合 --> 使用變化點
    
    這邊先講4點，後面兩點之後再說
    
    5. 里氏替換 (繼承後的重寫，指導繼承的設計)
    6. 迪米特法則 (類與類交互的原則)



> exercise07