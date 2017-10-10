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

### 第8课 使用数据处理函数

##### 8.1 函数
SQL中函数，各个DBMS所支持的都不同，如果使用过多的函数，可能会带来可移植问题。

##### 8.2 使用函数
```
大部分SQL实现支持以下类型的函数
1. 用于处理文本字符串(如删除，填充值，转换大小写等)的文本函数。
2. 用于在数值数据上进行的算术操作(如返回绝对值，进行代数运算)的数值函数。
3. 用于处理日期和时间值，并从这些值中提取特定成分(如返回两个日期之差，检查日期有效性)的日期和时间函数。
4. 返回DBMS正使用的特殊信息(如返回用户登录信息)的系统函数。
```

##### 8.2.1 文本处理函数
常见的文本处理函数

|函数|说明|
|:---:|:--:|
|LEFT()(或使用子字符串函数)|返回字符串左边的字符|
|RIGHT()(或使用子字符串函数)|返回字符串右边的字符|
|LOWER()(Access使用LCASE())|将字符串转换为小写||UPPER()(Access使用UCASE())|将字符串转换为大写|
|LTRIM()|去掉字符串左边的空格||RTRIM()|去掉字符串右边的空格|
|TRIM()、去掉字符串左边和右边的空格|
|SOUNDEX()|返回字符串的SOUNDEX值(读音相同)|
|LENGTH()(也使用DATALENGTH()或LEN())|返回字符串长度|

解释文本处理函数:SOUNDEX()

```
SOUNDEX()函数是一种和根据读音相同来比较的
1. SELECT cust_name, cust_contact FROM Customers WHERE SOUNDEX(cust_contact) = SOUNDEX('Michael Green');
```

##### 8.2.2 日期和时间处理函数
非常遗憾的是：日期和时间处理函数在SQL实现中差别很大，可移植性非常差。所以，关于具体DBMS支持的日期-时间处理函数，请参阅相应的文档。

##### 8.2.3 数值处理函数
数值处理函数仅处理数值数据，这些函数一般主要用于代数、三角或几何运算。数值处理函数在SQL差别不大。

|函数|说明|
|:---:|:---:||ABS()|返回一个数的绝对值||COS()|返回一个角度的余弦||EXP()|返回一个数的指数值||PI()|返回圆周率||SIN()|返回一个角度的正弦||SQRT()|返回一个数的平方根||TAN()|返回一个角度的正切|

### 第9课 汇总数据

##### 9.1 聚集函数

|函数|说明|
|:---:|:---:||AVG()|返回某列的平均值||COUNT()|返回某列的行数||MAX()|返回某列的最大值||MIN()|返回某列的最小值||SUM()|返回某列值之和|
##### 9.1.1  AVG()函数
AVG函数计算表中列的平均值。AVG()只能用来确定特定数值列的平均值.AVG函数忽略列值为NULL的行。

- select avg(prod_price) as avg_price from products;

##### 9.1.2 COUNT()函数
```
COUNT函数有两种实现方式:
1. 使用count(*)，对表中行的数目进行计数。无论是空值(NULL)或非空值。
2. 使用count(columnName)对表特定列具有值进行计数，忽略NULL值。
3. select count(vend_state) from vendors;语句忽略NULL值。
```

##### 9.1.3 MAX()函数
MAX()返回指定列中的最大值。

- select max(prod_price) as max_price from products;

##### 9.1.4 MIN()函数
MIN()的功能正好与MAX()功能相反，它返回指定列的最小值。

##### 9.1.5 SUM()函数
SUM()用来返回指定列值的和(总计)。

- select sum(item_price) as sum_price from orderitems where order_num = 20005;
- select sum(item_price*quantity) as total_price from orderitems where order_num = 20005;

注: 利用标准的算术运算符，所有的聚集函数都可以执行多个列上的计算。

##### 9.2 聚集不同的值
使用关键字: DISTINCT关键字，过滤相同的值。

- select avg(distinct prod_price) as avg_price from products where vend_id = 'DLL01';

##### 9.3 组合聚集函数
select 语句可以根据需要包含多个聚集函数。

