# Guava学习笔记:Optional优雅的使用null
```
Java中的null指针很难处理,有时候就会导致throws NullPointerException();
```
```
使用Optional强行让程序员思考null使用场景
```
```
java 1.8提供替代方法
```

### Optional函数
##### 常用静态函数
```
1. Optional.of(T):获得一个Optional对象,内部包含一个非null的T数据,如果T=null,立刻报错
```
```
2. Optional.absent():获得一个Optional对象,内部为空值
```
```
3. Optional.fromNullable(T):T可以是null或非空(Optional.fromNullable(null) 等价于Optional.absent())
```

##### 实例方法
```
1. boolean isPresent():如果Optional包含的T实例不为null,返回true,否则返回false
```
```
2. T get():返回T实例,必须不能空,否则抛错.一般调用前都需要先判断isPresent()
```
```java
if(optional.isPresent()){
	return optional.get();
}
```
```
3. T or(T):若Optional实例中包含了传入的T的相同实例，返回Optional包含的该T实例，
否则返回输入的T实例作为默认值.通常如下使用
```
```java
Optional.fromNullable(name).or("火星人");
```

```
4. 返回Optional实例中包含的非空T实例，如果Optional中包含的是空值，返回null，
逆操作是fromNullable()
```
```
5.  Set<T> asSet()：返回一个不可修改的Set，该Set中包含Optional实例中包含的所有非空存在的T实例，且在该Set中，
每个T实例都是单态，如果Optional中没有非空存在的T实例，返回的将是一个空的不可修改的Set
```



















