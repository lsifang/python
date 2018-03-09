#===========读方法=============#
# 1、read(【字节数】) 全部读取（默认全部）注意(字节数也包括换行或者制表符)
# 2、f.readline() 每次读取一行(从当前的位置读取一行)
# 3、f.readlines() 全部读取并把每一行（或者说是按照换行符进行处理后的一段）当作一个元素存入一个列表

# 注意：文件就是一个迭代器，怪不得也是指针型的遍历，每次操作都会移动指针的位置

f=open('b.txt','r')
# t=f.read(9)
# print(f.tell())
# print(t)
# f.close()
# f.seek(9)
# x=f.readline()
# y=f.readline()
# print(x,end='')
# print(y)
# t=f.readlines()
# print(t)
# print(f.tell())
import collections
if f.readable():
    print(isinstance(f,collections.Iterator))
    print(next(f))
    print(next(f))
    print(next(f))
    print(f.__next__())
    f=open('b.txt','r')
    t=f.readlines()  #你看，这里返回的是一个空的列表#如果前边不重新定义f的话
    print(isinstance(t,collections.Iterator))   #readlines()不是一个迭代器应为他是一个列表
    t=iter(t)
    print(isinstance(t,collections.Iterator))
    print(next(t))

#———————判定方法———————#
# if f.readable():########主要是为了代码的容错处理