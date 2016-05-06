#第7章:方法
```
本章目的:如何处理参数和返回值,如何设计方法签名,如何为方法编写文档.
```
[TOC]
###第38条:检查参数的有效性
```
大多数方法和构造器对于传递给它们的参数值都会有某些限制.这符合"在发生错误之后尽快检测出错误"的一个普遍原则的具体情景.
```
#####在方法执行前,对参数进行检查
```
请在方法执行前先对参数进行检查,这样如果失败将会出现适当的异常.如果推迟检查参数或忽略检查参数,可能导致错误或异常转移,或者破坏了某个对象的内部状态,在将来某个不确定时后报出异常或错误.
```
#####公有的方法,要用Javadoc的@throws标签(tag)
```
使用@throws标签,在文档中说明违反参数值限制时会抛出的异常(62).
```
#######公有方法
- 举例:
```java
    /**
     * Returns a BigInteger whose value is {@code (this mod m}).  This method
     * differs from {@code remainder} in that it always returns a
     * <i>non-negative</i> BigInteger.
     *
     * @param  m the modulus.
     * @return {@code this mod m}
     * @throws ArithmeticException {@code m} &le; 0
     * @see    #remainder
     */
    public BigInteger mod(BigInteger m) {
        if (m.signum <= 0)
            throw new ArithmeticException("BigInteger: modulus not positive");

        BigInteger result = this.remainder(m);
        return (result.signum >= 0 ? result : result.add(m));
    }
```

#######未被导出的方法,作为包的创建者,应确保将有效的参数值传递进来.因此,非公有方法通常应该使用断言
- 举例:
```java
//Private helper function for recursive sort
private static void sort(long a[], int offset, int length){
	assert a!= null
    assert offset >= 0 && offset<= a.length;
    assert length >= 0 && length <= a.length - offset;
    ...
}
```
Note:
```
断言是要求被断言的条件将会为真,否则将会抛出AssertionError.如果没有起到作用,本质上也不会有成本开销.
```

#####有些参数即使方法本身没有用到,对方法的参数检查有效性尤其重要
```
有些参数,方法本身没有用到,可能是为了保存起来供以后使用,这种情况的参数检查也是非常重要的
```
- 举例:
```
第18条中,有一个方法:static List<Integer> intArrayAsList(final int[] a){...},参数是一个int数组,返回一个数组的List视图.
如果方法客户端传递null进入,且方法体省略了条件检查,那么后果不堪设想.
```

#####构造器参数的检查
```
构造器正是将参数保存起来的一种特殊的方法,所以控制进入的参数要求,检查构造器参数的有效性非常重要
```

#####例外情况
```
在方法执行它的计算任务前,应该先检查它的参数,但这一规则也有些例外.
```
#######第一种例外
```
有些检查工作非常昂贵,或者根本是不切实际的,而且有效性检查已隐含在计算过程中完成.
```
- 举例:
```
比如,一个为对象列表排序的方法:Collections.sort(List),sort方法会进行List列表中元素进行比较,如果不能比较的也会抛出ClassCastException异常,所以,如果提前检查列表元素是否可以相互比较,毫无意义.
```
```
注意的是,如果不加选择地使用这种方法将会导致失去失败原子性(64)
```

#######第二种例外
```
有些计算会隐式地执行必要的有效性检查,如果检查不成功,就会抛出错误的异常.这种情况下,应该使用异常转译(61)技术,将计算过程中抛出的异常情况转换到正确的异常.
```

#####总结
```
1. 本条目,不是告诉读者:对参数的任何限制都是件好事.其实,应该对方法必要的输入参数进行检查,对参数的限制应该越少越好
```
```
2. 每当编写方法或者构造器时候,应该考虑它的参数有哪些限制.且在方法体的开头处,通过显式的检查来实施这些限制.这个习惯至关重要.
```

