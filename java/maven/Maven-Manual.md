# Maven-Manual
[TOC]

### Maven 构建zip
```
├── bin
│   ├── start and other script...
├── conf
│   ├── config files...
├── lib
│   ├── library jars...
│   ├── runnable jar...
├── logs
└   └── log files...
```
##### Pom中提供profile文件配置
```xml
<profiles>
		<profile>
			<id>default</id>
			<properties>
				<props>collector</props>
			</properties>
			<activation>
				<activeByDefault>true</activeByDefault>
			</activation>
		</profile>
		<profile>
			<id>real</id>
			<properties>
				<props>collector.real</props>
			</properties>
		</profile>
	</profiles>
```

#####Pom中提供build配置
```xml
<build>
		<finalName>apm-data-collector</finalName>
		<filters>
			<filter>${props}.properties</filter>
		</filters>
		<resources>
			<resource>
				<directory>src/main/resources</directory>
				<includes>
					<include>**/*.properties</include>
				</includes>
				<filtering>true</filtering>
			</resource>
			<!-- 保证jar包中的xml依赖于properties文件，不写死 -->
		</resources>
		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-resources-plugin</artifactId>
				<version>2.6</version>
				<configuration>
					<encoding>UTF-8</encoding>
				</configuration>
			</plugin>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-jar-plugin</artifactId>
				<configuration>
					<excludes>
						<exclude>log4j.properties</exclude>
						<exclude>*.properties</exclude>
					</excludes>
					<manifestEntries>
						<Main-Class>org.vlis.dc.master.ZeromqBroker</Main-Class>
					</manifestEntries>
				</configuration>
			</plugin>
			<plugin>
				<artifactId>maven-assembly-plugin</artifactId>
				<configuration>
					<descriptors>
						<descriptor>src/main/assembly/assembly.xml</descriptor>
					</descriptors>
				</configuration>
				<executions>
					<execution>
						<id>make-my-jar-with-dependencies</id>
						<phase>package</phase>
						<goals>
							<goal>single</goal>
						</goals>
					</execution>
				</executions>
			</plugin>
		</plugins>
	</build>
```
##### 提供assembly.xml
```xml
<assembly
	xmlns="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.0"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.0 http://maven.apache.org/xsd/assembly-1.1.0.xsd">
	<id>server</id>
	<formats>
		<format>zip</format>
	</formats>
	<fileSets>
		<fileSet>
			<directory>${project.basedir}/src/main/script</directory>
			<outputDirectory>bin</outputDirectory>
            <fileMode>755</fileMode>
		</fileSet>
		<fileSet>
			<directory>${project.basedir}/src/main/resources</directory>
			<includes>
				<include>log4j.properties</include>
			</includes>
			<outputDirectory>config</outputDirectory>
		</fileSet>
		<fileSet>
			<directory>${project.basedir}/src/main/resources/monit-5.17.1</directory>
			<outputDirectory>ext/monit-5.17.1</outputDirectory>
		</fileSet>
	</fileSets>
	<dependencySets>
		<dependencySet>
			<outputDirectory>/lib</outputDirectory>
			<useProjectArtifact>true</useProjectArtifact>
			<scope>runtime</scope>
		</dependencySet>
	</dependencySets>
</assembly>
```

### 启动脚本
```sh
#!/bin/sh
for pid in $(ps -ef|grep ZeromqBroker|grep -v grep|cut -c 9-15);do
	kill -9 $pid
done

for i in `ls $ESCLIENT_HOME/lib/*.jar`; do
	CLASSPATH=$i:$CLASSPATH
done

nohup java -classpath $CLASSPATH -Xms512m -Xmx1024m  -XX:+HeapDumpOnOutOfMemoryError org.vlis.dc.master.ZeromqBroker $* &
```