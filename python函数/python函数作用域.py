#========作用域========#
# 1、函数外部不可以访问函数内部的变量
# 2、函数内部可以访问函数外部的变量

a=1
def test():
    a=10
    print(a)
test()
print(a)
# print(b)

# 3、高大上的命名空间（实际上也就是作用于的体现形式，就是变量在哪里可以被访问）比如说学生a在三班,那么这个三班对于a来说就是一个命名空间.
#   不同的具体的操作范围

# 有哪些具体的命名空间分类python-LEGB
# 1、L-local...函数内的命名空间。作用域：整个函数体内部
# 2、E-Enclosing function locals....外部嵌套函数的命名空间。。。作用范围：闭包函数
# 3、G-Global...全局命名空间。。。作用范围：当前文件（或者模块）
# 4、B-Builtin...内建模块命名空间。。。作用范围。。所有文件（或者模块）

# 注意：是按照l->e->g->b的顺序查找（当然，是在本层调用时）
a=999
def test():
    a=666
    def test2():
        global a
        a=333
        print(a)
        print(locals())
    test2()
    print(a)
test()
print(a)