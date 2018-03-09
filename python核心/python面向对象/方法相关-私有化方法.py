class person:
    __age=18
    def __run(self):
        print('running...')     #使用场景。。只有在类内使用而不想要外界使用


print(person.__dict__)

p1=person()