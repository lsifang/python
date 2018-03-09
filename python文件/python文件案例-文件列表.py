# 1、遍历所有的文件
import os
import shutil
path='files'
if not os.path.exists(path):
    exit('文件夹不存在')
os.chdir(path)
file_list=os.listdir('./')
for file_name in file_list:
    houzei=file_name.rpartition('.')[2]
    # index=file_name.rfind('.')
    # houzei=file_name[index+1:]
    if not os.path.exists(houzei):
        os.mkdir(houzei)
    shutil.move(file_name,houzei)

