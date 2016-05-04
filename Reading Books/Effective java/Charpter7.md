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










