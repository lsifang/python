class D:
    def __init__(self,name,job):
        self.name=name
        self.job=job

class A(D):
    def __init__(self,age):

        self.age=age

class B(D):
    def __init__(self,name,id,job):
        super(B, self).__init__(name,job)
        self.id=id

class C(A,B):
    def __init__(self,name,age,id,job):
        A.__init__(self,age)
        B.__init__(self,name,id,job)
    def __enter__(self):
        print('enter')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('eixt')
c1=C(4,5,6,7)

print(c1.__dict__)
print(C.mro(),'***************',end='\n')
with C(4,5,6,7):
    print('body')


def chu(x,y):
    try:
       a=x/y
    except Exception as ze:
        return('不能为0',ze)
    else:
        return(a)
    finally:
        print('finally')

try:
    print(chu(1,'abc'))
except NameError as ne:
    print('参数未找到%s'%ne)

with open('liebuchong.py','r+',encoding='utf-8') as f:
    print(f.readlines())