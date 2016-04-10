#第5章：泛型
[TOC]
```
泛型可以告诉编译器每个集合中接受哪些对象类型，编译器自动为你的插入进行转化。没有泛型之前，从集合中读取到的每个对象都需要手动强转。
```
```
本章目的：最大的限度的使用泛型的优势，使整个过程尽可能地简单化。
```
###术语
|术语|示例|所在条目|
|:---:|:---:|:---:|
|参数化的类型|List< String >|23|
|实际类型参数|String|23|
|泛型|List< E >|23,26|
|形式化类型参数|E|23|
|无限制通配符类型|List< ? >|23|
|原生态类型|List|23|
|有限制类型参数|< E extends Number>|26|
|递归类型限制|< T extends Comparable< T > >|27|
|有限制通配符类型|List< ? extends Number >|28|
|泛型方法|static < E > List< E > asList(E() a)|27|
|类型令牌|String.class|29|

###第23条：请不要在新代码中使用原生态类型
```
声明中具有一个或者多个类型参数的类或者接口，就是泛型类或接口。eg:List<E>
```
```
每个泛型都定义一个原生态类型(eg:List),Java的设计者允许使用它们，完全为了提供兼容性。
```
#####原生态类型的危害
```
出错并不能立即发现，直到运行代码到具体对象是才会抛出异常。程序员应该要尽量让所有的错误在编译时就发现
```
- 举例
 ```java
  //Now a raw collection type  -- don't do this
  private final Collection stamps = ...;
  // i can add other class instance to it ,there are not warning or default
  stamps.add(new Coin(...));
 ```
Note:可以将对象实例new Coin()放入到stamps集合中，编译和运行都不会出现任何问题，直到从stamp集合中取coin时才会抛出:Throws ClassCastException异常。

#####使用泛型优势
```
1. 如上例所示，使用泛型，将会在编译时，就能定位代码错误。
```
```
2. 保证类型安全。从集合中删除元素时，不再需要进行手工强转。而原生态类型需要手动强转Class类型
```
- 举例:
```java
//for loop with parameterized iterator declaration - typesafe
for(Iterator<Stram> i = stamps.iteerator();i.hasNext();){
	Stamp s = i.next(); // 无需转换
    ...//Do something with the stamp
}
```

#####原生态类型List和参数化的类型List< Object >比较
```
1. 前者逃避了泛型检查，后者则明确告知编译器，能够持有任意类型的对象。比如:你能将 List<String>传递给类型List的参数，但是不能传给类型为List<Object>的参数。
```
```
2. 泛型有子类型化的规则，List<String>是原生态类型List的一个子类型，而不是参数化类型List<Object>的子类型(25).因此，使用原生态类型，会失掉类型安全性，但是List<Object>则不会。
```
- 举例():
```java
public class RawType {
    //Uses raw type (List) -- fails at runtime
    public static void main(String [] args){
        List<String> strings = new ArrayList<String>();
        unsafeAdd(strings,new Integer(42));
        String s = strings.get(0);
    }
    private static void unsafeAdd(List list,Object o){
        list.add(o);
        return;
    }
}
```
Note:这段代码会有警告，但却可以编译过，直到运行是才会抛出错误。如果将函数写成下面的，则在编译时候就会发现问题。
```java
private static void unsafeAdd（List <Object> list,Object o){
	list.add(o);
    return ;
}
```

#####无限制的通配符类型(List< ? >)
```
在不确定或者不关心实际的类型参数时，可以使用一个问号来使用泛型。不要使用原生态类型，非常危险。
```
- 举例：
```java
//Unbounded wildcard type -- typesafe and flexible
static int numElementsInCommon(Set< ? > s1,Set< ? > s2){
	int result = 0;
    for(Object o1 : s1){
    	if(s2.contains(o1)){
        	result++;
        }
    }
    return result;
}
```

