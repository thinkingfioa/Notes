#第4章:类和接口
[TOC]
```
本章目的:介绍设计出有用,健壮,灵活的类和接口的准则.
```

###第13条:使类和成员的可访问性最小化(封装类内部数据和其实现细节)

#####将类或接口写成包级私有的原因
 - 表示在以后的发行版本中,可以对它进行修改,替换,或者删除.无需担心影响到现有的客户程序
 - 如果做成公有的,则就有责任永远支持它,保持兼容性
举例:如果一个包级私有的顶层类(接口),只在一个类的内部用到,请考虑将这个顶层类变成使用的类的私有嵌套类(22条)

#####成员(域,方法,嵌套类和嵌套接口)有四种可能访问级别,依次递增顺序:
1. **private** : 只有声明该成员的顶层类才能访问
2. **default** : 声明该成员的内部任何类都可以访问
3. **protected** : 声明该成员的内部任何类都可以访问 + 该类的子类也可以访问
4. **public** : 任何地方都可以访问

#####写类的变量+方法时提醒
1. 如果一个类实现了一个接口，那么接口的方法必须都被声明为public,因为接口中的所有方法都被默认为公有访问级别
2. 使用**protected**,表示已经导出API的一部分，以后版本中，要注意维护。
3. 为了测试，最多将级别调至为**default**
4. 实例域+静态域决不能是公有的(14条),写成**public**,则表示放弃对这个值进行限制的权利.
5. 长度为非零的数组,总是可变的.客户端总是可以进行修改数组的内容
6. 除公有静态final域的特殊情况,公有类都不应该包含公有域.并且要确保公有的静态final域所引用的对象都不是可变的

```java
//客户端可以对方法的返回值,进行修改
// Protential security hole!
public static final Thing[] VALUE ={ ... };
```
Remark:应该使用下面的方法
```java
//改成是不可修改,或是一个新的备份
private static final Thing[] PRIVATE_VALUE ={ ... };
public static final List<Thing> VALUES = Collections.unmodifiableList(Array.asList(PRIVATE_VALUES));

private static final Thing[] PRIVATE_VALUE ={ ... };
public static final Thing[] values(){
	return PRIVATE_VALUES.clone();//使用的时候请慎重,参考第三章的clone方法部分
}
```

### 第14条:在公有类中使用访问方法,而非公有域
#####条款：
```
如果类可以在它所在的包的外部进行访问，就应该提供访问方法。共有类不应该直接暴露数据域，否则就是放弃该域的控制权。
```
#####忠告：
```
1. 所有的公有的数据域，都应该用包含私有域和公有的访问方法来代替。
2. 如果一个类是包级私有，或则是私有的嵌套类，直接暴露它的数据域没有本质的错误。因为客户端代码如果要使用数据域，也必须限定在包含该类的包中。
3. 如果一个类直接暴露其不可变的数据域，危害就比较小。
```

###第15条:使可变性较小化
#####不可变类
```
1. 不可变类：实例一旦创建，在对象的整个生命周期内固定不变。实例中包含的所有的信息必须在创建该实例的时候就提供。
```
```
2. 五条规则

	<1> 不要提供任何会修改对象状态的方法
    <2> 保证类不会被扩展。一般做法是使这个类成为final类，或提供静态工厂+私有构造方法
    <3> 使所有的域都是final的
    <4> 是所有的域都成为私有的。防止客户端获得访问被域引用的可变对象的权限，修改域引用的对象(反射)
    <5> 确保对于任何可变组件的互斥访问。如果这个类具有指向可变对象的域，必须确保客户端无法获得指向这些对象的引用
```

- 举例

```java
package vlis;

public final class Complex {
    private final double re;
    private final double im;
    public Complex(double re, double im){
        this.re = re;
        this.im = im;
    }
    public double realPart(){
        return re;
    }
    public double imaginaryPart(){
        return im;
    }
    public Complex add(Complex c){
        return new Complex(re+c.re , im + c.im); // this is important
    }
    public Complex subtract(Complex c){
        return new Complex(re - c.re,im - c.im);
    }
    public Complex multiply(Complex c){
        return new Complex(re * c.re - im*c.im,
            re *c.im + im*c.re);
    }
    @Override public boolean equals(Object o){
        if(o == this){
            return true;
        }
        if(!(o instanceof Complex)){
            return false;
        }
        Complex c = (Complex) o;
        // please use compare instead of ==
        return Double.compare(re, c.re) == 0 &&
            Double.compare(im,c.im) ==0;
    }
    @Override public int hashCode(){
        int rusult = 17+(int)re;
        return 31*rusult+(int)im;
    }
    @Override public String toString(){
        return "("+re+" + " +im+"i)";
    }
}
```
Note:
1. Functional做法：类Complex提供的算数运算，运算后的一律是返回新的Complex实例，而不是修改这个实例。这种Functional做法在不可变类中都用到了。

