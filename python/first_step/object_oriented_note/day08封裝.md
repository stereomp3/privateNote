## Part 3-1 封裝-設計思想

* 封裝思想: 分而治之，變則疏之，高內聚，低耦合  ---> "分"

  * 分而治之: 將一個大的需求分解為許多類，每個類處裡一個獨立的功能
  * 變則疏之: 變化的地方獨立封裝，避免影響其他類
  * 高內聚: 類中個方法都在完成一項任務，類的職責要單一
  * 低耦合: 類與類的關聯性與依賴性要低，每個類獨立，讓一個類的改變，盡少影響其他類

  

* 便於分工
* 便於復用
* 可擴展性強


## Part 3-2 強化-封裝設計思想

> **行為上的不同讓類去區分，數據上的不同讓對象去區分**

> exercise01~02


## Part 3-3 信息管理系統1

> 作項目(student_manager_system)，介紹軟體架構

* 需求: 實現對信息的增加、刪除、修改、各種查詢等操作

* 分析: 介面可能使用控制台，也可能使用Web等等

	識別對象:  界面視圖類     邏輯控制類      數據模型類(在介面和邏輯中封裝數據用)
	MVC架構--->  View         Controller        Model(如果View和Controller要交互數據過多，就要用Model封裝)

* 分配職責:

	界面視圖類: 負責處理界面邏輯，比如顯示菜單，獲取輸入，顯示結果等...
	邏輯控制類: 負責存儲學生信息，處理業務邏輯。比如添加、刪除等...
	數據模型類: 定義需要處裡的數據類型。比如學生信息

* 設計

	數據模型類: StudentModel
	    數據: 編號 id/*唯一*/, 姓名 name, 年齡 age, 成績 score
	
	邏輯控制類: StudentManagerController
	    數據: 學生列表 __stu_list
	    行為: 獲取列表 stu_list, 添加學生 add_student,
	          刪除學生 remove_student, 修改學生 update_student,
		  根據成績排序 order_by_score。


## Part 3-4 信息管理系統2

> 做完了 StudentModel裡面的功能

> 做完了 StudentManagerController裡面的功能


## Part 3-5 信息管理系統3

> 做了 StudentManageView裡面的功能


## Part 3-6 信息管理系統4

> 做完了 StudentManageView裡面的功能



## 總結:

> 類調用另一類:

```python
# 最常調用
實例成員: 使用對象操作     EX: self.__controller = StudentManagerController()

類成員  : 使用類操作       EX: 類.類變量
```

> 把day6裡面 shopping.py 改成面向對向的寫法，寫在day8