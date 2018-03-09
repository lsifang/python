def test(a,b):
    print(a+b)
print(test,type(test),id(test))

test2=test
test2(1,3)
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('%.2f%%' % r)


#函数的参数接受的是另一个函数时。叫做高阶函数。是可以的
l=[{'name':'sz1','age':15},{'name':'sz3','age':18},{'name':'sz2','age':11}]
def getkey(x):
    return x['age']
result=sorted(l,key=getkey)
print(result)

def caculete(num1,num2,caculetefunc):
    print(caculetefunc(num1,num2))
def sum(a,b):
    return(a+b)
def jian(a,b):
    return(a-b)

caculete(6,2,jian)

#----------返回函数--------------#
#一个函数的返回值是另一个函数

def getfunc(flag):
    #在定义几个函数
    def sum(a,b,c):
        return(a+b+c)
    def jian(a,b,c):
        return(a-b-c)

    #根据不同的flag返回不同操作的函数
    if flag=='+':
        return sum
    elif flag=='-':
        return jian

result=getfunc('+')
# print(result,type(result))
print(result(5,3,4))

#------------匿名函数----------#
# 1、lambda 参数1，参数2：表达式（参数）..直接调用
result=(lambda x,y: x+y)(1,2)
print(result)

newfunc=lambda x,y: x+y
print(newfunc(5,6))


# sorted中的key
# key=相当于
for i in l:
    key=i
def get_k(key):
    return key['age']
l=[{'name':'sz1','age':15},{'name':'sz3','age':18},{'name':'sz2','age':11}]
l1=sorted(l,key=get_k,reverse=True)  #默认传的值就是上面for循环里的i
print(l1)
print(sorted(l,key=lambda x:x['age']))
l2=sorted(l,key=lambda u:u['name'])
print(l2)