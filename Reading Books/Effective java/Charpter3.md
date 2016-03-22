#第3章 : 对于所有的对象都通用的方法
[TOC]
>Note:主要讨论类Object中非final的方法(eg: equals(),hasCode(),toString(),clone())

##第8条:覆盖equals时遵守的通用约定
>Note:类Object中缺省的equals()方法,是判断类的每个实例是否与自身相等,也就是说,堆中是否是同一个对象实例
```java
public Client{
	public static void main(String [] args){
    	Object obj = new Father();
        Father fa = (Father)obj;
        if(fa.equals(obj)){
        	//其实两个是同一个实例,所有一定是true
        	System.out.println("thinking_fioa");
        }
    }
}
```

#### 下面的情况,可以直接使用缺省的equals()
 - 类的每个实例本质上都是唯一的.比如:Thread.代表的是活动的实体
 - 不关心类是否提供"逻辑相等"的测试功能
 - 超类已经覆盖了equals()方法,也是符合的子类逻辑比如:AbstractSet类
 - 类是私有的或是包级私有的,可以确定的是它的equals方法永远不会被调用,所以应该覆盖equals()方法,并抛出异常

#### 下面情况:重新覆盖Object.equals()方法
>Note:当发现,类应该有自己独特的"逻辑相等"的概念,应该覆盖。相等的含义不仅仅表示两个引用是同一个对象.
>举例:当Integer或者Date作为映射表(map)的的键(key),或者集合(set)的元素时,要小心处理这里所谓的equals()方法

#### 覆盖equals()方法是,必须做到以下几点
 - 自反性: x.equals(x)应该返回为true
 - 对称性: 任何非null的应用值x和y,当且仅当y.equals(x) 返回true时,x.equals(x)也必须返回true
 - 传递性: x.equals(y) ---> return true, y.equals(z) ---> return true, x.equals(z)也应该return true;
 - 一致性: 多次执行x.equals(z)时,结果必须一样的.
>Note: x是非 null ,则 x.equals(null) 必须 return false;

#### 依次举例说明重要性
 1. **对称性重要性解释**
 - 用户想写一个类CaseInsensitiveString,这个类是一个忽略大小写的字符串

```java
 package vlis;

public final class CaseInsensitiveString {
    private final String s;
    public CaseInsensitiveString(String s){
        if(s == null){
            throw new NullPointerException();
        }
        this.s = s;
    }
    @Override
    public boolean equals(Object o){
    	//如果两个CaseInsensitiveString类的String相等,则是相等的
        if(o instanceof CaseInsensitiveString){
            return s.equalsIgnoreCase(((CaseInsensitiveString) o).s);
        }
        //如果想也同意CaseInsensitiveString和String相等
        if(o instanceof String){
            return s.equalsIgnoreCase((String)o);
        }
        return false;
    }
}
```
 - 一个重大的问题是:不满足对称性,也就是CaseInsensitiveString类可以判断也String相等,但是对称却不行.如果有
```java
List<CaseInsensitiveString> list = new ArrayList<CaseInsensitiveString>();
```
那么调用list.contains(s)返回的结果将不可预测.

 2. **传递性重要性**解释:传递性,要留意子类与父类之间的equals是否相等.
  - 子类增加新的域,影响到equals的比较结果
```java
package vlis;
//父类点:Point
public class Point {
    private final int x;
    private final int y;
    public Point(int x,int y){
        this.x = x;
        this.y = y;
    }
    @Override
    public boolean equals(Object o){
        if(o instanceof Point){
            Point point = (Point)o;
            return (point.x == this.x) && (point.y == this.y);
        }
        return false;
    }
}
package vlis;
public class ColorPoint extends Point{
    //为Point点添加属性:Color,代表颜色。但我们应该铭记:复合方式优先与继承,这里最好采用复合方式
    private final Color color;
    public ColorPoint(int x,int y,Color color){
        super(x,y);
        this.color = color;
        @Override
        public boolean equals(Object o){
            if(!(o instanceof ColorPoint)){
                return false;
            }
            return super.equals(o) && (((ColorPoint) o).color == this.color);
        }
       // ...//Remainder omitted
    }
}
```
>Note:
> - 我们发现以下代码,将有逻辑失去对称性,point.equals(cp) --> return true;而cp.equals(point) --> return false;
```java
Point point = new Point(1,2);
ColorPoint cp = new ColorPoint(1,2,Color.RED);
```
> - 如果将ColorPoint中的方法equals(Object o)改成以下的,会失去传递性,p1.equals(p2)  --> reture ture; 且 p2.equals(p3)  --> reture ture;而p1.equals(p3)  --> reture false;
> ```java
>  public boolean equals(Object o){
            if(!(o instanceof Point)){ // 如果想非常限定类Class,可以使用getClass()来判断.getClass()请参考反射笔记
                return false;
            }
            if(!(o instanceof ColorPoint)){
                return o.equals(this)
            }
            return super.equals(o) && (((ColorPoint) o).color == this.color);
        }
> ```
> ```java
>         ColorPoint p1 = new ColorPoint(1,2,Color.RED);
            Point p2 = new Point(1,2);
            ColorPoint p3 = new ColorPoint(1,2,Color.BLUE);
> ```

