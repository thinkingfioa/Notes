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

##### 12.1.1 关系表关系表的设计就是把信息分成多个表，一类数据一个表。各个表通过共同的值进行关联。

##### 12.2 创建联结
```
当from子句后接多个表时候，表示联结产生了。select子句后面所接的字段，分别来自于两个表中。
1. select vend_name, prod_name, vend_city, vendors.vend_id from vendors, products where vendors.vend_id = products.vend_id;

如果没有Where子句，那么返回结果就是笛卡尔积。
```

##### 12.2.3 联结多个表
select prod_name, vend_name, prod_price, quantity from OrderItems, Products, Vendorswhere Products.vend_id = Vendors.vend_idAND OrderItems.prod_id = Products.prod_idAND order_num = 20007;

### 第13课 创建高级联结

##### 13.1 使用表别名
```
使用表别名优点:
1. 缩短SQL语句
2. 允许在一条select语句中多次使用相同的表
select cust_name, cust_contact from Customers AS C, Orders AS O, OrderItems AS OIwhere C.cust_id = O.cust_id and OI.order_num = O.order_num and prod_id = 'RGAN01'
```

##### 13.2 使用不同类型的联结
四种联结: 1. 内联结或等值联结, 2. 自联结(self-join), 3. 自然联结(natural join), 4. 外联结(outer join)。

##### 13.2.1 自联结
问：查询与Y Lee同一公司的所有顾客。

```
1. 使用子查询
- select cust_name, cust_address from customers where cust_name = (select cust_name from customers where cust_contact = 'Y Lee')
```

```
2. 使用自联结
- select C1.cust_name, C2.cust_address from customers as C1, customers as C2 where C1.cust_name = C2.cust_name and C1.cust_contact = 'Y Lee'
```

```
用自联结而不用子查询:
1. 但许多DBMS处理联结远比处理子查询快得多。
```

##### 13.2.2 自然联结

##### 13.2.3 外联结
```
许多联结将一个表中的行和另一个表中的行相关联，但有时候需要包含没有关联行的那些行。如，以下工作:
1. 对每个顾客订单进行计数，包括至今尚未下订单的顾客。
2. 列出所有产品以及订购数量，包括没人订购的产品。

上述举例，包括了那些相关表中没有关联的行。这种联结称为外联结。
```

```
检索所有顾客及其订单
1. 内联结(inner join): 
select Customers.cust_id, Orders.order_num from Customers inner join Orders on Customers.cust_id = Orders.cust_id;
2. 外联结(left outer join):
select Customers.cust_id, Orders.order_num from Customers left outer join Orders
on Customers.cust_id = Orders.cust_id;
外联结的使用的是left outer join是从左边的表(Customers)中选择行，所以如果右表没有对应的id则补充。要注意on后面的表Customers和Orders顺序。
3. 外联结(right outer join)
select Customers.cust_id, Orders.order_num from Customers right outer join Orders on Orders.cust_id = Customers.cust_id;
4. 全外联结(full outer join)
select Customers.cust_id, Orders.order_num from Orders full out join Customers
on Orders.cust_id = Customers.cust_id;
两个表的行的最大集合。
```

##### 13.3 使用带聚集函数的联结
```
检索所有顾客及每个顾客所下的订单数
1. select Customers.cust_id, count(Orders.order_num) AS num_ord
from Customers inner join Orders on Customers.cust_id = Orders.cust_id
group by Customers.cust_id;
```

#### 13.4 使用联结和联结条件
```
联结和联结的使用要点:
1. 注意使用的联结类型。有内联结，外联结等
2. 联结语法每个DBMS可能不一样。
3. 保证使用正确的联结条件，否则返回不正确的数据。
4. 应该总是使用联结条件，否则会得到笛卡尔积。
5. 在一个联结中可以包含多个表，甚至可以对每个联结采用不同的联结类型。虽然这样做是合法的，一般也很有用，但应该在一起测试它们 前分别测试每个联结。这会使故障排除更为简单。
```

### 第14课 组合查询
利用UNION操作符将多条Select语句合成一个结果集。

##### 14.1 组合查询
SQL 允许执行多条查询语句(多条Select语句)，并将结果作为一个查询结果集返回。

```
主要有两种情况需要使用组合查询:
1. 在一个查询中，从不同的表返回结构数据。
2. 对一个表执行多个查询，按一个查询返回数据。

注：一般多个Where子句的Select语句都可以作为一个组合查询。也就是说将Where子句拆分开来。
```

##### 14.2 创建组合查询
用操作符UNION操作符组合多条Select语句，将他们的结果组合成一个结果集。

##### 14.2.1 使用UNION操作符
```
查询Illinois、Indiana和Michigan等美国几个州的所有顾客的报表，和不管位于哪个州的所有的Fun4All
1. 使用UNION操作符查询。
select cust_name, cust_contact, cust_email from Customers
where cust_state in ('Illinois','Indiana','Michigan')
UNION
select cust_name, cust_contact, cust_email from Customers
where cust_name = 'Fun4All';

2. 使用Where子句
select cust_name, cust_contact, cust_email from Customers
where cust_state in ('Illinois','Indiana','Michigan') or cust_name = 'Fun4All'
```

```
Union和Where子句比较:
1. 对于较复杂的过滤条件，或者从多个表(而不是一个表)中检索数据的情形，使用UNION可能会使处理更简单。
2. 多数DBMS使用内部查询优化程序，使用Union关键字会在内部组合它们，所以性能几乎无差别。但使用Union操作符也请注意下性能问题。
```

##### 14.2.2 UNION规则
```
Union非常好用，但使用组合前请注意下以下规则：
1. UNION必须由两条或两条以上的SELECT语句组成，语句之间用关键字UNION分隔。
2. UNION每次查询必须包含相同的列，表达式，聚集函数。(各个列不需要以相同的次序列出)。
3. 列数据类型必须兼容:类型不必完全相同，但必须是DBMS可以隐含转换的类型。
```

##### 14.2.3 包含或取消重复的行
UNION从查询结果集中自动去除了重复的行。

```
使用关键字:Union All的会返回所有的匹配行。
Union All操作符是Where不能替代的。
```

##### 14.2.4 对组合查询结果排序
用Union组合查询时，只能使用一条Order by子句，它必须位于最后一条Select语句。





















