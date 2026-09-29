'''改错'''
'''
下面代码想实现：依次打印列表中的前三个“今天计划做”，但运行时报错。请找出错误并改正：
```python
plans = ["学Python", "健身", "阅读", "写作"]
for i in range(3):
    print(f"今天计划做：{plans[i]}")
```
（虽然能运行，但可读性不高，你能把它改成用 for 直接遍历列表吗？）
'''


'''回答'''
for i in ["学Python", "健身", "阅读", "写作"]:
    print(f"今天计划做：{i}")



'''优化'''
plans = ["学Python", "健身", "阅读", "写作"]
for plan in plans[:3]:
    print(f"今天计划做：{plan}")