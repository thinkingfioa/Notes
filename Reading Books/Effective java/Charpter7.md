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