###第39条:必要时进行保护性拷贝
```
有时可能由于其他程序员对你的API产生误解,导致的各种不可预期的行为,所以,应该能保持健壮的类.
```
- 举例:
```java
public final class Period {
// Broken "immutable" time period class
    private final Date start;
    private final Date end;
    
    /**
     * @param start the beginning of the period
     * @param end the end of the period;must no precede start
     * @throws IllegalArgumentException if start is after end
     * @throws NullPointerException if start or end is null
     */
    public Period(Date start,Date end){
        if(start.compareTo(end) > 0){
            throw new IllegalArgumentException(start + " after"+end);
        }
        this.start = start;
        this.end = end;
    }
    public Date getStart(){
        return start;
    }
    public Date getEnd(){
        return end;
    }
}
```
Note:
```
乍一看,这个类不可变,且对构造器输入的数据进行了检查.但是由于Date类本身是可变的,所以,并不能保证不可变性.下面客户端,则修改了不可变类.
```
```java
//Attack the internals of a Period instance
Date start = new Date();
Date end = new Date();
Period p = new Period(start,end);
end.setYear(78);//Modifies internals of p!
```

#####对可变参数进行保护性拷贝
```java
//make defensive copies of parameters
public Period(Date start,Date end){
	this.start = new Date(start.getTime());
    this.end = new Date(end.getTime());
    
    if(this.start.commpareTo(this.end) > 0){
    	 throw new IllegalArgumentException(start + " after"+end);
    }
}
```
#######深度探讨
```
1. 保护性拷贝是在检查参数的有效性(38)之前进行的,并且有效性检查是针对拷贝后的对象,而不是原始对象.
```
Note:
```
这样做,是非常必要的.这样可以避免"危险阶段"期间从另一个线程改变类的参数.危险阶段是指:检查参数开始,直到拷贝参数之间的时间段.
```
```
2. 并没有用Date的clone方法进行保护性拷贝.因为Date是非final的,不能保证clone方法一定返回的是java.util.Date的对象:可能返回出于恶意而设计的不可信的子类实例.
```
```
3. 上面的修改,Period实例仍然可以被修改
```
```java
// Second attack on the internals of a Period instance
Date start = new Date();
Date end = new Date();
Period p = new Period(start,end);
p.getEnd().setYear(78);//Modifies internals of p!
```
Note:
```
解决办法:返回不可变内部域的保护性拷贝
```
```java
    public Date getStart(){
        return new Date(start.getTime());
    }
    public Date getEnd(){
        return new Date(end.getTime());
    }
```
```
4. 访问方法和构造器不同,它们在进行保护性拷贝的时候允许使用clone方法.因为,我们直到Period内部的Date对象是java.util.Date
```
```java
 public Date getStart(){
        return start.clone());
    }
    public Date getEnd(){
        return end.clone());
    }
```
```
5. 采用新的构造器和新的访问方法之后,Period真正不可变了.所有的域都被真正封装到对象的内部.
```

#####参数的保护性拷贝使用场景
```
参数的保护性拷贝并不是针对不可变类,应该参考下面的两点
```
#######第一点
```
如果编写方法或者构造器时,允许用户提供的对象进入内部数据结构,需要考虑:客户提供的对象是否可能是可变,如果是,是否可以容忍进入数据结构后发生变化,如果不允许进入的参数在发生变化,则应该使用参数的保护性拷贝.
```
- 举例:
```
如果,客户端提供的类实例作为了内部Map实例的键(key),则明显不能变.
```
#######第二点
```
内部组件,返回到客户端,同样需要认真考虑是否需要保护性拷贝.
```
#####尽量使用不可变的对象作为内部组件
```
一个非常重要的启示:只要有可能,都应该使用不可变的对象作为对象内部的组件,这样就不需要在为保护性拷贝(15)操心．比如前面的Period例子，有经验的程序员将会使用long　start = Date.getTime()基本类型来作为内部时间.因为Date是可变的.
```

#####总结
```
如果类具有从客户端得到或者返回到客户端的可变组件,类就必须保护性拷贝这些组件.如果受到拷贝的成本限制,且信任客户端,则在文档中指明,以代替保护性拷贝.
```

