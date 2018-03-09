#公有属性 （name） 可以在父类，派生类，模块内其他位置，其他模块（引入后）正常访问


#私有属性（_name） 可以在父类、派生类正常访问，在模块内其他位置也可以访问但会产生一个警告，其他模块（引入后）不可以访问！！__
                    # all__=['_name']这个方法可以给允许访问的私有化属性授权，后边是一个列表。


#完全私有化属性（__name）,属性前跟两个下划线。类内可以访问。。在其他地方不可以访问.
#                         但在其他模块访问模式和_(一个下划线开头的)原则一样

#python并不支持私有化属性，而是以属性名重整的机制达到伪私有化的效果》__a重整为{_(类名)__a}这样的名称
class Animal:
    a=10
    _b=20
    __c=30
    def test(self):
        print(Animal.a)
        print(Animal._b)
        print(Animal.__c)
class dog(Animal):
    def test2(self):
        print(dog.a)
        print(dog._b)
        print(dog.__c)
p=Animal()
print(p._Animal__c)