#####不可变类的优点
#######不可变对象简单
```
1. 不可变对象在创建时就具有整个生命周期的完整状态，程序员无需做额外的工作维护约束关系
```
```
2. 不可变对象可以被自由的共享，本质上是线程安全的，不要求同步。甚至，也可以共享它们的内部信息。
	Note：BigInteger类内部使用：符号数值+int数组，共同表示。这个如果是产生某个BigInteger的负数，则可以将符号取反，int数组共享，无需拷贝数组。
```
```
3.  不可变类可以提供一些静态工厂(第1条)，把频繁被请求的实例缓存起来。让客户端共享现有的实例，且线程安全。
```
- 举例

```java
//频繁被请求的不可变的对象，使用静态工厂提供
private static final Complex ZERO = new Complex(0,0);
private static final Complex ONE = new Complex(1,0);
private static final Complex I = new Complex(0,1);
public static Complex valueOfZero(){
	return Zero;
}
public static Complex valueOfOne(){
	return One;
}
public static Complex valueOfI(){
	return I;
}
```
```
4. 不可变对象不需要进行保护性拷贝(第39条),因为拷贝后的始终等于原始对象。因此，不需要为不可变的类提供clone方法或者拷贝构造器(11).
```
#####不可变类的唯一缺点
```
对于每一个不同的值，都需要一个单独的对象，对于大型的对象的情景，创建的代价巨大。
```
- 举例(BigInteger)
```java
BigInteger b1 = new BigInteger(...);
BigInteger b2 = new BigInteger(...);
b2 = b1+b2;
b2 = b2*b1;//
```
Note: 这短短的4句java代码，创建了四个不可变的巨型对象，其实很多都是中间生成过渡变量。除了最后结果，其他的对象都被丢弃。

#######解决办法
```
1. 提供经常用到的哪些多步操作，比如“模指数"这样的多步操作。多步操作中使用可变"配套类(包级私有可变)"作为基本类型提供，而无需每个步骤单独创建一个对象。
```
```
2. 如法预测，则最好的方式是提供一个公有的可变配套类。比如:String类的公有配套类StringBuilder。
```
#######私有构造方法+公有静态工厂
```
   不可变类，不允许被子类化，除了使用关键字:final，另一个比较灵活的方法是：私有构造方法(包级也可以)+公有静态工厂来代替公有构造器。
```
- 举例：
```java
public class Complex{
	private final double re;
    private final double im;
    
    private Complex(double re,double im){
    	this.re = re;
        this.im = im;
    }
    public satic Complex valueOf(double re,double im){
    	return new Complex(re,im);
    }
    ...//Remainder unchanged
}
```

Note:
1. 这种方法灵活，它允许使用多个包级私有的实现类，也就是可以被继承。
2. 提供改善静态工厂的对象缓存能力，且具有静态工厂的诸多优势(1)

#####不可变类实际中规则
```
1. 没有一个方法能够对对象的状态产生外部可见的改变。所以，不可变类允许拥有一个或者多个非final的域
2. 不可变类中，一个非常有效的方法：请缓存某些开销昂贵的计算结果，节省计算开销。
```

#####不可变类的序列化问题
```
    如果一个不可变类实现Serializable接口，同时包含一个或者多个指向可变对象的域，为了防止攻击者可能从不可变的类创建可变的的实例。不可变类必须提供一个显示的readObject或者readResolve方法，或者使用ObjectOutputstream.writeUnshared和ObjectInputStream.readUnshared方法(76)
```
#####忠告:
```
1. 不要为每一个get方法编写一个相应的set方法，除非有好的理由将类成为可变的类。
2. 尽量使用小的值对象，应为java平台库已将其写成不可变类。
3. 当遇到较大的值对象为不可变时，请提供可变的配套类
4. 有些类写成不可变类是不切实际的，但仍要尽可能的限制它的可变性。
```

