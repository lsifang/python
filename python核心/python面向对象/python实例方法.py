class person:
    def eat(self,foot):
        print("在吃：",self,foot)
    def run():      #这个是闹着玩的，具体开发中并没有什么卵用
        print('run')
# 1、标准调用--实例调用
p=person()
p.eat('肉')
print(p)

#其他调用本质就是直接找到函数本身。嗯，通过类名去找。不常用
#2、其他调用——类调用
person.eat(p,'排骨')

#3、其他调用——间接调用
func=person.eat
func(p,'骨头')

person.run()  #这个是闹着玩的，具体开发中并没有什么卵用