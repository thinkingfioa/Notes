#java 反射机制
[TOC]
Note:
	1. 正常方式:引入需要的“包.类” ---> 通过new实例化 ---> 取得实例化对象
	2. 反射方式:实例化对象 ---> getClass()得到类 ---> 得到完整的“包.类"名称

### Class类的常用方法
|序号|方法|描述|
|:---:|:---:|:---:|
|1|Class<?> forName(String className)|传入完整的"包.类"名称得到这个类|
|2|Constructor[] getConstructors()|得到一个类的全部构造方法|
|3|Fileds[] getDeclaredFields()|得到本类单独定义的全部属性|
|4|Filed[] getFileds()|得到本类继承而来的全部属性|
|5|Methods[] getMethods()|所有的公有（public）方法，包括继承类的公有方法，也包括实现接口的方法|
|6|Methods[] getDeclaredMethods()|包括public,private,private,default的方法，包括实现接口的方法，不包括继承来的方法，|
|7|Method getMethod(String name,Class... parameter)|返回一个具体的Method对象|
|8|Class[] getInterfaces()|得到类的全部接口|
|9|String getName()|得到类的完整"包.类"名称|
|10|Package getPackage()|得到类的包|
|11|Class<?> getSuperClass()|得到一个类的父类|
|12|Object newInstance()|得到类Class的实例化对象|

#####(1)三种方法得到某个特定的类
1. 使用`Class.forName(String className)`得到，也是**推荐**的
```java
Class<?> clazz1= Class.forName("org.apache.vlis.Agent");
```
2. 使用某一个对象 X ,调用对象方法`getClass()`得到
```java
Father father = new Father();
Class<?> clazz2 = father.getClass();
```
3. 使用某一个类Class得到
```java
Class<?> clazz3 = Father.class;
```

#####(2)通过在(1)得到了某个特定的类，接下来要实例化对象
1. 通过使用`newInstance()`方法
Note:`newInstance()`方法，需要实例化的类必须有无参的构造函数
```java
Class<?> clazz = Class.forName("org.apache.vlis.Father");
//类Father，必须有无参的构造函数
Father father = (Father) clazz.newInstance();
```
2. 通过使用`getConstructors()`方法得到有参构造函数
```java
Class<?> clazz = Class.forname("org.apache.vlis.Father");
Constructor<?> constructors[] = clazz.getConstructors();
Father father = (Father) constructors[index].newInstance("fatherName",47);
```
3. Constructor常用方法
|序号|方法|描述|
|:---:|:---:|:---:|
|1|int getModifiers()|得到构造方法修饰符(public,private,protected)|
|2|String getName()|得到构造方法的名称|
|3|Class<?> getParameterTypes()| 得到参数的类型|
|4|T newInstance(Object.. args)|实例化，得到类的对象|

#####(3)通过在(1)中得到了某个特定的类，然后得到具体的方法，在使用invoke(...)方法执行
- Method 类中常用方法

|序号|方法|描述|
|:---:|:---:|:---:|
|1|int getModifiers()|得到本方法修饰符(public,private,protected)|
|2|String getName()|得到方法的名称|
|3|Class<?> getParameterTypes()| 得到参数的类型|
|4|Class<?> getReturnType()|得到方法的返回值|
|5|Class<?> getExceptionTypes()| 得到一个方法的全部抛出异常|
|6|Object invoke(Object obj,Object... args)|实例化，得到类的对象|
基础Class
```java
package vlis;
public class Thinking{
	private String name;
    public void setName(String Name){
    	this.name = Name;
    }
    public String getName(){
    	return this.name;
    }
	public Thinking(){
    }
    public void Print(){
     	System.out.println("thinking_fioa")
    }
    public static void Println(String op,String name){
    	System.out.println("thinking_fioa " +op+" "+name";
    }
}
```
1. 反射调用多参的静态方法(public)
```java
package vlis;
public class Client{
	public static void main(String [] args){
    	try{
    		Class<?> clazz = Class.forName("vlis.Thinking");
        	Method print = clazz.getMethod("Print",new Class[]{String.class,String.class});
        	print.invoke(null,new Object[] { " love "," panpingping"});
    	}catch(Exception e){
    		e.printStackTrace();
    	}
    }
}
```
2. 反射调用非静态方法(public)
```java
package vlis;
public class Client{
	public static void main(String [] args){
    	try{
    		Class<?> clazz = Class.forName("vlis.Thinking");
            Thinking thinking = (Thinking) clazz.newIntance();//Thinking类中一定要有无参构造函数
        	Method print = clazz.getMethod("Print",new Class[]{String.class,String.class});
        	print.invoke(thinking,new Object[] { " love "," panpingping"});
    	}catch(Exception e){
    		e.printStackTrace();
    	}
    }
}
```
3. 反射调用非静态方法无参函数
```java
package vlis;
public class Client{
	public static void main(String [] args){
    	try{
    		Class<?> clazz = Class.forName("vlis.Thinking");
            Thinking thinking = (Thinking) clazz.newIntance();//Thinking类中一定要有无参构造函数
        	Method print = clazz.getMethod("Print");
        	print.invoke(thinking);
    	}catch(Exception e){
    		e.printStackTrace();
    	}
    }
}
```
4. 封装setXXX(...),getXXX(...),使反射得到的对象可以操作具体的属性
Note:如果类中有多个属性时，另写一个setter(...),getter(...)操作方法
 - 基础类Father

