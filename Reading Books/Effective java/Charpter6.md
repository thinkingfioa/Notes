#第6章:枚举和注解
```
本章目的:讨论使用新的类型:枚举类型+注解类型
```
[TOC]

###第30条:用enum代替int常量
```
枚举类型是指由一组固定的常量组成合法值的类型.
```
```
通常也有用一组具名的int常量来使用,这种方法称为int枚举模式.采用int枚举模式的程序十分脆弱,具有诸多缺点.
```
#####int枚举模式缺点
```
1. 类型安全性和使用方便性都没有任何帮助,甚至可以将一个APPLE传到想要ORANGE的方法中,编译器都没有提供警告.
```
```
2. 因为int枚举是编译时常量,如果客户端使用了枚举常量关联的int发生变化,客户端就必须从新编译.
```
```
3. 将int枚举翻译成可打印的字符串,没有任何便利的方法.且在调试器中,它所显示出来的也只是一个数字,不方便.
```

#####枚举类型
```java
public enum Apple { FUJI,PIPPIN,GRANNY_SMITH }
public enum Orange{ NAVEL,TEMPLE,BLOOP }
```
#######枚举类型优点
```
1. Java枚举类型是通过公有的静态final域为每个枚举常量导出实例的类,不提供任何可以访问的构造器.所以,保证了final和单例的特性.
```
```
2. 枚举提供编译时的类型安全.如果声明一个参数的类型为Apple,则可以办证传入的参数一定属于三个有效的Apple值之一.
```
```
3. 包含同名常量的多个枚举类型可以在一个系统中和平共处.同时,修给枚举类型中的值,无需客户端代码重新编译,因为常量值并没有被编译到客户端代码中
```
```
4. 可以通过调用toString方法,将枚举转换成可打印的字符串.
```
```
5. 枚举类型还允许添加任意的方法和域,并实现任意的接口
```
```
6. 枚举天生就是不可变的,因此所有的域都是final(15).可以是公有的,但最好做成私有并提供公有的访问方法(14).
```
#####枚举类型使用
#######举例:
```
为了将数据与枚举常量关联起来,得声明实例域,并编写一个带有数据并将数据保存在域中的构造器.
```
```
太阳系中有8颗行星,每颗行星都有质量和半径,从而给定物体的质量,就可以计算出一个物体在行星表面的重量.
```
```java
public enum Planet {
    MERCURY(3.302e+23,2.439e6),
    VENUS(4.869e+24,6.052e6),
    EARTH(5.975e+24,6.378e6),
    MARS(6.419e+23,3.393e6),
    JUPITER(1.899e+27,7.149e7),
    SATURN(5.685e+26,6.027e7),
    URANUS(8.683e+25,2.556e7),
    NEPTUNE(1.024e+26,2.477e7);
    private final double mass;
    private final double radius;
    private final double surfaceGravity;
    
    private static final double G = 6.67300E-11;
    //Constructor
    Planet(double mass,double radius){
        this.mass = mass;
        this.radius = radius;
        this.surfaceGravity = G*mass/(radius*radius);
    }
    public double mass(){
        return this.mass;
    }
    public double radius(){
        return this.radius;
    }
    public double surfaceWeight(double mass){
        return mass * surfaceGravity; // F = ma;
    }
}
```
```java
public class WeightTable{
	double earthWeight = Double.parseDouble(args[0]);
    double mass = earthWeight / Planet.EARTH.surfaceGravity();
    for(Planet p : Planet.values()){
    	System.out.println("Weight on %s is %f%n",p.toString(),p.surfaceWeight(mass));
    }
}
```

#####枚举常量的设计考虑1
```
1. 与枚举常量关联的有些行为,如果只需要定义在枚举的类或者包,请将方法写成私有的,或者是包级私有.
```
```
2.如果一个枚举具有普遍适用性,就应该成为一个顶层类.如果只被用在一个特定的顶层类中,就应该成为顶层类的一个成员类(22)
```
- 举例:Java.math.RoundingMode枚举
```
RoundingMode枚举表示十进制小数的舍入模式.类RoundingMode用于DigDecimal类,但是抽象的本质又不属于DigDecimal类.所以将类RoundingMode变成一个顶层类.
```

