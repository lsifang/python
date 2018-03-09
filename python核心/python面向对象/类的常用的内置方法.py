#——---常用内置方法————#
# 一、信息格式化方法
# 1、__str__  当实例化对象被直接打印时时自动调用(用字符串描述这个实例)
# class person(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return ('name=%s,age=%s'%(self.name,self.age))
# p1=person('dawvy',18)
# print(p1)
# s=str(p1)   #注意这种方式

#2、repr（）  这种方法主要是面向开发人员  在使用__str__方法后应用
class person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # def __str__(self):            #这个主要是面向用户
    #     return ('name=%s,age=%s'%(self.name,self.age))
    def __repr__(self):
        return ('这里边放关于这个实例的技术类文档')     #如果实例不存在__str__方法将会自动调用这个方法。如果存在需要利用repr（）函数调用
p1=person('dawvy',18)
print(p1)
s=str(p1)   #注意这种方式
print(repr(p1))

import datetime

t=datetime.datetime.now()
print(t)
print(repr(t))
tmp=repr(t)
result=eval(tmp)
print(result)