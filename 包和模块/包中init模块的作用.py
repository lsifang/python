#再包被外界导入时还会自动的调用这个文件

import json

print(dir(json))

print(json.__file__)