#==========================#
# generator   是生成器的标识符
# 是一个特殊的迭代器（就是一个迭代器而已）
# 可以被next（）函数作用
# 创建方式
# 1、生成器表达式——————把列表推导式的【】换成（）
# 列表推导式
l=[1,2,3,4,5,6]
newl='@'.join([str(i**2) for i in l if i%2==0])
item=iter(newl)
print(item,type(newl))
newsheng=(str(i**2) for i in l if i%2==0)
print(newsheng,type(newsheng))
for j in newsheng:
    print(j)
newsheng1=(str(i**2) for i in l if i%2==0)
print(next(newsheng1))
print(newsheng1.__next__())

# 2、生成器函数。。。这里是关键字  必须包含yield语句。。。（这这里，终于明yield。yield。yield白这个玩意是什么了吧）
# 这个函数的执行结果就是“生成器”？？？//每当这个函数生成的生成器被调用时。这个yield语句就是一个状态（类似于指针），
# 当次调用执行的是 本所指向的！yield到上一个yield！之间的代码块(包括本次指向的yield本身)！！！！yield是一个状态语句（指针、索引、key）
# yield是阻断。暂停函数的执行
def test():
    print('xxxx')
    yield
    for i in range(5):
        print(i)
    print('a')
    yield 2

    print('b')
    yield 3

    print(3)
    yield 4

    print(4)
    yield 5

    print(5)
p=test()
print(p,type(p))
print(next(p))
print('////////////')
print(next(p))
print('////////////')
print(next(p))
print('////////////')
print(next(p))
print('////////////')
print(next(p))
print('////////////')

def sq():
    for i in range(10):
        print('************hello************',end='\t')
        yield i
j=sq()
print(j.__next__(),end='\t')
print(j.__next__(),end='\t')
print(j.__next__(),end='\t')
print(j.__next__(),end='\t')

print('hello',end='\t')
print('hello',end='\t')
print('hello',end='\t')
print('hello',end='\t')
