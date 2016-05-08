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
程序的期望输出结果应该是："Set","List","Unknown Collection".但实际输出结果全是是"Unknown Collection"
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
Note:
```
name方法在类Wine声明，并且被子覆写。如预期结果一样："wine, sparking wine和champagne".
```
```
这时覆写与重载一个非常大的区别，重载是编译期间决定执行逻辑，覆写是会在执行期间根据对象类型来决定执行逻辑
```

#######CollectionClassifier示例中最佳修正方案是
```
提供静态方法，根据instanceof来判断具体对象类型，注意要从具体到一般，子类到父类的顺序。
```
```java
public static String classify(Collection< ? > c){
	return c instanceof Set ? "Set" : c instanceof List ? "List" : "Unknown Collection";
}
```

#####重载机制特点
```
由于重载机制的执行逻辑是编译期间决定的，而且重载机制使用时，可能导致程序员困惑，这就是一个失败的类。
```

#####如何避免胡乱使用重载机制
```
1.安全保守策略：永远不要导出两个具有相同参数数目的重载方法。
```
```
2. 如果方法使用可变参数，保守的策略是永远不要重载它(42除外)。
```
- 举例：

```
比如ObjectOutputStream类，对于每个基本类型，它的Write方法都有变形。并不是采用重载write方法，分别是:writeBoolean(boolean),writeInt(int),writeLong(long)变形。这样可读性变得很强。
```
```
3. 对于构造器，并不能使用不同名称，所以可能选择采用静态工厂(1),而不是构造器方式。
```
```
4. 如果导出多个具有相同参数数目的重载方法，但是方法的参数类型具有根本不同，不可能把一种参数的实例转换成另一种参数类型，那么，重载也是可以接受的。比如:ArrayList有一个构造器参数是:int，另一个是Collection参数,就是可以接受。
```

#####要特别留心基本类型的自动装箱，可能导致真正的麻烦
- 举例：
```java
public class SetList {
    public static void main(String [] args){
        Set< Integer > set = new TreeSet< Integer>();
        List< Integer > list = new ArrayList< Integer >();
        for(int i = -3;i<3;i++){
            set.add(i);
            list.add(i);
        }
        for(int i =0;i<3;i++){
            set.remove(i);
            list.remove(i);
        }
        System.out.println(set + " " +list);
    }
}
```
Note:
```
预期结果:[-3 -2 -1] [-3 -2 -1],事实结果是:[-3 -2 -1][0 1 2]
```

#######输出结果解释
```
set.remove(i)选择重载方法是remove(E),它会将i从int自动装箱到Integer中。这是符合我们整个思路的。但是list.remove(i)调用选择重载方法remove(int index)，从列表指定位置去除元素，先去除第一个元素，再去除第二个元素，再去除第三个元素。但是有一种方法是，可以调用list的另一个重载对象:list.remove(Object o).
```
```java
for(int i =0;i<3;i++){
	set.remove(i);
    list.remove(Integer.valueOf(i));
}
```
Note:
```
如果代码是上面这样的，那么整个输入符合我们期望的结果:[-3 -2 -1][-3 -2 -1]
```

#######输出结果引发的思考
```
正如前面所说：如果重载方法的参数类型有质的区别，那么重载也是可以接受的。比如上面案例的根本原因是：remove(Object)和remove(int)重载导致的，而且再加上java中自动装箱的影响。这也更能体现一个重要观点：自动装箱和泛型加入java语言一部分后，谨慎重载变得更加重要了。
```

#####如果重载方法执行相同的逻辑，允许重载
- 举例：
```
String类中有重载方法，但执行逻辑一样
```

```java
 public boolean contentEquals(StringBuffer sb) {
        synchronized (sb) {
            return contentEquals((CharSequence) sb);
        }
    }
    
public boolean contentEquals(CharSequence cs) {
        if (value.length != cs.length())
            return false;
        // Argument is a StringBuffer, StringBuilder
        ....
    }
```
Note:
```
尽管违反了本条目的规则，但是两个重载方法最终在相同参数被调用，执行相同的功能，重载就不会带来危害。
```

#####总结
```
本节被提出的主要目的是：让程序员知道执行那个重载方法。尽量避免重载。
```

