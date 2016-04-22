#第6章:枚举和注解
```
本章目的:讨论使用新的类型:枚举类型+注解类型
```

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











