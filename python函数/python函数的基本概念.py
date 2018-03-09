# #-----------hanshu--------------#
# 内奸函数
# 第三方函数
# 自定义函数
#不定长参数可以放一个元组参数标识符是(*tuple)号。。。。。(**dict)两个星星代表是接受一个字典
def myfunc(*t):
    print(t,type(t))
myfunc(4,5,6,7)

#参数装包-》拆包
# 装包，当参数定义为一个元组或者一个字典时。把传过来的参数先包装成一个集合包。
# 拆包。把封装后的集合包拆分成单个的个体如元素或者键值对
def mysun(a,b):
    print(a+b)
def dic(**dc):
    # print(type(dc))
    print(dc)
    #拆包
    mysun(**dc)
dic(a=1,b=2)

# 缺省参数
def hit(who,somebody='doudou'):
    """

    :param who:
    :param somebody:
    :return:
    """
    print ('%s想打%s'%(who,somebody))

hit('wo')
hit('我','jinchen')
#python的函数参数传递方式是地址传递。只有当参数为不可变类型比如整型才不会影响到原参数。但为可变类型如列表则会影响到元变量参数
#------函数得返回值------#
#注意： 一般自定义函数都有返回值所以在引用时需要先赋值给一个变量
# a=func()