###第16条:复合优先于继承(类继承类)
```
提示:”继承“一词指的是实现继承(类继承类)，不包括接口继承(类实现接口+接口继承接口)。
```
#####继承打破封装性
```
子类依赖于超类中特定功能的实现细节，所以跨包继承可能由于发行版本中父类不同，导致子类遭到破坏。
```
- 举例 1.
Note:需要一个类可以记录HashSet类共添加了多少个元素。
```java
// Broken
public class InstrumentedHashSet<E> extends HashSet<E> {
    private int addCount = 0;
    public InstrumentedHashSet(){
    }public InstrumentedHashSet(int initCap,float loadFactor){
        super(initCap,loadFactor);
    }
    @Override public boolean add(E e){
        addCount ++;
        return super.add(e);
    }
    @Override public boolean addAll(Collection<?  extends E> c ){
        addCount+=c.size();
        return super.addAll(c);
    }
    public int getAddCount(){
        return addCount;
    }
}
public class Client {
    public static void main(String args[]) throws Exception{
       InstrumentedHashSet<String > s = 
           new InstrumentedHashSet<String>();
       s.addAll(Arrays.asList("pan","ping","ping"));
       System.out.println("thinking_fioa : " + s.getAddCount());//输出结果是:6
    }
}
```

Note:
```
1. 输出结果是6，因为其实HashSet内部的addAll()方法是基于add()方法实现的。所以重复计数了
```
```
2. 如果采用“修正”这个子类的addAll()方法，不能从根本解决问题。不能保证以后的发行版本的具体实现情况。
```
```
3. 完全覆写addAll()方法，不依赖HashSet的addAll()方法，这样做并不是总是可行的，因为可能无妨对于子类来说的私有域。
```
- 举例 2.
```
    假设一个程序的安全性依赖于这样一个事实：所有被插入某个集合中的元素都满足某个先决条件。那么采用方法：对集合进行子类化，并覆盖所有能够添加元素的方法，以保证进入集合的元素满足先决条件。如果在后续发行版本中，超类没有增加插入元素的新方法，则采用的做法可以正常工作。一旦超类增加了新的添加元素方法，则采用的做法将存下安全漏洞。
```

#####避免安全漏洞的方法
```
1. 复合：不用扩展现有的类，而是在新的类中添加一个私有域，它引用类的一个实例。
2. 转发:新类中的每个实例方法可以调用包含的现有类实例中对应的方法，并返回结果
```
- 复合/转发代替InstrumentedHashSet类

```java
public class ForwardingSet<E> implements Set<E> {
    // Reusable forwarding class
    private final Set<E> s;
    public ForwardingSet(Set<E> s) {
        this.s = s;
    }
    public int size() {
        return this.s.size();
    }
    public boolean isEmpty() {
        return this.s.isEmpty();
    }
    public boolean contains(Object o) {
        return this.s.contains(o);
    }
    public Iterator<E> iterator() {
        return this.s.iterator();
    }
    public Object[] toArray() {
        return this.s.toArray();
    }
    public <T> T[] toArray(T[] a) {
        return this.s.toArray(a);
    }
    public boolean add(E e){
        return this.s.add(e);
    }
    public boolean remove(Object o){
        return this.s.remove(o);
    }
    public boolean containsAll(Collection<?> c){
        return this.s.containsAll(c);
    }
    public boolean addAll(Collection<? extends E>c){
        return this.s.addAll(c);
    }
    public boolean retainAll(Collection<?> c){
        return this.s.retainAll(c);
    }
    public boolean removeAll(Collection<?> c){
        return this.removeAll(c);
    }
    @Override public boolean equals(Object o){
        return this.s.equals(o);
    }
    @Override public int hashCode(){
        return this.s.hashCode();
    }
    @Override public String toString(){
        return this.s.toString();
    }
    @Override
    public void clear() {
        this.s.clear();
    }
}
```
```java
public class InstrumentedSet<E> extends ForwardingSet<E> {
    //Wrapper class
    private int addCount = 0;
    public InstrumentedSet(Set<E> s){
        super(s);
    }
    @Override public boolean add(E e){
        addCount++;
        return super.add(e);
    }
    @Override public boolean addAll(Collection<? extends E> c){
        addCount +=c.size();
        return super.addAll(c);
    }
    public int getAddCount(){
        return this.addCount;
    }
}
```
Note:
1. InstrumentedSet类被成为包装类(Wrapper class),技术来源于设计模式:Decorator模式。每一个InstrumentedSet实例都把另一个Set实例包装起来。
2. Set接口的存在至关重要。这种设计格外的灵活，几乎没有缺点。这里的包装类InstrumentedSet可以包装任何Set实现类。
3. 特别注意一点的是:Decorator模式中的包装类不适合用在回调框架中。因为被包装起来的对象并不知道它外面的包装对象，所以它会传递一个指向自身的引用(this)

