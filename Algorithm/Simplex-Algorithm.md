# 单纯形法
```
单纯形法是一种算法，主要解决线性规划问题。通俗的说：在一个凸可行域中，利用单纯形法，找到各个关键点。最优解就是这些关键点的其中一个(或者是一个平面）。
```
### 基础概念
```
单纯形法，仅适用于线性规划，线性规划必须是一种凸优化。
```
##### 凸优化
凸优化表示问题的可行域是“凸”的。“凸”形的可行域的标准是：你在这个可行域里面任意取2个点，然后把它们连成一条线，那么这条线一定会在可行域内。比如下面的球。
![](https://pic4.zhimg.com/3121ab3881139a8fde91f0ded97c3a4b_b.jpg)

##### 峰
峰就是常见的局部最优解。也就是说，多个峰出现，肯定会有鞍点。有鞍点，那么形状肯定不是凸的。那个线性规划则不适用。

![](https://pic2.zhimg.com/5ac19b42be35fa31af829aad3d401f81_b.jpg)

##### 综上
1. 单纯形法是凸优化算法。
2. 凸优化中只有一个峰，该峰是全局最优。（峰可能是一个平面)
3. 单纯形法寻找**路线优化目标函数**，直至达到一个峰，而该峰就是全局最右。

### 数学角度理解线性规划问题
##### 解决什么问题？
线性规划是研究在一组线性不等式或等式约束下使得某一线性目标函数取最大（或最小）的极值问题。
要求必须是凸形域

##### 线性规划标准型
![](https://github.com/thinkingfioa/Notes/blob/master/Algorithm/pictures/simplex-1.png)

##### 如何转化为标准型
- 1. 目标函数极小化，即：minz=cx, 令w=-z ,则maxw=-cx
- 2. 约束条件为不等式:
 - 约束条件为=<不等式，则在约束条件的左端加上一个非负的松弛变量；
 - 约束条件为>=不等式，则在约束条件的左端减去一个非负的松弛变量
- 3.![](https://github.com/thinkingfioa/Notes/blob/master/Algorithm/pictures/simplex-2.png)

### 举例: 二维平面几何。
##### 线性规划的一般形式
![](https://github.com/thinkingfioa/Notes/blob/master/Algorithm/pictures/Simplex3.png)
##### 线性规划的可行域
```
蓝色部分，就是可行域。我们很容易发现，可行域是凸形域。所以是一个典型的线性规划问题。
上过高中的同学大部分都知道，最优解就是在可行域的顶点。接下来，单纯形法就是利用矩阵方式找到这些可行域的顶点。
```
![](https://github.com/thinkingfioa/Notes/blob/master/Algorithm/pictures/Simplex4.png)
##### 转化为标准型线性规划问题
![](https://github.com/thinkingfioa/Notes/blob/master/Algorithm/pictures/Simplex5.png)

### 单纯形法
```
IBM提供了基本库包，可以直接调用。
单纯形法是一个不断迭代的算法，找到可行域中的顶点，得到最优解。
关注下面几点:
1. 如何判断当前解为最优解？
2. 如何选进基变量?
3. 如何选出基变量?
```

##### 判断当前最优解
如果找到一个基可行解,对非基变量xj对应的检验数![]((https://github.com/thinkingfioa/Notes/blob/master/Algorithm/pictures/Simplex6.png)都是<=0，那么找到最优解。如果出现检验数=0情况，说明找到解是对应于一个平面可行域。
![](https://github.com/thinkingfioa/Notes/blob/master/Algorithm/pictures/Simplex7.png)
##### 进基变量
从一个非基变量 -> 基变量.挑选原则:![](https://github.com/thinkingfioa/Notes/blob/master/Algorithm/pictures/Simplex8.png)
##### 出基变量
从一个出基变量 -> 非基变量.![](https://github.com/thinkingfioa/Notes/blob/master/Algorithm/pictures/Simplex9.png)

##### 具体思路

### 参考文档:
http://blog.csdn.net/wayne508/article/details/16617801
