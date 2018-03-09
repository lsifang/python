#==========递归=========#
# 1、递归并不是一个特殊的函数，而是一种体现（闭包也是，高阶函数也是）
# 2、递归就是自己调用自己（自己搞自己）
# 3、传递和回归

def jiecheng(num):
    '''
    jiecheng
    :param num:
    :return:
    '''
    if num==1:
        return 1 #回归
    return num*jiecheng(num-1) #递归
p=jiecheng(2)
print(p)


def monay(i):
    if i<=10:
        return i*0.1
    if i>10 and i<=20:
        return (i-10)*0.075+monay(10)
    if i>20 and i<=40:
        return (i-20)*0.05+monay(20)
    if i>40 and i<=60:
        return (i-40)*0.03+monay(40)
    if i>60 and i<=100:
        return (i-60)*0.015+monay(60)
    if i>100:
        return (i-100)*0.01+monay(100)

p=monay(float(input('请输入今年利润？万')))
print(p)
