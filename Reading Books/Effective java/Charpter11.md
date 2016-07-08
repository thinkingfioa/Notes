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
#####




