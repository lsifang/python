class Person:
    def __init__(self,age):
        self.__age=age
    # def __str__(self):
    #     return '%d%s'%(self.__age,'hello')
    def setage(self,value):
        if isinstance(value,int) and 0<value<100:
            self.__age=value
        else:
            print('不正常的年龄')
    def getage(self):
        return self.__age
    def __str__(self):
        return "%d,%s"%(self.__age,"hello world")
p1=Person(20)
print(p1.getage())
p1.setage(30)
print(p1.getage())
print(p1)