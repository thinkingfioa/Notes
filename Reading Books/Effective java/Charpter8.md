#第８章：通用程序设计
[TOC]
```
本章目的：讨论Java语言的具体细节，包括下面这几个部分
```
|本章讨论的内容|
|:---:|
|局部变量的处理|
|控制结构|
|类库的用法|
|各种数据类型的用法|
|反射机制与本地方法|
|优化和命名惯例|

###第45条：将局部变量的作用域最小化
```
将局部变量的作用域最小化，可以增强代码的可读性和可维护性，降低出错。本条目和第13条本质是一样的(13)
```
#####最有力的方法
```
1. 请在第一次使用的它的地方声明。如果声明太早，则不容易读。
```
```
2. 如果还没有足够的信息对一个变量进行有意义的初始化，应该推迟这个声明，直到可以初始化为止。
```
#######例外
```
如果一个变量被一个方法初始化且这个初始化方法可能抛出异常，同时try块的外部该变量也被使用。那么这个try块前，需要声明，但try块前，并不能被"有意义地初始化"。
```

#####循环中的变量作用域
```
for循环中允许声明循环变量，它们的作用域限制在循环体中。普遍的for循环方法(46)
```
```java
// Preferred idiom for iterating over a collection
for(Element e : c){
	doSomething(e);
}
```
#######推荐使用for循环，避免使用while循环
```
1. for循环中声明的变量，作用于仅限于循环体中，而while循环的控制变量，作用域很广。当遇到"剪贴-粘贴"时，极容易出错。
```
```
2. for循环简短，增强了可读性。
```
```
3. 有一种非常棒的写法，经常使用的
```
```java
for(int i =0,n = expensiveComputation();i<n;i++){
	doSomething(i);
}
```

#####还有一种方法得到本条目目的：是方法小而集中
```
另个方法合并，那么第一个方法的局部变量会在另一个操作的代码范围内有效。一个长方法是不被推荐的
```

###第46条：for-each循环优先于传统的for循环
#####传统的for循环举例
#######第一种
```java
//No longer the preferred idiom
for(Iterator i = c.iterator();i.hasNext;){
	doSomething((Element)i.next());
}
```
#######第二种
```java
for(int i=0;i<a.length;i++){
	doSomething(a[i]);
}
```
#####推荐使用的for-each循环
```java
//The preferred idiom for iterating
for(Element e : elements){
	doSomething(e);
}
```

#####推荐理由
```
1. 传统的for循环中，无论是迭代器或索引变量的变化性有程序员控制，容易错误。而且，出错并不容易发现。
```
```
2. 利用for-each循环不会有性能损失，而且容易理解。冒号(:)可以理解为"从里面取数据"
```
#######举例说明，传统for循环容易出错
```
1. 传统for循环，出现BUG
```
```java
// have a BUGGGGGGGGGGGGGGGGGGGGGG
for(Iterator<Face> i = faces.iterator();i.hasNext();){
	for(Iterator<Face> j = faces.iterator();j.hasNext();){
    	System.out.println(i.next() + " " + j.next());
    }
}
```
Note:
```
期望输出结果是一个全排列的结果，但是实际输出结果却不是。原因在于:i.next()变化影响的。
```
```
2. 采用for-each循环代码,思路清晰，不易出错。
```
```java
for(Suit suit: suits){
	for(Rank rank: ranks){
    	deck.add(new Card(suit, rank));
    }
}
```

#####感悟
```
如果你在编写一个类型表示的是一组元素，一定要考虑实现Iterable。这样用户就可以利用for-each循环遍历你的类型，她会深深爱上你的
```
#####总结
```
for-each循环的简洁性和预防Bug方面的优势巨大，但是遗憾的是，下面三种情况无法使用for-each循环
```
```
1. 过滤---如果需要遍历集合，并删除选定的元素，就需要显式的迭代器，因为需要调用remove方法
```
```
2. 转换---如果需要遍历列表或者数组，并修改它的部分或者全部的元素值，就需要列表迭代器或者数组索引，以便修改数据
```
```
3. 平行迭代---如果需要并行地遍历多个集合，需要显式控制迭代器或者索引变量，以便可以同步迁移。
```
```
如果可以使用for-each循环，请使用for-each循环。如果是上面三种情况，请留心本条目上面所提到的陷阱。
```

