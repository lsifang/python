#经典类
#新式类
class Person:
    def __init__(self,name):
        self.name=name
    pass

p=Person('world')
#增
p.age=18
#改
p.age=16
#查
p.__dict__
#删除
del p.age
#p.__dict__  对象的所有属性

p.pets=['huahua','heihei']
p.pets.append('huanhuan')
print(p.pets)
s=list(p.__dict__.values())
print(s,type(s),len(s))
print(Person.__dict__)
print(Person.__name__)
print(Person.__init__(p,'hello'))

#元类
type
# 创建类（对象）的类
print('*'*30)
class person:
    __slots__ = ['age','name','num','sex']
    pas=1
    def __init__(self,sex):
        self.sex=sex

p=person('hello')
print(p.sex)
print(person.sex)
print(person.name)
print(person.pas)
print(p.pas)

print('---'*30)
# 类的另类定义方法
def run(self):
    print(self)
xxx=type('dog',(),{'count':0,'run':run})
print(xxx.count)
print(xxx.__dict__)
print(xxx.__name__)
print(xxx.__module__)
a=xxx()
print(a)
a.run()