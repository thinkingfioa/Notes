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
```
C++中的Set是一个有序集合
```
##### insert
```cpp
  std::set<int> myset;
  std::set<int>::iterator it;
  std::pair<std::set<int>::iterator,bool> ret;

  // set some initial values:
  for (int i=1; i<=5; ++i) myset.insert(i*10);   

  //执行前: 10, 20, 30, 40, 50
  ret = myset.insert(20);  // no new element inserted
  //执行后: 10, 20, 30, 40, 50

  if (ret.second==false) it=ret.first;  // "it" now points to element 20

  //执行前: 10, 20, 30, 40, 50
  myset.insert (it,25);                 // max efficiency inserting
  myset.insert (it,24);                 // max efficiency inserting
  myset.insert (it,26);                 // no max efficiency inserting
  //执行后: 10, 20, 24, 25, 26, 30, 40, 50
  
  //执行前: 10, 20, 24, 25, 26, 30, 40, 50
  int myints[]= {5,10,15};              // 10 already in set, not inserted
  myset.insert (myints,myints+3);
  //执行后: 5, 10, 15, 20, 24, 25, 26, 30, 40, 50
```
##### erase
```cpp

```
  std::set<int> myset;
  std::set<int>::iterator it;

  // insert some values:
  for (int i=1; i<10; i++) myset.insert(i*10);  // 10 20 30 40 50 60 70 80 90

  it = myset.begin();
  ++it;                                         // "it" points now to 20
  // 执行前: 10, 20, 30, 40, 50, 60, 70, 80, 90; (*it) = 20
  myset.erase (it);
  //执行后: 10, 30, 40, 50, 60, 70, 80, 90; 
  
  //执行前: 10, 30, 40, 50, 60, 70, 80, 90;
  myset.erase (40);
  //执行后: 10, 30, 50, 60, 70, 80, 90; 
  
  it = myset.find (60);
  //执行前: 10, 30, 50, 60, 70, 80, 90; 
  myset.erase (it, myset.end());
  //执行后: 10, 30, 50;
```

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