#####枚举类型设计考虑2
```
如果需要将本质上不同的行为与每个常量关联起来,请参考下面例子如何书写
```
- 举例:
```
编写一个枚举类型,表示计算器的四大基本操作.
```
```java
public enum Operation {
    //Enum type that switches on its own value
    //Not Recommended
    PLUS,MINUS,TIMES,DIVIDE;
    double apply(double x,double y){
        switch(this){
            case PLUS: return x+y;
            case MINUS:return x-y;
            case TIMES: return x*y;
            case DIVIDE:return x/y;
        }
        throw new AssertionError("Unknow op: " + this);
    }
}
```
Node:
```
这段代码可以运行,但是非常脆弱,同时不利于维护.
```
#######解决办法:特定于常量的方法实现
```
将不同的行为与每个枚举变量关联起来:在枚举类型中声明一个抽象的apply方法,并在特定于常量的类主体中,覆写方法.
```
```java
public enum Operation {
    //Recommended 
    PLUS{ 
        double apply(double x ,double y){
            return x+y;
        }
    },
    MINUS{ 
        double apply(double x ,double y){
            return x-y;
        }
    },
    TIMES{ 
        double apply(double x ,double y){
            return x*y;
        }
    },
    DIVIDE{ 
        double apply(double x ,double y){
            return x/y;
        }
    };
    abstract double apply(double x,double y);
}
```

#######类Operation覆盖toString来返回与该操作关联的符号
```java
public enum Operation {
    PLUS("+"){
        double apply(double x,double y){
            return x+y;
        }
    },
    MINUS("-"){
        double apply(double x,double y){
            return x-y;
        }
    },
    TIMES("*"){
        double apply(double x,double y){
            return x* y;
        }
    },
    DIVIDE("/"){
        double apply(double x,double y){
            return x/y;
        }
    };
    private final String symbol;
    Operation(String symbol){
        this.symbol = symbol;
    }
    @Override
    public String toString(){
        return symbol;
    }
    abstract double apply(double x,double y);
}
public static void main(String args[]) throws Exception {
    double x = Double.parseDouble(args[0]);
    double y = Double.parseDouble(args[1]);
    for (Operation op : Operation.values()) {
        System.out.printf("%f %s %f = %f%n", x, op, y, op.apply(x, y));
    }
}
```

#####枚举类型的方法valueOf(String)方法.
```
枚举类型有一个自动产生的valueOf(String)方法,将常量的名字转成常量本身
```
```java
Operation plus = Operation.vlaueof("PLUS");
```
#######如果枚举类型中覆盖toString,要考虑编写一个fromString方法.
```
因为外部程序只是将toString的字符串与枚举类型实例对等,所以需要提供一个fromString方法.
```
```java
public enum Operation {
    PLUS("+") {
        double apply(double x, double y) {
            return x + y;
        }
    },
    MINUS("-") {
        double apply(double x, double y) {
            return x - y;
        }
    },
    TIMES("*") {
        double apply(double x, double y) {
            return x * y;
        }
    },
    DIVIDE("/") {
        double apply(double x, double y) {
            return x / y;
        }
    };
    private static final Map<String, Operation> stringToEnum = new HashMap<String, Operation>();
    static {
        for (Operation op : values()) {
            stringToEnum.put(op.toString(), op);
        }
    }

    public static Operation fromString(String symbol) {
        return stringToEnum.get(symbol);
    }

    private final String symbol;

    Operation(String symbol) {
        this.symbol = symbol;
    }

    @Override
    public String toString() {
        return symbol;
    }

    abstract double apply(double x, double y);
}
```

#####策略枚举
```
多个枚举常量同时共享相同的行为,则考虑使用策略枚举
```
```
下面的例子,考虑用一个枚举表示薪资.五个工作日,超过正常的8个小时工作时间产生加班工资.双休日所有工作都是加班工资.
```
- 举例:
```java
enum PayrollDay {
    MONDY, THESDAY, WEDNESDAY, THURSDAY, FRIDAY,
    STATURDAY, SUNDAY;
    private static final int HOUR_PER_SHIFT = 8;
    double pay(double hoursWorked,double payRate){
        double basePay = hoursWorked * payRate;
        
        double overtimePay=0;
        switch(this){
            case STATURDAY: 
            case SUNDAY:
                overtimePay = hoursWorked * payRate /2;
            deafult://Weekdays
                 overtimePay = hoursWorked <= HOUR_PER_SHIFT ? 0:(hoursWorked - HOUR_PER_SHIFT)*payRate /2;
                break;
        }
        return basePay + overtimePay;
    }
```
Note:
```
这段代码简洁,但是维护困难.如果想将一个元素添加到枚举中,要记住修改switch语句.编译器并不会提醒.
```

