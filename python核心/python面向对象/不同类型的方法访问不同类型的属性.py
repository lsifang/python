class person(object):
    age=0
    def shili(self):
        print(self)
        print(self.age)
        print(self.num)
    @classmethod
    def lei(cls):
        print(cls)
        print(cls.age)
        print(person.age)
        # print(cls.num)
    @staticmethod
    def jing():
        print('')
# 实例方法可以调用类属性和实例属性
# 类方法可以直接调用类属性而不能直接调用实例属性
# 静态方法都不能直接调用但可以通过调用类名访问类属性
p=person()
p.num=10
p.shili()
p.lei()
print(person.__class__)
print(int.__class__)