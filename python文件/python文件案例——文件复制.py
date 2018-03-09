# #要求：把一个文件内容复制到另一个文件当中
# 1、读取源文件内容以x.txt为源文件，以cc.txt为副本文件
# 2、写入源文件内容

# 1、打开源文件及副本文件
import os
os.chdir('./three')
sourse_file=open('two.txt','r',encoding='utf-8')  #这里注意需要保证代码的统一
fuben_file=open('one.txt','a',encoding='utf-8')
# 2、读取数据
for i in sourse_file:
    fuben_file.write(i)

# 3、关闭文件

sourse_file.close()
fuben_file.close()