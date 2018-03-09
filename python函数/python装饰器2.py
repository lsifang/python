#------------------------#
# 1、装饰器一般作用于函数（一说装饰器那就是函数的附加）
# 2、装饰器的作用就是给下面紧跟的函数附加一些功能
#2装饰器就是一个函数，然后是一个闭包函数，一般返回的是一个函数体。函数体包裹一些附加功能和需要装饰的函数。装饰器的参数一般是一个函数。返回值是
# 经过功能附加的一个函数体。

def checklogin(func):
    def inner():
        print('登录验证···')
        func()
    return inner
# 功能函数####python提供了语法糖写法（更加快捷方便的方式而已）
@checklogin #等同于fss=checklogin(fss)
def fss():
    # checklogin()
    print('发说说')
# fss=checklogin(fss)
# 等同于fss=def inner():
#               print('dengluyanzheng...')
#               fss()
@checklogin #等同于fss=checklogin(ftp)
def ftp():
    # checklogin()
    print('发图片')
#等同于ftp=def inner():
 #          print('dengluyanzheng..')
 #          ftp()

#相关的逻辑代码
btmindex=2
if btmindex==1:
    fss()
    # checklogin(fss)
else:
    ftp()
    # checklogin(ftp)

#发说说或者发图片必须有一个前提，就是用户必须登陆

#验证登陆
#1、直接在业务逻辑里边修改，增加验证操作###这是野路子，是笨办法
#2、直接在功能函数里边修改，方便代码重用...新建功能代码嵌套调用。
#注意：根据’开放封闭‘原则：已经写好的代码，尽量不再修改（封闭），如果想要新增功能，在原先代码的基础上单独扩展（开放）
#另外：功能函数尽量保证‘单一原则’。比如发说说就只发说说，不要验证登陆