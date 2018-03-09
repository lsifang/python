#数学函数-自带函数

#abs（num）返回绝对值

num=10
num1=-10
print (abs(num),abs(num1))

#max()最大值
print(max(1,2,3,4))

#min()最小值
print(min(1,2,3,4,5))

#round(num[,n]) 四舍五入
p=3.14159
pi=round(p,3)
print(pi,type(pi))

#pow(x,y)
#        x**y
print(pow(2,3))

####数学函数--math模块函数
#导入
import math
#math.函数名（）


#ceil（）上取整，相当于四舍五入永远的入
#floor() 下取整，相当于四舍五入永远的舍

print(math.ceil(pi))
print(math.floor(pi))
print(type(math.floor(pi)))


#sqrt() 开平方函数

print(math.sqrt(17))


#log()
print(math.log(1000, 100))