#####如何选择复合 Or 继承
```
1. 只有当子类真正是超类的子类型(subtype)时，才适合继承。也就是说两个类A和B，确实存在"is-a"关系。否则，全部选择复合。
```
```
2. 在决定使用继承而不是复合之前，请问自己几个问题:你正在试图扩展的类，它的API中有没有缺陷？如果有，是否愿意将超类的API缺陷传播到子类中。继承会将父类的所有缺陷传播到子类中，而复合则允许设计新的API来隐藏这些缺陷。
```

###第17条:要么为继承而设计，并提供文档说明，要么就禁止继承
#####专门为继承而设计的类
```
专门为继承而设计的类应该具有良好类说明文档。该类必须有文档说明它可覆盖的方法的自用性(self-use)
```
#####如何设计允许继承的类
#######构造器注意点
```
1. 构造器决不能调用被覆盖的方法，无论是直接调用还是间接调用。
Note:如果父类的构造器使用了可覆盖的方法，那么子类如果覆写这个方法，则覆写的方法会在子类构造器完成前先被调用。后果很严重......
```
#######处理Cloneable和Serializable接口问题
```
问题：无论实现Cloneable和Serializable哪个接口都不是好主意，实现子类的程序员需要承担一些责任。不过也有手段处理(11,74).
Note: 继承实现了Cloneable或Serializable接口的父类，需要提醒的是：clone和readObject方法在行为上类似于构造器。所以，无论是clone该是readObject，都不可以调用可覆盖的方法，无论是直接还是间接。
```
#######处理实现Serializable类且该类有一个readResolve或writeReplace方法。
```
父类中的readResolve或writeReplace方法应改成受保护的方法，而不是私有的方法。因为子类需要覆写或继承使用，否则整个逻辑就可能有问题
```
- 基础知识补充
 - writeReplace()
```
Note: writeReplace()方法可以使对象被写入流以前，用一个对象来替换自己。writeReplace()方法在ObjectOutputStream准备将对象写入流以前调用，ObjectOutputStream会先检查序列化的类是否定义了writeReplace()方法，如果定义了这个方法，则会通过调用它，用另一个对象替换它，写入流中。注意返回对象要与原对象类型兼容。
```
 - readResolve()
```
Note：readResolve方法可以使对象从流中读出后，用另一个实例对象来代替。readResolve()方法在ObjectInputStream会检查反序列化的对象是否定义了这个方法，如果定义了，则会指定返回的对象。注意对象类型兼容问题。
```
 - 序列化的类的顺序.
```
a. writeReplace();
b. writeObject();
c. readObject();
d. readResolve();
```
- 举例:readResolve()方法经常用于单例中。
```java
public final class MySingleton implements Serializable{

    private static final long serialVersionUID = -8476498064100630042L;
    private MySingleton(){}
    private static final MySingleton instance = new MySingleton();
    public static MySingleton getInstance(){
        return instance;
    }
    public Object readResolve() throws  ObjectStreamException{ // 保证传输或输入文件过程中也要是单例
        return instance;
    }
}
```

#####处理普通类(不是final类，也不是设计继承类)
```
问题：每次都这个类修改，都会影响到这个类的扩展的客户类
```
#######禁止子类化
```
采用(15)中描述的禁止子类化的方法
1. 将类写成final
2. 将所有的构造器改为private,或default,再添加一些公有的静态工厂
```
#######类实现了某个能反应其本质的接口(Set,List,Map)
```
请坚决将类写成非子类化类，因为想使用者采用(16)中介绍的装饰器设计模式，不要采用继承子类化方式。
```
#######类没有实现标准的接口
```
问题：如果具体的类没有实现标准的接口，那么禁止继承可能会给有些程序员带来不便。
```
```
要求：如果你认为允许该类子类化，保证完全消除这个类中可覆盖方法的自用特性。也就是说：确保这个类永远不会调用它的任何可覆盖的方法。

方法：用“直接调用可覆盖方法的私有辅助方法”来代替“可覆盖方法的每一个自用调用”。也就是将每一个可覆盖方法的代码体移到一个私有的“辅助方法”中。
```

