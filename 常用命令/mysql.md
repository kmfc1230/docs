# MySQL数据库常用命令总结
参考资料：https://www.modb.pro/db/373448  
1、远程登录mysql服务器
```shell
# -h host   -P port
# -u user   -p password
mysql -h host -P port -u root -p
Enter password: 
# 退出
mysql> quit;
```
2、查询数据库
```shell
show databases;
```
3、进入数据库
```shell
use databasename;
```
4、列出数据库中的表
```shell
show tables;
```
5、查看某个表全部字段
```shell
desc tablename;
desc tablename\G;   # 每行分开显示
show create table tablename\G; #（不仅可以显示表信息，还可以显示建表语句）
```
6、查看当前用户
```shell
select user();
```
7、查看当前使用的数据库
```shell
select database();
```
8、查询数据库版本
```shell
select version();
```
9、创建数据库
```shell
create database db1;
# 可以指定字符集
create database db1 charset=utf8;
```
10、创建新表
```shell
CREATE TABLE USER(
   id INT NOT NULL AUTO_INCREMENT,
   NAME VARCHAR(30) NOT NULL,
   PASSWORD VARCHAR(32) NOT NULL,
   age INT(11)  NOT NULL,
   sex VARCHAR(2) DEFAULT '男' CHECK (性别 IN ('男','女')),
   birthday DATE,
   PRIMARY KEY ( id )
   )ENGINE=INNODB DEFAULT CHARSET=utf8;
```
11、查询数据库状态
```shell
show status;            # 当前会话状态
show global status;     # 全局数据库状态
show slave status\G;    # 查看主从数据库状态
```
12、查询数据库参数
```shell
show variables;
```
13、修改数据库参数
```shell
show variables like 'max_connect%';
set global max_connect_errors = 1000;   # （重启数据库会失效，要在配置文件中修改）
```
14、查看当前数据库队列
```shell
show processlist;
```
15、创建用户并授权给某个数据库(待验证)
```shell
grant all on databasename.* to `user1`@`localhost` identified by `123456`;
```
16、查询表数据
```shell
select * from mysql.db;             # 查询表中所有字段
select count(*) from mysql.user;    # conut(*)表示表中有多少行       
select db,user from mysql.db;       # 查询表中多个字段
select * from mysql.db where host like '10.0.%';    # 按条件查询，通配符%
```
17、插入数据
```shell
insert into db1.t1 values(1,'jack')
```
18、更改表中某行数据
```shell
update db1.t1 set name = 'rose' where id=1;
```
19、清空表数据
```shell
truncate table t1;
```
20、删除表
```shell
drop table t1;
```
21、删除数据库
```shell
drop database db1;
```
22、数据库备份
```shell
mysqldump -uroot -p mysql > /path/mysql.sql
Enter password: 
```
23、数据库恢复
```shell
mysql -uroot -p mysql < /path/mysql.sql
Enter password: 
```
24、新建普通用户
```shell
create user test identified by '123456';
```
25、更改普通用户(name)密码
```shell
set password for name=password('admin');
```
26、查看用户(name)权限
```shell
show grants for name;
```
27、脚本中执行mysql命令
```shell
mysql -uroot -p -e"show databases"
Enter password: 

echo "show databases"|mysql -uroot -p
Enter password: 

# 以下是执行大量mysql语句采用的方式
mysql -uroot -h hostname -p <<EOF

mysql语句

EOF
```