#####原生态类型(List)与无限制的通配符类型(List< ? >)比较
```
1. 无限制通配类型Set< ? >是类型安全的，而原生态类型List则不安全
```
```
2. 可以将任何元素放进原生态类型的集合中，破坏该集合的类型的安全性。但是不能将任何元素放到Collection< ? >中，编译出错。
```
```
3. 如果你无法将任何元素放进Collection< ? >中，而且根本无法猜测你会得到哪种类型的对象。要是无法接收这些条件，可以使用泛型方法(27),或者有限制的通配符类型(28).
```

#####使用原生态类型的两种特殊情况
```
必须明确的是：在代码中，请不要使用原生态类型。但有以下两种特殊情况，都是源于"泛型信息可以在运行时擦除(25)"
```
```
1. 类文字中必须使用原生态类型。eg: List.class和String[].class都是合法的，但是 List< String >.class则是不合法的。
```
```
2. 与instanceof操作符有关。泛型信息在运行时被擦除，因此在参数化类型而非无限制通配符上使用instanceof操作符是非法的。但使用无限制通配符显得多
```
- 举例:
```java
//Legitimate use of raw type - instanceof operator
if(o instanceof Set){
	Set< ? > m = (Set< ? >)o;//转成参数化类型或者原生态类型
}
```

#####总结
```
1. 原生态类型容易出错，不能保证类型安全，请不要使用，除了上面两个特殊情况。
```
```
2. Set< Object >是个参数化类型，表示可以包含任何对象类型的一个集合，提供安全性。
3. Set< ? >则是一个通配符类型，只能包含某种未知对象类型的一个集合，提供安全性。
4. Set是个原生态类型，脱离了泛型系统，不安全性。
```

###第24条：消除非受检警告
#####本条目目的:
```
尽可能消除每一个非受检警告。因为消除了所有的警告，就可以确保代码类型安全。
```
#####@SuppressWarnings("unchecked")的使用
```
如果无法消除警告,同时可以证明引起警告的代码是类型安全的.使用@SuppressWarnings("unchecked")注解来禁止这条警告.
```
#######使用注意事项
```
1. SuppressWarnings注解可以用在任何粒度的级别中,从单独的局部变量声明到整个类都可以.
```
```
2. 应该始终在尽可能小的范围中使用SuppressWarnings注解.通常可以是个变量声明,或是非常简短的方法或者构造器.请永远不要在整个类上使用SuppressWarnings,这样会掩盖许多重要的警告.
```
```
3. 如果不止一行的方法或者构造器中使用了SuppressWarnings注解,可以将它移到一个局部变量的声明中.
```
- 举例:

```java
// have warning code
public <T> T[] toArray(T [] a){
	if(a.length < size){
    	return (T []) Arrays.copyOf(elements,size,a.getClass());
    }
    System.arraycopy(elements,0,a,0,size);
    if(a.length > size){
    	a[size] = null;
    }
    return a;
}
```
Note:注解SupressWarnings放在return语句中是非法的.如果将注解放到整个方法上,在实践中千万不要这样做.应该采取声明一个局部变量:result.
```java
// no have warning code by adding local variable
public <T> T[] toArray(T [] a){
	if(a.length < size){
    	@SuppressWarnings("unchecked")
        T [] result = (T []) Arrays.copyOf(elements,size,a.getClass());
    	return result;
    }
    System.arraycopy(elements,0,a,0,size);
    if(a.length > size){
    	a[size] = null;
    }
    return a;
}
```
```
4. 每次使用SupressWarnings("unchecked")注解时,都要添加一条注释,详细讲解为什么这么做是安全的.可以帮助理解代码,避免错误.
```
#####总结
```
1. 非受检警告很重要,不要忽略它们,每条警告都可能出现ClassCastException异常.要尽最大努力消除警告
```
```
2. 无法消除非受检警告,在尽可能小的范围内,使用@SupressWarnings("unchecked")注解禁止该警告.并注释使用注解安全的原因.
```

