'''题目'''
'''
写一个程序，询问用户的姓名、喜欢的食物、每月的零花钱（元），然后打印一句话，格式如下：
你好，小明！你喜欢的食物是 汉堡，每月零花钱 500 元。
（注意：零花钱要能进行数学运算，比如同时打印“两个月零花钱是 1000 元”）
'''

'''回答'''
name = input("你的名字是：")
f_food = str(input("你喜欢的食物是："))
monthly_p_money = float(input("每月的零花钱是（元）："))

print(f"你好，{name}!你喜欢的食物是 {f_food}，每月零花钱 {monthly_p_money}")
print(f"两个月的零花钱是： {monthly_p_money * 2}")


'''优化'''
name = input("你的名字是：")
f_food = input("你喜欢的食物是：")         # ✅ 直接赋值，不需要 str()
monthly_p_money = float(input("每月的零花钱是（元）："))

print(f"你好，{name}!你喜欢的食物是 {f_food}，每月零花钱 {monthly_p_money}")
print(f"两个月的零花钱是：{monthly_p_money * 2}")   # 注意：float 乘法结果可能带小数点