###第18条：接口优于抽象类
#####接口和抽象类
#######区别
```
1. 抽象类允许包含某些方法的实现，但接口不允许
```
```
2. 实现抽象类定义的类型，类必须成为抽象类的一个子类。但是只要类定义了所有必要的方法，并且遵守通用的约定，就被允许实现一个接口。
```
#######接口的优点
```
1. 现有的类可以很容易被更新，以实现新的接口

Note：一般来说，扩展一个现有类，如果实现Comparable接口，只需要增加必要的方法和一个implements子句。如果是实现抽象类，则要将抽象类放到类型层次的高处，所有的现有类变成子类，迫使所有的子类都必须扩展这个新的抽象类。间接伤害到类层次
```
```
2. 接口是定义mixin(混合类型)的理想选择

Mixin类型：类除了实现自己的“基本类型”之外，还可以实现这个mixin类型，表明提供某些可供选择的行为。比如Comparable就是一个mixin接口

Note：这样的接口(eg:Comparable接口)之所以被成为mixin，是因为它允许任选的功能可能被混合到类型的主要功能中。如果换成是类用于定义mixin，则可能面临单继承的约束。
```
```
3. 接口允许我们构造非层次结构的类型框架

Note:接口可以提供非常良好的灵活性
```
```
4. Decorator模式(16)中，接口使得安全地增强类的功能成为可能。
```
#####如何更好使用接口
Note：由于接口不允许包含方法的实现，所以采用 **接口+抽象类** 组合使用，将二者优点结合起来。
```
接口的作用仍然是定义类型,但是抽象类接管了所有与接口实现相关的工作
```
#######优点(接口+抽象类)
```
1. 允许现有类自由选择自己实现接口还是继承抽象类
2. 如果现有类已经有一个父类,则可以手工实现接口.更方便的做法是:定义内部私有类扩展抽象类,将接口方法的调用转发内部私有类的实例
```

-  举例:
```java
// Interface + AbstractInterface
    static List< Integer > intArrayAsList(final int[] a){
        if (a == null){
            throw new NullPointerException();
        }
        return new AbstractList<Integer>(){
            public Integer get(int i){
                return a[i];
            }
            @Override
            public Integer set(int i,Integer val){
                int oldVal = a[i];
                a[i]=val;  // Auto-unboxing
                return oldVal; //Autoboxing
            }
            public int size(){
                return a.length;
            }
        };
    }
```

```
Note:
1. 例子充分说明了:接口+抽象类的巨大作用,极大方便用户使用与扩展
2. 新扩展的类是一个匿名类,不可被访问
3. 例子中存在int值和Integer实例之间来回的转换,可能存在性能问题
```
#####如何编写抽象类
```
首先需要仔细研究接口,确定最为基本方法,为接口的非基本方法提供具体实,也可根据使用最为基本方法.将基本方法定位抽象方法,留给子类实现.
```
- 举例:
```java
public abstract class AbstractMapEntry <K,V> implements Map.Entry<K,V>{
    
    public abstract K getKey();
    public abstract V getValue();
    
    public V setValue(V value){
        throw new UnsupportedOperationException();
    }
    @Override
    public boolean equals(Object o){
        if(o == this){
            return true;
        }
        if(!(o instanceof Map.Entry)){
            return false;
        }
        Map.Entry<K, V> arg = (Map.Entry) o;
        return equals(getKey(),arg.getKey()) &&
            equals(getValue(),arg.getValue());
    }
    private static boolean equals(Object o1, Object o2){
        return o1 == null? o2 == null:o1.equals(o2); // beautiful still ,blank still
    }
    @Override
    public int hashCode(){
        return hashCode(getKey()) ^ hashCode(getValue()); // exclusive or
    }
    private static int hashCode(Object obj){
        return obj == null?0:obj.hashCode();
    }
}
```