###第25条:列表优先于数组
#####数组和泛型不同点
```
1. - 数组是协变的.意思是:如果Sub为Super的子类型,那么数组类型Sub[]是Super[]的子类型.
   - 泛型是不可变的,对于任意两个不同的类型Type1和 Type2,List<Type1>既不是List<Type2>的子类型,也不是List<Type2>的超类型.
```
- 举例:
```java
//Fails at runtime,can pass Compile
Object [] objectArray = new Long[1];
objectArray [0] = "I don't fit in"; //Throws ArrayStroeException at runtime.
```
```java
//Won't compile
List<Object> ol = new ArrayList<Long> (); // Incompatible types
ol.add("I don't fit in");
```

```
2. - 数组是具体化的.因此数组会在运行时才知道并检查它们的元素类型约束.所以,将String保存到Long [] 中,会在运行时才得到一个ArrayStoreException异常.
  - 类型是通过擦除来实现的.泛型只在编译时强化它们的类型信息,运行时丢弃(或擦除)它们的元素类型信息.擦除就是使泛型可以与没有使用泛型的代码随意进行互用(23)
```

#####数组和泛型不能混用使用
```
创建泛型,参数化类型或者类型参数的数组是非法的.eg:new List<E> ();因为它不是类型安全的
```
- 举例说明:
```java
// Why generic array creation is illegal -- won't compile!
List< String > [] stringLists = new List< String > [1];//(1)
List< Integer > intList = Arrays.asList(42);           //(2)
Object[] objects = stringLists;                        //(3)
objects[0] = intList;                                  //(4)
String s = stringList[0].get(0);                       //(5)
```

Note:
```
1. 假设第1行合法,创建一个泛型数组
2. 第2行创建并初始化一个包含单个元素的List< Integer >
3. 第3行将List< String > 数组保存到一个Object数组变量中,这是合法的,因为数组是协变的.
4. 将List< Integer >保存到Object数组里唯一的元素中,这是可以的,因为泛型是通过擦除实现的:List< Integer >实例的运行时类型只是List,List< String > [] 实例的运行时类型则是list[],因此这种安排不会出现ArrayStoreException异常.
5. 但是在第5行中,运行时出现ClassCastException异常.所以让编译器在第1行就编译不通过
```

#####创建无限制通配类型的数组讨论
```
不可具体化类型是指其运行时表示法包含的信息比它的编译时表示法包含的信息更少的类型.
```
```
无限制的通配符类型,如List< ? >和Map< ?,? >唯一可具体化的参数化类型.所以创建无限制通配类型的数组是合法的.
```
#######禁止创建泛型数组可能不太可行
```
1. 这表明泛型一般不可能返回它的元素类型数组(部分解决方案见29)
```
```
2. 这也意味着在结合使用可变参数(varargs)方法(42)和泛型时会出现令人费解的警告
```
#######当使用泛型数组创建错误时,处理方法
```
当得到泛型数组创建错误时,最好的解决方法通常是优先使用集合类型List< E >,而不是数组类型E[].
```
- 举例:

```java
// List-based generic reduction
static < E > E reduce(List< E > list, Funciton< E > f, E initVal){
 // init : 0 --> '+' , : 1 --> '*', :"" --> String.
	List< E > snapshot;
    synchronized(list){
    	snapshot = new ArrayList< E >(list);
    }
    E result = initVal;
    for( E e : snapshot){
    	result = f.apply(result,e);
    }
    return result;
}

interface Function< T > {
	T apply(T arg1,T arg2);
}
```
Note:这里只列出优秀代码,如上例所示.具体比较可以参考书本.

#####总结
```
1. 数组是协变且可以具体化的;泛型是不可变的且可以擦除的.
```
```
2. 一般来说,数组和泛型不能很好的混合使用.如果你将它们混合使用,且得到编译器的错误或警告,请考虑使用列表代替数组.
```

