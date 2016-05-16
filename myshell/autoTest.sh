#! /bin/bash

JMETER_PID=`ps -aux|grep /root/apache-jmeter-2.13/bin/ApacheJMeter.jar|awk '{print $2}'`
echo " jmeter_pid + $JMETER_PID" 

#REMOTE_CMD="pkill -f tomcat;cd /root/apache-tomcat-7.0.68/bin; ./catalina.sh start"
if [ -n "$JMETER_PID" ] ; then
	pkill -f "jmeter"
else
	echo "jmeter is not alive"
fi

scp sun@10.10.105.81:/home/sun/mylib/apm/* ./apm

scp sun@10.10.105.81:/home/sun/workspace/java_workspace/TestWebApp/target/TestWebApp-1.0.war ./web
scp ./web/* root@10.10.101.34:/root/apache-tomcat-7.0.68/webapps


#scp ./apm/* root@10.10.101.34:/root/apache-tomcat-7.0.68/apm/all_on

ssh root@10.10.101.34 "pkill -f tomcat"
ssh root@10.10.101.34 "source /etc/profile;cd /root/apache-tomcat-7.0.68/bin; ./catalina.sh start"

if [ -f "testFile.jtl" ] ; then
	rm testFile.jtl
fi
jmeter -n -t threadpool.jmx -l threadpool.jtl &