#######简单实现(simple implementation)
```
简单实现实现了整个接口,可以被继承,也可以直接使用,eg:AbstractMap.SimpleEntry就是一个简单实现
```
#####提醒
```
1. 抽象类较接口优势:
Note: 抽象类的演变比接口的演变要容易的多.在后续的版本中,为抽象类增加一个具体方法比较容易,但是接口是则需要修改所有的实现类.
```
```
2. 接口+抽象类的方式可以减小为接口添加一个方法的代价,但是,对于那些不从抽象类继承接口的类仍然要被破坏.
```
#####总结
```
1. 设计公有的接口,一定要非常谨慎,接口一旦被公开发行,并且被广泛使用,想改变接口几乎不可能.
```
```
2. 当演变的容易性比灵活性和功能更为重要的时候,应该使用抽象类定义类型.也可以采取使用接口+抽象类的方式.
```

###第19条:接口只用于定义类型
#####实现接口,唯一目的
```
类实现接口时,接口就充当可以引用这个类的实例的类型,去子类化.其他任何目的而定义接口都是不恰当的.
```
#####常量接口(java.io.ObjectStreamConstants)的探讨
```
常量接口没有包含任何方法,只包含静态的final域,每个域都导出一个常量,并符合上面的目的.
```
#######常量接口出现原因
```
使用这些常量的类实现这个接口,以避免用类名来修饰常量名.
```
#######常量接口模式是对接口的不良使用
```
1. 类的内部使用某些常量,纯粹是实现细节.实现常量接口,会导致这样的实现细节泄露.
```
```
2. 代表一种承诺:在将来的发行版本中,这个类被修改了,它不再需要使用这个常量,也依然必须实现这个接口,以确保二进制兼容.
```
```
Note: 二进制兼容是:保证类一样,以兼容之前的版本.
```
```
3. 如果是非final类实现常量接口,则所有的子类的命名空间也会被接口中的常量所"污染"
```
#######替代常量接口的选择方法
```
1. 如果常量与现有的类或接口紧密相关,就将常量添加到类或接口中
```
```
2. 如果这些常量最好被看作是枚举类型的成员,就应该使用枚举类型(30)导出常量
```
```
3. 使用不可实例化的工具类
Note:如果需要大量利用工具类导出的常量,可以考虑使用静态导入(static import)机制,避免使用类名修饰常量名
```
- 举例
```java
//Constant utility class
public class PhysicalConstants {

    private PhysicalConstants(){ }
    public static final double MAX_VALUE=1;
    public static final double MIN_VALUE = 0;
}
```

###第20条: 类层次优先于标签类
#####标签类
```
用标签域(tag)来表示多种风格的实例的类
```
- 举例

```java
package vlis;

public class Figure {
    //Tagged class
    enum Shape {RECTANGLE,CIRCLE };
    private final Shape shape;
    //RECTANGLE
    private double length;
    private double width;
    //CIRCLE
    private double radius;

    Figure(double radius){
        this.radius = radius;
        this.shape = Shape.CIRCLE;
    }
    Figure(double length, double width){
        this.shape =Shape.RECTANGLE;
        this.length = length;
        this.width = width;
    }
    public double area(){
        switch(shape){
            case RECTANGLE: return length*width;
            case CIRCLE: return Math.PI * (radius)*(radius);
            default: throw new AssertionError();
        }
    }
}
```
#######标签类的缺点:冗长,容易出错,效率低下
```
1. 类中充斥着样本代码,包括枚举声明,标签域以及条件语句.破坏了可读性.
```
```
2. 实例承担着其他风格的不相关的域.域不能被做成final的,除非构造器初始化所有不相关的域
```
```
3. 构造器必须不借助编译器,来设置标签域,独立初始化正确的数据域
```
```
4. 如果要添加风格,必须修改源文件,同时必须记得给每个条件语句都添加一个条件.
```
#####子类型化(取代标签类)
#######构建子类型原则
```
1. 定义一个抽象类,将标签类中依赖于标签值的方法提取到抽象类中,定义为抽象方法.
```
```
2. 如果还有其他方法不依赖于标签的值,直接定义实现在抽象类中.
```
```
3. 所有都用到的某些数据域,放到抽象类中.
```
```
4. 子类中都包含:与子类相关的数据域+抽象方法的相应实现
```
- 举例
```java
    abstract class Figure {
        abstract public double area();
    }
    class Circle extends Figure {
        private final double radius;

        Circle(double radius) {
            this.radius = radius;
        }

        public double area() {
            return Math.PI * radius * radius;
        }
    }
    class Rectangle extends Figure {
        private final double length;
        private final double width;
        Rectangle(double length, double width) {
            this.length = length;
            this.width = width;
        }
        public double area(){
            return length*width;
        }
    }
```

