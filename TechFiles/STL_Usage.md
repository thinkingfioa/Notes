# STL 容器文档

```
@author 鲁伟林
之前常用的语言是: C++。现在使用的是Java，所以抽空整理下C++集合的使用方法。
gitHub地址：https://github.com/thinkingfioa/Notes/blob/master/TechFiles/STL_Usage.md
```

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
C++中的Set是一个有序-去重集合
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
  // 执行前: 10, 20, 30, 40, 50, 60, 70, 80, 90; //(*it) = 20
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
```
返回队首
```
```cpp
  std::deque<int> mydeque;

  mydeque.push_front(77);
  mydeque.push_back(20);
  //执行前: 77, 20
  mydeque.front() -= mydeque.back();
  //执行后: 57, 20
```

##### back
```
双向队列的尾部
```
```cpp
  std::deque<int> mydeque;

  mydeque.push_back(10);

  while (mydeque.back() != 0)
    mydeque.push_back ( mydeque.back() -1 );

```

##### push_back
```cpp
  std::deque<int> mydeque;
  //执行前: []
  mydeque.push_back(1);
  //执行后: [1]
  
  //执行前: [1]
  mydeque.push_back(2);
  //执行后: [1,2]
```

##### push_front
```cpp
  std::deque<int> mydeque (2,100);     // two ints with a value of 100
  //执行前: 100, 100
  mydeque.push_front (200);
  //执行后: 200, 100, 100
  
  //执行前: 200, 100, 100
  mydeque.push_front (300);
  //执行前: 300, 200, 100, 100
```

##### pop_back
```cpp
  //执行前: 
  mydeque.push_back (10);
  mydeque.push_back (20);
  mydeque.push_back (30);
  //执行后: 10, 20, 30
  
  //执行前: 10, 20, 30
  mydeque.pop_back(); 
  //执行后: 10, 20
```

##### pop_front
```cpp
  //执行前: 
  mydeque.push_back (100);
  mydeque.push_back (200);
  mydeque.push_back (300);
  //执行后: 100, 200, 300
  
  //执行前: 100, 200, 300
  mydeque.pop_front();
  //执行后: 200, 300
```
##### insert
```cpp
  std::deque<int> mydeque;

  // set some initial values:
  for (int i=1; i<6; i++) mydeque.push_back(i); // 1 2 3 4 5

  std::deque<int>::iterator it = mydeque.begin();
  ++it;
  
  //执行前: 1, 2, 3, 4, 5
  it = mydeque.insert (it,10); 
  //执行后: 1, 10, 2, 3, 4, 5
  // "it" now points to the newly inserted 10

  //执行前: 1, 10, 2, 3, 4, 5
  mydeque.insert (it,2,20);                     // 1 20 20 10 2 3 4 5
  //执行后: 1, 20, 20, 10, 2, 3, 4, 5
  // "it" no longer valid!

  it = mydeque.begin()+2;

  //执行前: 1, 20, 20, 10, 2, 3, 4, 5
  std::vector<int> myvector (2,30);
  mydeque.insert (it,myvector.begin(),myvector.end());
  //执行后: 1, 20, 30, 30, 20, 10, 2, 3, 4, 5
```
##### erase
```cpp
  // set some values (from 1 to 10)
  for (int i=1; i<=10; i++) mydeque.push_back(i);

  // erase the 6th element
  //执行前: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
  mydeque.erase (mydeque.begin()+5);
  //执行后: 1, 2, 3, 4, 5, 7, 8, 9, 10
  
  // erase the first 3 elements:
  //执行前: 1, 2, 3, 4, 5, 7, 8, 9, 10
  mydeque.erase (mydeque.begin(),mydeque.begin()+3);
  //执行后: 4, 5, 7, 8, 9, 10

```
##### swap
```cpp
  unsigned int i;
  std::deque<int> foo (3,100);   // three ints with a value of 100
  std::deque<int> bar (5,200);   // five ints with a value of 200
  
  //执行前: foo [100, 100, 100]
  //       bar [200, 200, 200, 200, 200]
  foo.swap(bar);
  //执行后: foo [200, 200, 200, 200, 200]
  //       bar [100, 100, 100]
```

##### 遍历
```cpp
for (std::deque<int>::iterator it = mydeque.begin(); it!=mydeque.end(); ++it) {
  std::cout << ' ' << *it;
}
```
```cpp
  while (!mydeque.empty()) {
    sum+=mydeque.back();
    mydeque.pop_back(); 
  }
```

### algorithm

