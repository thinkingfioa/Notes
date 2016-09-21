# 第5章: 基础构建模块
```
本章目的:本章介绍Java类库中一些最有用的并发构建模块.及使用这些模块来构造并发应用程序时的一些常用模式
```
[TOC]

### 5.1 同步容器类
```
同步容器类包括:Vector和Hashtable.
实现线程安全的方式是:将它们的状态封装起来,并对每个公有方法都进行同步,是的每次只有一个线程能访问容器的状态
```

##### 5.1.1 同步容器类的问题
```
同步容器类是线程安全的,但是某些情况下可能需要额外的客户端加锁来保护复合操作.
常见的复合操作:迭代(遍历),"若没有则添加".
```
- 举例 1:
```
即使Vector是线程安全类,但是下面的例子任然非线程安全
```

```java
public static Object getLast(Vector list){
	int lastIndex = list.size() -1 ;
    return list.get(lastIndex);
}

public static void deleteLast(Vector list){
	int lastIndex = list.size() -1;
    list.remove(lastIndex);
}
```
Note:
```
上面的代码,在并发访问时,明显会出现并发错误.可能会抛出异常:ArrayIndexOutOfBoundsException异常
```
####### 解决方法
```
使用加锁机制:synchronized(this){...},保证原子性操作
```
- 举例 2:
```
Vector在进行遍历是也会出现上面的并发问题
```
```java
for(int i =0;i<vector.size();i++){
	doSomethinkng(vector.get(i));
}
```
Note:
```
相同的原因:因为另一个线程并发修改了Vector.解决方法:synchronized(vector){...}
```

##### 5.1.2 迭代器与ConcurrentModificationException
```
无论在直接迭代还是在Java 5.0引入的for-each循环语法中,对容器类进行迭代的标准方式都是使用Iterator.
```
```
迭代过程中,不允许迭代的容器被修改,否则就会抛出一个ConcurrentModificationException异常.
所以,使用迭代器期间无法避免的对容器加锁.
```
```
并发异常采用实现方式:将计算器的变化与容器关联起来,如果在迭代期间计算器被修改了,那么hasNext或next将抛出ConcurrentModificationException异常.
```
```
单线程代码也可能抛出ConcurrentModificationException异常,当对象直接从容器中删除而不是通过Iterator.remove删除,就会抛出.
```
- 举例:
```java
List <Widget> widgetList
	= Collections.synchronizedList(new ArrayList<Widget>());
//可能抛出ConcurrentModificationException
for(Widget w : widgetList){
	doSomething(w);
}
```
Note:
```
javac会将使用Iterator代码,反复调用hasNext和next来迭代List对象.
```

####### 探讨
```
在开发中,并不希望在迭代期间对容器加锁.因为这可能会严重影响系统的吞吐量.
```
####### "克隆"容器,避免迭代容器加锁
```
使用"克隆"容器,并在副本上进行迭代.副本被放在线程内,所以线程安全.
不过,克隆的过程仍然需要对容器加锁.
```

##### 隐藏迭代器
```
虽然加锁可以防止迭代器抛出ConcurrentModificationException异常,但必须要记住所有对共享容器进行迭代的地方都需要加锁.
而且,有时候,迭代器会应海沧起来.下面举例
```
- 举例:
```java
public class HiddenIterator {
    @GuardedBy("this")
    private final Set<Integer> set = new HashSet<Integer>();

    public synchronized void add(Integer i) {
        set.add(i);
    }

    public synchronized void remove(Integer i) {
        set.remove(i);
    }

    public void addTenThings() {
        Random r = new Random();
        for (int i = 0; i < 10; i++)
            add(r.nextInt());
        System.out.println("DEBUG: added ten elements to " + set);
    }
}
```
Note:
```
方法addTenThings中可能抛出ConcurrentModificationException异常,因为toString中,会对迭代器进行遍历.
真正的问题在于HiddenIterator不是线程安全的.
```
```
如果使用synchronizedSet来包装HashSet,就不会发生这种错误.
```

####### 隐藏迭代器提醒
```
一些hashCode和equals等方法也会间接执行迭代操作.比如,两个容器比较,或者容器作为另一个容器的元素或键值.
还有的比如:containsAll,removeAll和retainAll.
```

