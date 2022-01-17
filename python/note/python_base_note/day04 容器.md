## Part 4-1 : 列表相關知識
> 列表和字符串都是可迭代對象(可以用在for)



#### 函數

* 將多個字符串拼接為一個 `list --> str`  (列表轉換成字符串)

  * str = `"連接符".join(列表) # 用連接符連接列表內容`

* 將一個字符串分拆為多個 `str --> list `  (字符串轉換成列表)

  * 列表 = `"a-b-c-d".split(-) # 以-分開字符`

  

#### 列表推導式

> EX1:

```python
list01 = [5,56,67,7,89]

list02 = []
for item in list01:
	list02.append(item + 1)
# 上面這3行可以寫成下面這一行

list02 = [item + 1 for item in list01]  # 列表推導式，從for開始讀
```



> EX2:

```python
list01 = [5,56,67,7,89]

list02 = []
for item in list01
	if item % 2 == 0 
		list03.append(item)
# 上面這4行可以寫成下面這一行

list02 = [item for item in list01 if item % 2 == 0] # 列表推導式
```



exercise01~03








## Part 4-2 : 元組

> **元組 : 變量組成的不可變序列容器    按需分配**
> **列表 : 變量組成的 可變 序列容器    預留空間**
> 列表會擴容，當預留空間滿了的時候，會新建一個更大的空間，拷貝原有數據，把表頭指向新的地方

> 表頭是隱藏的位置，我們的變數先指向表頭，表頭在指向其他地方，我們看不到表頭的ID，所有編程語言都是這樣幹的



* 元組介紹

  1. 創建 :

     ```python
     tuple01 = ()
     tuple02 = tuple()
     
     tuple01 = (12,33,4)  # 小誇號可加可不加，建議還是加	
     list01 = ["a","b","c"]
     tuple02 = tuple(list01) # 放入可迭代對象(元組常放列表)
     print(tuple02)
     ```

     > output:

     ```python
     ( 'a', 'b', 'c' )
     ```
     
     * list02 = list(tuple01) # 也可以元組轉列表
     * tuple02 = (1,) # 如果元組中只有一個元素要加逗號，不然視為變數
     
  2. 查詢 :
  
     * 特殊寫法 :

       ```python
       tuple03 = ("a", "b", "c")
       a, b, c = tuple03 # 把元組裡面的值賦予到3個變數裡，列表也可以用
       print(a)
       print(b)
       print(c)
       ```
  
       > output:
  
       ```
       a
       b
       c
       ```
  
       

> 索引 :

```python
print(tuple02[-1]) # 打印最後一個
```



> 切片 :

```python
print(tuple02[:2]) # 打印前兩個
```



> 循環 :

```python
fot item in tuple02: 
	print(item) # 打印tuple02中的每個元素
```



* 變量交換的本質就是創建元組 :  `x, y = y, x`

* 格式化字符串的本質也是創建元組 : `"姓名:%s, 年齡:%d"%("tarena", 15)`



exercise04






## Part 4-3 : 字典

> 字典定義 : 由一系列鍵值對組成的可變 "散列" 容器

* 鍵值就像是兩個變量，一個鍵對應一個值，且每條紀錄 "無序" (映射)
* 鍵必須唯一且不可變(字符串/數字/元組)，值沒有限制

​	

> 字典用 哈希運算 去決定變數放哪裡，可以快速找到需要的事物，分類



#### 字典介紹
1. 創建 :
	
	````python
	dict01 = {}
	dict02 = dict()  # 放可迭帶對象
	
	dict01 = {101: "a", 102: "b", 103: "c"}
	dict02 = dict([(101,"a"), (102,"b")]) # 可以區分得出來鍵值就可以，小中夸號不影響
	````
	
	
	
2. 添加 :
	
	```python
	dict01[104] = "d"  # 新建
	```
	
	
	
3. 修改 :
	
	```python
	dict01[104] = "e"  # 對已存在鍵值對應的內容做修改
	```
	
	
	
4. 查找 :
	
	> **key  // 索引和切片在字典裡沒意義，因為他無序**
	
	```python
	print(dict01[102])
	if 106 in dict01:
	    print(dict01[106])  # 強烈建議在印出字典前加判斷，查找是否有對應的自在字典裡，不然會報錯
	```
	
	
	
	
	

#### 字典循環 (for)

```python
dict01 = {101: "a", 102: "b", 103: "c"}
```

* 找出鍵

  ```python
  for key in dict01:
      print(key)
  ```

  > output:

  ```python
  101
  102
  103
  ```

  

* 找出值

  ```python
  for value in dict01.values:
  print(value)
  ```

  > output:

  ```python
  a
  b
  c
  ```



* 找出鍵和值(使用tuple方式呈現)

  ```python
  for item in dict01.items(): # 這個印出的是元組，比較不好使用，建議在開發使用下面的方法
  print(item)
  ```

  > output:

  ```python
  (101, 'a')
  (102, 'b')
  (103, 'c')
  ```

  