###第47条：了解和使用类库
- 举例：
```
希望产生位于0和某个上界之间的随机数。很多程序员可能写出下面的代码
```

```java
private static final Random rand = new Random();

//Common but deeply flawed!
static int random(int n){
	return Math.abs(rand.nextInt()) % n;
}
```
#####这个方法有三个缺点
#######第一个缺点
```
如果n是一个比较小的2的乘方，那么经过相当短的周期后，产生的随机序列就会重复
```
#######第二个缺点
```
如果n不是2的乘方，那么平均起来，有些数会比其他的数出现的更为频繁。书本中提供了测试用例，可以参考。
```
#######第三个缺点
```
在少数情况下，它的失败是灾难的，返回一个落在指定范围之外的数。因为，加入rand.nextInt()返回Integer.MIN_VALUE，那么使用Math.abs也会返回Integer.MIN_VALUE，所以取模操作符(%)将会返回一个负数。
```

#####解决方法
```
使用类库函数:Random.nextInt(int);就可以得到希望的结果。
```

#####使用类库的好处
```
1. 使用标准库，充分利用已经提供的标准类库的专家知识，以及他人的使用经验。
```
```
2. 不必浪费工作在底层细节上，而放在框架上。
```
```
3. 由于Java版本的维护，可能有高级程序员帮你维护代码，提升性能
```
```
4. 类库代码一方面代表这主流代码，让自己编写的代码更有优势，已读，可维护。
```

#####建议程序员都要熟悉的类库
```
java.lang, java.util,java.io等
```
```
Collections Framework(集合框架)，java.util.concurrent包中并发工具(68,69)
```

#####总结
```
不要重新发明轮子。如果自己做的工作很常见，看看有没有类库已经实现了
```
```
如果自己不清楚类库有没有提供，要仔细查一查
```
```
类库的代码应该是非常稳定的，而且性能应该可以达到最优，而且，随着类库版本的更新，可能得到不断的改进。
```

###第48条:如果需要精确的答案，请避免使用float和double
```
float和double提供广泛的数值范围，但并没有提供完全精确的结果，所以float和double不应该用于需要精确的结果场合。
```

#####对精度有特别要求的场合
```
对精度有要求的场合，可以使用DigDecimal,int或long进行代替。
```
#######BigDecimal有两个缺点
```
1. 与使用基本运算相比，BigDecimal不方便
```
```
2. BigDecimal性能不好，很慢。
```

#######使用int或long取决与设计数值的大小
```
使用int或long时，需要注意数组大小，并且单位也是很重要的。
```

#####总结
```
1. 对任何需要精确答案的计算任务，请不要使用float或double
```
```
2. 如果不介意使用基本类型而带来不便，请使用BigDecimal。同时BigDecimal提供8中舍入方式，很方便。
```
```
3. 如果执行代码很注重性能，而且涉及的数值不太大，可以考虑使用int或long.如果数组范围没有超过9位的十进制数字，可以使用int；
如果不超过18位数字，可以使用long.超过18位数字，必须使用BigDecimal
```

###第49条：基本类型优先于装箱基本类型
#####Java有一个类型系统由两部分组成
```
基本类型:int,double,boolean,float等,, 和引用类型:String,List等.每个基本类型对应于引用类型:Integer,Double,Boolean.
```
```
java1.5版本后增加了自动装箱和自动拆箱.但并没有抹去基本类型和装箱基本类型之间的区别.对这两种类型进行选择很重要
```

#####基本类型和装箱基本类型之间的区别
```
1. 基本类型只有值,而装箱基本类型则具有与它们的值不同的同一性.也就是说,两个装箱基本类型可以具有相同的值和不同的同一性
```
```
2. 基本类型只有功能完备的值,而每个装箱基本类型除了对应基本类型的所有的功能值之外,还有一个非功能值:null
```
```
3. 基本类型通常比装箱基本类型更节省时间和空间.
```

