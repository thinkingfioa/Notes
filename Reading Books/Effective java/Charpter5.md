#第5章：泛型
[TOC]
```
泛型可以告诉编译器每个集合中接受哪些对象类型，编译器自动为你的插入进行转化。没有泛型之前，从集合中读取到的每个对象都需要手动强转。
```
```
本章目的：最大的限度的使用泛型的优势，使整个过程尽可能地简单化。
```
###术语
|术语|示例|所在条目|
|:---:|:---:|:---:|
|参数化的类型|List< String >|23|
|实际类型参数|String|23|
|泛型|List< E >|23,26|
|形式化类型参数|E|23|
|无限制通配符类型|List< ? >|23|
|原生态类型|List|23|
|有限制类型参数|< E extends Number>|26|
|递归类型限制|< T extends Comparable< T > >|27|
|有限制通配符类型|List< ? extends Number >|28|
|泛型方法|static < E > List< E > asList(E() a)|27|
|类型令牌|String.class|29|

###第23条：请不要在新代码中使用原生态类型
```
声明中具有一个或者多个类型参数的类或者接口，就是泛型类或接口。eg:List<E>
```
```
每个泛型都定义一个原生态类型(eg:List),Java的设计者允许使用它们，完全为了提供兼容性。
```
#####原生态类型的危害
```
出错并不能立即发现，直到运行代码到具体对象是才会抛出异常。程序员应该要尽量让所有的错误在编译时就发现
```
- 举例
 ```java
  //Now a raw collection type  -- don't do this
  private final Collection stamps = ...;
  // i can add other class instance to it ,there are not warning or default
  stamps.add(new Coin(...));
 ```
Note:可以将对象实例new Coin()放入到stamps集合中，编译和运行都不会出现任何问题，直到从stamp集合中取coin时才会抛出:Throws ClassCastException异常。

#####使用泛型优势
```
1. 如上例所示，使用泛型，将会在编译时，就能定位代码错误。
```
```
2. 保证类型安全。从集合中删除元素时，不再需要进行手工强转。而原生态类型需要手动强转Class类型
```
- 举例:
```java
//for loop with parameterized iterator declaration - typesafe
for(Iterator<Stram> i = stamps.iteerator();i.hasNext();){
	Stamp s = i.next(); // 无需转换
    ...//Do something with the stamp
}
```

#####原生态类型List和参数化的类型List< Object >比较
```
1. 前者逃避了泛型检查，后者则明确告知编译器，能够持有任意类型的对象。比如:你能将 List<String>传递给类型List的参数，但是不能传给类型为List<Object>的参数。
```
```
2. 泛型有子类型化的规则，List<String>是原生态类型List的一个子类型，而不是参数化类型List<Object>的子类型(25).因此，使用原生态类型，会失掉类型安全性，但是List<Object>则不会。
```
- 举例:














