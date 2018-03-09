#=====写入=============#
# f.write('[zifuchuan]')
# 这个方法有一个返回值，返回的是写入的字节数

f=open('b.txt','a')
if f.writable():
    num=f.write('xinzenghenf')
    print(num)
f.flush() #立即清空缓存并写入磁盘flush()
f.close()



#============关闭============#
# 为什么要关闭
# 1、释放系统资源
# 2、立即清空缓存写入磁盘（也就是立即存档）###相当于避免因为断电等意外事件导致文档写入或读取混乱