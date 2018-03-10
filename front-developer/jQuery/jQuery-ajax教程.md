# jQuery的\$.ajax教程
```
@author 鲁伟林
一直开发后端，现在开始全栈培养自己。jQuery中，非常重要的的就是$.ajax的理解，本博客主要帮助初学者理解$.ajax到底怎么回事
参考网址是：http://www.cnblogs.com/tylerdonet/p/3520862.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/jQuery/
```
---

## 1. ajax的概念
ajax不是语言，而是一门能不需要重新加载页面，能够部分更新页面的一种强大的技术

## 2. jQuery的\$ajax用法
### 2.1 原理和概念
- 1.jQuery.ajax(options): 通过HTTP请求加载远程数据
- 2.ajax()返回其创建的XMLHttpRequest对象，大多数我们无需直接操作该对象
- 3.如果指定了dataType选项，请确保服务器返回正确的MIME信息(如xml返回的"text/xml")
- 4.ajax()只有一个参数，参数key/value对象，包含各配置及回调函数信息
- 5.jQuery1.2版本可以跨域加载JSON数据，需要将dataType选项设置为JSONP。

## 3. jQuery的\$ajax的参数列表
### 3.1 url(String)
发送请求的地址(默认：当前页地址)

### 3.2 type(String)
请求方式(如："POST"和"GET")，默认是"GET"

### 3.3 timeout(Nmber)
设置请求超时时间(毫秒)，此设置将覆盖全局设置

### 3.4 beforeSend(Function)
发送请求前可修改XMLHttpRequest对象的函数，如添加自定义HTTP头
##### 代码:
```html
beforeSend: function(request){
// do something
}
```

### 3.5 cache(Boolean)
是否将请求结果设置缓存(默认:true)，设置为false将不会从浏览器缓存中加载请求信息。开发初期，建议设置为false,否则不方便调试

### 3.6 complete(Function)
请求完成后回调函数(请求成功或失败时均调用)。参数: XMLHttpRequest对象，成功信息字符串
##### 代码:
```html
complete: function(request, textStatus){
// do something
}
```

### 3.7 contentType(String)
发送信息至服务器时内容编码类型，默认值适合大多数应用场合(默认:"application/x-www-form-urlencoded")

### 3.8 data(Object, String)
发送到服务器的数据。将自动转换为请求字符串格式，GET请求中将附加在URL后
##### 代码:
```html
data : {
	"executorAddress":executorAddress,
	"triggerTime":triggerTime,
	"logId":logId,
	"fromLineNum":fromLineNum
}
```

### 3.9 dataType(String)
定义服务器返回的数据类型，可用值:

- 1."xml": 返回XML格式数据，可用jQuery处理
- 2."html": 返回纯文本HTML格式数据，可包含script元素
- 3."script": 返回纯文本JavaScript代码。不会自动缓存结果
- 4."json": 返回JSON数据
- 5."jsonp": JSONP 格式。使用 JSONP 形式调用函数时，如 "myurl?callback=?" jQuery 将自动替换 ? 为正确的函数名，以执行回调函数。

### 3.10 error(Function)
请求失败时调用此方法。三个参数：XMLHttpRequest对象，错误信息，(可能)捕获的错误对象
##### 代码:
```html
error: function(request, textStatus, errorThrown){
// do....
}
```

### 3.11 global(Boolean)
是否触发全局AJAX事件(默认:true)。设置为false，将不会触发全局AJAX事件，用于控制不同的ajax事件

### 3.12 ifModified(Boolean)
仅在服务器数据改变时获取新数据。使用HTTP包Last-Modified头信息判断(默认：false)

### 3.13 processData(Boolean)
设置发送数据的信息格式(默认: true)，设置为true的时候发送数据将被转换为对象，以配合默认内容类型"application/x-www-form-urlencoded"

### 3.14 success(Function)
请求成功后回调函数。这个方法有两个参数: 服务器返回数据，返回状态
##### 代码:
```html
success: function(data, textStatus){
//data就是请求返回的对象，可以直接使用(.)来拿到属性
}
```

### 3.15 具体案例
```html

$.ajax({
    type : 'POST',
    url : base_url + '/joblog/logKill',
    data : {
        "executorAddress":executorAddress,
        "triggerTime":triggerTime,
        "logId":logId,
        "fromLineNum":fromLineNum
    },
    dataType : "json",
    success : function(data){
        if (data.code == 200) {
            layer.open({
                title: I18n.system_tips,
                btn: [ I18n.system_ok ],
                content: I18n.system_opt_suc ,
                icon: '1',
                end: function(layero, index){
                    logTable.fnDraw();
                }
            });
        } else {
            layer.open({
                title: I18n.system_tips,
                btn: [ I18n.system_ok ],
                content: (data.msg || I18n.system_opt_fail ),
                icon: '2'
            });
        }
    },
});
```

##### 解释:
- 1.layer.open({...});是显示出一个弹出层layer，类似于windows的对话框






