#####举例说明上面三点区别的重要性
#######区别1例子:比较器例子
```
设计Integer值的比较器,compare方法第一个参数<第二个,等于第二个,大于第二个,分别返回负数,零和正数
```
```java
//Broken comparator - can you spot the flaw?
Comparator< Integer > naturalOrder = new Comparator< Integer > (){
	public int compare(Integer first, Integer second){
    	return first < second ? -1 :(first == second ? 0 : 1) ;
    }
};
```
Note:
```
这个比较器,可以通过很多测试用例.但是有一个致命的Bug:
naturalOrder.Compare(new Integer(42),new Integer(42));这个代码输出为:1,但我们期望输出应该是0
```
#######解释输出:1解释
```
表达式:first<second执行计算会导致first和second引用自动拆箱,也就是提取了基本类型值.这一步表达式计算符合预料.
接下来表达式:first == second,是比较对象引用是否在执行上具有同一性.这当然不具有同一性,所以结果是:false.
```
```
对装箱基本类型运用==操作符几乎总是错误的.
```
#######修正比较器的例子
```java
Comparator< Integer > naturalOrder = new Comparator< Integer > (){
	public int compare(Integer first,Integer second){
    	int f = first;
        int s = second;
        return f<s?-1:(f==s?0:1);
    }
}
```

#######区别2例子:混合使用基本类型和装箱基本类型举例
```
当一项操作中混合使用基本类型和装箱基本类型时,装箱基本类型就会自动拆箱
```
```java
public class Unbelievable{
	static Integer i;
    public static void main(String [] args){
    	if (i == 42){
        	System.out.println("Unbelievable");
        }
    }
}
```
Note:
```
上面代码运行会抛出NullPointerException异常.因为Integer会被自动拆箱,而且在java中所有的对象引用域一样,初始值都是null.
当对一个null对象引用进行自动拆箱,就会得到NullPointerException异常
```
#######区别3例子:考虑性能问题
```
借用第5条中的例子
```
```java
//Hideously slow program!
public static void main(String [] args){
	Long sum = 0;
    for(long i =0;i<Integer.MAX_VALUE;i++){
    	sum +=i;
    }
    System.out.println(sum);
}
```
Note:
```
不小心将局部变量sum声明成装箱基本类型Long,编译器也没有任何错误或则警告,这样变量就反复在装箱和拆箱,导致性能下降
```

#####何时使用装箱基本类型
```
1. 作为集合中的元素,键和值.不能将基本类型放在集合中,因此必须使用装箱基本类型
```
```
2. 在参数化类型中(5章),必须使用装箱基本类型作为类型参数,比如,无法将变量声明为ThreadLocal<int>类型,因此必须使用ThreadLocal<Integer>代替.
```
```
3. 进行反射的方法调用时(53),必须使用装箱基本类型
```

#####总结
```
1. 基本类型要优先于装箱基本类型.基本类型更加简单,而且快速
```
```
2. 当存在自动装箱时,要特别留心.当程序用==操作符比较两个装箱基本类型时,会进行同一性的比较,这一般不是我们想看到的结果.
```
```
3. 混合使用基本类型和装箱基本类型时,装箱基本类型就会自动拆箱.
```
```
4. 当程序反复的进行装箱和拆箱,会导致高开销和不必要的对象创建
```

###第50条:如果其他类型更合适,则尽量避免使用字符串
```
字符串在Java语言中使用频繁.很多不适合使用字符串的场合,也被使用字符串.
```
```
本条目就是讨论一些不应该使用字符串的情形
```
#####字符串不适合代替其他的值类型
```
当有一段数据从文件,网络,或者键盘设备,进入程序后,通常是以字符串的形式存在的.很多人倾向于继续保留这种形式,但只有当这段数据本质上
确实是文本信息时,这种想法才是合理的.否则就应该转换成适当的类型,数值类型转换成int,float,BigInteger类型等.
```
#####字符串不适合代替枚举类型
```
枚举类型比字符串更适合用来表示枚举类型的常量(30)
```
#####字符串不适合代替聚集类型
```
如果一个实体有多个组件,用一个字符串来表示这个实体通常很不恰当
```
```java
//Inappropriate use of string as aggregate type
String compoundKey = className +"#"+i.next();
```
Note:这种方法很过缺点
```
1. 加入分割符也出现在某个域中,结果将是混乱的
```
```
2. 如果想单独访问域,必须解析这个字符串,过程慢而且繁琐.
```
```
更好的做法是:简单的编写一个类来描述这个数据集,通常是一个私有的静态成员类(22)
```
#####字符串不适合代替能力表
```
有时候,字符串被用于对某种功能进行授权访问
```
- 举例:
```
考虑设计一个线程局部变量的机制,这个机制提供的变量在每个线程中都有自己的值.
```

