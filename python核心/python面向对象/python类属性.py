class Money:
    age=18
    count=1
    num=666

s=Money()
Money.name='hello'
print(s.age)
print(Money.age)
print(Money.name)
print(s.name)
print(s.__class__)
print(Money.__name__)
print(Money.__class__)
print(dict.__class__)
print(dict.__name__)
#所有说，变量类型就是一个类（__class__）。而我们自定义一个类就相当于自定义了一个变量类型
a=str('hello ersbad asd')
print(a.__class__)
print(str.__class__)
print(s.__class__)
print(Money.__class__)

#对象属性会优先到自己内部去找，没有找到会找类内部去找
s.name='ziji'
print(s.name)
print(Money.name)

###这里发现了一个有意思的东西，既然类名.__dict__可以查询类属性，那么内建的类有什么属性呢？发现想字符串、字典等函数都出来了。以后查询方便啦
# print(str.__dict__)
print(a.title())
# print(dict.__dict__)
a={'a':'b','c':'d','e':'f'}
# print(dict.__dict__)
#原来上边的是我管折弯发现的，python早已为我们准备好了学习的方法。。helphelphelp（）help（）。这个东西以后要常用
# help(str)
# help(dict)

#__dict__是什么玩意
# __dict__是对象的内置属性，它指向了一个字典，而想对象属性、对象函数、对象方法的（变量名或者是Key）都存储在这个字典内
# 比如
two=Money()
two.__dict__={'name':'lsf','age':18}
print(two.name)  #访问到了！！！神奇吧！！
print(two.__dict__['name'])  #这样也访问到了！！！神奇吧！！
#注意：不同的对象（物件）的__dict__(内置字典属性)是修改的权限不一样的。对象的可以这样定义或者修改，但是！！类！！不可以

#——————————关键子————__slots__————————————#
#首先他是属于类的关键字（方法？函数？）
#它的作用是限定这个类所衍生（产生？实例化？）的对象所能添加的属性名称
#为什么？防止该类所衍生的对象之间的差异千奇百怪！
class Person:
    __slots__ = ['name','age','height','sex'] #以后这个类衍生的对象只能新增这些属性
    pass

class student():
    count=0
    def __init__(self,name):
        self.name=name
        student.count+=1
    def get_count(self):
        print(student.count)
sf=student('四方')
sf.get_count()
print(dir(sf))
print(sf.__dict__)
print(dir(student))
print(student.__dict__)