#######解决办法:策略枚举
```
策略枚举:每当添加一个枚举常量时,就强制选择一种加班报酬策略.将加班工作计算移到一个私有的嵌套枚举中,再将这个策略枚举的实例倡导PlayrollPay枚举的构造器中.
```
```java
enum PayrollDay {
    MONDAY(PayType.WEEKDAY), 
    TUSEDAY(PayType.WEEKDAY), 
    WEDNESDAY(PayType.WEEKDAY), 
    THURSDAY(PayType.WEEKDAY), 
    FRIDAY(PayType.WEEKDAY), 
    SATURDAY(PayType.WEEKEND), 
    SUNDAY(PayType.WEEKEND);
    
    private final PayType payType;

    PayrollDay(PayType payType) {
        this.payType = payType;
    }

    double pay(double hoursWorked, double payRate) {
        return payType.pay(hoursWorked, payRate);
    }

    // The strategy enum type
    private enum PayType {
        WEEKDAY {
            double overtimePay(double hours, double payRate) {
                return hours <= HOURS_PER_SHIFT ? 0 : (hours - HOURS_PER_SHIFT) * payRate / 2;
            }
        },
        WEEKEND {
            double overtimePay(double hours, double payRate) {
                return hours * payRate / 2;
            }
        };
        private static final int HOURS_PER_SHIFT = 8;

        abstract double overtimePay(double hours, double payRate);

        double pay(double hoursWorked, double payRate) {
            double basePay = hoursWorked * payRate;
            return basePay + overtimePay(hoursWorked, payRate);
        }
    }
}
```

#####何时使用枚举
```
每当需要一组固定常量的使用,也是使用枚举最佳的时候.比如:行星,一周的天数,棋子,菜单的选项,操作代码等.
```

#####总结
```
1. 枚举易读,而且类型安全,功能也更加强大.
```
```
2. 枚举一般都不需要显式的构造器或者成员.
```
```
3. 当在枚举中,遇到多种行为与单个方法关联时.如果是特定于常量的方法要优先于启用自有值的枚举.如果是多个枚举常量同时共享相同的行为时,则考虑策略枚举
```

###第31条:用实例域代替序数
```
所有的枚举都有一个ordinal方法,返回每个枚举常量在类型中的数字位置.枚举天生就与一个单独的int值相关联
```
```java
//Abuse of ordinal to derive an associated value - DON'T DO THIS
public enum Ensemble{
	//DON'T DO THIS
    SOLO,DUET,TRIO,QUARTET,QUINTET,
    SEXTET,SEPTET,OCTET,NONET,DECTET;
    public int numberofMusicians(){
    	return ordinal() + 1;
    }
}
```
Note:
```
上面的例子初次使用往往还可以,但是维护,就是一场噩梦.根本无法将int值与常量对应起来.
```
#####解决方法
```
永远不要根据枚举的序数导出与它关联的值,而是要将它保存在一个实例域中
```
```java
public enum Ensemble{
	 SOLO(1),DUET(2),TRIO(3),QUARTET(4),QUINTET(5),
    SEXTET(6),SEPTET(7),OCTET(8),NONET(9),DECTET(10),
    TRIPLE_QUARTET(12);
    private final int numberOfMusicians;
    Ensemble(int size){
    	this.numberOfMusicians = size;
    }
    public int numberOfMusicians(){
    	return numberOfMusicians;
    }
}
```

#####总结
```
1. Enum规范中写道:程序员不需要方法ordinal,这个方法设计成用于像EnumSet和EnumMap这种基于枚举的通用数据结构的.
```
```
2. 建议程序员最好完全避免使用ordinal方法.
```

###第32条:用 EnumSet代替位域
```
如果一个枚举类型的元素主要用于集合中,一般就使用int枚举模式(30),将2的不同倍数赋予每个常量
```
```
程序中经常使用的位域方式.
```
```java
public class Text{
	public static final int STYLE_BOLD = 1<<0;//1
    public static final int STYLE_ITALIC = 1 <<1; // 2
    public static final int STYLE_UNDERLINE = 1 <<2;//4
    public static final int STYLE_STRIKETHROUGH = 1 << 3; //8
    
    //Patameter is bitwise OR of zero or more STYLE_ constants
    public void applyStyles(int styles){ ... }
}
```
Note:
```
位域方式有着int枚举常量的所有缺点,甚至更多.
```
```
1. 位域以数字形式打印时,翻译位域比翻译简单的int枚举常量要困难的多.而且,当要遍历位域表示的所有元素也没有很容易的方法.
```

