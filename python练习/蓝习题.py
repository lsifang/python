a=1
def xxx():
    a=2

xxx()
print(a)

a=[]
def xxx(a):
    a.append(1)
xxx(a)
print(a)
a=iter(range(10))
next(a)
next(a)
next(a)
next(a)
next(a)

