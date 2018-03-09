# for i in range(1,101):
#     if i%3!=0:
#         continue
#     print(i)
for i in range(1,10):
    for j in range(1,i+1):
        num=j*i
        print('%d*%d=%d'%(j,i,num),end='\t')
    print('')
