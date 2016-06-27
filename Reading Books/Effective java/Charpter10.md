#第10章:并发
[TOC]
```
本章目的:线程并发机制可以提高程序性能,但也存在较多困难.本章介绍基本并发程序开发技巧
```

###第66条:同步数据访问共享的可变数据
```
关键字synchronized可以保证同一时刻,只有一个线程可以执行某个方法,或者某个代码块.
```
##### 同步
```
同步不仅可以阻止一个线程看到对象处于不一致的状态下之中,还可以保证进入同步方法或者同步代码块的每个线程,
都看到由同一个锁保护的之前所有的修改效果
```
```
如果没有同步,一个线程的变化就不能被其他线程看到
```

#####Java语言规范保证读或者写一个变量的原子性
```
读取一个非long或double类型的变量,可以保证返回的值是某个线程保存在该变量中的,也就是说,大家共享这个变量,并发的修改这个变量.但写入和读出都是原子性的.
```

#####对共享可变数据的访问不能保证同步的后果
```
后果很严重
```
- 举例:
```
下面的例子:阻止一个线程妨碍另一个线程的任务
```
```
Java类库提供了Thread.stop方法,但是这个方法很久就不提倡使用.因为Thread.stop方法不安全,会导致数据遭到破坏,所以请不要使用方法:
Thread.stop()
```
```
要阻止一个线程妨碍另一个线程,建议做法:
让第一个线程轮询(poll),这个域开始是false,但通过第二个线程设置为true,表示第一个线程将要终止自己.
```

#####阻止一个线程妨碍另一个线程的任务探讨
```java
// Broken! - How long would you expect this program to run ?
public class StopThread{
	private static boolean stopRequested;
    
    public static void main(String [] args) throws InterruptedException{
    	Thread backgroundThread = new Thread(New Runnable(){
        	public void run(){
            	int i = 0;
                while( ! stopRequested){
                	i++;
                }
            }
        });
        backgroundThread.start();
        
        TimeUnit.SECONDS.sleep(1);
        stopRequested = true;
    }
}
```
Note:
```
这段程序在我的机器是,始终循环.并不是预期一秒后结束
```
######始终循环的原因
```
由于没有同步,就不能保证后台线程何时看到主线程对stopRequested的值所做的改变.
```

#######解决方法一
```
使用volatile关键字
```
```
用volatile关键字修饰的变量,线程在每次使用变量的时候,都会读取变量修改的后的值.但volatile不能保证互斥访问
```
```java
public class StopThread {

    private static volatile boolean stopRequested;
    
    public static void main(String [] args) throws InterruptedException{
        Thread backgroundThread = new Thread(new Runnable(){
            public void run(){
                int i = 0;
                while( ! stopRequested){
                    i++;
                }
            }
        });
        backgroundThread.start();
        
        TimeUnit.SECONDS.sleep(1);
        stopRequested = true;
        System.out.println("thinking_fioa");
    }
}
```
Note:
```
关键字volatile保证了stopRequested修改后,线程可以看到.
它可以保证任何一个线程在读取该域的时候都将看到最近刚刚被写入的值.
```
```
需要提醒的是:volatile不能保证互斥性,因为可能都读取同一个值,但一个修改另一个未感知前也修改了这个值,则互斥失败.
```

#######方法二
```
同步访问stopRequested域
```
```java
public class StopThread {
    //Properly synchronized cooperative thread termination
    private static volatile boolean stopRequested;
    
    private static synchronized void requestStop(){
        stopRequested = true;
    }
    
    private static synchronized boolean stopRequested(){
        return stopRequested;
    }
    
    public static void main(String [] args) throws InterruptedException{
        Thread backgroundThread = new Thread(new Runnable(){
            public void run(){
                int i = 0;
                while( ! stopRequested()){
                    i++;
                }
            }
        });
        backgroundThread.start();
        
        TimeUnit.SECONDS.sleep(1);
        requestStop();
        System.out.println("thinking_fioa");
    }
}
```
Note:
```
方法requestStop(),stopRequested()保证同步访问stopRequested.
```

#####volatile不能保证互斥解释
```
考虑下面代码,生成不同的SerialNumber
```
```java
// Broken - requires synchronization
private static volatile int nextSerialNumber = 0;

public static int generateSerialNumber(){
	return nextSerialNumber++;
}
```
Note:
```
增量操作符(++)操作不是原子的,先读取值,再写回一个新值.但是,假如第二个线程在第一个线程读取旧值和写回新值期间读取这个值,那么互斥访问失败.
```
#####类Atomic*
```
Java类库中java.util.concurrent.atomic提供一部分可以保证互斥的类.比如:AtomicLong.推荐使用
```

