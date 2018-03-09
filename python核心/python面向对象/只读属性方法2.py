#---#
# 2、__setattr__
class person(object):
    #当我们通过 实例.属性 = 值 ，给一个实力增加一个属性，或者说修改一下属性的值的时候，都会调用这个方法
    #注意，只要出现这种模式的赋值，都会自动的调用这个方法，无论在任何作用域
    #在这个方法内部，才会把这个属性以及对应的数据，给存储在__dict__(实例内部变量的键值对字典)字典里边
    def __setattr__(self, key, value):
        print(key,value)

        #1、判定key是否是我们要设置的只读属性的名称
        #假如age属性是只读属性
        if key in ['age','sex'] and key in self.__dict__.keys():
            print('这个属性是只读属性')

        #2、u如果不是只读属性的名称，真正的给他添加到实例属性里边
        else:
            # self.key=value      #注意：这是个坑，这样的写法将会导致死循环。因为这个写法刚好会自动地调用__setattr__方法
            self.__dict__[key]=value
        pass

p1=person()
p1.age=18
# p1.name='lilei'
print(p1.__dict__)  #如果__setattr__方法内部不赋值的话  这里并没有任何属性的键值对
p1.age=20
p1.sex='男'
print(p1.__dict__)
p1.sex='女'
print(p1.__dict__)

p1.__dict__['sex']='女'

print(p1.sex)
###’‘类’‘都有哪些内置的属性
print(person.__name__,'***',person.__dict__,'***',person.__bases__,'***',person.__class__,'***',person.__doc__,'***',person.__module__)
##''实例（常说的对象）都有哪些内置属性''
print(p1.__class__,p1.__dict__)