#--------------------#
# 1、set.intersection(otherset)  注意注意：与&运算符一样&&&&&&&
# 另外:返回的交际集合与最前边的集合类型一样如可变或不可变
#新知识:Intersection()可与其他可迭代对象起作用如字符串\元组\列表.注意的是把这些可迭代对象先转换为集合在进行运算
# &
# &
# &
# 2、set.intersectionupdate(otherset)...把交集付给原集合（set）
s1={1,2,3,4,5}
s2={4,5,8,6,12}
s=s1.intersection(s2)
s3=s1 & s2
print(s)
print(s3)

#=============并集==============#

# 1、set.union(otherset)
# 2、符号  |
# 3、set.update(otherset)

#============差集============#
# 1、set.difference(otherset)
#2、符号 -  减号
# 3、set.difference_update(otherset)