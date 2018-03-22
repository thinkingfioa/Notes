# CSS-Position用法的理解
```
@author 鲁伟林
CSS语法中，对于position的使用一直搞不清楚，特写此博客，帮助自己理解和记忆
gitHub地址: https://github.com/thinkingfioa/
```

## CSS中的定位(position)

### 1. position的定义
允许用户精确定义元素框出现的相对位置。可以是相对于它通常出现的位置，相对于其上级元素，相对于另一个元素，或者相对于浏览器视窗本身。

### 2. position的属性值
position属性指定了元素的定位类型。position属性的四个值。static和relative在文档流中，与fixed和absolute相反。

- 1.static  
- 2.relative
- 3.fixed
- 4.absolute

### 2.1 static
- 1.static是position的缺省值，一般不设置position属性时，默认是static。
- 2.静态定位元素(static)不会受到top，bottom，left，right影响

### 2.2 relative
- 1.相对本身位置的偏移(static定位下的元素位置为本身位置)。
- 2.受到top、bottom、left、right影响
- 3.且不会影响后面其他元素的位置。
- 4.原本空间不会改变(static和relative在文档流中，与fixed和absolute相反)

### 2.3 fixed
fixed是特殊的absolute，即fixed总是以浏览器的可视窗口(屏幕内网页窗口)进行定位。不占据空间

### 2.4 absolute
当一个元素A设置了position:absolute后，分为两种情况:

- 1.当元素A的父对象设置了position属性，且position的属性值为absolute或relative或fixed，也就是说不是默认的，则元素A按照父对象来定位。如果父对象设置了margin、border、padding等属性，则元素A将会从padding开始的地方进行定位

- 2.如果元素A没有一个position属性的父对象，则以body为定位对象

### 3. 参考文档
[参考1](https://www.cnblogs.com/cby-love/archive/2016/04/08/5366274.html)
[参考2](https://www.cnblogs.com/mogu-xiaonao/p/5380603.html)

















