# Maven
[TOC]

## 1. Requirements
|  Maven Version |  JDK  |
|----------------|-------|
| 3.0 ~ 3.1.1    | JDK5+ |
| 3.2.1 ~ 3.2.5  | JDK6+ |
| 3.3.1 ~        | JDK7+ |

## 2. Setting
* conf/settings.xml

```xml
<!-- Default: ${user.home}/.m2/repository -->
<localRepository>/m2/repository</localRepository>
```

## 3. Commands
* clean
* package
* install
* deploy
* -dmaven.test.skip=true

常用命令组合
- mvn clean install(打包命令)
- mvn clean compile -U -e(编译，同时强行跟新本地jar包)


## 4. Scope
* compile 缺省值，会随着项目一起发布。 
* provided 容器或JDK已提供范围，不会随项目发布
* runtime编译时不需要，运行的时候才需要，  JDBC API Jar
* test 只在测试时使用，不会随项目发布
* system 类似provided，采用本地jar包

## 5. Modules
* 父项目

```xml
<groupId>xxx.yyy</groupId>
<artifactId>zzz</artifactId>
<version>0.0.1-SNAPSHOT</version>
<packaging>pom</packaging>

<modules>
	<module>moduleA</module>
</modules>

<properties>
	<xxx.version>0.0.1</xxx.version>
</properties>

<dependencyManagement>
	<dependencies>
		<dependency>
			<groupId>xxx.yyy</groupId>
			<artifactId>xxx</artifactId>
			<version>${xxx.version}</version>
		</dependency>
	</dependencies>
</dependencyManagement>

<build>
	<!-- 插件声明但不加载，可由子Module继承使用 -->
	<pluginManagement>
		<plugins>
			<plugin>...</plugin>
		</plugins>
	</pluginManagement>
	<!-- 插件声明加载 -->
	<plugins>
		<plugin>...</plugin>
	</plugins>
</build>
```

* 子项目

```xml
<parent>
	<groupId>xxx.yyy</groupId>
	<artifactId>zzz</artifactId>
	<version>0.0.1-SNAPSHOT</version>
</parent>
<artifactId>moduleA</artifactId>
<!-- 常用的格式：jar/war，隐藏默认为jar -->
<packaging>jar</packaging>
```

