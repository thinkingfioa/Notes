# 第二章:创建和销毁对象
[TOC]
## 4. 通过私有构造器强化不可实例化的能力(只提供静态方法的类使用)
1. 如果一个类,不想被实例化,通过将类写成**Abstract类**行不通,因为Abstract 类可以被继承,其子类也可以实例化
2. 最优方法:
```java
// Suppress default constructor for noninstantiablility
private ClassName(){
	throw new AssertionError();
}
```
 - 优: 该类确保不会被实例化,即使类的内部调用都不行 
 - 缺: 该类不能被子类化,也就是继承不行

####结论: 
1. 类不可实例化时，将构造函数写成私有的

## 5. 避免创建不必要的对象(优先考虑重用对象,而不是创建功能相同的新对象)
1. 同时提供**静态工厂方法**和**构造器的不可变类**,优先使用静态工厂得到对象.
> eg:静态工厂方法`Boolean.valueOf(String)` **好于** `new Boolean(String)`
2. 重用已经被修改的可变对象
>案例分析: 类Person,提供方法:isBabyBoomer(),验证是否位于1946-1964间出生的孩子
```java
public class Person{
	private final Date birthData;
    public boolean isBabyBoomer(){
    	// DON'T DO THIS
    	Calendar gmtCal = Calendar.getInstance(TimeZone.getTimeZone("GMT));
        gmtCal.set(1946,Calendar.JANUARY,1,0,0,0);
        Date boomStart = gmtCal.getTime();
        gmtCal.set(1964,Calendar.JANUARY,1,0,0,0);
        Date boomEnd = gmtCal.getTime();
        return birthData.compareTo(boolmStart) >= 0 &&
        		birthData.compareTo(boolmEnd) < 0;
    }
}
```
>**每次调用方法** `isBabyBoomer()`, 产生**4个实例**:gmtCal,TimeZone,boomStart,boomEnd.多次调用方法,会比较消耗性能
```java
class Person{
	private final Date birthDat;
    private static final Date BOOM_START;
    private static final Date BOOM_END;
    static{
    	Calendar gmtCal = Calendar.getInstance(TimeZone.getTimeZone("GMT));
        gmtCal.set(1946,Calendar.JANUARY,1,0,0,0);
        BOOM_START = gmtCal.getTime();
        gmtCal.set(1964,Calendar.JANUARY,1,0,0,0);
        BOOM_END = gmtCal.getTime();
    }
    public boolean isBabyBoomer(){
     return birthData.compareTo(BOOM_START) >= 0 &&
        		birthData.compareTo(BOOM_END) < 0;
    }
}
```
>一个JVM每加载一次,只有**一份BOOM_START,BOOMEND,gmtCal,TimeZone**.**但是**,如果该Person的方法一次都没有调用,则就**划不来**,因此,自然想到了:**延迟初始化**。
3. 优先使用**基本类型**而不是**自动装箱基本类型**，要当心无意识的自动装箱(long , Long)

####结论:
1. 小对象创建廉价
2. 重量级的对象注意服用
3. 对比**39条规则**

##6. 消除过期的对象引用
1. 自己写代码，造成内存泄露
 - 案例分析：自己写一个** `Stack`集合**，考虑：栈显示增长，然后收缩，那么从栈中弹出的元素**会不会被回收**？答案是：不会。因为栈中还维持其过期引用(obsolete reference)
 - 解决办法：手动清空，手动清空的另一个好处：当程序错误的想引用已经出栈的元素，会出现`NullPointerException`异常。
 - Note：只要类是自己的管理内存，程序员就应该警惕内存泄露问题，一旦元素被释放掉，其引用要清空。
2. 缓存造成内存泄露
 - WeakHashMap的使用，也就是弱引用。
3. 监听器和其他的回调造成内存泄露
 - 解释1：实现一个API，客户在这个API中注册回调，却没有显示取消注册，那么就会积聚
 - 解释2：回调立即被当做垃圾回收的最佳方法就是保存弱引用(weak reference)

##7.避免使用终结方法:Finalize方法,从Object类中继承而来。在从堆中永久删除对象之前，垃圾回收器调用该对象的Finalize方法，但何时调用，无法确定。
1. 取代Finalize方法
>1. Note:Finalize方法,不可预测,极其危险,一般情况下不要使用.
>2. 如果类对象封装的资源,确实需要终止,常用的方法是:提供一个显示的终止方法.典型的例子:InputStream,OutputStream,java.sql.Connection上的close方法.
>3. 显示的终止方法通常要与try-finally结构结合起来使用.也就是说,在finally子句中调用显式的终止方法.
```java
//try-finally block guarantees execution of termination method
Foo foo = new Foo(...);
try{
	//Do what must bu done with foo
} finally{
	foo.Close();
    foo.removeResources();//Explicit termination method
}
```
>4. 当子类复写了终结方法,可以将子类的终结方法放入try{...}中,finally{...}则再执行父类的终结方法
2. 终结方法的好处
 1. 充当安全网:当客户端无法调用显式的终止方法.但要考虑额外的代价(FileInputStream,FileOutputStrea,Timer,Connection)
 2. 本地对等体相关的(没有懂)