#######第一种设计方法
```
利用客户提供的字符串键,对每个线程局部变量的内容进行访问授权
```
```java
//Broken - inappropriate use of string as capability!
public class ThreadLocal{
	private ThreadLocal(){}//Noninstantiable
    //Set the current thread's value for the named variable
    public static void set(String key,Object value);
    //Return the current thread's value for the named variable
    public static Object get(String key);
}
```
Note:
```
这个方法一个问题在于:字符串键代表了一个共享的全局命名空间.要使这种方法可行,客户端提供的字符串键必须是唯一的:如果两个客户端碰巧使用同一个字符串,那么会导致两个客户端都失败.
```
#######第二种设计方法
```
为了修正第一种设计方法,改成使用一个不可伪造的键来代替字符串.
```
```java
public class ThreadLocal{
	private ThreadLocal(){}//Noninstantiable
    
    public static class Key(){ }
    //Generates a unique ,unforgeable key
    public static Key getKey(){
    	return new Key();
    }
    public static void set(Key key,Object value);
    public static Object get(Key key);
}
```
#######第三种设计方法
```
实际在,可以在第二种设计方法中,取消静态方法,将ThreadLocal变成线程局部变量.
```
```java
public final class ThreadLocal{
	public ThreadLocal(){}
    public void set(Object value);
    public Object get();
}
```
#######第四种设计方法
```
第三种设计方法的API并不是类型安全的,因为当你从线程局部变量得到它时,必须将值从Object转换成它实际的值.
采用将ThreadLocal类泛型化(26),使这个API变成类型安全的就容易多了
```
```java
public final class ThreadLocal< T > {
	public ThreadLocal(){}
    public void set(T valude);
    public T get();
}
```
Note:
```
上面的代码与前面的两个基于键的API相比,更加快速,更优雅.
```
#####总结
```
1. 如果可以使用更加合适的数据类型,或者编写更加适当的数据类型,就应该避免使用字符串来表示对象.
```
```
2. 经常被错误地用字符串来代替的类型包括基本类型,枚举类型和聚集类型
```

###第51条:当心字符串连接的性能
```
想要产生单独一行的输出,或者构造一个字符串来表示较小的,大小固定的对象,使用连接操作符"+"是非常合适的.
但是,连接操作符"+"不是适合运用到大规模的场景中.为了连接n个字符串而重复地使用字符串连接符,需要n的平方级的时间.
```
```
字符串都是不可变(15)的,两个串连接在一起,内容都是被拷贝的
```
- 举例:
```java
//Inappropriate use of string concatenation - Performs horribly
public String statement(){
	String result = "";
    for(int i=0;i<numItems();i++){
    	result +=lineForItem(i);
    }
    return result;
}
```
Note:
```
上面的代码,可能产生巨大的性能问题.第15条中,应该使用StringBuilder代替String.(StringBuffer类已经过时了,不要使用)
```
#######修改后的版本代码
```java
public String statement(){
	StringBuilder b = new StringBuilder(numItem() * LINE_WIDTH);
    for(int i=0;i<numItems();i++){
    	b.append(lineForItem(i));
    }
    return b.toString();
}
```
Note:
```
第二种方法比第一种方法的执行速度快80倍.因为第一种执行方法的时间是平方级增加,第二种做法线性增加.
```

#####总结
```
不要使用字符串连接操作符来合并多个字符串,除非性能无关紧要.如果遇到多个字符串,请使用StringBuilder的append方法.
```

###第52条:通过接口引用对象