##### find
```cpp
  //数组中查询
  int myints[] = { 10, 20, 30, 40 };
  int * p;

  p = std::find (myints, myints+4, 30);
  if (p != myints+4)
    //输出: 30
  else
    std::cout << "Element not found in myints\n";

  // vector中查询
  std::vector<int> myvector (myints,myints+4);
  std::vector<int>::iterator it;

  it = find (myvector.begin(), myvector.end(), 30);
  if (it != myvector.end())
    //输出: 30
  else
    std::cout << "Element not found in myvector\n";
```

##### copy
```cpp
  int myints[]={10,20,30,40,50,60,70};
  std::vector<int> myvector (7);
  //执行前: myvector: 
  std::copy ( myints, myints+7, myvector.begin() );
  //执行前: myvector: 10, 20, 30, 40, 50, 60, 70
```

##### swap
```cpp
  int x=10, y=20;                              // x:10 y:20
  //执行前: x:10, y:20
  std::swap(x,y);                              // x:20 y:10
  //执行后: x:20, y:10


  std::vector<int> foo (4,x), bar (6,y);       // foo:4x20 bar:6x10
  
  //执行前: foo[20, 20, 20, 20]
  //       bar[10, 10, 10, 10]
  std::swap(foo,bar);                          // foo:6x10 bar:4x20
  //执行前: foo[20, 20, 20, 20]
  //       bar[10, 10, 10, 10]
```
##### count
```cpp
  int myints[] = {10,20,30,30,20,10,10,20};   // 8 elements
  //记录数组myints中，10的个数
  int mycount = std::count (myints, myints+8, 10);
  //输出结果 mycount = 3

  std::vector<int> myvector (myints, myints+8);
  //记录数组myvector中，20的个数
  mycount = std::count (myvector.begin(), myvector.end(), 20);
  //记录数组myvector中，20的个数

```

##### replace
```cpp
int myints[] = { 10, 20, 30, 30, 20, 10, 10, 20 };
//执行前: myvector: []
std::vector<int> myvector (myints, myints+8);            
//执行后: myvector: 10, 20, 30, 30, 20, 10, 10, 20

//执行前: myvector: 10, 20, 30, 30, 20, 10, 10, 20
std::replace (myvector.begin(), myvector.end(), 20, 99); 
//执行前: myvector: 10, 99, 30, 30, 99, 10, 10, 99
```
##### fill
```cpp
//执行前 myvector: []
std::vector<int> myvector (8);                      
//执行后 myvector: 0,0,0,0,0,0,0,0

//执行前 myvector: 0,0,0,0,0,0,0,0
std::fill (myvector.begin(),myvector.begin()+4,5);   
//执行后 myvector: 5,5,5,5,0,0,0,0
//执行后 myvector: 5,5,5,5,0,0,0,0
  std::fill (myvector.begin()+3,myvector.end()-2,8); 
//执行后 myvector: 5,5,5,8,8,8,0,0
```
##### reverse
```cpp
std::vector<int> myvector;
for (int i=1; i<10; ++i) myvector.push_back(i);   // 1 2 3 4 5 6 7 8 9

//执行前: 1,2,3,4,5,6,7,8,9
std::reverse(myvector.begin(),myvector.end());    // 9 8 7 6 5 4 3 2 1
//执行后: 9,8,7,6,5,4,3,2,1
```
##### sort
```cpp
//升序
bool myfunction (int i,int j) { return (i<j); }

//升序
struct myclass {
  bool operator() (int i,int j) { return (i<j);}
} myobject;

int main () {
  int myints[] = {32,71,12,45,26,80,53,33};
  //执行前: myvector: []
  std::vector<int> myvector (myints, myints+8);             
  //执行后: myvector: 32,71,12,45,26,80,53,33
  
  //缺省的排序是升序(<)
  //执行前: 32,71,12,45,26,80,53,33
  std::sort (myvector.begin(), myvector.begin()+4);          
  //执行后: 12,32,45,71,26,80,53,33

  //执行前: 12,32,45,71,26,80,53,33 using function as comp
  std::sort (myvector.begin()+4, myvector.end(), myfunction); 
  //执行后: 12,32,45,71,26,33,53,80

  // using object as comp
  //执行后: 12,32,45,71,26,33,53,80
  std::sort (myvector.begin(), myvector.end(), myobject);   
  //执行后: 12,26,32,33,45,53,71,80
}
```
##### merge
```
将两个有序的组合sort1[], sort2[]。归并成一个新的有序组合。
```
```cpp
  int first[] = {5,10,15,20,25};
  int second[] = {50,40,30,20,10};
  std::vector<int> v(10);

  std::sort (first,first+5);
  std::sort (second,second+5);
  //执行前: first: 5,10,15,20,25
  //       second: 10,20,30,40,50
  //       v:[]
  std::merge (first,first+5,second,second+5,v.begin());
  //执行后: first: 5,10,15,20,25
  //       second: 10,20,30,40,50
  //       v:5,10,10,15,20,20,25,30,40,50
```
##### min
```cpp
  //输出: 1
  std::cout << "min(1,2)==" << std::min(1,2) << '\n'  
  //输出: 1
  std::cout << "min(2,1)==" << std::min(2,1) << '\n';
  //输出: 'a'
  std::cout << "min('a','z')==" << std::min('a','z') << '\n';
  //输出: 2.72
  std::cout << "min(3.14,2.72)==" << std::min(3.14,2.72) << '\n';
```
##### max
```cpp
  //输出: 2
  std::cout << "max(1,2)==" << std::max(1,2) << '\n'  
  //输出: 2
  std::cout << "max(2,1)==" << std::max(2,1) << '\n';
  //输出: 'z'
  std::cout << "max('a','z')==" << std::max('a','z') << '\n';
  //输出: 3.14
  std::cout << "max(3.14,2.72)==" << std::max(3.14,2.72) << '\n';
```
##### 二分查找
```
lower_bound(val), 返回容器中第一个值 >= val的元素的iterator位置
```
```
upper_bound(val): 返回容器中第一个值 > val的元素的iterator位置。
```

