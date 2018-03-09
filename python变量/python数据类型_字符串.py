#
name='a'\
'b'
print(name)

name=r'\n\\\t'
print(name)
#--------------------------字符串切片-------------------------------#
name='abcsdefg'
result=''
for i in name:
    result=i+result
print(result)
#反转字符串
name[::-1]
print(name[-1:-5:-1])