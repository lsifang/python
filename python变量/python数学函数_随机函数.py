#随机函数

import random
#random() 无参数范围[0,1)内的随即小数

print(random.random())

#choice([])列表内的随机取值
a=[1,2,5,4,'a','hello\'']
print(random.choice(a))

#uniform(x,y)x~y之间的随机小数 randint(x,y)x~y之间的随即整数

print(random.uniform(2,5))
print(random.randint(2,5))

#randrange(x,y,[n]) x~y之间的随即整数，n为可选参数[步长]
print(random.randrange(1,15))
print(random.randrange(1,15,2))