### 5.2 并发容器.
```
Java 提供了一系列的并发容器
```
```
1. ConcurrentHashMap用来替代同步且基于散列的Map;CopyOnWriteArrayList用在遍历操作为主要操作的情况代替同步List
2.  新的容器类型 :Queue和BlockingQueue.
ConcurrentLinkedQueue是传统的队列,PrioritQueue(非并发)优先队列.
Queueu上的操作不会阻塞,如果队列为空,则获取元素操作返回空值.
BlockingQueue增加可阻塞的插入和获取等操作.
3. Java 6.0提供ConcurrentSkipListMap和ConcurrentSkipListSet分别作为SortedMap和SortedSet的并发替代品.
```

##### 5.2.1 ConcurrentHashMap
```
同步容器类在执行每个操作期间都持有一个锁.
```
```
ConcurrentHashMap并不是每个方法都在同一个锁上同步,而是使用一种粒度更细的加锁机制,称为分段锁.
分段锁:任意数量的读取线程可以并发访问Map,执行读取操作的线程和执行写入的线程可以并发访问Map,并且一定数量的写入线程可以并发地修改Map.
```
```
ConcurrentHashMap加强了同步容器类,提供的迭代器不会抛出ConcurrentModificationException异常.因此迭代过程中无需对容器加锁.
```
####### ConcurrentHashMap牺牲因素.
```
ConcurrentHashMap在进行计算的方法,如size和isEmpty,这些方法的语义减弱了.有可能返回的计算时已经过期.因为往往返回的是近视值,而不是精确值.
```

##### 5.2.2额外的原子Map操作.
```
ConcurrentHashMap提供很多复合操作,例如"若没有则添加","若相等则移除"等.
```
```
需要提醒一点的是:ConcurrentHashMap不能被加锁来执行独占访问,不能使用客户端加锁来创建新的原子操作.
```

##### 5.2.3 CopyOnWriteArrayList
```
CopyOnWrite容器即写时复制的容器。通俗的理解是当我们往一个容器添加元素的时候，不直接往当前容器添加，
而是先将当前容器进行Copy，复制出一个新的容器，然后新的容器里添加元素，添加完元素之后，再将原容器的引用指向新的容器
```
```
CopyOnWriteArrayList用来替代同步List.同样在迭代期间不需要对容器进行加锁或复制.
```
```
CopyOnWriteArrayList使用的是"写入时复制",也就是说,每次修改时,都会创建并重新发布一个新的容器副本.
```
```
需要提醒的是:每当修改容器时都会复制底层数组,是需要一定的开销的.
当迭代操作远远多于修改操作时,应该考虑使用CopyOnWriteArrayList.
```

###### CopyOnWriteArrayList源码分析
```
add操作时,会复制出一个新的容器,添加完元素之后，再将原容器的引用指向新的容器.
```
```java
public boolean add(E e) {
    final ReentrantLock lock = this.lock;
    lock.lock();
    try {
        Object[] elements = getArray();
        int len = elements.length;
        Object[] newElements = Arrays.copyOf(elements, len + 1);
        newElements[len] = e;
        setArray(newElements);
        return true;
    } finally {
        lock.unlock();
    }
}
```
```
读取时,无需加锁,允许多个读者.
```
```java
public E get(int index) {
    return get(getArray(), index);
}
```

### 5.3 阻塞队列和生产者 - 消费者模式
```
阻塞队列提供阻塞的put和take方法,以及支持定时的offer和poll方法.
```
```
队列可以是有界的,也可以是无界的.无界的则永远不会满,也就是说put方法永远不会阻塞.
```
```
BlockingQueue简化了生产者-消费者,同事允许任意数量的生产者和消费者.
```
```
阻塞队列同样提供一个offer方法,如果数据项不能被put到队列中,那么将会返回一个失败的状态.
这样可以采取的负荷过载处理逻辑
```
##### BlockingQueue的几种实现介绍
```
1. LinkedBlockingQueue和ArrayBlockingQueue也是FIFO队列,二者分别与LinkedList和ArrayList类似.
```
```
2. PriorityBlockingQueue是一个按优先级排序的队列.
要提醒的是:PriorityBlockingQueue既可以根据元素的自然顺序来排列比较元素(如果实现了Comparable方法).
也可以使用Comparator来比较.
```
```
3. SynchronousQueue实际上不是一个真正的队列,它没有存储空间,它维护的是一组线程,这些线程等待者把元素加入和移出.
```
####### SynchronousQueue的理解
```
SynchronousQueue队列没有为队列中的元素维护存储空间,因此put和take会一直阻塞,直到有另一个线程已经准备号参与到交付的过程中.
仅当有足够的消费者,并且总有一个消费者准备好获取交付的工作时,才适合使用同步队列.
```

##### 5.3.1示例:桌面搜索(代理程序)






















