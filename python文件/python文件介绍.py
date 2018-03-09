#=======文件=======#
# 1、打开
# open()函数

#模式（常用）大全：
# ---'r'只读模式(文件不存在会报错)--
# ---'w'只写模式(文件不存在会新建)(会覆盖原文件)--
# ---'a'只写模式(文件不存在会新建)，但是新增内容会增加到文件的结尾（也就是新增）
#---'rb''wb''rb'.分别是以二进制模式操作。比如音频图片视频等
#----'+' 在上述模式中跟一个+号。代表读写。带拥有+号前边的独特个性。比如文件不存在时报错还是创建等

# 这里也有指针操作的特性，比如先读后写就会把指针放在文件最后

f=open('b.txt','w')
jpg=open('xxx.jpg','rb')
jpg2=open('xxx2.jpg','wb')

# # 2、定位-》读写
# .read（）
# .write()
# conten=f.read()
# print(conten)
f.write('#000')
content=jpg.read()
print(type(content))
fromcon=content[0:len(content)//2]
jpg2.write(fromcon)

# 3、关闭
# .close()
f.close()
jpg.close()
jpg2.close()

#==========定位操作==========#
# 1、seek(【偏移量】，【可选参数（0,1,2）】)。0是默认相对于起始位，1是相对于当前指针位置。2是相对于末尾位置（二进制才能用，前边的偏移量必须是-数）
# 2、f.tell() 获取当前文件指针的位置
