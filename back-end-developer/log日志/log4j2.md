# log4j2 日志使用和共享
```
@author 鲁伟林
工作量:
1. log4j2 是一个高性能日志系统。Java日志系统，首选log4j2。
2. 网上关于log4j2配置信息非常多，但鱼龙混杂，在加上某度的搜索功能，不敢恭维。许多博客，就是把英文版log4j2翻译一通，自己都不一定能跑起来。
3. 本文共享我工作中使用的log4j2配置，帮助各位满足项目中日志输出
4. log4j2配置提供了异步和同步日志输出
5. 日志输出分不同的级别，分别输出到不同的文件中
6. 日志文件利用日志文件个数和日志文件大小控制，防止日志过多消耗机器磁盘空间
gitHub地址:https://github.com/thinkingfioa/netty-learning/tree/master/netty-private-protocol
欢迎各位Follow
```
---

### 踩过的坑 - (阅读本博客解决）
- 1.配置的日志输出格式(log_pattern)，无效
- 2.日志不往日志文件中输出。日志文件的大小size一直为0
- 3.不会将日志分级别输出到不同的文件中
- 4.日志严格控制日志文件个数和日志文件的大小，防止磁盘满了
- 5.使用log4j2日志异步输出模式，提高日志输出性能

## 1. 共享log4j2配置
给大家共享下我的log4j2的配置

##### 代码:
```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="OFF">
    <properties>
        <!--  -->
        <property name="log_pattern">%d{yyyy-MM-dd HH:mm:ss.SSS} [%t] %-5level %C{1}.%M(%F:%L) - %msg%n</property>
        <property name="log_home">~/logs/netty-learning</property>
        <property name="file_name">netty-private-protocol</property>
        <property name="every_file_size">20M</property>
        <property name="output_log_level">debug</property>
        <property name="file_count">20</property>
        <property name="error_file_count">3</property>
    </properties>

    <Appenders>
        <Console name="Console" target="SYSTEM_OUT">
            <ThresholdFilter level="trace" onMatch="ACCEPT" onMismatch="DENY"/>
            <PatternLayout pattern="${log_pattern}"/>
        </Console>
        <!-- RollingFile -->
        <RollingFile name="RollingFile" fileName="${log_home}/${file_name}.log" filePattern="${log_home}/${file_name}-%d{yyyy-MM-dd}-%i.log">
            <PatternLayout pattern="${log_pattern}"/>
            <SizeBasedTriggeringPolicy size="${every_file_size}"/>
            <DefaultRolloverStrategy max="${file_count}"/>
            <Filters>
                <ThresholdFilter level="error" onMatch="ACCEPT" onMismatch="NEUTRAL"/>
                <ThresholdFilter level="warn" onMatch="ACCEPT" onMismatch="NEUTRAL"/>
                <ThresholdFilter level="info" onMatch="ACCEPT" onMismatch="NEUTRAL"/>
                <ThresholdFilter level="trace" onMatch="ACCEPT" onMismatch="DENY"/>
            </Filters>
        </RollingFile>
        <!-- RollingRandomAccessFile -->
        <RollingFile name="RollingFile1" fileName="${log_home}/${file_name}-error.log" filePattern="${log_home}/${file_name}-error-%d{yyyy-MM-dd}-%i.log">
            <SizeBasedTriggeringPolicy size="${every_file_size}"/>
            <DefaultRolloverStrategy max="${error_file_count}"/>
            <Filters>
                <ThresholdFilter level="error" onMatch="ACCEPT" onMismatch="NEUTRAL"/>
                <ThresholdFilter level="warn" onMatch="ACCEPT" onMismatch="DENY"/>
            </Filters>
            <PatternLayout pattern="${log_pattern}"/>
        </RollingFile>
    </Appenders>

    <Loggers>

		 <!--  此处的name="org.lwl"必须要改，否则日志无法输出到文件中。定义的格式也不对 -->
		 <!-- 请将name="org.lwl"改成: name="你的项目包前缀" -->
        <!-- log4j2 asyn more fast-->
        <AsyncLogger name="org.lwl" level ="${output_log_level}" additivity="false" includeLocation="true">
            <appender-ref ref="RollingFile"/>
            <appender-ref ref="RollingFile1"/>
            <appender-ref ref="Console"/>
        </AsyncLogger>

        <!-- log4j2 Synchronous --> -->
        <!-- <root level="${output_log_level}">
            <appender-ref ref="RollingFile"/>
            <appender-ref ref="RollingFile1"/>
            <appender-ref ref="Console"/>
        </root> -->
    </Loggers>
</Configuration>
```

