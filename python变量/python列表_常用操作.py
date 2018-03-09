
#_*_encoding:utf-8_*_
#-----------------增加--------------------#
list=['a','b','c','d','e']
nums=[1,2,3,4,5,6]
#appen（元素）自动增加到列表的最后  会修改原列表
#insert（索引，元素） 增加到指定位置
list.append(nums)
list.insert(1,'hi')
str='yes'
#extend() 列表中增加一个可迭代变量 如列表,字符串也可以
list.extend(nums)
list.extend(str)


#加号运算+++++#print(list+str)会报错只能是列表

print(list+nums)

print(list)

#------------删除---------------------#
#del 语句  是一个语句，直接删除
del list[1]

# pop()移除列表指定索引的元素并返回此元素，默认值为-1及最后一个
result=list.pop()
list.pop(-3)
#remove()删除列表中制定的元素 默认删除最左边一个 没有返回值
list.remove('y')



print(result)
print(list)