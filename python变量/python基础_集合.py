#===========概念============#

# 1、无序的，不可指定访问集合内单个元素的集合  类型名称是set或者frozenset(可变和不可变)
#注意。每次输出是set的元素排序都会变化
l={1,2,3,4}
print(type(l))
# 2、set()函数，函数内是一个可迭代对象如str，list tuple.对象为dic仅仅是key可以被取到
#3、frozenset（）函数用法一样
s=set('123')
s1=set([1,2,3])
s2=set((1,2,3))
s3=set({1:'a',2:'b'})
print(s,type(s))
print(s1,type(s1))
print(s2,type(s2))
print(s3,type(s3))

#注意，在创建一个空集合时必须加上set（）或者frozenset（）函数，不然会被识别成字典


#-------------增加-----------#

# 1、是通过一个对象方法新增 s.add()
s.add('4')
print(s)

#-------------删除-----------#
# 1、s.remove（）函数
# 2、s.discard()对象方法
#3、s.pop()对象方法随即删除某个
# 4、s.clear()清空一个集合

# 5、del  删除集合变量
it=iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
it=iter(s)
for v in it:
    print(v)