###第26条:优先考虑泛型
```
编写自己的泛型比较困难些,但是非常值得花时间去学习如何编写.
```
#####下面将以第6条中简单堆栈实现作为例子,利用泛型强化这个类
```java
public class Stack {
    //Object-based collection - a prime candidate for generics
    private Object[] elements;
    private int size = 0;
    private static final int DEFAULT_INITIAL_CAPACITY = 16;
    
    public Stack(){
        elements = new Object[DEFAULT_INITIAL_CAPACITY];
    }
    public void push(Object e){
        ensureCapacity();
        elements[size++]=e;
    }
    public Object pop(){
        if(size == 0){
            throw new EmptyStackException();
        }
        Object result = elements[--size];
        elements[size] = null;
        return result;
    }
    public boolean isEmpty(){
        return size == 0;
    }
    private void ensureCapacity(){
        if(elements.length == DEFAULT_INITIAL_CAPACITY){
            elements = Arrays.copyOf(elements, 2*size+1);
        }
    }
```
#####第1步:声明添加一个或者多个类型参数.这个例子中将栈中的元素类型写为:E(42)
```java
public class Stack<E> {
    //Initial attempt to generify Stack = won't compile
    private E[] elements;
    private int size = 0;
    private static final int DEFAULT_INITIAL_CAPACITY = 16;
    
    public Stack(){
        elements = new E[DEFAULT_INITIAL_CAPACITY];// won't compile
    }
    public void push(E e){
        ensureCapacity();
        elements[size++]=e;
    }
    public E pop(){
        if(size == 0){
            throw new EmptyStackException();
        }
        E result = elements[--size];
        elements[size] = null;
        return result;
    }
    public boolean isEmpty(){
        return size == 0;
    }
    private void ensureCapacity(){
        if(elements.length == DEFAULT_INITIAL_CAPACITY){
            elements = Arrays.copyOf(elements, 2*size+1);
        }
    }
}
```
```java
 public Stack(){
        elements = new E[DEFAULT_INITIAL_CAPACITY];
    }
```
Note:上面这句报错,因为使用了不可具体化的类型数组(25),每当编写用数组支持泛型时,都会有这个问题.

#####第2步:处理数组支持泛型报错的两种方法
#######第一种:使用强转,直接绕过创建泛型数组的禁令,+消除警告
```
1. 使用强转,直接绕过创建泛型数组的禁令
```
```java
public Stack(){
        elements = (E[])new Object[DEFAULT_INITIAL_CAPACITY];
}
```
```
2. 证明未受检的转换是安全的,要在尽可能小的范围中禁止警告(24) : 由于elements变量是私有域,同时push方法中的参数类型也是E,所以未受检的转换不会有风险.
```
```java
@SuppressWarnings("unchecked")
public Stack(){
	elements = (E[])new Object[DEFAULT_INITIAL_CAPACITY];
}
```
#######第二种:将elements域的类型从E [] 改为Object []. + 消除错误
```
1. 将elements域的类型从E [] 改为Object [].
```
```java
public class Stack<E> {
    private Object[] elements; // E[] change to  Object[]
    private int size = 0;
    private static final int DEFAULT_INITIAL_CAPACITY = 16;
    
    public Stack(){
        elements = new Object[DEFAULT_INITIAL_CAPACITY];
    }
    public void push(E e){
        ensureCapacity();
        elements[size++]=e;
    }
    public E pop(){
        if(size == 0){
            throw new EmptyStackException();
        }
        E result = elements[--size]; // Won't compile, Error!!!
        elements[size] = null;
        return result;
    }
    public boolean isEmpty(){
        return size == 0;
    }
    private void ensureCapacity(){
        if(elements.length == DEFAULT_INITIAL_CAPACITY){
            elements = Arrays.copyOf(elements, 2*size+1);
        }
    }
}
```
```
2. 强转+禁止警告
```
```java
//Appropriate suppression of unchecked warning
 public E pop(){
        if(size == 0){
            throw new EmptyStackException();
        }
        //push requires elements to be of type E,so cast is corret
        @SuppressWarnings("unchecked")
        E result = (E)elements[--size]; // Error!!!
        elements[size] = null;
        return result;
    }
```
#######处理报错的两种方法的比较
```
1. 禁止数组类型的未受检转换比禁止标量类型的更加危险,所以作者建议第二种方案
```
```
2. 但是由于实际应用中Stack泛型类,代码中经常调用方法public E Pop(){ ... },第二种方法中需要多次转换成E,而不是初始化的时候转换成E []
```