#####代替使用位域的方法:EnumSet类
```
java.util包中的类EnumSet类有效的表示从单个枚举类型中提取的多个值的多个集合.
```
```
EnumSet内容都表示为位矢量,查看内部实现发现,如果底层的枚举类型有64个或者更少的元素,那么整个EnumSet就是用单个long表示,性能也是非常好的.
```
#######修改案例
```java
public class Text{
	public enum Style{
    	BOLD,ITALIC,UNDERLINE,STRIKETHROUGH;
    }
    //Any Set could be passed in,but EnumSet is clearly best
    public void applyStyles(Set<Style> styles){ ... }
}
```
#######客户端代码
```java
text.applyStyles(EnumSet.of(Style.BOLD,Style.ITALIC));
```
Note:
```
applyStyles方法采用的是Set< Style >而非EnumSet< Style >.这样就可以接收接口而非接受实现类型.
```

#####总结
```
1. 正是因为枚举类型要用在集合(Set)中,所以没有理由用位域来表示它,请使用EnumSet类,EnumSet类优点太多.
```
```
2. EnumSet有一个缺点:无法创建不可变的EnumSet,不过可以使用Collections.unmodifiableSet将EnumSet封装起来,但影响简洁性和性能.
```

###第33条:用EnumMap代替序数索引
#####枚举类型序数提供数组下标(unRecommand)
```
有时候可能会见到oridinal方法(31)来索引数组的代码,例如下面用于表示一种烹饪的香草.
```
```java
public class Herb {
    public enum Type{
        ANNUAL,PERENNIAL,BIENNIAL
    }
    private final String name;
    private final Type type;
    Herb(String name,Type type){
        this.name = name;
        this.type = type;
    }
    @Override
    public String toString(){
        return name;
    }
}
```
```
假设有一个香草的数组,需要按照类型(一年,二年,多年)来将植物分类.所以需要提供三个集合.
```
```java
        //Using ordinal() to index an array --- don't Do This
        Herb [] garder = ... ;
        Set< Herb > [] herbsByType = (Set<Herb >[] ) new Set[Herb.Type.values().length];
        for(int i = 0; i<herbsByType.length;i++){
            herbsByType[i]=new HashSet< Herb >();
        }
        for( Herb h : garden){
            herbsByType[h.getType().ordinal()].add(h);// Distrubte Herb by year
        }   
```
Note:上面程序中使用ordinal()来控制下标,隐藏许多问题
```
1. 数组不能与泛型兼容(25),程序需要进行未受检的转换,所以会有警告出现
```
```
2. 最严重的问题是:当你使用枚举的序数进行索引的数组时,务必小心处理正确的int值;int不能提供枚举的类型安全,如果使用错误的值,则很难发现.
```

