#第11章:序列化
[TOC]
本章目的:讨论对象序列化API,提供一个框架用来将对象编码成字节流,并从字节流编码中重新构建对象
```
对象序列化:将一个对象编码成一个字节流
对象反序列化:将原来序列化的字节流反序列化一个对象
本章将介绍一种非常棒的特性:序列化代理模式(78),可以避免对象序列化很多缺陷
```

###第74条:谨慎地实现Serializable接口
```
一个类的实例想被序列化,只需"implements Serializable"接口即可.所以导致很多程序员任务序列化很简单.
虽然一个类可被序列化的直接开销非常低,但是为了序列化而付出的长期开销确实实实在在的.
```
#####实现Serializable接口代价
```
1. 最大的代价:一旦一个类被发布,就大大降低了"改变这个类的实现"的灵活性.
```
```
如果一个类实现了Serializable接口,它的字节流编码就变成了它的导出API的一部分.
一旦这个类被广泛使用,且并没有设计一种自定义的序列化形式,那么该类只能保持最初的内部表示法.也就是说,类中的私有的和包级私有的实例域都将变成导出的API的一部分,不符合"最低限度地访问域"(13)
```
```
假如采用了默认的序列化形式,那么这个类将不能被比较大的变动,否则可能导致序列化不一致问题,抛出错误.
应该仔细设计一个高质量的序列化形式,并且很长时间类都使用这中形式(75,78).
设计良好的序列化形式也许会给类的演变带来限制,但是设计不好的序列化会导致类根本无法使用
```
```
序列化演变受到限制,这种限制的一个例子与流的唯一标识符有关,通常成为序列化版本UID.
```
#######序列化版本UID作用
```
每个可序列化的类都有一个唯一标识号与它想关联.如果没有指定long类型的UID,那么系统会自动根据这个类调用一个复杂计算产生标识号.
```
```
这个标识号产生的值会受到类名称,接口名称,以及所有的公有的和受保护成员的名称影响.
如果你通过任何方式改变这些信息,比如,增加一个不是很重要的工具方法,自动产生的序列版本UID将会变化.可能导致序列化失败,则兼容性将会破坏.
```
```
2. 第二个代价:出现Bug和安全漏洞的可能性
```
```
序列化机制是语言之外的对象创建机制.无论是接受默认的行为,还是覆盖了默认的行为,反序列化机制都是一个"隐藏的构造器",
所以要确保:反序列化过程必须也要保证所有"由真正的构造器建立起来的约束关系",而且不允许攻击者访问正在构造过程中的对象内部信息.
```
```
依靠默认的反序列化机制,很容易使对象的约束关系遭到破坏,以及遭受非法访问(76)
```
```
3. 第三个代价:随着类发行新的版本,相关的测试负担也增加
```
```
当一个可序列化的类被修订的时候,非常关键的一点是:检查能否在新版本中序列化,然后在旧版本中反序列化.同时,还需要确保反序列化的结果与原先保持一致.测试的工作量非常大
```
#####实现Serializable接口好处
```
如果一个类将要加入到某个框架中,并且该框架依赖于序列化来实现对象传输或持久化,对于这个类来说,实现Serializable接口就非常必要了.
```
#####何时实现Seriablizable接口
```
1. 为了继承而设计的类(17)应该尽可能少地去实现Seriablizable接口,用户的接口也应该尽可能少的继承Seriablizable接口.
```
```
如果违反上面的规则,扩展这个类或者实现这个接口的程序员将会背上沉重负担.但有些情况违反这条规则却是合适的
```
- 举例:
```
如果一个类或者接口存在的目的主要是为了参与到某个框架中,该框架要求所有的参与者都必须实现Seriablizable接口,
那么实现或扩展Seriablizable接口是有意义的.
```

