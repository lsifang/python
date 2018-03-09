#_*_encoding:utf-8_*_
# class.__bases__   查询父类
#父类是object类的就是   新式类


# 不是object类的就是经典类
# python3中默认继承object类

class person:
    __slots__ = ['name','__age']
    def __init__(self,name):
        self.name=name
        self.__age=18
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        self.__age=value

class student(object):
    pass


print(person.__bases__)
print(student.__bases__)
print('*'*30)
p=person('davy')
print(p.name)
print(p.age)
p.age=20
print(p.age)
###-----@property————在经典类中的使用————————##

# def a(func):
#     def b():
#         print('\'*****\'')
#         func()
#     return b
#
# def hello():
#     print('****')
# hello=a(hello)  #hello()=b():printxxx+hello()
# hello()
# python3暂时不知道怎么创建一个经典类

#-只需要记住。property在经典类中只有···私有化属性的读取功能 （阉割版的peoperty）
###