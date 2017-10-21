# try-catch-finally
```
@author 鲁伟林
本文主要经过案例分析Java语言中: try-catch-finally中执行流程。
先给出总结，供自己和文档阅读者参考，后面给出案例代码，进行系统分析，帮组理解。
gitHub地址: https://github.com/thinkingfioa/Notes/blob/master/java/try-catch-finally.md
```

### 总结
对以上所有的例子进行总结

1. finally语句块中有return，由于finally是最后执行，所以肯定return是有效的。
2. finally块中抛出异常，方法肯定抛出异常
3. finally语句中无return，修改返回值是无效的。
 
### 如何使用
1. 尽量不要在finally写return语句，return语句在try-catch中使用。finally无return的修改返回值是无效的。
2. finally块中避免使用return语句，因为finally块中如果使用return语句，会显示的消化掉try、catch块中的异常信息，屏蔽了错误的发生
3. finally块中避免再次抛出异常，否则整个包含try语句块的方法回抛出异常，并且会消化掉try、catch块中的异常

### 案例1 
##### 代码
```java
public class Test {
    public static final String test() {
        String t = "";
        try {
            t = "try";
            return t;
        } catch (Exception e) {
            t = "catch";
            return t;
        } finally {
            t = "finally";
        }
    }
    
    public static void main(String[] args) {
        System.out.println(Test.test());
    }
}
```
##### 结果
输出: try
##### 分析
1. try语句中的return，返回的其实是系统重新定义了一个局部引用t’。这个引用指向了引用t对应的值，也就是try。
2. finally语句中把引用t赋值为"finally"，因为return的返回一个局部引用t’，所以根本不会改变。

### 案例2
##### 代码
```java
public class Test {

    public static final String test() {
        String t = "";
        try {
            t = "try";
            return t;
        } catch (Exception e) {
            t = "catch";
            return t;
        } finally {
            t = "finally";
            return t;
        }
    }

    public static void main(String[] args) {
        System.out.print(Test.test());
    }}
```
##### 结果
输出: finally
##### 分析
1. try语句中的return语句给忽略。
2. 代码最终会进入finally语句块中，所以这次返回的是finally。

### 案例3
##### 代码
```java
public class Test {

    public static final String test() {
        String t = "";
        try {
            t = "try";
            Integer.parseInt(null); // throw java.lang.NumberFormatException
            return t;
        } catch (Exception e) {
            t = "catch";
            return t;
        } finally {
            t = "finally";
        }
    }

    public static void main(String[] args) {
        System.out.print(Test.test());
    }

}
```
##### 结果
输出: catch
##### 分析
1. try语句里面会抛出java.lang.NumberFormatException，所以程序会进入catch语句块中。
2. t赋值为catch，在执行return之前，会把返回值保存到一个临时变量里面t '。
3. 执行finally的逻辑，t赋值为finally，但是返回值和t'已经没有关系了，输出是catch。


### 案例4
##### 代码
```java
public class Test {

    public static final String test() {
        String t = "";
        try {
            t = "try";
            Integer.parseInt(null); // throw java.lang.NumberFormatException
            return t;
        } catch (Exception e) {
            t = "catch";
            return t;
        } finally {
            t = "finally";
            return t;
        }
    }

    public static void main(String[] args) {
        System.out.print(Test.test());
    }

}
```
##### 结果
输出: finally
##### 分析
finally语句中有return，最终一定输出它。因为它总是最后执行的代码。

### 案例5
##### 代码
```java
public class Test {

    public static final String test() {
        String t = "";
        try {
            t = "try";
            Integer.parseInt(null); // throw java.lang.NumberFormatException
            return t;
        } catch (Exception e) {
            t = "catch";
            Integer.parseInt(null); // throw java.lang.NumberFormatException
            return t;
        } finally {
            t = "finally";
            //return t;
        }
    }

    public static void main(String[] args) {
        System.out.print(Test.test());
    }

}
```
##### 结果
输出: 抛出java.lang.NumberFormatException
##### 分析
1. try语句中抛出java.lang.NumberFormatException，进入catch语句块中
2. catch语句也抛出java.lang.NumberFormatException。进入finally语句中
3. finally语句并没有任何return。所以无法改变语句返回结果，所以程序抛出java.lang.NumberFormatException

### 案例6
##### 代码
```java
public class Test {

    public static final String test() {
        String t = "";
        try {
            t = "try";
            Integer.parseInt(null);
            return t;
        } catch (Exception e) {
            t = "catch";
            Integer.parseInt(null);
            return t;
        } finally {
            t = "finally";
            return t;
        }
    }

    public static void main(String[] args) {
        System.out.print(Test.test());
    }

}
```
##### 结果
输出: finally
##### 分析
与上面相比，就是在finally语句中加入了return。所以程序会**忽略**catch语句块里面抛出的异常信息，返回“finally”值


### 案例7
##### 代码
```java
public class Test {

    public static final String test() {
        String t = "";
        try {
            t = "try";
            return t;
        } catch (Exception e) {
            t = "catch";
            return t;
        } finally {
            t = "finally";
            String.valueOf(null); // throws NullPointerException
            return t;
        }
    }

    public static void main(String[] args) {
        System.out.print(Test.test());
    }

}
```
##### 结果
输出: 抛出 NullPointerException异常
##### 分析
在finally语句中， 代码:String.valueOf(null)会导致程序抛出NPE异常，程序直接返回出去。
 