### 1.1 我的log4j2配置解释
- 1.标签\<properites\>中配置了一些基本属性。提醒各位"log_pattern"值得是日志输出格式，建议使用和我一样的"log_pattern"。当需要排查问题，查看日志时会感谢我的。
- 2.我的log4j2配置，是会分日志级别输出到不同的文件。日志级别为:info和debug输出到文件为:${file_name}.log文件中。日志级别为:error输出到${file_name}-error.log
- 3.日志文件存放在目录: ~/logs/netty-learning
- 4.log4j2提供同步日志输出和异步日志输出，我的log4j2配置在结尾部分，都分别给出。
- 5.经过测试，可以发现: AsyncLogger(异步)的确比root(同步)快很多

### 1.2 使用我的log4j2配置需要改动点
如果使用我的log4j2配置，基本需要改的都在标签\<properties\>中，相信大家一看就懂。

### 1.3 一定要改的点，特别提醒，大坑
- 1.lgo4j2有一个非常恶心的地方，我花费了很长时间才发现。我的配置中，在配置文件结尾，属性\<AsyncLogger\>中的: name="org.lwl"，请务必改成：name="你项目包前缀"。
- 2.否则，日志将写不进文件中，日志文件大小一直为0。且定义的${log_patter}也无效

### 1.3 Demo
具体项目参考地址: [log4j2](https://github.com/thinkingfioa/netty-learning/tree/master/netty-private-protocol)

##### 代码:
```
package org.lwl.netty;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class NettyClient {
    private static final Logger LOGGER = LogManager.getLogger(NettyClient.class);

	public static void main(String [] args) {
		LOGGER.info("Hello {}", "log4j2");
   }
}
```

### 2. log4j2日志同步输出
如果使用log4j2同步输出，请打开配置中下面这段代码:

##### 代码:
```
<!-- log4j2 Synchronous --> -->
<!-- <root level="${output_log_level}">
    <appender-ref ref="RollingFile"/>
    <appender-ref ref="RollingFile1"/>
    <appender-ref ref="Console"/>
</root> -->
```

##### Maven依赖:
```xml
<!-- log4j2 -->
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-core</artifactId>
    <version>2.10.0</version>
</dependency>
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-api</artifactId>
    <version>2.10.0</version>
</dependency>
<!-- log4j2 end. -->
```

### 3. log4j2日止异步输出
如果使用lo4j2异步输出，请使用下列代码:

##### 代码:
```
<!-- log4j2 asyn more fast-->
<AsyncLogger name="org.lwl" level ="${output_log_level}" additivity="false" includeLocation="true">
    <appender-ref ref="RollingFile"/>
    <appender-ref ref="RollingFile1"/>
    <appender-ref ref="Console"/>
</AsyncLogger>
```

##### Maven依赖
log4j2的异步输出，使用了无锁队列: disruptor。所以maven需要添加其依赖。

```xml
<!-- log4j2 -->
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-core</artifactId>
    <version>2.10.0</version>
</dependency>
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-api</artifactId>
    <version>2.10.0</version>
</dependency>
<dependency>
    <groupId>com.lmax</groupId>
    <artifactId>disruptor</artifactId>
    <version>3.3.7</version>
</dependency>
<!-- log4j2 end. -->
```

