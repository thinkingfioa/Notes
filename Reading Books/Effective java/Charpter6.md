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




































