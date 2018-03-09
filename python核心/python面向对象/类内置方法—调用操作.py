#------------call方法-------------#
# 当实例被直接调用时会自动的调用call方法

# class person:
#     def __call__(self, *args, **kwargs):
#         print('xxx',args,kwargs)
#     pass
#
# p1=person()
#
# p1(123,456,name='sz')

#创建很多个画笔，画笔的类型（铅笔，钢笔）画笔的颜色（red，yellow...）
class huabi(object):
    def __init__(self,p_type):
        self.p_type=p_type
        self.char={}
    def __call__(self, p_color):
        print('创建了一个%s类型的画笔，它的颜色是%s'%(self.p_type,p_color))

#有字典的形式去操作一个类的属性———增删改查
    def __setitem__(self, key, value):
        self.__dict__[key]=value
    def __getitem__(self, item):
        return self.__dict__[item]
    def __delitem__(self, key):
        del self.__dict__[key]
# def cteatepen(p_color,p_type):
#     print('创建了一个%s类型的画笔，它的颜色是%s'%(p_type,p_color))
# import functools
# pen1=functools.partial(cteatepen,p_type='钢笔')
# pen2=functools.partial(cteatepen,p_type='铅笔')
# pen1(p_color='红色')
# pen1('黄色')
pen1=huabi('钢笔')
pen1('红色')
pen2=huabi('铅笔')
pen2('黄色')
pen1['name']=1
print(pen1['name'])
print(pen1.__dict__)
del pen1['name']
print(pen1.__dict__)
pen1['name']='name'
print(pen1['name'])
print('**' * 30)
#############################################
class person(object):
    # __slots__ = ['__age','__name','__sorce','__sex','__dict__']
    def __init__(self,name):
        self.__dict__['name']=name
        self.__dict__['age']=28
    def __str__(self):
        return ('姓名:%s'%self.name)            #实例
    def __call__(self):                         #实例（）
        return ('姓名：%s。'%self.name)
    def __setitem__(self, key, value):
        print('setitem')
        self.key=value
    def __getitem__(self, item):
        print('setitem')
    def __delitem__(self, key):             #列表删除
        print('setitem')
    def __setattr__(self, key, value):      #当出现实例名.属性=值是会自动调用这个方法
        print('setattr')
        self.__dict__[key]=value
    @property
    def age(self):
        # print('propert')
        return self.age
    # @age.setter
    # def age(self,age):
    #     print('propert')
    #     self.__age=age
    # @age.deleter
    # def age(self):
    #     print('propert')
    #     del self.__age
p1=person('张三')
print(p1)
print(p1())
print(p1.__dict__)
print(p1.__dict__)
print(p1.age)