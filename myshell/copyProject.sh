#! /bin/bash

#ssh -t -p 22 ppp@192.168.2.114 'rm -rf /home/ppp/Desktop/application/apm-da-client/lib/apm-data-analyzer-0.0.1-SNAPSHOT.jar' 
echo 'Delete apm-data-analyzer.jar success'

unzip /Users/thinking/Documents/workspace/apm/apm-data-analyzer/target/apm-da-client-2.1.zip

scp ./apm-da-client/lib/apm-data-analyzer-0.0.1-SNAPSHOT.jar ppp@192.168.2.114:/home/ppp/Desktop/application/apm-da-client/lib/

rm -rf ./apm-da-client

echo 'Copy apm-data-analyzer.jar success'