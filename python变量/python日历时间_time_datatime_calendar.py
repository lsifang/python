#=============time模块==============#
# 1、获取当前的时间戳###当前时间距离19701月1日0时0分0秒的秒数。北京时间就是19701月1日8时0分0秒time.time()
import time
now=time.time()
years=now/(24*60*60*365)+1970

print(now,years,0.0938095551653*12)
#2、time.localtime(【可选填时间戳】) 时间元组，默认当前时间戳的年月日分时秒。 tm_wday=（0-6） 0是星期日
print(time.localtime(),type(time.localtime()))
lis=list(time.localtime())
#3、time.ctime([可选时间戳])，获取格式化的时间，默认为当前时间戳
##time.asctime([这里是一个时间元组])
######
at=time.ctime()
bt=time.asctime(time.localtime())
print(at,type(at))
print(bt,type(bt))
#4、获取自定的格式化时间time.strftime(【格式化字符串】，时间元组)
ct=time.strftime('%Y-%m-%d %I:%M:%S',time.localtime())
dt=time.strftime('%H:%M:%S',time.localtime())
print(ct,type(ct))
print(dt,type(dt))
#5、格式化时间--》时间元组time.strptime([格式化时间]，【格式化字符串】)
# 然后时间元组——————》时间戳time.mktime(【时间元组】)
et=time.strptime('2018-01-23 02:03:39',"%Y-%m-%d %I:%M:%S")
print(et)
print(time.mktime(et))

#6、time.clock()计算程序耗时.返回的是记录程序运行到函数出现位置的时间戳
start=time.clock()
num=0
for v in range(0,1000000):
    num=num+v
time.sleep(2)
end=time.clock()
print(end-start)
#7、程序休眠。推迟线程执行。time.sleep([秒数])
while True:
    ct=time.strftime('%Y-%m-%d %I:%M:%S',time.localtime())
    print(ct)
    time.sleep(1)

