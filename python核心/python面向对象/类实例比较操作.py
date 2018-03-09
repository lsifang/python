#_____________#所谓的比较对象实际上就是自己定一比较的规则，比如比较比较实例对象的某个属性
#方式1、实例方法。通过实例方法让这个类产生的实例对象拥有比较的功能
class person:
    def __init__(self,age,height):
        self.age=age
        self.height=height
    #== != > >= < <=
    def __eq__(self, other):  #self比较符前边的   other比较符后边的
        print(other)
        return self.age==other.age  #自定义比较规则
    def __ne__(self, other):  #不相等
        print('xxx')
        return self.age!=other.age
    def __gt__(self, other):  #大于
        pass
    def __ge__(self, other):    #大于等于
        pass
    def __lt__(self, other):    #小于
        pass
    def __le__(self, other):    #小于等于
        pass
    # 默认调用最符合比较符的方法。比如等于自动调用eq，但如果eq不存在就会调用ne
    #调换操作
p1=person(18,50)
p2=person(20,60)
print(p1 != p2)


print('*'*30)
# 注意事项
class pen:
    def __init__(self,money):
        self.money=money
    def __lt__(self, other):
        print(self.money)
        print(other.money)
        return self.money<other.money
pen1=pen(18)
pen2=pen(20)
print(pen1 < pen2)
print('*'*30)
print(pen1>pen2)    #这个操作将会调换__lt__方法中self和other的位置。也就是说大于就是一个反过来的小于。
                    # 也就是谁在小于号的箭头所在位置，谁就是self
# 大于和小于是一对。等于和不等于是一对 。大于等于和小于等于是一对
#方式2、通过装饰器补全比较操作的实例方法。就是自动推导出相对应的比较符这个装饰器叫做functools.total.ordering

import functools

@functools.total_ordering
class computer:
    def __lt__(self, other):
        pass
    def __le__(self, other):
        pass
    # def __eq__(self, other):
    #     pass
com1=computer()

print(computer.__dict__)

#-------------关于类实例对象的布尔值------------#
#首先明确非零即真，非空即真
#控制类实例的判断 布尔值 __bool__方法
class student:
    pass
    def __init__(self):
        self.age=10
    def __bool__(self):
        return self.age>=18   #false或者True或者具体的判断语句

p=student()

if p:
    print('xxxxxxxx')
else:
    print('ooooooo')