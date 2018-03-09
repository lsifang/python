while True:
    str=input('请输入一个三位数')
    num=int(str)
    while num>999 or num<100:
        str = input('请重新输入一个三位数')
        num = int(str)
    a=num//100
    b=num%100//10
    c=num%10
    result=(a**3+b**3+c**3==num)
    if result:
        print('是的')
    else:
        print('不是')