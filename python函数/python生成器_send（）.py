#=============send()========#
# 1、可以给yield语句传值
def test():
    res1= yield 1
    print(res1)
    res2=yield 2
    print(res2)
    res3 = yield 2
    print(res3)
    res4 = yield 2
    print(res4)
p=test()
print(p.__next__())
print('//////////')
print(p.__next__())
print('//////////')
print(p.send('000'))
p.close()  ##生成器关闭方法
p=test()
for i in p:
    print(i)