- select count(*) as num_items, min(prod_price) as min_price, max(prod_price) as max_price, sum(prod_price) as sum_price from products;

### 第10课 分组数据
将数据分组，使用Order by子句和Having子句。

##### 10.1 数据分组
目前为止的所有计算都是在表的所有数据或匹配特定的WHERE子句的数据上进行的。没有对应的分组概念。

- select count(*) as num_prods from products where vend_id = 'DLL01';

如果查询每个供应商提供的商品数，怎么查？答：需要使用分组，Order by子句和Having子句

##### 10.2 创建分组
分组是使用select语句的Group by实现的。

- select vend_id, count(*) num_prods from products group by vend_id;

使用group by子句分组数据，然后对每个组而不是整个结果集进行聚集。

```
使用GROUP BY子句前，需要了解一些重要的规定:
1. GROUP BY子句可以包含任意数目的列，因而可以对分组进行嵌套，更细致的进行分组。
2. GROUP BY子句嵌套了分组，数据将在最后指定的分组上进行汇总。
3. GROUP BY子句中列出的每一列必须是检索列或有效的表达式。如果在SELECT中使用表达式，则必须在GROUP BY子句中指定相同的表达式。不能使用别名。
4. 大多数SQL实现不允许GROUP BY列带有长度可变的数据类型。
5. 除聚集计算语句外，SELECT语句中的每一列都必须在GROUP BY子句中给出。
6. 如果分组列中包含具有NULL值的行，则NULL将作为一个分组返回。如果列中有多行NULL值，它们将分为一组。
7. GROUP BY子句必须出现在WHERE子句之后，Order by子句之前。
```

##### 10.3 过滤分组
Group by新建分组，使用Having子句过滤分组。如：查询至少有两个订单的顾客。

```
Where 子句和Having 子句的区别:
1. Where子句过滤的是行，而Having子句过滤的是分组。
2. Having子句可以替代Where子句，但是不建议这样做。
```

- select vend_id, count(*) as num_prods from products where prod_price >= 4 group by vend_id having count(*) > 2;

分析：首先，where语句先选出价格大于4的商品，然后按照vend_id来进行分组，再对分组进行过滤。

##### 10.4 分组和排序
|Order by|Group by|
|:---:|:---:|
|对产生的输出排序|对行分组，但输出可能不是分组的顺序|
|任意列都可以使用|只可能使用选择列或表达式列，而且必须使用每个选择列表达式|
|不一定需要|如果与聚集函数一起使用列(或表达式)，则必须使用|

一般使用GROUP BY子句后，也应该使用ORDER BY子句。

##### 10.5 Select子句的顺序
|子句|说明|是否必须使用|
|:---:|:---:|:---:
|SELECT|要返回的列或表达式|是|
|FROM|从中检索数据的表|仅在从表选择数据时使用|
|WHERE|行级过滤|否|
|GROUP BY|分组说明|仅在按组计算聚集时使用|
|HAVING|组级过滤|否|
|ORDER BY|输出排序顺序|否|

### 第11课 使用子查询

##### 11.2 利用子查询进行过滤
```
假如需要列出订购物品RGAN01的所有顾客，应该怎样检索?
1. 从订单详情表(OrderItems)中查询订购物品GRANO1的所有订单编号。
2. 根据订单编号，从表(Orders)中查询顾客ID
3. 根据顾客ID，从表(Customers)查询顾客信息。

select cust_name, cust_contact from customers
   where cust_id IN (select cust_id from Order
         where order_num IN (select order_num from OrderItems
                              where prod_id = 'GRANO1'));
```

作为子查询的Select语句只能查询单个列。企图查询多个列，是错误的。

##### 11.3 作为计算字段使用子查询
```
假如需要显示Customers表中每个顾客的订单总数，应该怎样写？
1. 从Customers表中检索顾客列表。
2. 对于检索的每个顾客，统计在Orders表中的数目。

select cust_name, cust_state,
    (select count(*) from Orders 
          where Orders.cust_id = Customers.cust_id) AS orders
from Customers order by cust_name;
该子查询检索到每个顾客执行一次。
```

### 第12课 联结表




