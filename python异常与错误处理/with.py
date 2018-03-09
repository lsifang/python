class Test:
    def __enter__(self):
        return  (self)
    def __exit__(self, exc_type, exc_val, exc_tb):   #1代表错误类型。2代表错误内容。三代表？追踪信息（错误定位） 借助traceback模块打印出具体在哪一行
        import traceback
        print(traceback.extract_tb(exc_tb))
        return True   #都能够返回true时，就不会报错。flase反之、

with Test() as x:
    print(x)

#上下文管理器

import contextlib
@contextlib.contextmanager
def test():
    print('1')
    yield  'xxx'
    print('2')

with test() as x:
    print('3',x)