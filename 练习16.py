'''改正'''
'''
下面这段代码想定义一个函数计算圆的面积（面积 = 圆周率 * 半径²），但调用时却报错 `TypeError`。请找出错误并改正：
```python
def circle_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area

print(circle_area())   # 想计算半径=5的面积
```
'''

def circle_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area

print(circle_area(5))   # 想计算半径=5的面积