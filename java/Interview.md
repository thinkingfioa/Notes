# Interview统计

###Collections.sort排序内部原理
```
归并排序；优化:TimSort(合并排序（merge sort）和插入排序（insertion sort）)
```
###hashMap原理，java8做的改变
```
引入了红黑树，
```
###B+,B-树
```
Ｂ＋树：所有的关键字［M/2－１，M-1]，初根节点，所有的个数大于1;且,非叶子节点只是索引,所有数据全部放到
```
###http的Get,Post请求
```
Get请求:参数位于url中，还有header这些
```
```
Post请求: 参数放于body中，其中header中有content-length指定有多长
```
###tcp的3次握手，4次挥手
```
3次握手:client --(syn M)--> server; server --(syn N, ack M+1)-->client; client  --(ack N+1)--> server;
```
```
4次挥手:client --(fin M)--> server; server --(ack M+1)--> client; server --(fin N)--> client; client --(ack N+1)-->server;
同时,client需要等候2个周期;
```
### 数据库事物特性
```
acid : 原子性,一致性,隔离性,持久性
```
### 数组和ArrayList区别
### 抽象类和接口区别
```
抽象类中有属性,方法实现,但接口没有,且属性必须是public static final
```
```
抽象类是类的抽象,接口仿佛是具有某种功能
```
### 网络的拥塞控制
```
慢开始->拥塞控制,快恢复,快重传;
```

###