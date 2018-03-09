class person:
    @classmethod
    def run(cls,who):
        print(cls,who,'is running...')
        return 1
    pass

print(person.run('路志磊'))
p=person()
p.run('张雷召')
l=[1,2,3,45]
list.sort(l)