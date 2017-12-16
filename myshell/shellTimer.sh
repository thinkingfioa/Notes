#!/bin/bash

pid=$1
fileName="mjvm"+${pid}+".txt"
echo $pid

interval=0.5 # unit s
while [[ true ]]; do
	echo $(date +"%y-%m-%d %H:%M:%S") >> ${fileName}
        gcM=`jstat -gc ${pid}` # fetch into
        #eval ${gcM}
        echo $gcM >> ${fileName}
	sleep $interval
done
