#_*_encoding:utf-8_*_
import os  #引入os模块

#=======重命名=========#
# os.rename([原文件名]，【修改后的文件名】)
# os.rename('a.txt','x.txt')  # 重命名文件（这里是直接写的，不需要打开文件）

# os.rename('first','one')   #重命名文件夹


#os.renames()  重命名文件以及文件的目录名称

# os.renames('one/one.txt','three/two.txt')

#======删除======#
# 1、删除文件
# 1、os.remove(【文件路径】)  #文件不存在会报错
# os.remove('xxx2.jpg')

# 2、删除目录
# 1、os.rmdir(【文件夹名】) 删除目录#目录非空会报错
# os.rmdir('three')  #这里会报错，目录非空
# os.rmdir('one')  #目录不错在会报错
# os.rmdir('one/one')

# 2、os.removedir()  #树状删除。。会删除目录以及目录的路径
# os.removedirs('one/one')



#___________新建文件夹_____________#

# 1、os.mkdir(【目录名称】，【可选参数mode】)  #这样子记（makedir创建文件夹  ）
#详解mode参数。。代表的是文件夹的读写操作权限（读的值是4  写2 执行1）例如
# os.mkdir('c',0o777)  #1+2+4都等于7.第一个是管理员  第二个是xxx  第三个数字是xxx
# 格式都是0o开头  后边跟三个权限的相加，三个数字一一对应访问者  比如0o764

# os.mkdir('a')  #文件夹已存在会报错


# 2、os.makedirs()创键文件夹以及路径
# os.makedirs('b/c/d')  #文件夹已存在会报错



#_______________获取当前目录_________________#

print(os.getcwd())   #获取当前目录
os.chdir('E:\python基础\python函数')   #(changedir)  改变默认的当前目录
print(os.getcwd())  #默认目录已经改变

print(os.listdir())
print(os.listdir('E:\python基础\python文件'))  #获取目录的文件列表(默认参数为当前目录)
open('cc.txt','w')

# './'一个点+一个斜杠、、、文件所在的当前目录
# '../'两个点+一个斜杠、、、文件所在目录的上一级目录