#####不可变类在并发中的作用
```
避免本条目所讨论到的问题,最佳的办法就是不共享可变数据.要么是不可变的数据(15),要么将可变的数据限制在单个线程中.
```
```
要充分理解框架和类库,防止引入所不知道的线程
```

#####常用的做法
```
让线程在短时间内修改一个数据对象,然后与其他线程共享,这是可以接受.这种对象被称为事实上不可变的.
```
```
通常采用的方法有:static域类静态初始化,保持成volatile域,final域,或者将它放到并发的集合中(69)
```
#####总结
```
当多个线程共享可变的数据时,每个读或者写数据的线程都必须执行同步.
```
```
如果只需要线程之间的交互通信,而不需要互斥,volatile修饰符可以接收同步形式.
```

###第67条:避免过度同步
```
66条告诫我们缺少同步的危险性.但本条目则担心过度同步可能会导致性能降低,死锁,甚至不确定的行为.
```

#####设计同步方法或者代码块警告
```
1. 在一个被同步的方法或者代码块中,永远不要放弃对客户端的控制.
换句话说,在一个被同步的区域内部,不要调用设计成要被覆盖的方法,或者由客户端以函数对象的形式提供的方法(21).否则,将无法控制整个同步是否有问题
```
- 举例:
```
实现一个观察到集合包装.该类允许客户端将元素添加到集合中时预定通知.这就是观察者模式.
```

```java
public class ObservableSet< E > extends ForwardingSet< E >{
    //Broken - invokes alien method from synchronzied block
    public ObservableSet(Set<E> set) {
        super(set);
    }
    
    private final List<SetObserver< E > > observers = new ArrayList<SetObserver <E>>();
    
    public void addObserver(SetObserver< E >  observer){
        synchronized(observers){
            observers.add(observer);
        }
    }
    
    public void removeObserver(SetObserver< E >  observer){
        synchronized(observers){
            observers.remove(observer);
        }
    }
    
    private void notifyElementAdded(E element){
        synchronized(observers){
            for( SetObserver< E >  observer : observers){
                observer.added(this.element);
            }
        }
    }
    
    @Override
    public boolean add(E element){
        boolean added = super.add(element);
        if(added)
            notifyElementAdded(element);
        return added;
    }
    
    @Override
    public boolean addAll(Collection<? extends E> c){
        boolean result = false;
        for(E element : c){
            result != add(element);
        }
        return result;
    }
}

```
Note:
```
方法addObserver方法预定通知,方法removeObserver方法取消预定.最终通过回调接口的实例都会被传递个方法
```
```java
pubilc interface SetObserver< E >{
	void added(ObserverableSet< E> , E element);
}
```
#####案例检验上面的代码
```
1. 粗略检验下,ObservableSet显示正常
```
```java
public static void main(String [] args){
	ObservableSet< Integer > set = new ObservableSet<Integer > (new HashSet<Integer> ());
    set.addObserver(new SetObserver<Integer> (){
    	public void added(ObservableSet< Integer> s, Integer e){
        	System.out.println(e);
        }
    });
    for(int i = 0;i<100;i++){
    	set.add(i);
    }
}
```
Note:
```
上面的程序是典型的将added方法交予用户使用,允许客户端自定义逻辑.程序执行正常
```
```
2. 想实现,如果某个值为23,观察者要将自身删除.
```
```java
set.addObserver(new SetObserver<Integer> (){
    	public void added(ObservableSet< Integer> s, Integer e){
        	System.out.println(e);
            if(e == 23){
            	s.removeObserver(this);
            }
        }
    });
```
Note:
```
程序会抛出ConcurrentModificationException异常,
```
```
问题在于,当notifyElementAdded调用观察者的added方法时,正处于遍历observers列表的过程,不允许进行删除.
```
```
3. 尝试一个比较奇特的例子:编写一个试图取消预订的观察者,但是不直接调用removeObserver.而是用另一个线程的服务完成
这个观察者使用一个executorService(68)
```
```java
set.addObserver(new SetObserver<Integer> (){
    	public void added(final ObservableSet< Integer> s, Integer e){
        	System.out.println(e);
            if(e == 23){
            	ExecutorService executor =
                	Executors.newSingleThreadExecutor();
                final SetObserver<Integer> observer = this;
                try{
                	executor.submit(new Runnable(){
                    	public void run(){
                        	s.removeObserver(observer);
                        }
                    }).get();
                }catch(ExecutionExceptin ex){
                	throw new AssessertionError(ex.getCause());
                }catch(IntegeruptedException ex){
                	throw new AssessertionError(ex.getCause());
                }finally{
                	executor.shutdown();
                }
            }
        }
    });
```
Note:
```
这次,程序可能出现死锁.后台线程调用s.removeObserver,企图锁定observers,但是主线程掌握锁,并且主线程在等待线程删除观察者.
```