##### 堆排序
```
std::make_heap将[start, end)范围进行堆排序，默认使用less<int>, 即最大元素放在第一个。

std::pop_heap将front（即第一个最大元素）移动到end的前部，同时将剩下的元素重新构造成(堆排序)一个新的heap。

std::push_heap对刚插入的（尾部）元素做堆排序。

std::sort_heap将一个堆做排序,最终成为一个有序的系列，可以看到sort_heap时，必须先是一个堆（两个特性：1、最大元素在第一个 2、添加或者删除元素以对数时间），因此必须先做一次make_heap.
```
```cpp
//升序。左a右b，当a>b的时候，双方交换位置，
bool inc_cmp(int a,int b){ return a > b; }

//降序
bool des_cmp(int a, int b){ return a < b; }

int num[10]={3, 1, 2, 5, 6, 4};

int main()
{   
    //默认建立一个大根堆。
    make_heap(num, num+6);
    //小根堆: make_heap(num, num+6, inc_cmp);
}
```
```cpp
  vector<int> ivec;  
  for(int i=3;i<=7;++i)  
      ivec.push_back(i);  
  for(int i=5;i<=9;++i)  
      ivec.push_back(i);  
  for(int i=1;i<=4;++i)  
      ivec.push_back(i);  
  //执行前: 3,4,5,6,7,5,6,7,8,9,1,2,3,4 
  make_heap(ivec.begin(),ivec.end());//做最大堆排序，其实还在vector容器内  
  //执行后: 9,8,6,7,7,5,5,3,6,4,1,2,3,4 
  
  //执行前: 9,8,6,7,7,5,5,3,6,4,1,2,3,4 
  pop_heap(ivec.begin(),ivec.end());//删除最大堆，其实是把数据放到最后了！  
  //执行后: 8,7,6,7,4,5,5,3,6,4,1,2,3,9 
  
  //执行前: 8,7,6,7,4,5,5,3,6,4,1,2,3,9 
  ivec.pop_back();  
  //执行后: 8,7,6,7,4,5,5,3,6,4,1,2,3
  
  //执行前: 8,7,6,7,4,5,5,3,6,4,1,2,3
  pop_heap(ivec.begin(),ivec.end());//删除最大堆，其实是把数据放到最后了！
  //执行后: 7,7,6,6,4,5,5,3,3,4,1,2,8 

  //执行前: 7,7,6,6,4,5,5,3,3,4,1,2,8 
  ivec.pop_back();  
  //执行后: 7,7,6,6,4,5,5,3,3,4,1,2
 
  //执行前: 7,7,6,6,4,5,5,3,3,4,1,2
  ivec.push_back(15);  
  //执行后: 7,7,6,6,4,5,5,3,3,4,1,2,15 
  
  //执行前: 7,7,6,6,4,5,5,3,3,4,1,2,15 
  //放入最大堆，其实是把新加入的数据，按照堆排加入堆内  
  push_heap(ivec.begin(),ivec.end());
  //执行后: 15,7,7,6,4,6,5,3,3,4,1,2,5 

  //执行前: 15,7,7,6,4,6,5,3,3,4,1,2,5   
  sort_heap(ivec.begin(),ivec.end());//把堆排顺序，还原成一般的排序算法  
  //执行后: 1 2 3 3 4 4 5 5 6 6 7 7 15 
```

##### 归并排序























