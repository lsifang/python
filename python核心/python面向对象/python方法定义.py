# 方法划分
# 依据：方法的第一个参数必须要接受的数据类型


# 1、实例方法
# 接受的第一个参数是一个默认参数——实例（self）


# 2、静态方法
# 并没有默认参数  方法前的装饰器标识@staticmethod


# 3、类方法
# 接受的第一个参数是一个默认参数——类（cls）并且类方法前的@classmethod
class person:
    def __init__(self,name):
        self.name=name
    def eat(self):      #实例方法  self代表实力本身
        print('这是一个实例方法',self.name)
        return self.name

    @classmethod        #@classmethod
    def leifangfa(cls):   #类方法，cls代表类本身
        print('zhe是一个类方法',cls)

    @staticmethod          #@staticmethod
    def jingtai():        #静态方法 没有默认参数
        print('zheshiyige静态方法')



p=person('hello')
q=person('world')
print(p.eat())
print(q.eat())
print(person.eat(p))
# p.eat()
# p.leifangfa()
# p.jingtai()
# # person.eat()
# # person.leifangfa()
# # person.jingtai()
# # print(p.__dict__)
# # print(p.__dir__())
# print(dir(person))
# print(person.__dict__)
# print(help(person))
# person.eat(p)