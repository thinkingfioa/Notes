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

#####第25条:列表优先于数组















