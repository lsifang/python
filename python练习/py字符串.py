s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('哦名的成绩提高了%.1f%%' % r)

n1 = 255
n2 = 1000
print(hex(n1))

def chengfa(*args):
    num=1
    for i in args:
        num=num*i
    return num
hello=chengfa(1,2,3,4,5,6)
print(hello)
def trim(s):
    j=''.join([a for a in s if a!=' '])
    return j
def trip(s):
    while s[0]==" ":
        s=s[1:]
    while s[-1]==" ":
        s=s[:-2]
    return s
print(trim('  helo   '))
print(trip("  hello  "))

def findmm(l):
    if l==[]:
        return (None,None)
    min = l[0]
    max = l[0]
    for i in l:
        if i<min:
            min=i
        if i>max:
            max=i
    return(min,max)
print(findmm([1,2,5,8,4]))
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
l3=[s.lower() if isinstance(s,str) else s for s in L1]
print(L2)
print(l3)
def triangles():
    d=[1]
    while True:
        yield d
        d=[1]+[d[i]+d[i+1] for i in range(len(d)-1)]+[1]
t=triangles()
n=1
while True:
    print(next(t))
    n=n+1
    if n==13:
        break
