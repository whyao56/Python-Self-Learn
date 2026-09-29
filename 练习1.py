'''题目'''
'''创建三个变量分别存储家乡城市、邮编、平均温度，并用三种 print 方式打印'''

'''回答'''
city = "北京"
post_code = 100000
average_temperature = 20

print(city)
print(f"{post_code}")
print(f"{average_temperature}")


'''优化'''
# 方式1：用 + 连接（记得把数字转成字符串）
print("我的家乡是" + city + "，邮政编码是" + str(post_code) + "，平均气温" + str(average_temperature) + "度")

# 方式2：用逗号分隔
print("我的家乡是", city, "，邮政编码是", post_code, "，平均气温", average_temperature, "度")

# 方式3：用 f-string（最推荐）
print(f"我的家乡是{city}，邮政编码是{post_code}，平均气温{average_temperature}度")