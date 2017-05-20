# Curl命令

### Get命令
```
curl http://www.baidu.com?name=luweilin\&from=2017-05-18%2010:22:45\&to=2087%2008:70:18
```

### Post命令
```
curl --data "account=thinking&password=123456" http://192.168.30.29:1000/application/user/login
```

##### 登陆保存到cookie,然后查询其他信息
```
curl -c cookie.txt --data "account=thinking&passwd=123456" http://192.168.30.29:1000/application/user/login
curl -b cookie.txt http://192.168.30.29:1000/application/getAllInfo.
```