#### 如何编写高质量的equals方法
 - 使用"\=="操作符检查"参数是否为这个对象的应用","=="是一种性能优化手段
 - 使用instanceof操作符检查"参数是否为正确的类型"
 - 把参数转换成正确的类型,也就是强转类型
 - 编写完成equals方法后,检查是否符合标准:对称,传递,一致

#### 书写equals方法时,注意以下几点
 - 覆盖equals时总要覆盖hashCode(参考第9条)
 - 不要企图让 equals 过于智能
 - 不要将equals声明中的Object换成其他类型,否则,会出现很隐蔽的bug.以下代码就是**错误**的:
```java
public boolean equals(MyClass o){
	...
}
```

##第9条:覆盖equals时总要覆盖hashCode
Note: **在每个覆盖了equals方法的类中,也必须覆盖hashCode方法**,hashCode方法将会让该类结合所有基于散列的集合一起正常运作,eg:HashMap,HashSet,HashTable;

#### Object规范,规定:
1. 应用程序多次调用同一对象的hashCode方法,必须始终返回同一个整数
2. 如果两个对象的equals方法return true;则hashCode方法必须返回同样的整数结果
3. 尽量为不同的对象产生不相等的散列码

#### 例子说明
###### 覆写了equals(...)方法,并将PhoneNumber类作为key,发现两个equals()返回true时,Map并不承认.

```java
package vlis;

public class PhoneNumber {
    private final int areaCode;
    private final int prefix;
    private final int lineNumber;
    public PhoneNumber(int areaCode,int prefix ,int lineNumber){
        rangeCheck(areaCode,999,"area code");
        rangeCheck(prefix,999,"prefix");
        rangeCheck(lineNumber,9999,"line number");
        this.areaCode = areaCode;
        this.prefix = prefix;
        this.lineNumber =lineNumber;
    }
    private static void rangeCheck(int arg,int max,String name){
        if(arg <0 && arg > max){
            throw new IllegalArgumentException(name +":"+arg);
        }
    }
    @Override
    public boolean equals(Object o){
        if( o == this){
            return true;
        }
        if(!(o instanceof PhoneNumber)){
            return false;
        }
        PhoneNumber pn = (PhoneNumber)o;
        return pn.lineNumber == this.lineNumber && pn.areaCode == this.areaCode && pn.prefix == this.prefix;

        // no hashCode method
    }
}
```
```java
Map<PhoneNumber,String> m = new HashMap<PhoneNumber,String>() ;
m.put(new PhoneNumber(707,867,5390),"Jenny")
```
如果客户端调用:`m.get(new PhoneNumber(707,867,5390)`,得到的却是:null,并**没有得到期望的"Jenny"**,**原因**:没有覆写方法:hashCode方法.

1. 简单的书写hashCode方法的准则:
>
> 1. 把某个非零常数值，比如说17，保存在一个叫result的int类型的变量中。
> 2. 对于对象中每一个关键域f（指equals方法中考虑的每一个域），完成以下步骤：
>   a. 为该域计算int类型的散列码c：
>  	 - i. 如果该域是boolean类型，则计算(f ? 0 : 1)。
> 	 - ii. 如果该域是byte、char、short或者int类型，则计算(int)f。
>  	 - iii. 如果该域是long类型，则计算(int)(f^(f>>>32))。
>  	 - iv. 如果该域是float类型，则计算Float.floatToIntBits(f)。
>  	 - v.   如果该域是double类型，则计算Double.doubleToLongBits(f)得到一个long类型的值，然后  按照步骤2.a.iii，对该long型值计算散列值。
>  	 - vi.如果该域是一个对象引用，并且该类的equals方法通过递归调用equals的方式来比较这个域，则同样对这个域递归调用hashCode。如果要求一个更为复杂的比较，则为这个域计算一个“规范表示（canonical representation）”，然后针对这个范式表示调用hashCode。如果这个域的值为null,则返回0（或者其他某个常数，但习惯上使用0）。
>  	 - vii.   如果该域是一个数组，则把每一个元素当做单独的域来处理。也就是说，递归地应用上述规则，对每个重要的元素计算一个散列码，然后根据步骤2.b中的做法把这些散列值组合起来.
>  	 
>    b.按照下面的公式，把步骤a中计算得到的散列码c组合到result中：result   =result*37+c

