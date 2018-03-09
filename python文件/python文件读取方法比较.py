f=open('b.txt','r')
if f.readable():
    for i in  f:
        print(i)
