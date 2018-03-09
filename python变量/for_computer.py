
# # 1、输入
# num1=float(input('请输入第一个数值'))
# num2=float(input('忽如第二个树枝'))
# #2、计算
# num=num1+num2
# #3、输出
#
# print(num)

while True:
# 1、输入
    num1=float(input('请输入第一个数值'))
    num2=float(input('忽如第二个树枝'))
    if num1>100 or num2>100:
        print('你输入的数值有误，青春')
        continue
    #2、计算
    num=num1+num2
    #3、输出

    print(num)
    isq=input('是否想要退出（q:退出）')
    if isq=='q':
        break

'''while 条件循环时使用
    for 遍历循环时使用
'''