2. 根据hashCode书写准则,为类PhoneNumber覆写hashCode方法
```java
@Override
public int hashCode(){
	int result = 17;
    result = (result<<5) -result + areaCode;//(result<<5 -i)等同于:result*31,但速度更快
    result = result*31 + prefix;
    result = result*31 + lineNumber;
    return result;
}
```
3. 书写hashCode方法,注意以下几点
 - 排除equals方法中比较计算没有用到的任何域;
 - 如果一个类是不可变的,考虑把hashCode()方法的返回值,保存起来.
 - 不要试图从散列码计算中排除掉一个对象关键部分来提高性能

##第10条:  建议始终要覆盖toString
####下类情况toString会被自动调用
 - 对象被传递给println,printf,字符串联操作符(+)
 - assert或者被调试器打印出来

####建议:
 - 可以指定toString方法返回值的格式,并且最好再提供一个相匹配的静态工厂方法或构造器,方便程序员在对象与字符串表示法之间来回转换
 - 无论是否指定格式,也就是是否提供相匹配的静态工厂方法或构造器.都应该为返回值中包含的所有信息,提供一种编程式的访问途径.方便程序员从返回值中得到关键属性.

##第11条:谨慎地覆盖clone : 无需调用构造器就可以创建对象
>Cloneable接口的目的是作为对象的一个mixin接口(mixin interface),表明这样的对象允许克隆.

####本条目的:本条目告诉你如何实现一个行为良好的clone方法,并讨论何时适合这样做,并讨论其他的可替代做法.

##### 使用clone方法,需要考虑以下点:

- 一个类实现了Cloneable,Object的clone方法才会返回该对象的**逐域拷贝**,否则就会抛出:CloneNotSupportedException.也就是说:想调用Object中的clone方法,必须实现Cloneable.
- 注意<1>: clone返回是它的类的一个新实例,并不是一个新的引用,所以`x.clone()!= x  --> return true;
>类PhoneNumber重新覆写clone方法
```java
@Override
public PhoneNumber clone(){
	try{
    	(PhoneNumber)super.clone();
    }catch(CloneNotSupportedException e){
    	throw new AssertionError();//can't clone
    }
}
```
>Remark:clone()方法返回的就是PhoneNumber类了,也就是我们所期待的.
- 注意<2>:如果对象中包含的域引用了可变的对象,使用上面简单的clone实现可能会发生灾难.应该使用**深度拷贝**
>举例说明:

```java
package vlis;

public class PhoneNumber implements Cloneable {
    private final int areaCode;
    private final int prefix;
    private final int lineNumber;
    private Son son=new Son();
    public PhoneNumber(int areaCode,int prefix ,int lineNumber){
        rangeCheck(areaCode,999,"area code");
        rangeCheck(prefix,999,"prefix");
        rangeCheck(lineNumber,9999,"line number");
        this.areaCode = areaCode;
        this.prefix = prefix;
        this.lineNumber =lineNumber;
    }
    public Son getSon(){
        return this.son;
    }
    public int getIineNumber(){
        return this.lineNumber;
    }
    private static void rangeCheck(int arg,int max,String name){
        if(arg <0 && arg > max){
            throw new IllegalArgumentException(name +":"+arg);
        }
    }
    @Override
    public boolean equals(Object o){
        if( o == this){
            return true;
        }
        if(!(o instanceof PhoneNumber)){
            return false;
        }
        PhoneNumber pn = (PhoneNumber)o;
        return pn.lineNumber == this.lineNumber && pn.areaCode == this.areaCode && pn.prefix == this.prefix;
    }
    @Override
    public PhoneNumber clone(){
        try{
           return (PhoneNumber)super.clone();
        }catch(CloneNotSupportedException e){
            throw new AssertionError();
        }
    }
}
```
**Remark:**类PhoneNumber有一个域:son对象,但只是一个引用,客户端调用如下代码,会发现pn中的son与pn1中的son其实是一个对象实例,修改原始的实例会破坏被克隆对象.这是不能容忍的.必须注意:clone方法,就是另一个构造器,必须与原来的对象保持独立.
```java
//clone后的对象并不是一个新的实例
          PhoneNumber pn = new PhoneNumber(88,88,8888);
          System.out.println("thinking_fioa -111->" + pn.getSon().getName());
          PhoneNumber pn1 = pn.clone();
          System.out.println("thinking_fioa -222->" + pn1.getSon().getName());
          pn1.getSon().setName("luweilin");
          System.out.println("thinking_fioa -333->" + pn.getSon().getName());