#######处理问题方法
```
数组其实充当的是:从枚举到值的映射,因此Map是最合适的.
```
```
java.util.EnumMap是非常快速的Map实现专门用于枚举键的.
```
```java
//Using an EnumMap to associate date with an enum
        Map<Herb.Type, Set<Herb>> herbsByType = 
            new EnumMap<Herb.Type, Set<Herb>>(Herb.Type.class);
        for(Herb.Type t : Herb.Type.values()){
            herbsByType.put(t, new HashSet<Herb>());
        }
        for(Herb b : gardern){
            herbsByType.get(b.getType()).add(b);
        }
```
Note:
```
1. EnumMap提供了高效的性能+安全类型保护,同时隐藏了底层实现细节
```
```
2. 注意一点是:EnumMap构造器采用了类型的Class对象,这是一个有限制的类型令牌(29),
```
#####枚举类型序数进行索引(两次)数组的数组
```
下面的程序使用一个数组将两个阶段映射到一个阶段的过渡(液体 --> 固体,固体 --> 气体)
```
```java
public enum Phase {
    //Using ordinal() to index array of array  -- DON'T DO THIS!
    SOLID,LIQUID,GAS;
    public enum Transition{
        MELT,FREEZE,BOIL,CONDENSE,SUBLIME,DEPOSIT;
        private static final Transition[][] TRANSITIONS = {
            { null, MELT,SUBLIME},
            {FREEZE,null,BOIL},
            {DEPOSIT,CONDENSE,null}
        };
        //Returns the phase transition from on phase to another
        public static Transition from(Phase src,Phase dst){
            return TRANSITIONS[src.ordinal()][dst.ordinal()];
        }
    }
}
```
Note:
```
程序初看感觉比较优雅,但事实并非如此.维护时,时刻记得这张二维表TRANSITIONS结构,编译器无法知道序数和数组索引之间的关系
```
#######解决办法:EnumMap
```
第一个map的键是枚举(起始阶段),值为另一个map.第二个map的键为第二个枚举(目标阶段),它的值为结果(阶段过渡).
也就是:Map(起始阶段,Map(目标阶段,阶段过渡))
```
```java
public enum Phase {
    //Using a nested EnumMap to associate date with enum parirs
    SOLID,LIQUID,GAS;
    public enum Transition{
        MELT(SOLID,LIQUID),
        FREEZE(LIQUID,SOLID),
        BOIL(LIQUID,GAS),
        CONDENSE(GAS,LIQUID),
        SUBLIME(SOLID,GAS),
        DEPOSIT(GAS,SOLID);
        private final Phase src;
        private final Phase dst;
        Transition(Phase src,Phase dst){
            this.src = src;
            this.dst = dst;
        }
        // Initialize the phase transition map
        private static final Map<Phase, Map<Phase,Transition>> m =
            new EnumMap<Phase, Map<Phase, Transition>>(Phase.class);
        static {
            for(Phase p: Phase.values()){
                m.put(p, new EnumMap<Phase,Transition>(Phase.class));
            }
            for(Transition trans : Transition.values()){
                m.get(trans.src).put(trans.dst,trans);
            }
        }
        public static Transition from(Phase src,Phase dst){
            return m.get(src).get(dst);
        }
    }
}
```
Note:
```
1. 静态初始化代码块的第一个循环初始化了外部map,得到了三个空的内容map.代码块中的第二个循环利用每个Transition中的每个状态得到具体的目标信息.
```
```
2. 如果现在想要增加一个新的阶段:Plasma(离子),需要给Phash添加一个新的常量(PLASMA,同时给Phase.Transition添加两种新常量(IONIZE(GAS,PLASMA)和DEIONIZE(PLASMA,GAS)添加到Phase.Transition列表.后一个类的设计,几乎不会有任何错误.
```

#####总结
```
不要使用序数来索引数组,而使用EnumMap.如果关系是多维的,使用EnumMap<...,EnumMap<...> >.
```
```
应用程序下,请不要使用Enum.ordinal,坚决杜绝(31)
```

###第34条:用接口模拟可伸缩的枚举
```
就几乎所有的方面,枚举类型都具有众多优势.但是有一个例外:枚举类型不能提供继承,也就是不可扩展.
```
```
有时候,为了让API的用户提供自己的操作,可以采用接口+枚举的方式.下面以第30条的Operation类型为例
```
```java
//Emulae extensible enum using an interface
public interface Operation{
	double apply(double x,double y);
}
public enum BasicOperation implements Operation{
    PLUS("+"){
        double apply(double x,double y){
            return x+y;
        }
    },
    MINUS("-"){
        double apply(double x,double y){
            return x-y;
        }
    },
    TIMES("*"){
        double apply(double x,double y){
            return x* y;
        }
    },
    DIVIDE("/"){
        double apply(double x,double y){
            return x/y;
        }
    };
    private final String symbol;
    Operation(String symbol){
        this.symbol = symbol;
    }
    @Override
    public String toString(){
        return symbol;
    }
}
```
Note:
```
虽然枚举类型不可扩展,但是接口可以提供扩展.如果想要定义另一个枚举类型,实现这个接口就好,并用新类型的实例代替基本类型.
```
#######扩展Operation操作类型,添加求幂(exponentiation)和求余(remainder)操作
```java
public enum ExtendedOperation implements IOperation{
    EXP("^"){
        public double apply(double x,double y){
            return Math.pow(x, y);
        }
    },
    REMAINDER("%"){
        public double apply(double x,double y){
            return x%y;
        }
    };
    private final String symbol;
    ExtendedOperation(String symbol){
        this.symbol = symbol;
    }
    @Override
    public String toString(){
        return symbol;
    }
}
```
Note:
```
只要被写成采用接口类型(Operation)而非实现(BasicOperation).新的枚举类型都可以正常使用.
```
#######客户端如何使用声明的ExtendedOperation枚举,方法1
```
可以在任何需要BasicOpertion枚举的地方单独传递一个ExtendedOperation枚举实例,而且还能传递完整的ExtendedOperation枚举类型
```
```java
public static void main(String args[]) throws Exception {
        double x = Double.parseDouble(args[0]);
        double y = Double.parseDouble(args[1]);
        test(ExtendedOperation.class , x,y);
    }
    private static<T extends Enum<T> & Operation> void test(Class<T> opSet,double x,double y){
        for(Operation op : opSet.getEnumConstants()){
            System.out.printf("%f %s %f = %f%n",x,op,y,op.apply(x, y));
        }
    }
```
Note:
```
使用了有限制的类型令牌(29),确保Class对象既表示枚举又是Operation的子类型(T extends Enum<T> & Operation)
```
#######客户端如何使用声明的ExtendedOperation枚举,方法2
```
使用Collection< ? extends Operation >,这是个有限制的通配符类型(28)
```
```java
    public static void main(String args[]) throws Exception {
        double x = Double.parseDouble(args[0]);
        double y = Double.parseDouble(args[1]);
        test(Arrays.asList(ExtendedOperation.values()) , x,y);
    }
    private static void test(Collection<? extends IOperation> opSet,double x,double y){
        for(IOperation op : opSet){
            System.out.printf("%f %s %f = %f%n",x,op,y,op.apply(x, y));
        }
    }
```