#####使用泛型一个巨大的好处
```
不需要显式的转换,并且会确保自动生成的转换会成功.
```
- 举例
```java
// Little program to exercise our generic Stack
public static void main(String [] args){
	Stack< String > statck = new Stack< String >();
    for(String arg : args){
    	stack.push(arg);
    }
    while(! stack.isEmpty()){
    	System.out.println(stack.pop().toUpperCase());
    }
}
```

#####解释为何Stack中的使用了数组而不是列表,违反了优先使用列表而非数组(25)
```
实际上并不是在泛型中使用列表,Java不是生来就支持列表,因此泛型如ArrayList,则必须在数组上实现.有的也是提升性能,比如HashMap也在使用数组.
```

#####有限制的类型参数:< E extends Father >
```java
class DelayQueue< E extends Delayed > implements BolckingQueue< E > ;
```
```
类型参数列表( < E extends Delayed >)要求实际的类型参数E必须是java.util.concurrent.Delayed的子类型,才可使用.这样允许DelayQueue的元素上利用Delayed方法,无需显式的转换,也不会有ClassCastException风险.
```

#####总结
```
1. 使用泛型比使用需要在客户端进行强转的类型来的更加安全,也更容易使用.
```
```
2. 在设计新的类型时,它们不需要这种转换就可以使用.这通常意味着类做成泛型的
```
```
3. 把类泛型化,当修改某个类的时候,不会破坏现有客户端.(23)
```

###第27条:优先考虑泛型方法
```
方法可以从泛型中受益.静态工具方法尤其适合于泛型化.
```
- 举例:
```java
// Generic method
public static < E > Set< E > union(Set< E > s1,Set< E > s2){
	Set< E > result = new HashSet< E >(s1);
    result.add(s2);
    return result;
}
```

```
Note:
1. 在三个集合的元素类型(两个参数和一个返回值),并在方法中使用类型参数
2. union方法的局限性在于,三个集合的类型(两个输入和一个返回值)必须全部相同.可以利用有限制的通配符类型,使这个方法更加灵活(28)
```

#####泛型方法的显著特性
```
泛型方法中无需明确指定类型参数的值,不像调用泛型构造器的时候必须指定.编译器会通过类型推导,计算类型参数的值.eg:对于上诉的程序而言,编译器发现union的两个参数都是Set< String >类型,则会知道类型参数E必须是String.
```

#####利用泛型方法,使创建参数化类型实例变得简单.
#######调用泛型构造器
```java
//Parameterized type instance creation with constructor
Map<String , List< String > > anagrams = new HashMap< String, List< String > > ();
```
Note:类型参数出现在变量声明的两边,显得冗余.
#######利用泛型静态工厂方法,与想使用的每个构造器对应,消除冗余.
```java
//Generic static factory method
public static <K,V> HashMap<K,V> newHashMap(){
	return new HashMap<K,V>();
}

//Parameterized type instance creation with static factory
Map<String,List<String>> anagrams = newHashMap();
```

