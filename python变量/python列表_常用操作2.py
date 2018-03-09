list=['f','e','d','c','b','a']

#------------查找-----------------#
#index() 获取某个元素的索引  从左往右  从第几个查找
idx=list.index('d')
print(idx)

#count()获取指定元素的个数
print(list.count('d'))

#[起始:结束:步长]【start：end ：step】
pic=list[1:5:2]
#【：：-1】反转整个列表
pi=list[::-1]
print(pic)
print(pi)