###第40条:谨慎设计方法签名
```
总结若干API设计技巧
```
#####谨慎地选择方法的名称
```
方法的名称应该遵循标准的命名习惯(56)
```
#####不要过于追求提供便利的方法
```
每个方法应该尽其所能。方法太多使得类难以学习，使用，文档化，测试和维护。
```
#####避免过长的参数列表
```
目标参数的个数是四个参数，或则更少。
```
#####解决过长的参数列表的三种方法
#######第一种：将方法分解成多个方法
```
将方法分解成多个方法，每个方法只需要这些参数的一个子集。这样可能会导致方法过多
```
- 举例：
```
比如java.util.List接口，并没有提供“在子列表中查找元素的第一个索引和最后一个索引”的方法，而提供两个方法：subList方法+indexOf方法+lastIndexOf方法。将原本需要三个参数的改为了两个参数的方法
```

#######第二种：创建辅助类
```
创建辅助类，用来保存参数的分组,一般辅助类为静态成员类(22).
```
- 举例：
```
比如一个表示纸牌游戏的类，可以将纸牌点数和花色封装成辅助类，这样参数就可以使用辅助类作为参数列表。
```

#######第三种：从对象构建到方法调用都采用Builder模式(2)
```
如果方法有多个参数，且参数有些是可选的，请定义一个对象来表示所有的参数，并允许客户端多次在对象上调用"setter"方法。一旦设置了需要的的参数，客户端就调用对象的方法，并对参数进行有效性检查。
```

#####对于参数类型，要优先使用接口而不是类(52)
```
使用具体的类作为参数，限制了客户端只能传入特定的实现，如果输入数据以其他形式存在，可能导致非常昂贵的拷贝操作。
```
#####对于boolean参数，要优先使用两个元素的枚举类型
```
它使代码更易于阅读和编写，也使以后更易于添加更多的选项。
```
```java
class Thermometer{
	public enum TemperatureScale{ FAHRENHEIT, CELSIUS };
    Thermometer.newInstance(TemperatureScale.CELSIUS);
}
```
Note:
```
1. Thermometer.newInstance(TemperatureScale.CELSIUS);不仅比Thermometer.newInstance(true);可读性更好，而且在未来发行将KELVIN添加到TemperatureScale中。
```
```
2. 如果想要将温度刻度单位的代码重构到枚举常量的方法中(30).eg:每个刻度单位都带一个double值。
```

###第41条：慎用重载
```
下面例子试图根据一个集合是Set,List或其他集合类型，来进行分类
```
- 举例：
```java
public class CollectionClassifier {
    //Broken! - What does this program print?
    public static String classify(Set<?> s){
        return "Set";
    }
    
    public static String classify(List<?> list){
        return "List";
    }
    
    public static String classify(Collection<?> c){
        return "Unknown Collection";
    }
    
    public static void main(String [] args){
        Collection<?> [] collections ={
            new HashSet<String>(),
            new ArrayList<BigInteger>(),
            new HashMap<String,String>().values()
        };
        for(Collection<?> c : collections){
            System.out.println(classify(c));
        }
    }
}
```
Note:
```
程序的期望输出结果应该是："Set","List","Unknown Collection".但实际输出结果是"Unknown Collection"
```

#######输出结果解释
```
1. classif方法被重载了，我们知道：调用哪个重载方法是在编译时就决定了。上面程序的for循环中，编译期间已经决定调用方法:String classify(Collection<?> c).
```
```
2. 对于重载方法的选择是静态的，在编译期间决定。对于被覆盖方法的选择是动态的，也就是说选择的依据是根据所在对象的运行时类型选择具体的调用方法。
```
- 举例：
```java
class Wine{
    String name(){
        return "wine";
    }
}

class SparklingWine extends Wine{
    @Override
    String name(){
        return "sparking wine";
    }
}

class Champagne extends SparklingWine{
    @Override
    String name(){
        return "champagne";
    }
}
public class Overriding {
    public static void main(String [] args){
        Wine [] wines ={
            new Wine(),new SparklingWine(),new Champagne()
        };
        
        for(Wine wine : wines){
            System.out.println(wine.name());
        }
    }
}
```




