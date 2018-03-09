import os
os.chdir('./three')
sourse_file=open('two.txt','r',encoding='utf-8')
fuben_file=open('three.txt','a',encoding='utf-8')

while True:
    cont=sourse_file.read(1024)
    if len(cont)==0:
        break
    print('-'*30)
    fuben_file.write(cont)

sourse_file.close()
fuben_file.close()