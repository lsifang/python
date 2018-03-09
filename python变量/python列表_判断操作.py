#------------------------#
#雷表是否包含某一个元素，类似于字符串的判断方式（a in b）
#cmp()函数。在python3中已不支持
a='abdfawersdcd'
print('a' in a)
print('d' not in a)



#---------排序排序排序排序排序排序排序排序------------#
# 内置函数sorted(可迭代对象，key=none,reverse=false)-------参数reverse代表升序或者降序 默认为false升序  返回一个列表
b=sorted(a,reverse=True)
print(b)
lis=[1,2,5,4,6,87,96,5]
print(sorted(lis,reverse=True))
lis=[('sz',18),('sz1',15),('sz2',17),('sz3',14),('sz4',19)]
#getkey函数指定key
def getkey(x):
    return x[1]
#记住怎么用就行了
print(sorted(lis,key=getkey,reverse=True))

#----------------------#

#list.sort(key,reverse) 这个是列表方法
print(lis.sort())  #没有返回值
print(lis)


#方法的用法就是【变量】.【方法名】（参数）。。。。。。。。而函数的用法是【模块】.【函数名】（[变量]，参数）
#函数一般都有返回值，而方法一般都没有