import math
#输入ax**2+bx+c=0（a！=0）
a=int(input('请输入第一个数值：'))
while a==0:
    a=int(input('请重新输入第一个数值不等于零：'))
b=int(input('请输入第二个数值：'))
c=int(input('请输入第三个数值：'))
#计算
# 公式  判断公式t=b**2-4ac等于0还是小于零还是大于零
#     x=(-b+(-)sqart(t))/(2*a)
# 判断
t=(b**2)-(4*a*c)
if t<0:
    print('此方程无解')
elif t==0:
    x=(-b)/(2*a)
    print('次方程得解为%d'%x)
elif t>0:
    x1=((-b)+math.sqrt(t))/(2*a)
    x2 = ((-b) - math.sqrt(t)) / (2 * a)
    print(x1,x2)
exit('the end')
#输出