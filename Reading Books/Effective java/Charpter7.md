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
######未被导出的方法,作为包的创建者,应确保将有效的参数值传递进来.因此,非公有方法通常应该使用断言
- 举例:
```java
//Private helper function for recursive sort
private static void sort(long a[], int offset, int length){
	assert a!= null
    assert offset >= 0 && offset<= a.length;
    assert length >= 0 && length <= a.length - offset;
    ...
}
````










