#=================时间日历calender模块=====================#
# 提供日历相关的功能
# 1、calendar.month([年份]，[月份])  打印指定年月份的文本日历
import calendar
print(calendar.month(2018,1))


#-----------------datetime----------------#
# 调用的是模块下的类下面的方法
import datetime
# 1、获取当前的时间
print(datetime.datetime.now())
print(datetime.datetime.today())
#2、单独获取
t=datetime.datetime.now()
print(type(t))
print(t.year)
print(t.month)
print(t.day)
print(t.hour)
#3、获取n天后的时间日期datetime.timedelta()
result=t+datetime.timedelta(days=7)
print(t)
print(result)
#4、计算两个日期之间的时间隔
first=datetime.datetime(2018,1,10,12,00,00)
print(first)
two=datetime.datetime.now()
jiange=two-first
print(jiange,type(jiange))
print(jiange.total_seconds())