#####解决方案
#######解决方案 1
```
使用将外来方法的调用移出同步的代码块来解决这个问题.对于notifyElementAdded方法,还涉及给observers列表拍张"快照".
```
```java
// Alien method moved outside of synchronized block - open calls
private void notifyElementAdded(E element){
	List<SetObserver< E > > snapshot = null
    synchronzied(observers){
    	snapshot = new ArrayList<SetObserver< E > > (observers);
    }
     for( SetObserver< E >  observer : snapshot){
         observer.added(this.element);
    }
}
```
#######解决方案 2
```
自从Java 1.5版本后,Java类库提供一个并发集合(69):CopyOnWriteArrayList.
```
```
CopyOnWriteArrayList会重新拷贝整个底层数组,实现所有的写操作.如果大量使用CopyOnWriteArrayList的性能将大受影响.但是对于观察者列表来说,由于几乎不会改动,并且经常被遍历,非常合适使用
```
```java
public class ObservableSet< E > extends ForwardingSet< E >{
    public ObservableSet(Set<E> set) {
        super(set);
    }
    
    private final List<SetObserver< E > > observers
    	= new CopyOnWriteArrayList<SetObserver <E> >();
    
    public void addObserver(SetObserver< E >  observer){
        observers.add(observer);
    }

    public boolean removeObserver(SetObserver< E >  observer){
        return observers.remove(observer);
    }

    private void notifyElementAdded(E element){
       for( SetObserver< E >  observer : observers){
            observer.added(this.element);
       }
    }

    @Override
    public boolean add(E element){
        boolean added = super.add(element);
        if(added)
            notifyElementAdded(element);
        return added;
    }

    @Override
    public boolean addAll(Collection<? extends E> c){
        boolean result = false;
        for(E element : c){
            result != add(element);
        }
        return result;
    }
}
```
#####开放调用
```
在同步区域之外被调用的外来方法被称为"开放调用".除了避免死锁外,同时还可以增加并发性.
```
```
我们应该在同步区域内做尽可能少的工作.获得锁,检查共享数据,根据需要转换数据,然后释放锁.任何耗时的动作,都应该在同步区域外进行.
```

#####同步性能讨论
```
永远不要过度同步.在多核时代,过度同步会浪费VM优化的巨大潜能.
```
```
1. 如果一个可变的类要并发使用,应该使这个类变成线程安全的(70).通过内部同步,将会获得明显比外部锁定的整个对象更高的并发性.
```
```
2. 如果在内部同步了类,就可以使用不同的方法来实现高并发性.例如分拆锁,分离锁和非阻塞并发控制.
```
```
3. 如果方法修改了静态域,那么你就必须同步这个域的访问,即使它往往只用于单个线程.
客户要在这个方法上执行外部同步是不可能的.因为不可能保证其他不相关的客户也会执行外部同步.比如:前面的例子:generateSerialNumber
```

#####总结
```
1. 为了避免死锁和数据破坏,千万不要从同步区域内部调用外来的方法.也就是说,尽量限制同步区域内部的工作量.
```
```
2. 当你设计一个可变类的时候,要考虑下它们是否该自己完成同步操作.
```
```
3. 避免过度同步,只有有足够的理由才在内部同步类.
```

###第68条:executor和task优先于线程
#####executor使用
```
1. 创建一个单线程处理器
```
```java
ExecutorService executor = Executors.newSingleThreadExecutor();
executor.execute(runnable);
```
```
2. 创建多个线程来处理队列的请求.
```
```java
ExecutorService executor = Executors.newCachedThreadPool();
```
Note:
```
如果对于大负载的服务器来说,缓存的线程池不是好的方法.在缓存的线程中,被提交的任务是立即响应的,直接交给线程执行.
如果没有线程可用,则创建一个新的线程.
```
```
3. 创建固定线程数目的线程池
```
```java
ExecutorService executor = Executors.newFixedThreadPool(100);
```
Note:
```
这样线程池的个数控制在100,控制线程池的上限.
```