#######为了继承而设计的类举例及解释
```
1. Throwable类实现Seriablizable接口,所以RMI的异常可以从服务器传到客户端
```
```
2. Component类实现Seriablizable接口,因此GUI可以被发送,保存和恢复
```
```
3. HttpServlet类实现Seriablizable接口,因此会话状态可以被缓存.
```
#####实现一个带实例域的类的忠告
```
如果你实现一个带有实例域的类,它是可序列化和可扩展的,该类的实例域被初始化成它们默认值(整数为0,boolean为false,对象引用为null),
这样就可能违背这些约束条件.
```
#######解决方法:添加readObjectNoData方法
```java
//readObjectNoData for stateful extendable serializable classes
private void readObjectNoData() throws InvaliaObjectException{
	throw new InvaliaObjectException("Stream data required");
}
```
#####如何实现父类不允许序列化,而允许子类序列化
```
如果一个类专门为了继承而设计的类,不可序列化.特别是超类并没有提供无参构造器,但其子类可能允许实现序列化,那么即使其子类实现了Serializable接口,也无法序列化.
所以,对于为了继承而设计的不可序列化的类,应该考虑提供一个无参构造器.
```
```
最好在所有的约束条件都已经建立的情况下再创建对象(15).不可盲目地为一个类增加无参构造器和单独的初始化方法,不然可能破坏约束关系.
```
#######解决办法
```
有一种办法可以给"不可序列化但可扩展的类"增加无参构造器,同时避免上面的不足.
```
- 举例:不可序列化父类
```java
public abstract class AbstractFoo {
    //Nonserializable stateful calss allowing serializable subclass
    private int x, y;// Our state
    
    //This enum and field are used to tract initialization
    private enum State{
        NEW,INITIALIZING,INITIALIZED
    }
    private final AtomicReference<State> init = new AtomicReference<State>(State.NEW);
    public AbstractFoo(int x, int y){
        initialize(x,y);
    }
    // This constructor and the following method allow
    // subclass's readObject method to initialize our state
    protected AbstractFoo(){}
    protected final void initialize(int x, int y){
        if(!init.compareAndSet(State.NEW, State.INITIALIZING)){
               throw new IllegalStateException(" Already initialized");
        }
        this.x = x;
        this.y = y;
        //Do anything else the original constructor did
        init.set(State.INITIALIZED);
    }
    protected final int getX(){checkInit(); return x;}
    protected final int getY(){checkInit(); return y;}
    // Must call from all public and protected instance methods
    private void checkInit(){
            if(init.get() != State.INITIALIZED){
                throw new IllegalStateException("Uninitialized");
            }
            ///...
    }
}
```
Note:
```
增加一个受保护的无参构造器,和一个初始化方法.初始化方法与正常的构造器具有相同的参数,并且建立起同样的约束关系
```
```
AbstractFoo类中所有的公有的和受保护的实例方法被调用之前都必须调用checkInit方法来检查
```
```
init域是一个原子引用,这种模式利用compareAndSet方法来操作枚举原子引用,这是很好的线程安全状态机的通用实现.
```
- 举例:子类序列化
```java
public class Foo extends AbstractFoo implements Serializable{
    private static final long serialVersionUID = -7508750994790720854L;

    // Serializable subclass of nonserializable stateful class
    private void readObject(ObjectInputStream s) throws IOException, ClassNotFoundException{
        s.defaultReadObject();
        //Manually deserialize and initialize superclass state
        int x = s.readInt();
        int y = s.readInt();
        initialize(x, y);
    }
    
    private void writeObject(ObjectOutputStream s) throws IOException{
        s.defaultWriteObject();
        //Manually serialize superclass state
        s.writeInt(getX());
        s.writeInt(getY());
    }
    
    //Constructor does not use the fancy mechanism
    public Foo(int x, int y){
        super(x, y);
    }
}
```

#####内部类与静态成员类实现Serializable接口
```
内部类(22)不应该实现Serializable接口.
```
```
静态成员类却可以实现Serializable接口
```

#####总结
```
千万不要认为实现Serializable接口很容易,因为后期的维护和更新非常耗费精力,所以之前要慎重考虑清楚.
```
```
如果遇到一个为了继承而设计的类,需要更加小心.如果允许子类实现Serializable接口,则需要提供一个可访问的无参构造器.
这个方案允许子类实现Serializable接口,但有不是强行需要实现Serializable接口.
```

