# STL 容器文档

### vector

##### push_back
```cpp
vector<int> myVector;
myVector.push_back(100);
```
##### pop_back
```
从后往前pop
```
```cpp
vector<int> myVector;
myVector.push_back(100);
myVector.push_back(200);
myVector.push_back(300);
//执行前: 100, 200, 300
myVector.pop_back();
//执行后: 100, 200
```
##### insert
```cpp
#include <iostream>
#include <vector>

int main ()
{
  std::vector<int> myvector (3,100);
  std::vector<int>::iterator it;
  //执行前: 100, 100, 100
  it = myvector.begin();
  it = myvector.insert ( it , 200 );
  //执行后: 200, 100, 100, 100
  
  //执行前: 200, 100, 100, 100
  myvector.insert (it,2,300);
  //执行后: 300, 300, 200, 100, 100, 100
    
  // "it" no longer valid, get a new one:
  it = myvector.begin();

  //执行前: 300, 300, 200, 100, 100, 100
  std::vector<int> anothervector (2,400);
  myvector.insert (it+2,anothervector.begin(),anothervector.end());
  //执行后: 300, 300, 400, 400, 200, 100, 100, 100

  int myarray [] = { 501,502,503 };
  //执行前: 300, 300, 400, 400, 200, 100, 100, 100
  myvector.insert (myvector.begin(), myarray, myarray+3);
  //执行后: 501, 502, 503, 300, 300, 400, 400, 200, 100, 100, 100

  return 0;
}
```
##### erase
```cpp
vector<int> myVector;
for(int i =0; i<10;i++) {
	myVector.push_back(i);
}

//执行前: 1, 2, 3, 4, 5, 6, 7, 8, 9
myVector.erase(myVector.begin() +5); // 移除下标为5的数,也就是myVector[5]=6
//执行后: 1, 2, 3, 4, 5, 7, 8, 9

//执行前: 1, 2, 3, 4, 5, 7, 8, 9
myVector.erase(myVector.begin(), myVector.begin() + 3);
//执行后: 4, 5, 7, 8, 9
```
##### swap
```cpp
  std::vector<int> foo (3,100);   // three ints with a value of 100
  std::vector<int> bar (5,200);   // five ints with a value of 200
  //执行前: foo: [100, 100, 100]
  //       bar: [200, 200, 200, 200, 200]
  foo.swap(bar);
  //执行后: foo: [200, 200, 200, 200, 200]
  //       bar: [100, 100, 100]
```
##### 遍历
1. 迭代器遍历
```cpp
for (it=myvector.begin(); it<myvector.end(); it++){
	std::cout << ' ' << *it;
}
```

### set
##### insert
##### erase
##### swap
##### find

##### 遍历

### stack

##### top
##### push
##### pop
##### swap

##### 遍历

### map

##### insert
##### erase
##### swap

##### 遍历

### queue

##### push
##### pop
##### swap
##### back
##### front

##### 遍历

### deque

##### front
##### back
##### push_back
##### push_front
##### pop_back
##### pop_front
##### insert
##### erase
##### swap

##### 遍历

### algorithm

##### find

##### copy

##### swap
##### count

##### replace
##### fill
##### reverse
##### sort
##### merge
##### min
##### max

##### 二叉搜索

##### 堆排序