## 6. Plugins
### 6.1 maven-compiler-plugin
* [配置参数链接](http://maven.apache.org/plugins/maven-compiler-plugin/compile-mojo.html)

```
<plugin>
	<groupId>org.apache.maven.plugins</groupId>
	<artifactId>maven-compiler-plugin</artifactId>
	<configuration>
		<!-- 源代码编译版本 -->
		<source>1.6</source>
		<!-- 目标平台编译版本 -->
		<target>1.6</target>
		<encoding>UTF-8</encoding>
		<fork>true</fork>
		<executable>${jdk.home}/bin/javac</executable>
		<compilerVersion>1.6</compilerVersion>
	</configuration>
</plugin>
```

### 6.2 maven-resources-plugin
[配置参数链接](http://maven.apache.org/plugins/maven-resources-plugin/resources-mojo.html)
```
<!-- 切换Profile用 -Preal -->
<profiles>
	<profile>
		<id>default</id>
		<properties>
			<!-- 指定${props}的值，用于build下的filter使用 -->
			<props>analytics</props>
		</properties>
		<activation>
			<!-- 默认使用当前Profile -->
			<activeByDefault>true</activeByDefault>
		</activation>
	</profile>
	<profile>
		<id>real</id>
		<properties>
			<props>analytics.real</props>
		</properties>
		<activation>
			<activeByDefault>false</activeByDefault>
		</activation>
	</profile>
</profiles>

<build>
	<filters>
		<filter>${props}.properties</filter>
	</filters>
	<resources>
		<resource>
			<directory>src/main/java</directory>
			<!-- 不添加指定目录下的某些文件 -->
			<excludes>
				<exclude>**/*.java</exclude>
			</excludes>
		</resource>
		<resource>
			<directory>src/main/resources</directory>
			<!-- 添加指定目录下的某些文件 -->
			<includes>
				<include>**/*.properties</include>
				<include>**/*.xml</include>
			</includes>
			<!-- 占位符替换 -->
			<filtering>true</filtering>
		</resource>
	</resources>

	<plugin>
		<groupId>org.apache.maven.plugins</groupId>
		<artifactId>maven-resources-plugin</artifactId>
		<configuration>
			<encoding>UTF-8</encoding>
		</configuration>
	</plugin>
</build>
```

### 6.3 maven-jar-plugin
[配置参数链接](http://maven.apache.org/components/plugins/maven-jar-plugin/jar-mojo.html)
```
<plugin>
	<groupId>org.apache.maven.plugins</groupId>
	<artifactId>maven-jar-plugin</artifactId>
	<configuration>
		<archive>
			<!-- 不对外公布jar包依赖的pom文件 -->
			<addMavenDescriptor>false</addMavenDescriptor>
			<manifestEntries>
				<Project-Name>${project.name}</Project-Name>
				<Project-Version>${project.version}</Project-Version>
				<!-- 指定Jar包的启动类 -->
				<Main-Class>org.vlis.apm.xxx.A</Main-Class>
			</manifestEntries>
		</archive>
		<excludes>
			<!-- 打包的时候不把这些配置文件打进jar包 -->
			<exclude>log4j.properties</exclude>
			<exclude>xxx.properties</exclude>
		</excludes>
	</configuration>
</plugin>
```

### 6.4 maven-assembly-plugin
```xml
<plugin>
	<artifactId>maven-assembly-plugin</artifactId>
	<configuration>
		<descriptors>
			<descriptor>src/main/assembly/assembly.xml</descriptor>
		</descriptors>
	</configuration>
	<executions>
		<execution>
			<id>make-assembly</id>
			<phase>package</phase>
			<goals>
				<goal>single</goal>
			</goals>
		</execution>
	</executions>
</plugin>
```
* assembly.xml [配置参数链接](http://maven.apache.org/components/plugins/maven-assembly-plugin/assembly.html)
```xml
<assembly
	xmlns="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.0"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.0 http://maven.apache.org/xsd/assembly-1.1.0.xsd">
	<id>server</id> <!-- 打包后缀 -->
	<formats>
		<format>zip</format> <!-- 打包格式 -->
	</formats>
	<fileSets>
		<fileSet>
			<directory>${project.basedir}</directory>
			<outputDirectory>/</outputDirectory>
			<includes>
				<include>README*</include>
				<include>LICENSE*</include>
				<include>NOTICE*</include>
			</includes>
		</fileSet>
		<fileSet>
			<directory>${project.basedir}/src/main/script</directory>
			<outputDirectory>bin</outputDirectory> <!-- 脚本打包到bin文件夹下 -->
		</fileSet>
		<fileSet>
			<directory>${project.basedir}/target/classes</directory>
			<includes>
				<include>*.properties</include>
				<include>*.xml</include>
			</includes>
			<outputDirectory>config</outputDirectory> <!-- 配置文件打包到config文件夹下 -->
		</fileSet>
	</fileSets>
	<dependencySets>
		<dependencySet>
			<outputDirectory>/lib</outputDirectory>  <!-- 依赖的jar打包到lib文件夹下 -->
			<useProjectArtifact>true</useProjectArtifact>
			<scope>runtime</scope>
		</dependencySet>
	</dependencySets>
</assembly>
```

### 6.5 maven-shade-plugin
[配置参数链接](https://maven.apache.org/plugins/maven-shade-plugin/shade-mojo.html)
```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-shade-plugin</artifactId>
  <executions>
    <execution>
      <phase>package</phase>
      <goals>
        <goal>shade</goal>
      </goals>
      <configuration>
        <relocations>
          <relocation>
            <pattern>org.codehaus.plexus.util</pattern>
            <shadedPattern>org.shaded.plexus.util</shadedPattern>
            <excludes>
              <exclude>org.codehaus.plexus.util.xml.Xpp3Dom</exclude>
              <exclude>org.codehaus.plexus.util.xml.pull.*</exclude>
            </excludes>
          </relocation>
        </relocations>
      </configuration>
    </execution>
  </executions>
</plugin>
```
### 6.6 maven-surefire-plugin
[配置参数链接](http://maven.apache.org/components/surefire/maven-surefire-plugin/test-mojo.html)
```xml
<!-- 首先需引入testng或Junit框架 -->
<dependencies>
	<dependency>
		<groupId>org.testng</groupId>
		<artifactId>testng</artifactId>
		<scope>test</scope>
	</dependency>
	<!--
	<dependency>
		<groupId>junit</groupId>
		<artifactId>junit</artifactId>
		<scope>test</scope>
	</dependency>
	-->
</dependencies>

<plugin>
	<groupId>org.apache.maven.plugins</groupId>
	<artifactId>maven-surefire-plugin</artifactId>
	<configuration>
		<skip>false</skip>
		<includes>
			<include>org/vlis/apm/analysis/ATest.class</include>
			<include>org/vlis/apm/analysis/BTest.class</include>
		</includes>
		<excludes>
			<exclude>**/CTest.class</exclude>
		</excludes>
	</configuration>
</plugin>
```

###  6.7 maven-jgit-buildnumber-plugin
[使用链接](https://github.com/alx3apps/jgit-buildnumber)
```
<plugin>
	<groupId>ru.concerteza.buildnumber</groupId>
	<artifactId>maven-jgit-buildnumber-plugin</artifactId>
	<executions>
		<execution>
			<id>git-buildnumber</id>
			<goals>
				<goal>extract-buildnumber</goal>
			</goals>
			<phase>prepare-package</phase>
		</execution>
	</executions>
</plugin>
```

###  6.8 proguard-maven-plugin
[使用链接](http://wvengen.github.io/proguard-maven-plugin/proguard-mojo.html)
```xml
<plugin>
	<groupId>com.github.wvengen</groupId>
	<artifactId>proguard-maven-plugin</artifactId>
	<version>2.0.8</version>
	<executions>
		<execution>
			<phase>package</phase>
			<goals>
				<goal>proguard</goal>
			</goals>
		</execution>
	</executions>
	<configuration>
		<libs>
			<lib>${jdk.home}/jre/lib/rt.jar</lib>
			<lib>${jdk.home}/jre/lib/jce.jar</lib>
		</libs>
		<injar>${project.build.finalName}.jar</injar>
		<outjar>${project.build.finalName}-pg</outjar>
		<obfuscate>true</obfuscate>
		<attach>true</attach>
		<attachArtifactClassifier>pg</attachArtifactClassifier>
		<addMavenDescriptor>false</addMavenDescriptor>
		<proguardInclude>src/main/config/proguard.conf</proguardInclude>
		<options>
			<!-- 忽略所有告警 -->
			<!-- <option>-ignorewarnings</option> -->
			<!-- 不做压缩 -->
			<option>-dontshrink</option>
			<!-- 不优化输入的类文件 -->
			<option>-dontoptimize</option>
			<!-- 混淆时不会产生形形色色的类名 -->
			<option>-dontusemixedcaseclassnames</option>
			<!-- 指定不去忽略非公共的库类 -->
			<option>-dontskipnonpubliclibraryclasses</option>
			<!-- 指定不去忽略包可见的库类的成员 -->
			<option>-dontskipnonpubliclibraryclassmembers</option>
			<!-- 输出生成信息 -->
			<option>-verbose</option>
			<!-- 保持源码名与行号（异常时有明确的栈信息），注解（默认会过滤掉所有注解，会影响框架的注解） -->
			<option>-keepattributes
				Signature,Deprecated,SourceFile,LineNumberTable,*Annotation*</option>
			<!-- 保持包注解类 -->
			<option>-keep class **.package-info</option>
		</options>
	</configuration>
	<dependencies>
		<dependency>
			<groupId>net.sf.proguard</groupId>
			<artifactId>proguard-base</artifactId>
			<version>4.11</version>
			<scope>runtime</scope>
		</dependency>
	</dependencies>
</plugin>

<!-- JDK5 -->
<plugin>
	<groupId>com.pyx4me</groupId>
    <artifactId>proguard-maven-plugin</artifactId>
    <version>2.0.4</version>
</plugin>
```

* 常用语法
```
-keep interface com.clock.api.**{*;} // 不混淆com.clock.api包下的接口
-keep class com.clock.bean.**{*;}//不混淆所有的com.clock.bean包下的类和这些类的所有成员变量
-keep class * extends com.clock.api.AbstractClass {//不混淆所有的继承自AbstractClass类的子类名和方法test
	public void test(java.lang.String);
}
//不混淆Serializable接口的子类中指定的某些成员变量和方法
-keepclassmembers class * implements java.io.Serializable {
    static final long serialVersionUID;
    private static final java.io.ObjectStreamField[] serialPersistentFields;
    private void writeObject(java.io.ObjectOutputStream);
    private void readObject(java.io.ObjectInputStream);
    java.lang.Object writeReplace();
    java.lang.Object readResolve();
}
```

###  6.9 versions-maven-plugin
[指令使用链接](http://www.mojohaus.org/versions-maven-plugin/plugin-info.html)
> mvn versions:set -DnewVersion=1.0.1

```xml
<plugin>
	<groupId>org.codehaus.mojo</groupId>
	<artifactId>versions-maven-plugin</artifactId>
</plugin>
```

### 6.10 maven-release-plugin
* setting.xml

```xml
<!-- 此处帐号需要有nexus上传jar包权限 -->
<servers>
	<server>
		<id>releases</id>
		<username>deployment</username>
		<password>123456</password>
	</server>
    <server>
		<id>snapshots</id>
		<username>deployment</username>
		<password>123456</password>
	</server>
</servers>
```
* pom.xml

```xml
<!-- nexus 发布地址，id与setting.xml下的id一致 -->
<distributionManagement>
	<repository>
		<id>releases</id>
		<name>Nexus Repository</name>
		<url>http://xxx.xxx.xxx.xxx:yyyy/nexus/content/repositories/releases/</url>
	</repository>
	<snapshotRepository>
		<id>snapshots</id>
		<name>Nexus Repository</name>
		<url>http://xxx.xxx.xxx.xxx:yyyy/nexus/content/repositories/snapshots/</url>
	</snapshotRepository>
</distributionManagement>
<scm>
	<!-- 项目git路径 -->
	<developerConnection>scm:git:http://xxx.xxx.xxx.xxx:yyyy/git/test.git</developerConnection>
	<tag>HEAD</tag>
</scm>

<plugins>
	<plugin>
		<groupId>org.apache.maven.plugins</groupId>
		<artifactId>maven-release-plugin</artifactId>
		<configuration>
			<!-- git帐号 -->
			<username>scm</username>
			<password>scm123</password>
			<!-- Tag名 -->
			<tagBase>${project.artifactId}-${project.version}</tagBase>
			<goals>-f pom.xml deploy</goals>
			<!-- 不使用默认的profile -->
			<useReleaseProfile>false</useReleaseProfile>
			<!-- 所有模块的发布版本以及新的SNAPSHOT开发版本都保持一致 -->
			<autoVersionSubmodules>true</autoVersionSubmodules>
			<checkModificationExcludes>
				<checkModificationExclude>.project</checkModificationExclude>
				<checkModificationExclude>.settings</checkModificationExclude>
				<checkModificationExclude>.classpath</checkModificationExclude>
				<checkModificationExclude>**\.project</checkModificationExclude>
				<checkModificationExclude>**\.settings</checkModificationExclude>
				<checkModificationExclude>**\.classpath</checkModificationExclude>
				<checkModificationExclude>**\target</checkModificationExclude>
			</checkModificationExcludes>
		</configuration>
	</plugin>
<plugins>
```

* 使用指令

```
mvn release:clean
	release:prepare
	-Dmaven.test.skip=true
	-DdevelopmentVersion=0.0.2-SNAPSHOT
	-DreleaseVersion=0.0.1
	-Dtag=release-build-0.0.1
	release:perform
```

* 先打一个project-0.0.1的Tag分支，版本号替换为project-0.0.1
* 将project-0.0.1.pom和project-0.0.1.jar上传到nexus上
* 当前分支版本号替换为0.0.2-SNAPSHOT

## 7. Issues
### 7.1 apm打包失败
* etc/profile
```
export JDK5_HOME=/usr/local/java/jdk1.5.0_22
export JDK6_HOME=/usr/local/java/jdk1.6.0_45
export JDK7_HOME=/usr/local/java/jdk1.7.0_80
```
### 7.2 apm混淆配置
* apm-extension

```xml
<groupId>org.vlis</groupId>
<artifactId>apm-agent</artifactId>
<version>${project.version}</version>
<classifier>pg</classifier>
```
* apm-trace

```xml
<groupId>org.vlis</groupId>
<artifactId>apm-agent</artifactId>
<version>${project.version}</version>
<classifier>pg</classifier>
```

### 7.3 apm和uam依赖hc-core
```
<!-- 将包上传到nexus上，被依赖的项目使用 -->
<repositories>
	<repository>
		<id>thirdparty</id>
		<url>http://xxx.xxx.xxx.xxx:yyyy/nexus/content/repositories/thirdparty/</url>
	</repository>
</repositories>

<dependencies>
	<dependency>
		<groupId>org.vlis</groupId>
		<artifactId>hc-core</artifactId>
		<version>${hc-core.version}</version>
	</dependency>
</dependencies>
```

### 7.4 apm-da-analyze和apm-es-server依赖的license-verfiy依赖uam-es-client
* 去除对uam-es-client的依赖

```xml
<!--
<dependency>
	<groupId>org.vlis</groupId>
	<artifactId>uam-es-client</artifactId>
	<version>1.0.0-SNAPSHOT</version>
</dependency>
-->
```

* 对es查询的部分提供接口

```java
public interface ISearch {
	public int getAllAgentNumber(String from, String to);
	
	public String getLastRecordTime();
}
```

* 原查询部分用接口替代

```java
public static int b(ISearch search, String xxx, ...) {
}
```
* 由apm-da-analyze和apm-es-server负责实现该接口

```java
public class LicenseSearch implements ISearch {
	//...
}
```

### 7.5 子Module如何抽取成独立项目
* 去除Module

```xml
<!--
  <parent>
      <groupId>xxx.yyy</groupId>
      <artifactId>zzz</artifactId>
      <version>0.0.1-SNAPSHOT</version>
  </parent>
-->
```

* 添加groupId和version

```xml
<groupId>xxx.yyy</groupId>
<version>0.0.1-SNAPSHOT</version>
```

* 将父类的版本号移到当前pom的dependency中

```xml
<dependency>
    <groupId>xxx.yyy</groupId>
    <artifactId>xxx</artifactId>
    <version>1.0.1</version>
</dependency>
```

* Plugin配置也需移到当前的pom中

```xml
<plugins>
  <plugin>
    <groupId>a.b.c</groupId>
    <artifactId>aaa</artifactId>
    <version>xxx.xxx.xxx</version>
    <configuration>...</configuration>
  </plugin>
</plugins>
```

