import os
# os.chdir('./files')
# file_list=os.listdir('./')
# for file_lis in file_list:
#     print(file_lis)
#     file_name=os.listdir('./'+file_lis)
#     for file_name1 in file_name:
#         print('\t',file_name1)
def listfilesTotxt(path,file):
    #列举所有的子文件夹以及文件
    # os.chdir('./%s'%path)
    dir_list=os.listdir(path)
    #遍历这个列表
    for dir_name in dir_list:
    #针对列表判断是否是文件夹
        new_filename=path+'/'+dir_name
        if os.path.isdir(new_filename):
            file.write(new_filename+'\n')
            listfilesTotxt(new_filename,file)
        else:
            file.write('\t'+dir_name+'\n')
    file.write('\n')
f=open('test.txt','a')
listfilesTotxt('files',f)