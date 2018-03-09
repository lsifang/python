import math
class jisuan:
    def __init__(self,num):
        self.num=num
    def add(self,x):
        self.num +=x
        return self.num
    def jian(self,x):
        self.num-=x
        return self.num
    def cheng(self,x):
        self.num *=x
        return self.num
    def chu(self,x):
        self.num=self.num/x
        return self.num
    def jieguo(self):
        return self.num

# jisuanqi=jisuan(int(input('请输入一个数字：')))
#
# while True:
#     fuhao = input('请输入一个运算符：')
#     if fuhao=='=':
#         print(jisuanqi.num)
#         break
#     a = int(input('请输入一个数字：'))
#     if fuhao=='+':
#         jisuanqi.add(a)
#     if fuhao == '-':
#         jisuanqi.jian(a)
#     if fuhao=='*':
#         jisuanqi.cheng(a)
#     if fuhao=='/':
#         jisuanqi.chu(a)


def add(x,y):
    num =x+y
    return num
num=int(input('数字'))
while True:
    fuhao = input('请输入一个运算符：')
    if fuhao=="=":
        print(num)
        break
    x=int(input('数字'))
    if fuhao=='+':
        num=add(num,x)
