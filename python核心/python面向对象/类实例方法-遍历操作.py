# class person:
#     def __init__(self):
#         self.result=1
#     def __getitem__(self, item):   #for in  会调用这个方法
#         self.result+=1
#         if self.result>=6:
#             raise StopIteration("停止遍历")
#         return self.result
#
# p=person()
# #如果通过for in 访问一个类实例，而这个实例内部刚好有一个__getitem__实例方法，那么就会调用此方法循环输出。
# #   如果该实例方法内部没有打破循环的条件，那么就会一直输入 return结果
# for i in p:
#     print(i)

# 方式2 __iter__方法

class person:
    def __init__(self):
        self.result = 1

    def __getitem__(self, item):  # for in  会调用这个方法
        self.result += 1
        if self.result >= 6:
            raise StopIteration("停止遍历")
        return self.result
    def __iter__(self):             #当存在这个方法时 for in 会优先调用这个方法
        return iter([1,2,3,4,5])


p = person()
# 如果通过for in 访问一个类实例，而这个实例内部刚好有一个__getitem__实例方法，那么就会调用此方法循环输出。
#   如果该实例方法内部没有打破循环的条件，那么就会一直输入 return结果
for i in p:
    if __name__=='__main__':
        print(i)