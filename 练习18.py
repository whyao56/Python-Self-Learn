'''题目'''
'''
### 🎯 练习18（变式题）
下面是计算三角形斜边的代码，但缺少了导入模块和正确调用。请补全并修正：
```python
a = 3
b = 4
c = sqrt(a**2 + b**2)   # 想使用 math 模块的 sqrt 函数
print(f"斜边长是 {c}")
```
修改后，要求程序能正确输出 5.0。
'''

'''回答'''
from math import sqrt
a = 3
b = 4
c = sqrt(a**2 + b**2)   # 想使用 math 模块的 sqrt 函数
print(f"斜边长是 {c}")


'''另一种方法'''
import math
a = 3
b = 4
c = math.sqrt(a**2 + b**2)   # 加上 math. 前缀
print(f"斜边长是 {c}")