#####抽象的工作单元--任务
```
以后应该尽量不要直接使用线程.使用ExecutorService
```
```
任务有两种:Runnable及其近亲Collable(有返回值).ExecutorService执行会非常灵活
```

#####定时器:timer
```
timer一般执行定时任务.如果timer线程抛出未捕捉的异常,timer就会停止执行.但是线程池executor支持多个线程,并且可以优雅的从抛出未受检异常的任务中恢复.
```

#####总结
```
Executor Framework的完整处理方法超出本书讨论内容,可以参考<<Java Concurrency in Practice>>(中文:Java并发编程实践)
```

### 第69条:并发工具优先于wait和notify
```
想要正确的使用wait和notify比较困难,就应该用更高级的并发工具来代替
```
```
java.util.concurrent中提供更高级的工具分三类:Executor Framework(68), 并发集合以及同步器.并发集合和同步器将在本条目中进行简单的阐述
```
#####并发集合
```
并发集合为标准的集合接口(eg:List,Queue,Map)提供了高性能的并发实现.为了提供高并发性,这些实现在内部自己管理同步(67)
```
```
并发集合保证内部同步并发,但不可能排除并发活动.这意味着客户无法原子的对并发集合进行方法调用.
有些集合接口已经通过依赖状态的修改操作进行了扩展,将集合基本操作合并到单个原子操作中
```
- 举例:
```
ConcurrentMap扩展了Map接口,并添加集合方法,包括putIfAbsent(key,value);
```
```java
private static final ConcurrentMap<String, String > map = new ConcurrentHashMap<String, String> ();

public static String intern(String s){
	String previousValue = map.putIfAbsent(s,s);
    return previousValue == null ? s : previousValue;
}
```
Note:
```
事实上可以做的更好写,因为ConcurrentHashMap对获取操作(如get)进行了优化.
```
```java
//Concurrent canonicalizing map atop ConcurrentMap - faster
public static String intern(String s){
	String result = map.get(s);
    if(null == result){
    	result = map.putIfAbsent(s,s);
        if(null == result){
        	result = s;
        }
    }
    return result;
}
```

#####阻塞操作扩展的集合接口
```
通过阻塞操作的集合接口,会一直等待(或阻塞)到成功执行为止.
```
#######BlockingQueue
```
BlockingQueue扩展了Queue接口,并添加了包括take在内的集合方法.也就是通常所说的生产者-消费者队列
一个或者多个生产者线程在工作队列中添加工作项目,如果满了,就等待
一个或者多个消费者线程从工作队列中取出并且处理.
不出所料,大多数ExecutorService实现(包括ThreadPoolExecutor)都使用了BlockingQueue(68)
```
#####同步器
```
同步器是一些线程能够等待另一个线程的对象,允许它们协调动作.最常用的同步器是CountDownLatch和Semaphore
```
#####倒计数锁存器
```
倒计数锁存器是一次性的障碍,允许一个或者多个线程等待一个或者多个其他线程来做某些事情.
CountDownLatch的唯一构造器带有一个int类型的参数,这个int参数是指允许所有在等待的线程被处理之前,必须在锁存器上调用CountDown方法的次数
```
- 举例:
```
假设想要构建一个简单的框架,用来给一个动作的并发执行定时
```
```java
//Simple framework for timing concurrent execution
public static long time(Executor executor, int concurrency, final Runnable action) throws InterruptedException{
	final CountDownLatch ready = new CountDownLatch(concurrency);
    final CountDownLatch start = new CountDownLatch(1);
    final CountDownLatch done = new CountDownLatch(concurrency);
    for(int i = 0;i<concurrency;i++ ){
    	executor.execute(new Runnable(){
        	public void run(){
            	ready.countDown(); // Tell timer we're ready
                try{
                	start.await(); //Wait till peers are ready
                    action.run();
                }catch(InterruptedException e){
                	Thread.currentThread().interrupt();
                }final{
                	done.countDown();//Tell timer we're done
                }
           }
        });
    }
    ready.await();
    long startNanos = System.nanoTime();
    start.countDown();
    done.await();
    return System.nanoTime() - startNanos;
}
```

