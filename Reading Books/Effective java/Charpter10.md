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













