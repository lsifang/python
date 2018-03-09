#--------遍历-----------#

#根据元素进行遍历
li=['a','b','c','a','d','e','f','g']

#遍历元素以及list.index()获取到索引
countr=0
for a in li:
    print(a,li.index(a,countr))
    countr+=1
#遍历索引然后获取到每个值
for index in range(len(li)):
    print(index,'=>'+li[index])

#枚举方法enumerate————把列表变为一个包含元元组的列表比如【a,a,a,a】变成【(0,a),(1,a),(2,a),(3,a)】
#遍历整个枚举对象

#idx,val=(0,a)
for idx,val in enumerate(li,1):
    print(idx,val)

#-------------------迭代器（遍历器）-----------------------#

# 迭代（或者遍历）：是访问集合元素的一种方式，按照某种顺序逐个访问集合中的每一项。就是遍历
# 可迭代对象：能够被迭代的对象，
#             判断依据是可被作用与for··in··循环。
#              函数验证方法是isinstance(li,collection.Iterable)
# 迭代器：可以【【自动】】记录遍历位置的对象（与可迭代对象区分） 是一个机器，默认指向（可迭代对象的第一个位置），通过函数next（），指向向后位移，相当于一个指针对象
#             只能往后，不能向前。
#         判断依据能否被作用于next（）函数
#             函数验证方法isinstance(li,collections.Iterator)
#             要注意的是，迭代器也是一个可迭代对象
#      生成一个迭代器的方法iter(li)
#         为什么会存在迭代器：
#              1、在迭代器被函数访问之前，元素可以不存在，访问之后元素可以被销毁。在访问一些巨大的列表或者无限的集合，可以很好的逐一个访问
#             而不会占用过多的内存。比如遍历或者访问~~~著名的斐波那契数列【0,1,1,2,3,5,8.....】后面一个数是前两位之和
#             2、提供了统一的访问集合的接口》在代码可读性及管理更加方便。比如元组、字符串、列表等可迭代对象

#          迭代器不能多次迭代。。。意思就是当一个迭代器的指针指向完毕后。再次使用只能重新创建
import collections
ite=iter(li)
print(isinstance(li,collections.Iterable))
print(isinstance(li,collections.Iterator))
print(isinstance(ite,collections.Iterable))
print(isinstance(ite,collections.Iterator))
print(ite)
# print(next(ite))
# print(next(ite))
# print(next(ite))
# print(next(ite))
for v in ite:
    print(v)
#-------------------#
ite=iter(li)
for v in ite:
    print(v)
