#--------------#
# __metaclass__表示元类的标识符
# class persong(metaclass=xxx(代表一个元类)):
# type
# __metaclass__=xxx(这里代表一个元类)  模块级别的

class person:
    # __metaclass__ = xxx(代表一个元类) 默认为type 父类级别的
    pass
class goodman(person):  #这里代表继承自一个父类
    pass

#===========类的注释==========#

class person:
    """
    关于这个类的描述，了的作用，类的构造函数等等
    Attributes:
        count:int 代表人的个数
    """
    #这个表示是人的个数
    count=1
    def run(self,distance,step):
        """
        这个方法的作用
        :param distance:参数的含义，参数的类型int，是否有默认值
        :param step:
        :return:返回值的含义，返回值的类型int
        """
        print('renzaipao')
        return

help(person)
a=10