###第75条:考虑使用自定义的序列化形式
```
如果一个类实现了Serializable接口，并且使用了默认的序列化形式，那么将可能永远也无法彻底摆脱这个类。
```
```
如果没有先认真考虑默认序列化是否合适，那么则不要贸然接受。一般来讲，只有当自行设计的自定义序列化形式和默认的序列化形式基本相同时，才会接受默认的序列化形式。
```
#####默认序列化
```
默认序列化形式描述了该对象内部所包含的数据，以及每个从这个对象到达其他的对象的内部数据。
同时也描述了所有这些对象被链接起来后的拓扑结构。但是，理想的序列化形式应该只包含该对象的逻辑数据。
```
```
如果一个对象的物理表示法等同于它的逻辑内容，可能适合使用默认的序列化形式。
```
- 举例：
```java
//Good candidate for default serialized form
public class Name implements Serializable{
	private final String lastName;
    private final String firstName;
    private final String middleName;
    //...
}
```
Note:
```
从逻辑的角度看，名字的确由三个串组成。实例域精确反映了它的逻辑内容。
```
#######还需要提供readObject方法
```
即使你确定使用默认的序列化形式是合适的，通常还必须提供一个readObject方法以保证约束性和安全性。
对于上例Name类而言，readObject方法必须确保lastName和firstName是非null.
```

#####物理结构无法反映逻辑结构的探讨。
```
另一个极端的例子，StringList类表示一个字符串列表(不考虑使用List)
```
- 举例:
```java
//Awful candidate for default serialized form
public final class StringList implements Serializable{
	private int size = 0;
    private Entry head = null;
    
    private static class entry implements Serializable{
    	String data;
        Entry next;
        Entry previous;
    }
    //...
}
```
Note:
```
逻辑意义上:一个字符串序列;物理意义上:双向列表.如果采用物理意义上的序列化形式,则会显示出链表的所有项,以及项之间的双向链接.
```

#######物理表示法和逻辑数据冲突
```
如果一个对象的物理表示法与它的逻辑数据内容有实质性的区别时,使用默认序列化形式有四大缺点
```

```
1. 使这个类的导出API永远地束缚在该类的内部表示法上
比如上面的例子,尽管StringList.Entry是私有类,但序列化将其变成公有API.该类永远也摆脱不掉维护链表项所需要的代码
```
```
2.消耗过多的空间
上面的例子,需要维护每项之间的所有链接关系.远远超出我们需要维护的逻辑数据.
```
```
3. 消耗过多的时间
序列化逻辑并不了解的对象图的拓扑关系,需要进行图遍历过程.上例就需要沿着next进行遍历
```
```
4. 引起栈溢出
因为需要进行图遍历,据作者所言,当StringList实例包含1258个元素时,对其序列化就会导致出错.
```
#####如何构建逻辑数据
```
比如上面的例子:StringList类,只需先包含链表中字符串的数目,再紧跟者这些字符串即可.这样就构成了StringList所表示的逻辑数据.
```
```
改写StringList类,提供writeObject和readObject方法,用来实现序列化.同时使用transient修饰的实例域,会从序列化中省略
```
- 举例:
```java
public class StringList {
    //StringList with a reasonable custom serialized form
    private transient int size = 0;
    private transient Entry head = null;
    
    //No longer Serializable
    private static class Entry{
        String data;
        Entry next;
        Entry previous;
    }
    
    public final void add(String s){
        //...
    }
    
    private void writeObject(ObjectOutputStream s) throws IOException{
        s.defaultWriteObject();
        s.writeInt(size);
        //Write the String List
        for(Entry e = head ; e != null ; e = e.next){
            s.writeObject(e.data);
        }
    }
    
    private void readObject(ObjectInputStream s) throws IOException, ClassNotFoundException{
        s.defaultReadObject();
        int numElements = s.readInt();
        //Read in all elements and insert them in list
        for(int i=0;i < numElements; i++){
            add((String) s.readObject());
        }
    }
}
```

Note:
```
1. 虽然StringList的所有域都是transient,但请仍然使用defaultWriteObject,和defaultReadObject.因为这样会极大的增加灵活性,
保持向前或向后的兼容性.
```
```
2. 这种修订后版本的序列化性能得到巨大的提升
```

