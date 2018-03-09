#------------偏函数------------#
import mysql.connector
conn=mysql.connector.connect(user='root',password='root',database='testguest')
con1=conn.cursor()
print(type(con1))
con1.execute('select * from tg_user where tg_id =16')
values = con1.fetchall()
print(values)
con1.close()
conn.close()

import functools
#偏函数。，指明哪一个函数，指明偏爱那个参数。属于原函数的延伸。增加了一个默认参数。。。。
#创建方式是functools.partial([函数名]，默认值)
int2=functools.partial(int,base=2)
numstr='111000101'
result=int2(numstr)
print(result)