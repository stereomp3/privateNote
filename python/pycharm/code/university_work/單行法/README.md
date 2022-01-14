單行法使用python，參考網址: https://www.itread01.com/content/1550489972.html

利用資料矩陣

x0 x1 x2 x3.....0 // z = nx1 + mx2 寫入 n m 0 0 0 ... 

x0 x1 x2 x3.....n // n表示 <= 的數字

x0 x1 x2 x3.....n

x0 x1 x2 x3.....n

x0 x1 x2 x3.....n



得出最佳解(Max Z)

data02是求最大值

```
Max z = 5x1 + 7x2
x0 + 2x1 <= 100
4x0 + 3x1 <= 250

// 有兩項比較數據，所以要加上x2,x3

(x1 , x2 >=0)
```



data04是求最小值

```
Min z = -x1 - x2
2x1 + x2 + x3 = 12
x1 + 2x2 + x4 = 9
xi>=0 i = 1,2,3,4
```



這個無法處理data03求最小值，要使用大M法





> 觀念[resource](https://ccjou.wordpress.com/2013/05/28/%E7%B7%9A%E6%80%A7%E8%A6%8F%E5%8A%83-%E4%BA%8C%EF%BC%9A%E7%AB%AF%E9%BB%9E%E8%88%87%E5%9F%BA%E8%A7%A3/)

![\begin{array}{llllll} x_1 & +x_2 & +x_3 & & &=4\\ & x_2 & & &+x_5 &=3\\ & &-3x_3 &+x_4 & +2x_5 &= 2. \end{array}](https://s0.wp.com/latex.php?latex=%5Cbegin%7Barray%7D%7Bllllll%7D+x_1+%26+%2Bx_2+%26+%2Bx_3+%26+%26+%26%3D4%5C%5C+%26+x_2+%26+%26+%26%2Bx_5+%26%3D3%5C%5C+%26+%26-3x_3+%26%2Bx_4+%26+%2B2x_5+%26%3D+2.+%5Cend%7Barray%7D&bg=ffffff&fg=000000&s=0&c=20201002)

每一個方程式的領先變數被該方程式鎖定，稱為軸變數 (pivot variable)；其他的變數未受限制，稱為自由變數 (free variable)。上式中，![x_1, x_2, x_3](https://s0.wp.com/latex.php?latex=x_1%2C+x_2%2C+x_3&bg=ffffff&fg=000000&s=0&c=20201002) 是軸變數，![x_4, x_5](https://s0.wp.com/latex.php?latex=x_4%2C+x_5&bg=ffffff&fg=000000&s=0&c=20201002) 是自由變數。係數矩陣 ![A](https://s0.wp.com/latex.php?latex=A&bg=ffffff&fg=000000&s=0&c=20201002) 的軸行 (對應軸變數的行向量) ![\begin{bmatrix} 1\\ 3\\ 0 \end{bmatrix}, \begin{bmatrix} 1\\ 1\\ 1 \end{bmatrix}, \begin{bmatrix} 1\\ 0\\ 0 \end{bmatrix}](https://s0.wp.com/latex.php?latex=%5Cbegin%7Bbmatrix%7D+1%5C%5C+3%5C%5C+0+%5Cend%7Bbmatrix%7D%2C+%5Cbegin%7Bbmatrix%7D+1%5C%5C+1%5C%5C+1+%5Cend%7Bbmatrix%7D%2C+%5Cbegin%7Bbmatrix%7D+1%5C%5C+0%5C%5C+0+%5Cend%7Bbmatrix%7D&bg=ffffff&fg=000000&s=0&c=20201002) 是線性獨立的，也就是說，![\begin{bmatrix} 1&1&1\\ 3&1&0\\ 0&1&0 \end{bmatrix}](https://s0.wp.com/latex.php?latex=%5Cbegin%7Bbmatrix%7D+1%261%261%5C%5C+3%261%260%5C%5C+0%261%260+%5Cend%7Bbmatrix%7D&bg=ffffff&fg=000000&s=0&c=20201002) 是可逆矩陣。設定自由變數為任意參數，線性方程的通解 (即解集合) 可表示為

![\begin{aligned} x_1&=-\frac{1}{3}\alpha+\frac{1}{3}\beta+\frac{5}{3} \\ x_2&=3-\beta\\ x_3&=\frac{1}{3}\alpha+\frac{2}{3}\beta-\frac{2}{3}\\ x_4&=\alpha\\ x_5&=\beta, \end{aligned}](https://s0.wp.com/latex.php?latex=%5Cbegin%7Baligned%7D+x_1%26%3D-%5Cfrac%7B1%7D%7B3%7D%5Calpha%2B%5Cfrac%7B1%7D%7B3%7D%5Cbeta%2B%5Cfrac%7B5%7D%7B3%7D+%5C%5C+x_2%26%3D3-%5Cbeta%5C%5C+x_3%26%3D%5Cfrac%7B1%7D%7B3%7D%5Calpha%2B%5Cfrac%7B2%7D%7B3%7D%5Cbeta-%5Cfrac%7B2%7D%7B3%7D%5C%5C+x_4%26%3D%5Calpha%5C%5C+x_5%26%3D%5Cbeta%2C+%5Cend%7Baligned%7D&bg=ffffff&fg=000000&s=0&c=20201002)