Note:
```
1. 第一个倒计数锁存器是:ready,工作线程用它来告诉timer线程它们已经准备好了.
```
```
2.  第二个倒计数锁存器是:start,最后一个工作线程调用ready.countDown时,timer线程记录下起始时间,并调用start.countDown,允许工作线程继续进行.
```
```
3. 第三个倒计数锁存器是:down,直到最后一个工作线程运行该动作,并调用down.countDown.一旦调用这个,timer线程就会苏醒,并记录下时间
```
#######总结
```
三个倒计数的锁存器,可以使用一个CyclicBarrier来代替,这样代码更加简洁.(参考:Java并发编程实战)
```

#####wait和notify用法
```
应该优先使用并发工具,而不是使用wait和notify,但可能必须维护使用wait和notify遗留代码.
```
```
1. wait方法被用来使线程等待某个条件
wait必须在同步区域内部被调用,这个同步区域将对象锁定在调用wait方法的对象上
```
- 举例:
```java
// The standard idiom for using the wait method
synchronzied(obj){
	while(<condition does not hold>)
    	obj.wait(); //Releases lock, and reacquires on wakeup
    ...// Perform action appropriate to condition
}
```
Note:
```
始终应该使用wait循环模式来调用wait方法;永远不要在循环之外调用wait方法.循环会在等待之前和之后测试条件
```

#######等待之前测试条件
```
等待之前测试条件,当条件已经成立时就跳过等待,这将可以确保活性(liveness).
如果条件已经成立,并且在线程等待之前,notify(或者nitifyAll)方法已经被调用,则无法保证该线程将会从等待中苏醒.
```
#######等待之后测试条件
```
等待之后测试条件,如果条件不成立的化继续等待,可以确保安全性(safety)
如果条件不成立的时候,如果线程继续执行,则可能会破坏被锁保护的约束关系
```
- 举例:
```
Note:当测试条件不成立时,下面的理由将会使一个线程苏醒过来
```
- 另一个线程可能已经得到了锁,并且从一个线程调用notify那一刻起,到等待线程苏醒过来的这段时间,得到锁的线程已经改变了受保护的状态
- 条件不成立,但是另一个线程可能意外地或恶意地调用notify
- 通知线程在唤醒等待线程时可能过度"大方".例如,即使只有某一些等待线程的条件已经被满足,但是通知线程可能仍然会调用notifyAll
- 在没有通知的情况下,等待线程也可能会苏醒.常称:伪唤醒.

#####notify和notifyAll使用
```
notify唤醒正在等待的线程,假设有这样的线程存在.而notifyAll唤醒的则是所有等待的线程
```
```
一种保守的做法是:总是使用nofityAll.因为它可以保证你将会唤醒所有需要被唤醒的线程.可能也会唤醒其他线程,
但这不影响程序的正确性,线程醒来后,会检查它们等待的条件,如果条件不满足,就会继续等待.
```
```
从优化的角度来说,如果处于等待状态的所有线程都在等待同一个条件,那么每次将只有一个线程从这个条件中被唤醒,应该选择调用notify,而不是notifyAll
```

#####总结
```
1. wait和notify非常难用,而java.util.concurrent提供更高级的语言,所以没有理由在新的代码中使用wait和notify.
```
```
2. 如果维护使用wait和notify的代码,务必确保始终是利用标准的模式从while循环内部调用wait.
一般情况下,优先使用notifyAll,而不是使用notify.
```

###第70条:线程安全性的文档化
```
当一个类的实例或者静态方法被并发使用的时候,需要说明该类在并发使用条件下的一系列的假设,和违反假设后,程序可能缺少足够的同步(66)或过度同步(67)
```
#####常见的线程安全性的几种级别
```
1. 不可变(immutable)----这个类的实例不可变的,所以,不需要外部的同步.例子:String,Long和BigInteger(15)
```
```
2. 无条件的线程安全(unconditionally thread-safe)----这个类的实例是可变的,但是这个类有足够的内部同步,所以,它的实例可以并发使用,无需任何外部同步.例子:Random和ConcurrentHashMap
```
```
3. 有条件的线程安全(conditionally thread-safe)----除了有些方法为进行安全的并发使用而需要外部同步之外,这种线程安全级别与无条件的线程安全相同.比如:迭代器(iterator),Collections.syschronized
```
```
4. 非线程安全(not thread-safe)----这个类的实例是可变的.并发地使用它们,客户必须利用自己选择的外部同步包围每个方法调用.例子:ArrayList和HashMap
```
```
5. 线程对立的(thread-hostile)----这个类不能安全地被多个线程并发使用,即使所有的方法调用都被外部同步包围.
线程对立的根源通常在于,没有同步地修改静态数据.这种类是因为没有考虑到并发性而产生的后果.
```
Note:
```
这些分类来自于<<Java Concurrent in Practice>>
```

