list=['hello','one','two','three']
print(list,type(list))
#列表生成
#列表推导式

nums=[2,3,4,5,6]
#
# result=[]
# for num in nums:
#     resultnum=num**2
#     result.append(resultnum)
# print(result)

#[(变量.表达式)  for 变量 in 列表 if条件]
resultlist='@'.join ([str(num**2) for num in nums if num%2==0])
print(resultlist)