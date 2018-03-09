#------计算函数-----#
# 作用
# 语法
# 参数
# 返回值
#len()计算字符串的个数
name='abcdefg'
print(len(name))

#find()查找出现位置索引  rfind()从右至左。未找到时返回值为-1,[n]可选参数为从第几个开始查找
num=name.find('d',4)
print(num)
#index()与上边类似，但未找到时程序出错


#----------------转换函数------------------#
#replace（）替换字符串函数  不会修改原字符串本身

# print(name.replace('a','l'，【n】))

#capitalize() 字符串首字母大写

#title（）字符串每个单词的首字母大写

#lower()所有字符串都变为小写  upper（）见字符串内所有字符都变为大写
name='hello'
#---------------填充压缩函数-----------------#
#ljust()填充在右边 rjust()  填充函数在左边  center（）平分分配在左右，多的一个分在右边
print(name.ljust(8,'x'))
print(name.rjust(8,'x'))
#strip()  lstrip()  rstrip()  去除函数
print(name.strip())
print(name.rstrip('elo'))

#------------分割拼接函数--------------#
#split()分割成列表类型,按照分隔符全部分割如果没有定义列表长度的话
#splitlines（）按照\n,\t等制表符自动分割字符串为列表，不需要指定分隔符


#partition（）分割成元组类型,包括三个元素。分隔符前边的，分隔符，分隔符后边的
#rpartition（）从右往左查找分隔符

res='wo-shi-fang-a*a(a'
print(res.split('-'))
print(res.partition('-'))

#join（）将指定分隔符加入到‘’‘可迭代对象’‘’内（列表，元组，字符串等）组成新的字符串
items=['wo','shi','da','ying','jia']
a='hello'
print('@'.join(items))
print('@'.join(a))


#--------------判断函数----------返回值均为布尔型--------------------#
# name.isalpha()是否都是字母至少有一个   name.isdigit()是否都是数字，至少有一个
#name.isalnum()是否都是字母或者数字，至少有一个
#name.isspace()是否都是空白符比如空格、换行等不可见转义符，至少有一个

#name.startswith(‘str’)字符串是否以某一个参数开始
# name.startswith(‘str’)字符串是否以某一个参数结束

fil='2018-2-8:某某单位.xls'
print(fil.endswith('.xls'))