#####泛型单例工厂
```
有时,会需要创建不可变但又适合于许多不同类型的对象.因为泛型是通过擦除(25)实现的,可以给所有必要的类型参数使用单个对象,但是需要编写一个静态工厂方法,重复给每个必要的类型参数分发对象.这种模式最常用的是函数对象(21)
```
- 举例:
```
编写一个接口,描述一个方法,该方法接收和返回某个类型T的值.
```
```java
public interface UnaryFounction< T > {
	T apply(T arg);
}
```
```
提供一个恒等函数.如果泛型被具体化了,每个类都需要一个恒等函数,但是它们被擦除后,就只需要一个泛型单例
```
```java
//Generic singleton factory pattern
private static UnaryFunction< Object > IDENTITY_FUNCTION = new UnaryFunction< Object > (){
	public Object apply(Object arg){
    	return arg;
    }
}
//IDENTITY_FUNCTION is stateless and its type parameter is
//unbounded so it's safe to share one instance across all types.
@SuppressWarnings("unchecked")
public static < T > UnaryFunction< T > identityFunction(){
	return (UnaryFunction < T > )IDENTITY_FUNCTION;
}
```
Note:恒等函数很特殊:它返回未被修改的参数,因此我们知道无论T的值是什么,用它作为UnaryFunction< T >都是类型安全的.所以使用@suppressWarnings("unchecked")来禁止警告.
```
利用泛型单例作为UnaryFunction< String > 和UnaryFunction< Number >.
```
```java
// Sample program to exercise generic singleton
public static void main(String [] args){
	String [] strings = {"pan","ping","ping"};
    UnaryFunction< String > sameString = identityFunction();
    for(String s :strings){
    	System.out.println(sameString.applys(s));
    }
    Number[] numbers = {1,2.0,3L};
    UnaryFunction< Number > sameNumber = identityFunction();
    for(Number n : numbers){
    	System.out.println(sameNumber.apply(n));
    }
}
```

#####递归类型限制(28)
```
通过某个包含该类型参数本身的表达式来限制类型参数是允许的,这就是递归类型限制.
```
```
限制:要求列表中的每个元素都能够与列表中的每个其他元素相比较,也就是说列表的元素可以相互比较.
```
- 举例:约束条件示例

```java
public interface Comparable< T >{
	int compareTo(T o);
}

//Returns the maximum value in a list - users recursive type bound
public static <T extends Comparable< T > > T max(List< T > list){
	Iterator< T > i = list.iterator();
    T result = i.next();
    while(i.hasNext()){
    	T t = i.next();
        if(t.compareTo(result) > 0){
        	result = t;
        }
    }
    return result;
}
```

#####总结:
```
1. 泛型方法就像泛型一样,使用起来比客户端需要强转返回值的方法更加安全和容易.
```
```
2. 使用泛型后,可以确保新方法可以不用转换就能使用.
```
```
3. 和类型一样,将现有方法泛型化,是新用户使用方便,且不会破坏现有的客户端.
```

###第28条:利用有限制通配符来提升API的灵活性
```
参数化类型是不可变的(25),也就是说,List< Type1 > 既不是List< Type2 >的子类型,也不是超类型.
```
#####提高API的灵活性
- 举例1:(26中堆栈例子)
```java
public class Stack < E >{
	public Stack();
    public void push( E e);
    public E pop();
    bublic boolean isEmpty();
    //PushAll method without wildcard type 
    public void pushAll(Iterable< E > src){
    	for(E e:src){
        	push(e);
        }
    }
}
```
Note:
```
这个方法 pushAll正确无误,但是缺乏灵活性.比如:一个Stack< Number >,并且调用pushAll(intVal),这里的intVal是Integer类型.由于Integer是Number的一个子类型,所以应该也允许的的
```
```java
Stack< Number > numberStack = new Stack< Number> ();
Iterable< Integer > integers = ...;
numberStack.pushAll(integers);
```

#######有限制的通配符类型,提高API灵活性.
```
pushAll的输入参数类型不应该为"E的Iterable接口",而应该为"E的某个子类型的Iterable接口" : Iterable< ? extends E >
```
```java
public void pushAll(Iterable< ? extends E > src){
	for(E e : src){
    	push(e);
    }
}
```
- 举例2:
```
为Stack< E > 提供popAll方法.
```
```java
//popAll method without wildcard type 
public void popAll(Collection< E > det){
	while(! isEmpty()){
    	dst.add(pop());
    }
}
Stack< Number > numberStack = new Stack< Number > ();
Collection< Object > objects = ...;
numberStack.popAll(objects); // Error,Won't Compile
```
Note:由于Collection< Object > 不是 Collection< Number> 的子类型,所以编译出错.

#######解决方案
```
popAll的输入参数类型,不应该是"E的集合",而应该是"E的某种超类的集合" : Collection< ? super E>
```
```java
//Wildcard type for parameter that servers an an E comsumer
public void popAll(Collection< ? super E > dst){
	while(! isEmpty()){
    	dst.add(pop());
    }
}
```