```
**Remark:**解决办法,请参考以下的代码(提醒:独立写自己的Stack或则List类的时候,一定要特别留意复制不到位,没有进行**深度拷贝**问题,可以参考:java.lang.Hashtable类中的clone方法)
```java
//将类PhoneNumber中的clone改成
@Override
    public PhoneNumber clone(){
        try{
           PhoneNumber pn = (PhoneNumber)super.clone();
           pn.setSon(son.clone());
           return pn;
        }catch(CloneNotSupportedException e){
            throw new AssertionError();
        }
    }
//在类Son中添加clone方法,实现接口Cloneable
@Override
    public Son clone(){
        try{
            return (Son)super.clone();
        }catch(CloneNotSupportedException e){
            throw new AssertionError();
        }
    }
```
- 总结:
 - (1) 实现Cloneable接口的类都应该用一个公共的方法覆盖clone.此方法首先调用super.clone,然后再修正任何需要修正的域(**深度拷贝**).
 - (2) 如果专门为继承而设计的类覆盖了clone方法,应该被声明为protected,且抛出CloneNotSupportedException异常,也不应该实现Cloneable接口


##### 利用**拷贝构造器或拷贝工厂** 来实现对象拷贝(比Cloneable/clone方法具有更多优势)
>这个方法相比Cloneable/clone方法具有很多优势,一般,拷贝构造器或者拷贝工厂可以带一个参数,参数类型是通过该类实现的接口.
```java
public HashSet(Collection<? extends E> c) {
        map = new HashMap<>(Math.max((int) (c.size()/.75f) + 1, 16));
        addAll(c);
    }
```

##第12条:考虑实现Comparable接口:compareTo方法位于Comparable接口中
- 使用场景:如果一个类的实例,具有**内在的排序关系**,就应该实现Comparable接口
```java
//为一个实现接口Comparable的类数组a,进行排序
Arrays.sort(a);
```
- CompareTo方法的通用约定:与equals方法一样,对称性,传递性,与equals保持一致性
- 违反comapareTo约定的类,会破坏其他依赖与比较关系的类,eg:TreeSet,TreeMap,Collections,Arrays,这些类内部都有搜索和排序算法.
- Comparable通用规定中:与equals保持一致.并不是强求的.如果不是一致的,最好说明下.举例:BigDecimal类中,Comparable方法与equals方法就不是一致的,new BigDecimal(1.0)与new BigDecimal(1.00),在Comparable方法上应该 return true;但在equals方法上,return false;所以对于TreeSet来说,只有一个对象.对于Map时,有两个对象.

#####使用Comparable方法准则:

 - 如果比较的不是同一个对象,throw new ClassCastException
 - 如果比较两个非常相近的类,建议使用包含关系处理
 - 方法Comparable的参数,不要写成Object,无需进行转换,请写具体的类.
 - 如果一个域并没有实现Comparable接口,可以使用一个Comparator来代替
```java
//为上面的类:CaseInsensitiveString添加Comparable方法
public final class CaseInsensitiveString implements Comparable<CaseInsensitiveString>{
	public int compareTo(CaseInsensitiveString cis){
    	return Sting.CASE_INSENSITIVE_ORDER.compare(this.s,cis);
    }
}
```
>**Remake:**
>1. `implements Comparable<CaseInsensitiveString>`指定Comparable方法只能用于CaseInsensitiveString类的比较.
>2. CompareTo(...)的参数是:CaseInsensitiveString,**不要写成Object**
>3. Sting.CASE_INSENSITIVE_ORDER.compare(this.s,cis);利用String中提供的Comparator比较器


