'''改错'''
age = int(input("年龄："))
eyesight = input("视力：")
if age >= 18 and eyesight >= 1.0:
    print("可以领驾照")
else:
    print("不能领驾照")



'''回答'''
age = int(input("年龄："))
eyesight = float(input("视力（精确到几点几）："))
if age >= 18 and eyesight >= 1.0:
    print("可以领驾照")
else:
    print("不能领驾照")