#####默认序列化可能会破坏对象约束关系
```
有些对象的约束关系要依赖与特定实现细节,这样采用默认的序列化,可能对象都无法恢复.
```
- 举例:
```
考虑散列表情况,物理表示法包含"键-值"项散列桶.即使在同一个JVM实现中,可能也无法保证每次运行结果一样.
所以,对于散列表而言,接收默认的序列化将会构成一个严重的Bug.所以散列表对象进行序列化和反序列化产生对象,会对约束关系遭到破坏.
```

#####序列化注意点

#######transient关键字的使用
```
当defaultWriteobject被调用时,每个未被标记为transient的实例域都会被序列化.
```
```
序列化时,对于冗余的域或则可以通过其他域计算得到的域,请使用transient关键字.
```
```
在决定一个域是否需要transient关键字时,一个重要的考察点:该域的值是否属于对象的逻辑状态的一部分.
如果正在使用自定义的序列化形式,应该将大多数或者所有的域标记为transient.就像StringList那样
```
#######默认序列化
```
当使用默认序列化时,那么被标记为transient域被反序列化时,这些域会被初始化为它们的默认值(false, 0, null).
```
```
如果这些值不能被transient域接受,第一种方法:可以提供一个readObject方法,先调用defaultReadObject,然后将这些域恢复为可接受的值(76).第二种方法:这些域被延迟到第一次被使用的时候才开始初始化(71)
```
#######对象序列化时,同步问题
```
无论是否使用默认序列化,读取整个对象状态的任何其他方法上强制任何同步时,那么也必须在对象序列化上强制这种同步.
如果是对象是一个线程安全对象(70),即使使用的是默认序列化形式,也必须提供并发的序列化
```
```java
//writeObject for synchronzied class with default serialized form
private synchronized void writeObject(ObjectOutStream s) throws IOException{
	s.defaultWriteObject();
}
```
Note:
```
这样将会避免其他动作相同的锁排列约束条件,解决死锁危险
```

#####总结
```
1. 当你考虑将类变成可序列化(74)时,只有当默认序列化形式满足对象的逻辑状态时,才可以使用默认序列化
```
```
2. 当采用自定义方法序列化时,仔细思考其逻辑表示.因为这将影响后期维护代价
```

