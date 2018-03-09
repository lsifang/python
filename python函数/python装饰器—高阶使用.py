#--------------叠加使用------------#
# 1、从上到下装饰。。。从下到上执行

def pri_line(func):
    def inner():
        print('-'*20)
        func()
    return inner
def pri_xing(func):
    def inner():
        print('*'*20)
        func()
    return inner

@pri_line
@pri_xing
def pri():
    print('天地不仁以万物为刍狗')

pri()

def crate(**args):
    print(args)
crate(a='2',b='2',c='4',name='hello')
#============返回值==========#
##注意：对于有参数和返回值的函数。无论是参数和返回值必须和原函数一致。无论是固定形参还是不定长形参，亦或是不定返回值
##对于接受参数的可变的装饰器，需要定义一个生成装饰器的函数
def getzsq(char):
    def zsq(func):
        def inner(*ars):
            print(char * 30)
            return func(*ars)
        return inner
    return zsq
@getzsq('=') # 时刻注意被装饰函数=装饰器（被装饰函数）。（也就是被装饰函数必须和装饰器里的===！！闭包！！===在！！同一层级！！。。！！！！
def te(*ars):
    num=0
    for i in ars:
        num =num+i
    return num
res=te(1,2,3)
print(res)