###第42条：慎用可变参数
```
可变参数机制通过先创建一个数组，然后将参数值传到数组中，最后将数组传递给方法。
```
```
下面的例子是求和
```
- 举例1：
```java
static int sum(int... args){
	int sum = 0;
    for(int arg : args){
    	sum+=arg;
    }
    return sum;
}
```
```
下面的例子，是求多个int参数的最小值,要求编写需要1个或者多个某种类型参数的方法
```
- 举例2:
```java
static int min(int... args){
	if(args.length == 0){
    	throw new IllegalArgumentException("Too few arguments");
    }
    int min = args[0];
    for(int i =0;i<args.length;i++){
    	if(args[i] < min){
        	min = args[i];
        }
    }
    return min;
}
```
Note:
```
上诉代码，唯一一个比较大的缺点是：需要编写1个或者多个参数，但上述代码可以接收不传参数，而且是在运行时才出错，编译期间无法发现。
```
#######比较好的做法
```java
static int min(int firstArg, int... remainingArgs){
	int min = firstArg;
    for(int arg : remainingArgs){
    	if(arg < min){
        	min = arg;
        }
    }
    return min;
}
```

#####一个提醒
```
不要将使用final参数数组的现有方法，改造成使用可变参数代替。
```
- 举例：
```java
public static void main(String args[]) throws Exception {
      int [] myArray={1,2,3};
      System.out.println(Arrays.asList(myArray));
    }
```
Note:
```
上面的输出毫无意义，这种做法在对象引用类型的数组才有作用。比如将上面的int改为Integer，则可以正确输出。
```
#######输出解释
```
Array.asList方法将int[]包装到List<int []>类型，如果直接调用printf输出，则输出的是数组的地址，产生令人遗憾的结果。
```
#######代替策略
```
发现Array提供了Arrays.toString方法，可以使用Arrays.toString代替Arrays.asList
```
```java
System.out.println(Arrays.toString(myArray));
```

#####性能问题的讨论
```
在重视性能的情况下，使用可变参数机制要特别小心。可变参数的每次调用都会导致进行一次数组分配和初始化，可能会影响到性能问题
```
#######解决办法
```
假设某个方法95%会调用3个或则更少的参数，可以采用声明5个重载的方式,非常有名的例子就是：EnumSet的of方法
```
```java
public void foo(){}
public void foo(int a1){}
public void foo(int a1,int a2){}
public void foo(int a1,int a2,int a3){}
public void foo(int a1,int a2,int a3,int ...rest){}
```

#####总结
```
当定义参数数目不定的方法时，可变参数方法是一种很方便的方法，但是不应该过渡滥用，同时需要考虑性能问题。
```

###第43条：返回零长度的数组或者集合，而不是null
```java
private final List<Cheese> cheesesInStock = ...;
/**
* @return an array containing all of the cheeses in the shop
* or null if no cheeses are available for purchase.
*/
public Cheese[] getCheeses(){
	if(cheesesInStock.size() == 0){
    	return null;
    }
    ...
}
```
#######客户端调用代码
```java
Cheese [] cheeses = shop.getCheeses();
if(cheeses != null && Arrays.asList(cheeses).contains(Cheese.STILTON)){
	System.out.println("Jolly good,just the thing");
}
```
#######而不是下面的代码
```java
if(Arrays.asList(shop.getCheeses()).contains(Cheese.STILTON)){
	System.out.println("Jolly good,just the thing");
}
```
Note:
```
对于一个返回null而不是零长度数组或者集合的方法，几乎每次用到该方法都要留意处理null特殊情况。很容易忘记写这种代码来处理null返回值
```

#####对于null返回值比零长度数组好的一个理由讨论
```
有人认为:null返回值比零长度数组更好，因为它避免了分配数组所需要的开销。
```
#######上面的观点不成立有两个原因
```
1. 在这个级别上担心性能问题是不明智的，除非分析表明这个方法正是造成性能问题的主要原型(55)
```
```
2. 如果每次返回同一个零长数组是有可能的，因为零长度数组是不可变的，而把不可变对象有可能被自由共享(15)，比如下面的实现
```
```java
//The right way to return an array from a collection
private final List<Cheese> cheesesInStock = ...;
private static final Cheese[] EMPTY_CHEESE_ARRAY = new Cheese[0];
/**
* @return an array containing all of the cheeses in the shop
*/
public Cheese[] getCheese[](){
	return cheesesInStock.toArray(EMPTY_CHEESE_ARRAY);
}
```
Note:
```
这是一种非常棒的代码手法。零长度数组常量被传递给toArray方法。这种做法永远也不会分配零长度的数组。
```
```java
//The right way to return a copy of a collection
public List<Cheese> getCheeseList(){
	if(cheesesInStock.isEmtpy())
    	return Collections.emptylist();
    else
    	return new ArrayList<Cheese>(cheesesInStock);
}
```
Note:
```
可以采用集合值的方法，返回同一个不可变的空集合
```

#####总结
```
如果返回类型为数组或者集合的方法没有理由返回null,而不是返回一个零长度的数组或者集合
```

###第44条：为所有导出的API元素编写文档注释






