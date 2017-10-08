# SQL必知必会_4

### 第2课 检索数据

##### 2.3 检索多个列
select column1, column2, column3 from tableName;

##### 2.4 检索所有的列 
select * from products;

```
注：
1. 缺点：使用通配符(*)，除非确实需要查询表的每一列，否则可能会降低检索和应用的性能.
2. 优点：能检索出表的不明确的列。
```

##### 2.5 检索不同的值
select distinct vend_id from products;

```
注:
1. distinct关键字作用于作用于其后的所有的列，不仅仅是其后的一列。
2. 如：select distinct vend_id,prod_price from products;那么这两列vend_id, prod_price都同，才会合并。
```

##### 2.6 限制结果
- select prod_name from products limit 5; 返回结果只有5行。
- select prod_name from products limit 5 offset 5; 返6,7,8,9,10这5行数据。

```
注:
1. 第一个被检索的行是第0行，而不是第1行。因此，LIMIT 1 OFFSET 1会检索第2行，而不是第1行.
2. MySQL和MariaDB支持简化版的LIMIT 4 OFFSET 3语句，即LIMIT 3,4。
```

##### 2.7  使用注释
1. 单行注释: #
2. 多行注释: /*. ...  */

### 第3课 排序检索数据
```
使用Select子句的Order by子句，根据需要检索排序出的数据
```

##### 3.1 排序数据
使用Order by语句排序Select检索出来的语句， Order by子句取一个或多个列的名字。

select prod_name, prod_price from products order by prod_price;
```
注：Order by子句， 必须是select的最后一条语句。
```

##### 3.2 按多个列排序
select prod_name, prod_price, prod_id from products order by prod_price, prod_name;

##### 3.3 按列位置排序
select prod_name, prod_price, prod_id from products order by 2, 3;
```
注:
1. order by 后面可以接数字，比如：2代表的是prod_price, 3代表的是prod_id。不推荐使用这种方式。
```

##### 3.4 指定排序方向
ASC 升序(默认)，DESC 降序。

- select prod_name, prod_price, prod_id from products order by prod_price DESC, prod_name;
- 如果DESC降序，必须对所有需要降序的列都要加上。

### 第4课 过滤数据

##### 4.2.3 范围值检查

- select prod_name, prod_price, prod_id from products where prod_price between 4 and 10;
 
##### 4.2.4 空值检查

 - select * from customers where cust_email is NULL; 空判断过滤数据
 - select * from customers where cust_email is not NULL; 非空判断过滤数据
 
### 第5课 高级数据过滤

##### 5.1.3 组合where子句
1. OR操作符和AND操作符。

```
select prod_name, prod_price, vend_id from products where vend_id = '1001' OR vend_id = '1005' and prod_price >= 10;
```

结果：

|prod_name|prod_price|vend_id|
|:---:|:---:|:---:|
| .5 ton anvil |       5.99 |    1001 |
| 1 ton anvil  |       9.99 |    1001 |
| 2 ton anvil  |      14.99 |    1001 |
| JetPack 1000 |      35.00 |    1005 |
| JetPack 2000 |      55.00 |    1005 |

分析：
```
OR操作符和AND操作符优先级不同。AND操作符的优先级 > OR操作符的优先级。所以上面的sql变成了:
select prod_name, prod_price, vend_id from products where vend_id = '1001' OR (vend_id = '1005' and prod_price >= 10 );
```

##### 5.2 IN操作符
- select prod_name, prod_price, vend_id from products where vend_id in ('1001', '1003') order by prod_price DESC;

IN操作符的优点

1. IN操作符一般比一组OR操作符更快
2. IN最大的优点是：可以包含其他SELECT语句，能够动态的建立WHERE子句。

##### 5.3 NOT操作符
Not操作符用作否定其后所跟的任何条件。

-  select * from products where Not vend_id = 1001 and prod_name = 'Safe';

|prod_id|vend_id|prod_name|prod_price|prod_desc|
|:---:|:---:|:---:|:---:|:---:|
|SAFE|1003|Safe|50.00|Safe with combination lock|
注：Not在这里只能作用与vend_id. 

### 第6课 使用通配符进行过滤

##### 6.1.1 百分号(%)通配符
在搜索串中，%表示任何字符出现任意次数。代表搜索模式中给定位置0个，1个，多个字符。排除匹配NULL的行。

- select prod_id, prod_name from products where prod_name like 'Jet%';
 
##### 6.1.2 下划线(_)通配符
在搜索串中，下划线(_)只匹配单个字符，而不是多个字符。只能是一个字符。

- select prod_id, prod_name from products where prod_name like 'JetPack _000';
 
##### 6.1.3 方括号([])通配符
只有微软的Access和SQL server支持。

##### 6.2 使用通配符的技巧
1. 要知道，使用通配符可能比其他的搜索耗费更长的时间，对数据库的压力更大。
2. 不要过度使用通配符，在其他操作符能达到效果的情况下，尽量不要使用通配符。
3. 尽量不要把通配符放在搜索模式的开始处，把通配符置于开始处，搜索起来最慢的。

### 第7课 创建计算字段

##### 7.1 计算字段
计算字段是运行时在SELECT语句内创建的。不同于数据库中表的列

##### 7.2 拼接字段
将表中的列数据，拼接到一起。将值联结在一起(将一个值附加到另一个值), 构成单个值。如：prod_name(prod_price).

```
拼接的操作符:
1. Access和SQL Server使用+号
2. DB2、Oracle、PostgreSQL、SQLite和Open Office Base使用||
3. MySQL和MariaDB中，必须使用特殊的函数。eg: concat(prod_name, '(', prod_price, ')')
```
```
Trim函数
1. RTRIM(String)函数去掉字符串右边的空格。
2. LTRIM(String)函数去掉字符串左边的空格。
3. TRIM(String)函数去掉字符串左边和右边空格。
```
```
As别名。重新为列起一个新的名字。
1.  select concat(prod_name, '(', vend_id, ')') as price_info from products;
```

##### 7.3 执行算术计算
算术运算符：加，减，乘，除

```
计算商品共卖出多少钱
1. select prod_id, quantity, item_price, quantity * item_price as expanded_price from orderitems where order_num = 20005;
```

 
 