###第76条:保护性地编写readObject方法
```
第39条中介绍了不可变的日期范围类,包含Date域.并且提供器构造器和访问方法保护性的拷贝Date对象
```
```java
public final class Period{
	private final Date start;
    private final Date end;
    
    public Period(Date start, Date end){
    	this.start=new Date(start.getTime());
        this.end = new Date(ent.getTime());
        if(this.start.compareTo(this.end) > 0){
        	throw new IllegalArgumentException(start +" after "+ end);
        }
    }
    
    public Date start(){
    	return new Date(start.getTime());
    }
    
    public Date end(){
    	return new Date(end.getTime());
    }
    public String toString(){
    	return start+", -"+end;
    }
}
```
Note:
```
Period对象的物理表示法正好反映它的逻辑数据,按照75条理论,可以使用默认序列化.只需要增加"implements Serializable"字样.
但是,要特别注意的是,如果这么做了,这个类将不再保证它的关键约束了.
```
#####约束条件破坏+原因解释
```
无法保证关键约束原因是:readObject方法实际上也是另一种公共的构造器.所以也必须要和其他的构造器一样,注意同样的所有注意的事项,
构造器必须检查其参数的有效性(38),并且必要时对参数进行保护性拷贝(39).所以readObject方法也必须要做到.
```
```
readObject方法是一个"用字节流作为唯一参数"的构造器.所以使用默认的readObject方法,攻击者可能会传入一个不符合要求的字节流,以来攻击
```
- 举例:
```java
//参看书本267页的例子.提供子接口,以达到违反约束条件的对象生成
```
#######解决办法
```
为Preiod类提供一个readObject方法,该方法首先调用defaultReadObject,然后检查反序列化之后的对象的有效性.
如果有效性失败,抛出InvalidObjectException异常.
```
```java
//readObject method with validity checking
private void readObject(ObjectInputStream s) throws IOException, ClassNotFoundException{
	s.defaultReadObject();//如果是未加transient关键字的域,就可以直接使用了
    //Check that our invariants are satisfied
    if(start.compareTo(ent) > 0){
    	throw new InvalidObjectException(start+ " after" +end);
    }
}
```
#####不可变的Period实例破坏+原因解释
```
攻击者可以通过使用伪造字节流,创建可变的Period实例.
```
```
字节流以一个有效的Period实例开头,然后附上两个额外的引用,指向Period实例的两个私有的Date域.
攻击者从ObjectInputStream中读取Period实例,然后读取附加在后面的"恶意编制的对象引用".
这些对象引用可以访问到私有的Date域所引用的对象.通过改变Date实例,攻击者改变了Period实例
```
- 举例:
```java 
public class MutablePeriod{
	//A period instanc
    public final Period period;
    //period's start field, to which we shouldn't have access
    public final Date start;
    publci final Date end;
    public MutablePeriod(){
    	try{
        	ByteArrayOutputStream bos = new ByteArrayOutputStream();
            ObjectOutputStream out = new ObjectOutputStream(bos);
            
            //Serialize a valid Period instance
            out.writeObject(new Period(new Date(), new Date()));
            
            /* Append rouge "previous object refs" for internal
            * Date fields in Period. For details, see"Java Object Serialization Specificatin," Section 6.4
            **/
            byte[] ref ={0x71, 0, 0x7e, 0,5}//Ref # 5
            bos.write(ref);//The start filed
            ref[4]=4 //Ref #4
            bos.write(ref);//The end field
            
            //Deserialize Period and "stolen" Date references
            ObjectInputStream in = new ObjectInputStream(
            	new ByteArrayInputStream(bos.toByteArray());
            period = (Period)in.readObject();
            start = (Date)in.readObject();
            end = (Date)in.readObject();
        }catch(Exception e){
        	throw new AssertionError(e);
        }
    }
}
```
```
运行下面的程序,可以看到攻击效果
```
```java
public static void main(String [] args){
	MutablePeriod mp = new MutablePeriod();
    Period p = mp.period;
    Data pEnd = mp.end;
    pEnd.setYear(78);
    PEnd.setYear(69);
}
```
Note:
```
上面的代码,虽然在Period实例被创建之后,它的约束条件没有被破坏,但是可以随意修改其内部组件是可能的.
那么原本依赖于其不可变性的所有问题,都可能成为问题.
```
#######解决变法
```
出现上面的问题在于,Period的readObejct方法并没有完成足够的保护性拷贝.
```
```
当一个对象被反序列化时,客户端不应该拥有该对象的引用.如果哪个域包含了这些对象引用,必须做保护性拷贝.
因此,对于不可变类,如果包含了私有的可变组件,必须提供readObject,并对这些组件进行保护性拷贝.
```
```java
//ReadObejct method with defensive copying and validity checking
private void readObject(ObjectInputStream s) throws IOException, ClassNotFoundException{
	s.defaultReadObject();
    //Defendsively copy our mutable components
    start = new Date(start.getTime());
    end = new Date(end.getTime());
    if(start.compareTo(end) > 0){
    	throw new InvalidObjectException(start +" after" +end);
    }
}
```
Note:
```
保护性拷贝位于有效性检查之前,也并没有利用Data的clone方法来进行保护性拷贝.
一个比较遗憾的一点是:使用final域是不可能进行保护性拷贝.因此,必须去掉start,end域的final修饰符.
```
```
也请不要再使用writeUnshared和readUnshared方法,安全性没有达到要求.
```
#####"石蕊"测试
```
"石蕊"测试可以测试默认的readObject方法是否可以被接受.
```
```
具体做法是:增加一个公有的构造器,对对象的所有非transient的域,无论是参数值是什么,都是不进行检查就可以保存到相应的域中.
如果不接受这种做法,那么一种做法是:请提供一个显示的readObject方法,进行有效性检查和保护性拷贝.
另一种做法是:使用序列化代理模式(78)
```

