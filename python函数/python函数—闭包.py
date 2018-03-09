#------------------#
# 1、前提是在嵌套函数内存在
# 2、子函数调用了父函数的参数或者变量
# 3、父函数返回值是子函数

#内部函数和内部函数所调用的外部函数参数以及变量称之为闭包

def line_config(content,lenght):
    def line():
        print('--'*(lenght//2)+content+'--'*(lenght//2))
    return line
line_config('闭包',40)
line1=line_config('闭包',40)
line1()
line1()
line1=line_config('开包',60)
line1()
line1()

###内部使用外部变量并变化时需要申明：：nonlocal
def test():
    num=10
    a=2
    def test2():
        num=2
        nonlocal a
        a=a+2
        print(num,'num')
        print(a,'a')
        #内部自己的变量
    print(a,'a')
    print(num,'num')
    test2()
    print(num,'num')
    return test2
result=test()
result()
###函数被调用时才会确定函数内部变量的值
# def test():
#     print(b)
# test()


def test():
    func=[]
    for i in range(1,4):
        def test2(num):
            def inner():
                print(num)
            return inner
        func.append(test2(i))
    return func
result=test()
result[0]()