#####总结
```
1. 使用接口,弥补了无法实现一个枚举类型继承到另一个枚举类型的小小不足.允许用户自定义枚举类型处理逻辑
```
```
2. 上例中BasicOperation和ExtendsOperation中,关联的逻辑代码如果共享功能比较多,可以考虑封装到一个辅助类或静态辅助方法中.
```

###第35条:注解优先于命名模式
|注解|解释|
|:---:|:---:|
|@Retention(RetentionPolicy.RUNTIME)|注解应该在运行时保留|
|@Target(ElementType.TYPE)|注解适用于类|
|@Target(ElementType.FIELD)|注解使用域|
|@Target(ElementType.METHOD)|注解使用方法|

#####命令模式
```
比如JUnit测试框架,原本一定要用test作为测试方法名称的开头.优缺点也不用管了,直接完全废除.
```
#####注解
#######Test注解类型
```java
//Marker annotation type declaration
/**
* Indicates that the annotated method is a test method
* Use only on parameterless static methods
*
*/
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Test{

}
```
Note:
```
1. Retention和Target注解被称作元注解
```
```
2. @Retention(RetentionPolicy.RUNTIME)元注解表明,Test注解应该在运行时保留.
```
```
3. @Target(ElementType.METHOD)元注解表明,Test注解只在方法声明中才是合法的.
```
```
4. Test注解只能用于无参的静态方法
```
#######现实中应用Test注解,称为标记注解
```java
public class Sample{
	@Test
    public static void m1(){  }
    public static void m2(){ }
    @Test
    public static void m3(){ 
    	throw new RuntimeException("Boom");
    }
    public static void m4(){}
    @Test
    public void m5(){ }
    public static void m6(){ }
    @Test
    public static void m7(){
    	throw new RuntimeException("Crash");
    }
    public static void m8(){    }
}
```
Note:
```
4个方法注解为测试:m1,m3,m5,m7
m1方法:正常通过
m3,m7方法中抛出异常
m5方法因为实例方法(非static),注解无效使用
```
#######简单的测试运行类
```
注解永远不会改变被注解代码的语义
```
```java
public class RunTests {
    public static void main(String [] args) throws Exception{
        int tests = 0;
        int passed = 0;
        Class<?> testClass = Class.forName("vlis.Sample");
        for(Method m : testClass.getDeclaredMethods()){
            if(m.isAnnotationPresent(Test.class)){
                tests++;
                try{
                    m.invoke(null);
                    passed++;
                }catch(InvocationTargetException wrappedExc){
                    Throwable exc = wrappedExc.getCause();
                    System.out.println(m+" failed: "+exc.getMessage());
                }catch(Exception exc){
                    System.out.println("INVALID @Test: " +m);
                }
            }
        }
        System.out.printf("Passed: %d, Failed: %d%n", passed,tests-passed);
    }
}
```
Note:
```
1. 利用Method.invoke反射方法运行Test方法
```
```
2. isAnnotationPresent方法告知该工具运行哪些方法
```
```
3. 异常类InvocationTargetException来捕捉测试方法抛出异常和反射机制
```