* 找出鍵和值(分開)

  ```python
  for k,v in dict01.items():
  print(k)
  print(v)
  ```

  > ouput:

  ```python
  101
  a
  102
  b
  103
  c
  ```



exercise05






## Part 4-4 : 強化-字典

#### 字典推導式
```python
dict_result = {}
	for item in range(1, 10):
		dict_result[item] = item ** 2
# 上面這三行可以寫成下面這一行

dict_result = {item: item ** 2 for item in range(1, 10)}


dict_result = {item: item ** 2 for item in range(1, 10) if item % 2 == 0} # 取裡面的偶數
```



exercise*06~09






## Part 4-5 : 集合 (最後一種容器)

> 集合定義 : 由一系列 (不重複 的 不可變類型變量)==(鍵) 組成的 可變散列容器

* 相當於是只有鍵沒有值得字典(鍵則是結合的數據)
* 集合無法讀取元素，沒辦法修改，只能刪掉再加
* 集合也用 哈希運算 多個重複變數在同一個位置，去除重複
* 集合價值 : 去重複，數學運算



#### 集合介紹

```python
set01 = set()
set02 = {"唐僧","悟空","八戒"}
```

1. 創建 :

  ```python
  list01 = ["A","b","c","A"]
  set03 = set(list01)
  print(set03)
  ```

  > output:

  ```python
  {'b', 'A', 'c'}  # 集合去除重複，位置隨機
  ```

  


2. 添加 :
	
	```python
	set01.add("A")
	```
	
	
	
3. 修改 :
	
	```python
	if A in set02: 
		set02.remove("A")
	```
	
	
	
4. 查找 :
	
	```python
	for item in set02:
	    print(set02)
	```
	
	
	
5. 數學運算
	
	```python
	set04 = {1, 2, 3}
	set05 = {2, 3, 4}
	```

	
	
	* 交集 (and)
	
	  ```python
	  print(set04 & set05)  # {2, 3}
	  ```
	
	* 聯集 (or)
	
	  ```python
	  print(set04 | set05)  # {1, 2, 3, 4}
	  ```
	
	* 補集 (notand)
	
	  ```python
	  print(set04 ^ set05) # {1, 4}
	  ```
	
	* 差集
	
	  ```python
	  print(set4 - set05) # {1}
	  print(set5 - set04) # {4}
	  ```
	
	* 子集、超集
	
	  ```python
	  set06 = {2, 3}
	  print(set06 < set04) # True 04是一個超集，06是他的子集
	  print(set04 > set06) # True 表示04裡有的06都有
	  ```
	
	  

#### 集合推導式

```python
{表達式 for 變量 in 可迭代對象}
```



exercise10~11





## Part 4-6 : 循環嵌套 (for for)
```python
print("*", end = " ")  # end默認是換行，現在把它改成空格
print("*", end = " ") 
print("*", end = " ") 
print("*", end = " ") 
```

> output:

```python
* * * *
```



#### 列表推導式嵌套
	list01 = ["香蕉","蘋果","哈密瓜"]
	list02 = ["咖啡","牛奶","雪碧","可樂"]
	
	list03 = []
		for r in list01:
			for c in list01:
				list03.append(r+c)
	# 上面4行可以寫成下面一行
	
	list03 = [r+c for r in list01 for c in list02]
	
	print(list03)	

> output:

```
['香蕉咖啡', '香蕉牛奶', '香蕉雪碧', '香蕉可樂', '蘋果咖啡', '蘋果牛奶', '蘋果雪碧', '蘋果可樂', '哈密瓜咖啡', '哈密瓜牛奶', '哈密瓜雪碧', '哈密瓜可樂']
```



exercise12~15







## 容器總結

* 字符串(str)

  ```
  儲存字符編碼，不可變序列
  創建字符串用""
  ```

  

* 列表(list)

  ```
  儲存變量，可變序列
  創建列表用[]
  
  列表添加元素: list01.append()    list01.insert() 
  
  列表表達式 --> [表達式 for 變量 in 可迭代對象 (可加可不加if...)]
  ```

  

* 元組(tuple)

  ```
  儲存變量，不可變序列
  創建元組用()
  
  元組沒有表達式，小誇號的表達式留給生成器用
  ```

  

* 字典(dict)

  ```
  儲存鍵值對，可變散列
  創建字典用{}
  
  集合添加元素: dict01[key] = "value"
  
  字典表達式 --> {item:表達式 for 變量 in 可迭代對象 (可加可不加if...)} 這裡的item是字典的索引
  ```

  

* 集合(set)

  ```
  儲存鍵，可變散列容器
  創建集合用set(), 或{單個元素沒有:}
  
  集合添加元素: set01.add()
  
  集合表達式 --> {表達式 for 變量 in 可迭代對象 (可加可不加if...)}
  ```

  

* 容器常常是一個包一個，各種容器互相配合嵌套



## 通用函數

* []   : 索引  (index)
* [:] : 切片  (slice)

* len()   : 計算內容長度
* sum() : 計算數總和
* max() : 計算最大值
* min() : 計算最小值

