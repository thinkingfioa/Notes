# Java Maven
[TOC]

### Maven打包
##### 将一个jar,install进Maven库
```
mvn install:install-file -Dfile=youJarName.jar -DgroupId=stream.cube -DartifactId=your-jar -Dversion=1.0 -Dpackaging=jar
```
