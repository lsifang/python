str='我就，是牛逼'
for a in str:
    print(a)
else:
    print('已全部打印完毕')
result=''
for a in str:
    result=a+result
print(result)
for i in range(1,101):
    if i%2==0:
        print('%s是偶数'%i)
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(j,i,j*i),end='\t')
    print(' ')