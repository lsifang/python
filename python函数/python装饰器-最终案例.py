#装饰器（一个高阶函数，包含一个闭包，接受一个函数体，返回一个函数体）
def checklogin(func):
    def inner():
        print('yanzhengdenglu..')  #附加的功能
        func()  #附加了装饰器的函数
    return inner  #返回一个附加了功能的函数体

#功能函数
@checklogin #fss==等于==checklogin(fss)====又等于===def inner();print('dengluyanzheng..')   fss().
def fss():
    print('fashuoshuo')
@checklogin
def ftp():
    print('fatupian')

#业务逻辑
button=1
if button==1:
    fss()
else:
    ftp()

#装饰器时间是立即执行。在被函数调用（或者说是装饰其他函数时）函数体内的输出或计算会被立即执行