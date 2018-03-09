# $-------------字典--------------$

#-----------------定义方式--------------------#

# 1、直接定义
#     key也就是索引不能够重复（重复了也不会报错，只是后边的会把前边的覆盖）
idc={'a':'ewr','b':'c','v':'sdfsfd'}
    # key不能够是可变的值比如列表或者变量（差不多的意思就是必须是字符串或者int）
# 初始化一个被称为“哈希表”的空间，一一对应
#2、静态方法dict.fromkeys(有序序列=》索引,有序序列+》值)

dic=dict.fromkeys('abc',666)#此处的dict相当于一个类方法的调用，是一个类
dic={1:2,2:3}.fromkeys('abc',666)#此处的方法是调用了一个实例化的类（也就是对象）的方法。这样做毫无意义
print(dic,type(dic))


#--------------增-----------------#
# 1、
dic['key']='value'
print(dic)


#--------------删----------------#
#1、del
del dic['key']
print(dic)
# 2、idc.pop(key,[value])  删除key对应的键值对并返回一个值,默认值就是value，有的话就回返回指定的【value】。原字典也会被影响到
result=dic.pop('a')
print(dic,result)

#3、dict.popitem()  删除按升序排序后的第一个值，并返回为一个元组
ditem=dic.popitem()
print(ditem,dic)

#4、dic.clear()  删除所有的字典内所有的值（霍霍，，，高大上的初始化工作）但并不删除字典（和del的区别）（clear是偷光而del不仅偷光还要杀人）。 没有返回值
dcle=dic.clear()
print(dcle,dic)

del dic


#-------------改--------------#
# 1、直接修改

#2、olddic.update(newdic)   olddic.update([newdic])  批量添加键值对（相当于一个字典）如果有重复的key则刷新

d={'old':18,'height':180}
print(d)
d.update({'old':20,'add':'xuchang'})
print(d)

#---------------查--------------#
# 1、dic[key]获取单个值  没有的话会报错
d={'b':'yes','a':'helo'}
# 2、通过dic.get(key，【指定返回值】),没有的话返回none或者指定得返回值 （可用于判断是否存在）
print(d.get('c'))
print(d.get('c',666))
print(d.get('a',666))
# 3、dic.setdefault(key,[指定返回值])  用法和dic.get()一模一样但是（会改变原字典本身）

#-------------查找所有的值-----------#
# 1、dic.values() 获取所有的值
# 2、dic.keys()获取所有的键
# 3、dic.items()获取所有的键值对
print(type(d.values()))
print(d.keys())
print(d.items())
print(tuple(d.keys()))
#注意：为什么返回值不是一个列表。是因为需要在原字典发生变化时（及时的改变获取到的结果）。
# 这个是一个dic view opject（字典视图对象）,可以通过list（）或者tuple（）函数转换

# 4、先遍历所有的key 然后根据指定的key获取相应的值==》dic.keys()
# 2、直接遍历所有的键值对==>dic.items()
for k,v in d.items():
    print(k,v)

#---------判断-----------#
# 1、key （not） in dic   判定的是key