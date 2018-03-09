# 方案1。全部设置为私有化属性，部分私有化属性的可读公开
#__属性名的__仅仅是表示属性的可访问限制
class person(object):
    # __slots__ =  这个是限制实例中的属性名称
    def __init__(self,sex):     #这个是内置实例属性。当需要传入参数在创建实例对象是传入
        self.__age=18           #默认的实例属性
        self.__run='run'
        self.__sex=sex          #必须创建的实例属性
    def getage(self):
        return self.__age   #私有化属性的可读方法 第一种方法
    @property               #property  记住这个装饰器
    def run(self):
        return self.__run   #优化后的私有性可读方法，这个装饰器的作用是访问属性一样访问方法
    @run.setter
    def run(self,value):    #@property 自动生成了额外的装饰器@xxx.setter   @xxx.deleter  用于修改和删除属性
        self.__run=value
    @run.deleter
    def run(self): 
        del self.__run
p=person('男')
print(p.getage())
print(p.__dict__)
print(p.run)
p.run='fly'
print(p.run)
del p.run
print(p.__dict__)
p.run='pa'
print(p.run)