#####新的注解类型:异常注解
```
为在抛出特殊异常时才成功的测试添加支持,声明一个性的注解类型
```
```java
/**
 * Indicates that the annotated method is a test method that
 * must throw the designated exception to succeed.
 * */
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface ExceptionTest {
    Class<? extends Exception > value();
}
```
Note:
```
这个注解的参数类型是:Class< ? extends Exception>.这个有限制的类型令牌(29)的意思是:某个扩展Exception的类的Class对象.
```
#######实际中应用这个注解+测试用例
```java
public class Sample2 {
    //Program containing annotations with a parameter
    @ExceptionTest(ArithmeticException.class)
    public static void m1(){//Test should pass
        int i = 0;
        i = i/i;
    }
    @ExceptionTest(ArithmeticException.class)
    public static void m2(){//Should fail(wrong exception)
        int [] a = new int[0];
        int i = a[1];
    }
    @ExceptionTest(ArithmeticException.class)
    public static void m3(){//Should fail (no exception)
    }
}
```
```java
public class RunTest2 {
    public static void main(String [] args) throws Exception{
        int tests = 0;
        int passed = 0;
        Class<?> testClass = Class.forName("vlis.Sample");
        for(Method m : testClass.getDeclaredMethods()){
            if(m.isAnnotationPresent(ExceptionTest.class)){
                tests++;
                try{
                    m.invoke(null);
                    System.out.printf("Test %s failed: no exception%n",m);
                }catch(InvocationTargetException wrappedExc){
                    Throwable exc = wrappedExc.getCause();
                    Class<? extends Exception> excType = 
                        m.getAnnotation(ExceptionTest.class).value();
                   if(excType.isInstance(exc)){
                       passed++;
                   }else{
                       System.out.printf("Test %s failed: expected %s,got %s%n", m,excType.getName(),exc.getMessage());
                   }
                }catch(Exception exc){
                    System.out.println("INVALID @Test: " +m);
                }
            }
        }
        System.out.printf("Passed: %d, Failed: %d%n", passed,tests-passed);
    }
}
```

#####ExceptionTest注解的参数类型改成Class对象数组
```
测试可以在抛出任何一个指定异常时都得到通过
```
```java
//Annotation type with an array parameter
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface ExceptionTest3 {
    Class<? extends Exception > [] value();
}
```
Note:
```
注解中数组参数的语法十分灵活.为了指定多元素数组,要用花括号({})将元素包围起来,并用都好(,)隔开.如果想使用单元素,和上面的写法一致
```
#######使用
```java
@ExceptionTest3({IndexOutOfBoundsException.class,NullPointerException.class})
public static void doublyBad(){
	List<String> list = new ArrayList<String>();
    //The spec permits this method to throw either
    //IndexOutOfBoundsException or NullPointerException
    list.addAll(5,null);
}
```
#########客户端测试
```java
public class RunTest3 {
    public static void main(String [] args) throws Exception{
        int tests = 0;
        int passed = 0;
        Class<?> testClass = Class.forName("vlis.Sample");
        for(Method m : testClass.getDeclaredMethods()){
            if(m.isAnnotationPresent(ExceptionTest3.class)){
                tests++;
                try{
                    m.invoke(null);
                    System.out.printf("Test %s failed: no exception%n",m);
                }catch(InvocationTargetException wrappedExc){
                    Throwable exc = wrappedExc.getCause();
                    Class<? extends Exception > []  excTypes = 
                        m.getAnnotation(ExceptionTest3.class).value();
                    int oldPassed = passed;
                    for(Class< ? extends Exception> excType: excTypes){
                        if(excType.isInstance(exc)){
                            passed++;
                            break;
                        }
                    }
                    if (passed == oldPassed) {
                        System.out.printf("Test %s failed: %s%n", m,
                            exc.getMessage());
                    }
                }catch(Exception exc){
                    System.out.println("INVALID @Test: " +m);
                }
            }
        }
        System.out.printf("Passed: %d, Failed: %d%n", passed,tests-passed);
    }
}

```

#####总结
```
1. 本条目示范了注解的优越性.既然有了注解,完全没有理由再使用命名模式
```
```
2. 一般来书,大多数程序员都不必要定义注解类型,但是所有的程序员都应该使用Java平台提供的预定义的注解类型(36,24)
```