#####使用私有锁对象,来代替一个公共可访问锁
```
使用一个公共可访问的锁对象,就意味着允许客户端以原子方式执行一个方法序列.这种灵活性可能导致性能收到影响,同时客户端还可以发起拒绝服务的攻击.
```
```
使用私有锁对象,可以避免这种拒绝服务攻击
```
```java
//Private lock object idiom - thwarts denial-of-service attack
private final Object lock = new Object();

public void foo(){
	synchronized(lock){
    
    }
}
```
Note:
```
这中私有锁对象不能被这个类的客户端程序访问,不可能妨碍对象的内部同步.我们应该把锁对象封装到它所同步的对象中(13)
```
```
注意lock域被声明为final的,应该保证其不变性.
```
```
必须注意的是:私有锁对象模式只能用在无条件的线程安全类上.有条件的线程安全类不能使用这种模式,因为客户端程序在有条件的线程安全情况下必须获得锁
```
```
私有锁对象特别适用于那些专门为继承而设计的类(17).
如果这种类对象使用它的实例作为锁对象,子类很可能无意中妨碍基类的操作.有时处于不同的目的而使用相同的锁,子类和基类可能会"相互绊住对方的脚"
```

#####总结
```
应当在文档中指明"哪些方法调用序列需要外部调用,以及在执行这些序列的时候要获得哪把锁"
```
```
如果编写无条件的线程安全类,应该考虑使用私有锁对象来代替同步方法.这样可以防止客户端程序和子类的不同步干扰.
```

###第71条:慎用延迟初始化
```
延迟初始化是延迟到需要域的值时才将它初始化的这种行为.这种方法既适合静态域,也适用于实例域.
虽然延迟初始化主要是一种优化,但它可以用来打破类和实例初始化的有害循环
```
```
延迟初始化像大多数优化一样,最好的建议"除非绝对必要,否则就不要这么做".
延迟初始化像一把双刃剑,它降低了初始化类或者创建实例的开销,却增加了访问被延迟初始化的域的开销.
```
```
延迟初始化有它的好处.如果域只在类的实例部分被访问,并且初始化这个域的开销很高,可能就值得进行延迟初始化.
```

#####多线程时,使用延迟初始化技巧.
```
如果两个或者多个线程共享一个延迟初始化的域,采用某种形式的同步是非常重要的,否则可能造成严重的Bug(66)
```
#######大多数情况下,正常初始化要优先于延迟初始化
```
1. 正常初始化的一个实例域.
```
- 举例:

```java
// Normal initialization of an instance field
private final FieldType filed = ComputeFieldValue();
```

```
2. 如果要利用延迟优化来破坏初始化的循环,就要使用同步访问方法
```
- 举例:

```java
// Lazy initialization of instance field - synchronized accessor
private FieldType field;

synchronized FieldType getField(){
	if(null == field){
    	field = computeFieldValue();
    }
    return field;
}
```

```
3. 推荐一种对静态域使用的延迟初始化:lazy initialization holder class
```
- 举例:

```java
// Lazy initialization holder class idiom for static fields
private static class FieldHolder{
	static final FieldType field = computeFieldValue();
}

static FieldType getField(){
	return FieldHolder.field;
}
```
Note:
```
这种方法非常优秀,保证同步访问.
```

```
4.  推荐一种对实例域使用的延迟初始化:双重检查模式
```
```
避免该域在初始化后,访问这个域时所带来的锁定开销(67).
利用两次检查模式:第一次检查有没有锁定,看看这个域是否被初始化;第二次检查时有锁定.
只有当第二次检查时表明这个域没有被初始化,才会调用computeFieldValue方法初始化.所以已经被初始化的就不会有锁定,域需要被声明为volatile
```
- 举例:

```java
//Double-check idiom for lazy initialization of instance fields
private volatile FieldType field;
FieldType getField(){
	FieldType result = field;
    if(null == result){   // First check (no locking)
    	synchronzied(this){
        	result = field;
            if(null == result){  //Second check (with locking)
            	field = result = computeFieldValue();
            }
        }
    }
    return result;
}
```

####### 使用局部变量result解释
```
这个变量的作用是确保field只在已经初始化的情况下读取一次,可以提升性能,给并发编程应用了一些标准.一般上述方法比没用局部变量的方法块25%
```

#######双重检查模式的变形:单重检查模式








