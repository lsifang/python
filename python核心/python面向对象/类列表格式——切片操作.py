####___________—————切片操作—————____________########
# class person:
#     def __getitem__(self, item):
#         print('getitem',item)
#     def __setitem__(self, key, value):
#         print(key.start,key.stop,key.step,value)
#     # def __delitem__(self, key):
#     #     pass
# p1=person()
# p1[0:4:2]=[1,2]
# p1[0:5:2]
# print(p1.__dict__)
# import random
#
# list=[1,2,3,4,5,6,8,9,5,52,74,85,5,58]
# def randlist(list):
#     # a=list.pop(random.randint(0,3))
#     newlist=[]
#     for i in range(3):
#         n=len(list)-1
#         t=list.pop(random.randint(0, n))
#         newlist.append(t)
#     print(newlist)
#     if len(list)>=3:
#         randlist(list)
#     return list
#
#
# print(randlist(list))

class person:
    def __init__(self):
        self.items=[1,2,3,4,5,6,7,8]
    def __getitem__(self, item):
        # print(item)
        return self.items[item]
    def __setitem__(self, key, value):  #切片操作只能修改不能新增 #key是一个列表的【0:4:2】 这是一个slice
        # print(key,value)
        self.items[key]=value
        if isinstance(key, slice):
            self.items[key.start:key.stop:key.step]=value  #这样也是可以的
    def __delitem__(self, key):
        del self.items[key]
p1=person()
p1[0:4:2]=['a','b']
print(p1.items)
del(p1[0:4:2])
print(p1.items)
