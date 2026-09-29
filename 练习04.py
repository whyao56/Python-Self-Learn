'''改错'''
'''
length = input("请输入长度：")
width = input("请输入宽度：")
area = length * width
print(f"面积是：{area}")
'''

'''回答'''
length = int(input("请输入长度："))
width = int(input("请输入宽度："))
area = length * width
print(f"面积是：{area}")


'''提示'''
'''
原代码的两个错误正是：
1. `input()` 返回的是字符串，直接 `length * width` 会变成字符串重复（输入5和3会得到"55555"），而不是数学乘法。
2. 没有将字符串转换成数字。
'''