###第36条:坚持使用Override注解
```
Override注解只能在方法声明中,表示被注解的方法声明覆盖了超类型中的一个声明.
```
```
Override注解能防止一大类的非法错误.比如:类Bigram表示一个双字母组或者有序的字母对.
```
```java
public class Bigram {
    //there is a bug
    private final char first;
    private final char second;
    public Bigram(char first,char second){
        this.first = first;
        this.second = second;
    }
    public boolean equals(Bigram b){
        return b.first == first && b.second == second;
    }
    public int hashCode(){
        return 31*first + second;
    }
    public static void main(String [] args){
        Set<Bigram> s = new HashSet<Bigram>();
        for(int i =0;i<10;i++){
            for(char ch = 'a';ch <='z';ch++){
                s.add(new Bigram(ch,ch));
            }
        }
        System.out.println("size : "+s.size());
    }
}
```
Note:
```
1. Question:输入内容是260,而不是我们期望26.
```
```
2. 问题在于:Bigram类的创建者原本想要覆盖equals方法(8),同时还记得覆盖hashCode.但却把equals方法的参数写成了Bigram类,导致了重载(41),而非覆盖.
```
```
3. 因此,Bigram从Object继承了equals方法,而默认的equals方法测试对象的同一性,也就是是否是同一个对象,就像==操作符一样.
```

#######加上@Override标注的Bigram.equals结果
```java
@Override
public boolean equals(Bigram b){
	return b.first == first && b.second == second;
}
```
Note:
```
如果加上这个@Override注解,编译器将会帮你检查,会报错提醒
```
#######那么,Bigram类中应该怎么写equals方法(8)
```java
@Override
public boolean equals(Object o){
	if(!(o instanceof Bigram)){
    	return false;
    }
    Bigram bigram = (Bigram) o;
    return b.first == first && b.second == second;
}
```
#######特殊情况
```
编写一个继承抽象类,可不必将Override注解放在该方法上.因为编译器会提醒覆盖超类的方法.
```

#####总结
```
1. 坚持使用Override注解,可以提醒你无意识的覆盖或者无意识覆盖不成功.
```
```
2. 只有一个特例:在具体的类中,不必标注你确信覆盖了抽象方法声明的方法.
```

###第37条:用标记接口定义类型
#####标记接口
```
标记接口是没有包含方法声明的接口,只是标明一个类实现了具有某种属性的接口.比如:Serializable接口(11),实现这个接口,表明它的实例可以被写到ObjectOutputStream("被序列化")
```
#####标记接口与标记注解比较(35)
#######标记接口优点
```
1. 标记接口定义的类型是由被标记类的实例实现的;标记注解则没有定义这样的类型
```
```
2. 它们可以被更加精确地进行锁定.

Note : 如果一个注解类型利用@Target(ElementType.TYPE)声明,它就可以被应用到任何类或者接口.假设有一个标记只适用于特殊接口的实现,如果将它定义成一个标记接口,就可以用它将唯一的接口扩展成它适用的接口.
```
#######标记注解优点
```
1. 可以通过默认的方式添加一个或者多个注解类型元素,给已被使用的注解类型添加更多的信息,因此标记注解类型会慢慢演变成丰富的注解类型.这种演变对于标记接口是不可能的.因为通常不可能在实现接口后再添加方法(18)
```
```
2. 标记注解在那些支持注解作为编程元素之一的框架中具有一致性,是属于注解机制的一部分.
```

#####标记接口与标记注解选择
```
1. 如果标记是应用到任何程序元素而不是类或者接口,就必须使用注解,因为标记接口只能用于类和接口
```
```
2. 如果标记只用于给类和接口,且编写一个或多个只接受有这种标记的方法(第一个条件),就应该使用标记接口而非注解.这样你就可以用接口作为相关方法的参数类型.
```
```
3. 第二个条件:如果第一个条件是否定的,那么要问问自己:是否要永远限制这个标记只用于特殊接口的元素?如果是,最好将标记定义成该接口的一个子接口.
```
```
4. 如果第一,第二条件都不满足,或许应该使用标记注解
```

#####总结:
```
1. 如果想要定义一个任何新方法都不会与之关联的类型,标记接口是最好的选择.
```
```
2. 如果想要标记程序元素而非类和接口,考虑到未来可能要给标记添加更多的信息,或者标记要适合于已经广泛使用注解类型的框架.那么请选择标记注解
```