```java
package vlis;
public class Father {
    private String name;
    private int age;
    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return this.name;
    }
    public void setAge(int Age){
        this.age = Age;
    }
    public int getAge(){
        return this.age;
    }
    public void Print(){
        System.out.println("thinking_fioa");
    }
    public Father(){
    }
}
```
 - Client类
```java
package vlis;
public class Client{
	public static void main(String [] args){
    	Class<?> clazz = null;
    	try{
        	clazz = Class.forName("vlis.Father");
        }catch(Exception e){
        	e.printStackTrace();
        }
        Object obj = clazz.newInstance();
        setter(obj,"setName","thinking_fioa",String.class);
        System.out.println(" ---> " + getter(obj,"getName"));
        setter(obj,"setAge",5,int.class);
        System.out.println(" ---> "+ getter(obj,"getAge"));
    }
    //setter(...)方法中,需要加入一个参数:Class<?> type,否则,处理int,double,float,不行.
    public static void setter(Object obj,String methodName,Object value,Class<?> type){
    	try{
        	Method method= obj.getClass().getMethod(methodName,type);
        	method.invoke(obj,value);
        }catch(Exception e){
        	e.printStackTrace();
        }
    }
    public static Object getter(Object obj,String methodName){
    	try{
        	Method method = obj.getClass().getMethod(methodName);
            return method.invoke(obj)
        }catch(Exception e){
        	e.printStackTrace();
        }
        return null;
    }
}
```


#####(4)通过在(1)中得到了某个特定的类，然后得到具体的Field(Field就是值属性,区别出:Filed[] getFields(),Field[] getDeclaredFields())
- Filed类常用的方法

|序号|方法|描述|
|:---:|:---:|:---:|
|1|Object get(Object obj)|得到一个对象中属性的具体内容
|2|void set(Object obj,Object value)|设置指定对象中属性的具体内容|
|3|int getModifiers()|得到属性的修饰符|
|4|String getName()|返回此属性的名称|
|5|void setAccessible(boolean flag)|设置一个属性是否可以被外部访问|
|6|boolean isAccessible()|判断属性是否可被外部访问|
|7|static void setAccessible(AccessibleObject[] array,boolean flag)|设置一组属性是否可被外部访问|

1. 虽然在反射中可以使用类的getXXX(),setXXX(...),修改属性。但比较麻烦,也可能类并没有提供。可以采用直接操作Filed域,也**更简单**
```java
//下面的代码中出现的类Father,是(3).4中所指的Father类
public class CLient{
	public static void main(String [] args){
    	Class<?> clazz = null;
        try{
        	clazz = Class.forName("vlis.Father");
        }catch(Exception e){
        	e.printStackTrace();
        }
        Object obj = clazz.newInstance();
        Field nameField = clazz.getDeclaredField("name");
        //name是private,设置其可以访问
        nameField.setAccessible(true);
        nameField.set(obj,"thinking_fioa");
        System.out.println(nameField.get(obj));
    }
}
```

#####(5)通过反射来操作数组
- Array(java.lang.reflect.Array)类常用的方法

|序号|方法|描述|
|:---:|:---:|:---:|
|1|Object get(Object array,int index)|根据下标取得数组内容|
|2|Object newInstance(Class<?> componentType,int length)|根据已有的数组类型开辟新的数组对象|
|3|void set(Object array,int index,Object value)|修改指定位置的内容|
>Note:特别提醒:对于一个数组来说,想要得到`Class<?> type`需要使用`array.getClass().getComponentType();`
```java
public class Client {
    public static void main(String args[]) throws Exception{
        int temp[] = {1,2,3};
        Class<?> clazz = temp.getClass().getComponentType();
        System.out.println("thinking_fioa ---> " + clazz.getName());
        Array.set(temp, 2, 4);
        System.out.println("thinking_fioa --->" + Array.get(temp, 2));
        }
}
```

