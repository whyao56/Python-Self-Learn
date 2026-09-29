'''改错'''
'''
下面这段代码想打印数字 1 到 5，但是运行时一直打印 1，进入死循环。请找出错误并改正：
num = 1
while num <= 5:
    print(num)
'''


'''回答'''
num = 1
while num <= 5:
    num = num + 1
    print(num)


'''优化'''
num = 1
while num <= 5:
    print(num)
    num += 1            # num += 1 是 num = num + 1 的简写，以后常用