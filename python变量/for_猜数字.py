import random
num=random.randint(1,500)
cont=0
while True:
    a = int(input('不妨猜一下我心里想的什么'))
    cont+=1
    if a<num:
        print('太小了')
    if a>num:
        print('太大了')
    if a==num:
        print('恭喜你，猜对了，答案就是%d'%num)
        print('猜了%d次'%cont)
        break