#####提醒
```
readObject方法类似与构造器,readObject方法不可以调用可被覆盖的方法,无论是直接调用,还是间接调用都不可以(17).
```
#####如何编写更加健壮的readObject方法
```
1. 对象引用域必须保持为私有的类,要保护性拷贝这些域中的每个对象.比如:不可变类中可变的域引用
```
```
2. 对于任何约束条件,必须在readObject方法方法中进行检查,如果检查失败,抛出InvalidObjectException异常
```
```
3. 如果整个对象图在被反序列化之后必须进行验证,就应该使用ObjectInputValidation接口
```
```
4. 无论是直接或者间接方式,都不要在readObject方法调用覆盖方法.
```
#####总结:
```
当编写readObject方法时,应当认为你正在编写一个公有的构造器.如果使用默认序列化形式,应该考虑后果
```

###第77条:对于实例控制,枚举类型优先于readResolve
```
第3条中讲述了Singleton模式,给出下面代码.这个类限制了构造器的访问
```
```java
public class Elvis{
	public static final Elvis INSTANCE = new Elvis();
    private Elvis(){}
    
    public void leaveTheBuilding(){//...}
}
```
Note:
```
如果这个类Elvis实现了"Serializable"接口,那么它将不能保证是一个Singleton.无论是使用默认的序列化形式,还是自定义序列化形式(75.
无论是否提供readObject方法(76),都被无法保证单例.
```
```
readObject方法无论是显示还是默认的,都会返回一个新建的实例.这个实例已经不同于初始化的实例.
```
#####readResolve特性
```
readResolve特性允许用readObject创建的实例代替另一个实例.
如果类定义了一个readResolve方法,那么在反序列化之后,就会在新建的对象上调用readResolve方法.然后该方法返回的对象引用将被返回,取代新的对象.
```
```java
//readResolve for instance control - you can do better!
private Object readResolve(){
	return INSTANCE;
}
```
Note:
```
Elvis类的readResolve方法忽略了被反序列化对象,只返回最初的实例.所以所有的实例域都应该被声明为transient.
```
```
如果依赖readResolve方法进行实例控制,带有对象引用类型的所有实例域则都必须声明为tranisent.否则攻击者可能采取MutalbePeriod攻击(76)
```
#######攻击者采用的技术
```
[具体的攻击过程,请参靠书本,不在详细诉说]
```
#####将可序列化的实例受控的类编写成枚举,是最佳选择
```
自Java 1.5以后,readResolve方法就不在是可序列化类中维持实例控制的最佳方法.该方法很脆弱.
```
```
如果将可序列化的实例受控的类编写成枚举,jVM将会保证只有固定数目的类实例
```
```java
//Enum singleton - the preferred approach
public enum Elvis{
	INSTANCE;
    private String [] favoriteSongs = {"Hound Dog", "Heartbreak Hotel"};
    public void printFavorites(){
    	System.out.println(Arrays.toString(favoriteSongs));
    }
}
```
#####readResolve进行实例控制技术
```
readResolve方法控制实例技术,相比较Enum枚举要复杂点,但是却是无法被淘汰.因为很多情况下,实例受控的类在编译期间并不知道实例个数,无法使用Enum类型
```
#####readResolve方法可访问性的探讨
```
1. readResolve方法在一个final类上，应该写成private
```
```
2. readResolve方法在一个非final类上，就必须认真考虑其访问性
如果是私有的，那么将只会对该类有作用
如果是包级私有的，那么将会对同一个包的子类有作用
如果是受保护或公有的，则对所有为覆盖readResolve方法子类都有效果
```
```
如果readResolve方法是受保护或公有的，并且子类没有覆盖，那么在子类进行反序列化时，就会产生一个超类，可能会导致ClassCastException异常。
```
#####总结：
```
应该尽可能地使用枚举类型来实施实例控制的约束条件
```
```
如果编译器无法做到实例个数的判断，需要提供一个具有readResolve方法的类，并确保该类所有的实例域都为基本类型，或者是transient
```