#####如何获得最大限度的灵活性,又能保证类型安全
```
为了获得最大限度的灵活性,要在生产者或者消费者的输入参数上使用通配符类型.
```
#######助记符
```
PECS :: producer-extends, consumer-super,也就是说:如果参数化类型表示一个T的生产者,就使用< ? extends T>;如果表示一个T的消费者,就使用<? super E>
```
#####相关案例分析

#######第25条中的static < E > E reduce(List< E > list,Function< E > f,E initVal),list参数应该是E的生产者,而参数f既是生产者也是消费者
```java
//Wildcard type for parameter that servers as an E producer
static < E > E reduce(List< ? extends E> list,Function< E > f,E initVal);
```
Note:如何想通过Function< Number> 简化一个List< Integer > ,就可以直接使用.

#######第27条中的public static < E > Set< E > union(Set< E > s1,Set< E > s2);,s1,s2参数都是生产者.
```java
public static < E > Set< E > union( Set< ? extends E> s1,Set< ? extends E> s2)
```
Note:返回的类型仍然都是Set< E > ,请不要用通配符类型作为返回类型.因为这样,会强制用户客户端代码中使用通配符类型.

#######重点讨论:第27条中的max方法
```
1. 初始声明
```
```java
public static < T extends Comparable< T > > T max(List< T > list)
```
```
2. 使用通配符类型的声明
```
```java
public static < T extends Comparable< ? super T > > T max(List< ? extends T> list)
```
Note:
```
1. 参数list,产生T的实例,所以将List< T >改为List< ? extends T > .
2. comparable始终是消费者,因此将Comparable< T > 改为Comparable< ? super T>
```
```
3. 举例说明,修改后的max函数是否真的起到作用(List<ScheduledFuture<?> > scheduledFutures = ...,具体参考书本中这节)
```
```
4. 修改过的max声明,方法体需要修改下
```
```java
public static <T extends Comparable< ? super T > > T max(List< ? extends T > list){
	Iterator< ? extends T > i = list.iterator();
    T result = i.next();
    while(i.hasNext()){
    	T t = i.next();
        if(t.compareTo(result) > 0){
        	result = t;
        }
    }
    return result;
}
```

#####类型参数和通配符之间具有双重性
```
类型参数和通配符之间具有双重性,许多方法都可以利用其中一个或者另一个进行声明
```
```
使用两种静态方法声明,来交换列表中的两个被索引的醒目.第一个使用无限制的类型参数(27),第二个使用无限制的通配符.
```
```java
// Two possible declarations for the swap method
public static < E > void swap(List< E > list,int i,int j);
public static void swap(List< ? > list,int i,int j);
```
#######选择类型参数 Or 通配符 ?
```
1. 在公共API中,第二种常用,因为它更简单.
```
```
2. 一般来说,如何类型参数只在方法声明中出现一次,就可以用通配符来取代它.
```
```
3. 如果是无限制的类型参数,就用无限制的通配符取代它;如果是有限制的类型参数,就用有限制的通配符取代它
```
#######使用通配符,注意事项
```
1. 下面代码报错,因为:编译优先使用通配符,而非类型参数
```
```java
public static void swap(List< ? > list,int i,int j){
	list.set(i,list.set(j,list.get(i)));//Error!,Won't Complie
}
```
Note:问题在于list的类型是List< ? >,你不能将null之外的任何值放到List< ? > 中.
```
2. 提供私有的类型参数方法解决错误
```
```java
public static void swap(List< ? > list,int i,int j){
	swapHelper(list,i,j);
}
// Private helper method for wildcard capture
private static < E > void swapHelper(List< E > list,int i,int j){
	list.set(i,list.set(j,list.get(i)));
}
```

#####总结
```
在API中使用通配符类型虽然比较需要技巧,但是使API变得灵活得多.要适当的利用通配符类型.记住一个原则:PECS.
```

###第29条:优先考虑类型安全的异构容器