#######子类化优点
```
1. 代码清晰,无原来版本中的所有的样板代码
```
```
2. 每个类型的实现都配有自己的类,类不用受到不相关的数据域的拖累,所有的域都可以是final
```
```
3. 编译器会确保每一个抽象方法都必须被实现,每一个数据域都要初始化
```
```
4. 可以清晰的反应类型之间本质上的层次关系.比如:Square,能反应出正方形是特殊的矩形
```
- 举例:
```java
class Square extends Rectangle{
	Square(double side){
    	super(side,side);
    }
}
```

#####总结
```
		当想编写包含显示标签域的时候,请考虑使用子类化方法,构造一个层次结构.
```

###第21条:用函数对象表示策略
#####函数对象
```
Java没有指针,想达到C语言中的函数指针的作用,也就是常说的策略(Strategy)模式,需要传递对象引用.这样的实例被称为:函数对象.
```
- 举例
```java
class StringLengthComparator{
	public int compare(String s1,String s2){
    	return s1.length()-s2.length();
    }
}
```

#######函数对象的设计
```
1. 如果具体的策略类,没有域,则所有的实例在功能上是相互等价的.则考虑使用单例模式,节省对象创建开销.
```
```
2. 设计具体的策略类时,需要定义一个策略接口.eg:Comparator类.这样客户端容易使用和维护.
```
- 举例
```java
//Strategy interface
public interface Comparator<T> {
	public int compare(T t1,T t2);
}
public StringLengthComparator implements Comparator<String>{
	public int compare(String s1,String s2){
    	return s1.length() - s2.length();
    }
}
```
Note:Comparator接口是泛型(26);

```
3. 如果策略类只使用一次,可以考虑使用匿名类(22).但提醒的是:匿名类每次使用都会创建一个新的实例
```
- 举例:
```java
Arrays.sort(StringArray,new Comparator<String>(){
	public int compare(String s1,String s2){
    	return s1.length() - s2.length();
    }
});
```

```
4. 如果策略类被反复执行,可以将函数对象存储到一个私有静态final域中重用.
```
```
5. 宿主类+私有嵌套策略类(eg:String中的CASE_INSENSITIVE_ORDER)
```
- 举例:
```java
Class Host{
	//嵌套类
	private static calss StrLenCmp implements Comparator<String>, Serializable{
    	public int compare(String s1,String s2){
        	return s1.length() - s2.length();
        }
    }
    //共用对象类
    public satic final Comparator<String> STRING_LENGTH_COMPARATOR= new StrLenCmp();
}
```

#####总结
```
1. 在Java中实现策略模式,要声明一个接口来表示该策略,每一个具体策略类需要实现这个接口的类.
```
```
2. 当具体策略类只被使用一次时,可以采用匿名类来声明和实例化这个具体策略类
```
```
3. 当具体策略类被重复使用时,可以采用**宿主类+私有嵌套策略类**实现.或则提供单例模式共享,注意导出的应该是静态final域
```

###第22条:优先考虑静态成员类
#####嵌套类介绍
```
嵌套类是指定义在另一个类的内部类,主要是为了它的外围类提供服务.
```
#######分类
```
嵌套类有四种:静态成员类+非静态成员类+匿名类+局部类
```
#####静态成员类
#######特点
```
1. 静态成员类是外围类的一个静态成员,与其他静态成员一样,遵守同样的可访问性规则.如果被声明是private,则只能外外围类的内部访问
```
```
2. 静态成员类与其他普通类一样,只是碰巧声明在另一个类的内部,可以访问外围类的所有成员,包括是私有成员
```
#######常见用法
```
静态成员类的一种常见用法是:作为公有的辅助类,仅当与它的外部类一起使用才有意义.
```
- 举例
```
考虑计算器类Calculator类,支持各种操作(30),则可以在计算器类Calculator类中加入一个公有静态成员类:Operation枚举.那么,客户端就可以使用诸如:Calculator.Operation.PLUS或Calculator.Operation.MINUS这样的名称来引用这些操作.
```


