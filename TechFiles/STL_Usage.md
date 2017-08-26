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
###### 迭代器遍历
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
```cpp
  int myints[]={12,75,10,32,20,25};
  std::set<int> first (myints,myints+3);     // 10,12,75
  std::set<int> second (myints+3,myints+6);  // 20,25,32
  //执行前: first [10, 12, 75]
  //        second [20, 25, 32]
  first.swap(second);
  //执行后: first [20, 25, 32]
  //       second [10, 12, 75] 
```

##### find
```cpp
  std::set<int> myset;
  std::set<int>::iterator it;

  // set some initial values:
  for (int i=1; i<=5; i++) myset.insert(i*10);    // set: 10 20 30 40 50

  // 执行前: 10, 20, 30, 40, 50
  it=myset.find(20);
  myset.erase (it);
  // 执行后: 10, 30, 40, 50
```

##### count
```
由于set集合不重复，所以count(val)返回的结果只有0或者1.
```
```cpp
  std::set<int> myset;

  // set some initial values:
  for (int i=1; i<5; ++i) myset.insert(i*3);    // set: 3 6 9 12

  //返回结果是: 1
  myset.count(3);
  //返回结果是: 0
  myset.count(5);
```
##### 遍历
```cpp
  int myints[] = {75,23,65,42,13};
  std::set<int> myset (myints,myints+5); //13, 23, 42, 65, 75

  for (std::set<int>::iterator it=myset.begin(); it!=myset.end(); ++it){
    std::cout << ' ' << *it;
  }
```

### stack

##### top
```cpp
  std::stack<int> mystack;
  mystack.push(10);
  mystack.push(20);

  mystack.top() -= 5; //mystack.top() 的值为20
```

##### push
```cpp
  std::stack<int> mystack;

  for (int i=0; i<5; ++i) mystack.push(i);
```

##### pop
```cpp
弹出栈的最上面
```

##### swap
```cpp
  std::stack<int> foo,bar;
  foo.push (10); foo.push(20); foo.push(30);
  bar.push (111); bar.push(222);
  // 执行前: foo [10, 20, 30]
  //        bar [111, 222]
  foo.swap(bar);
  // 执行后: foo [111, 222]
  //        bar [10, 20, 30]

```

##### 遍历
```cpp
  std::cout << "Popping out elements...";
  while (!mystack.empty())
  {
     std::cout << ' ' << mystack.top();
     mystack.pop();
  }
  std::cout << '\n';
```

### map
```
c++ 中的map是默认按照key的排序。所以每次插入都会做调整。
```

##### insert
```cpp
  std::map<char,int> mymap;

  // first insert function version (single parameter):
  mymap.insert ( std::pair<char,int>('a',100) );
```

##### erase
```cpp
  std::map<char,int> mymap;
  std::map<char,int>::iterator it;

  // insert some values:
  mymap['a']=10;
  mymap['b']=20;
  mymap['c']=30;
  mymap['d']=40;
  mymap['e']=50;
  mymap['f']=60;

  it=mymap.find('b');
  //执行前: a->10, b->20, c->30, d->40, e->50, f->60
  mymap.erase (it);                   // erasing by iterator
  //执行后: a->10, c->30, d->40, e->50, f->60

  //执行前: a->10, c->30, d->40, e->50, f->60
  mymap.erase ('c');                  // erasing by key
  //执行后: a->10, d->40, e->50, f->60
  
  it=mymap.find ('e');
  //执行前: a->10, d->40, e->50, f->60
  mymap.erase ( it, mymap.end() );    // erasing by range
  //执行后: a->10, d->40
```

##### swap
```cpp
  std::map<char,int> foo,bar;

  foo['x']=100;
  foo['y']=200;

  bar['a']=11;
  bar['b']=22;
  bar['c']=33;
  // 执行前: foo [x->100, y->200]
  //        bar [a->11, b->22, c->33]
  foo.swap(bar);
  // 执行前: foo [a->11, b->22, c->33]
  //        bar [x->100, y->200]
```

##### 遍历
```cpp
for (std::map<char,int>::iterator it=foo.begin(); it!=foo.end(); ++it) {
    std::cout << it->first << " => " << it->second << '\n';
}
```

### queue

##### push
```cpp
  std::queue<int> myqueue;
  myqueue.push (myint);
```

##### pop
```
弹出最后一个数。
```

##### swap
```cpp
  std::queue<int> foo,bar;
  foo.push (10); foo.push(20); foo.push(30);
  bar.push (111); bar.push(222);
  // 执行前: foo[10, 20, 30]
  //        bar[111, 222]
  foo.swap(bar);
  // 执行后: foo[111, 222]
  //        bar[10, 20, 30]
```

##### back
```
队列的最后一位
```
```cpp
  myqueue.push(12);
  myqueue.push(75);   // this is now the back
  //执行前: 12, 75
  myqueue.back() -= myqueue.front();
  //执行后: 12, 63
```

##### front
```
队列的队首
```
```cpp
  myqueue.push(77);
  myqueue.push(16);
  //执行前: 77, 16
  myqueue.front() -= myqueue.back();    // 77-16=61
  //执行后: 61, 16
```

##### 遍历
```cpp
  std::cout << "myqueue contains: ";
  while (!myqueue.empty())
  {
    std::cout << ' ' << myqueue.front();
    myqueue.pop();
  }
```

### deque
```
双向队列
```
##### front
```cpp
```
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























