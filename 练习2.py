'''改错'''
'''
city = "北京"
population = 21540000万
area = 16410.54
print("城市：" + city + "，人口：" + population)
print(f"面积：area 平方公里")
'''

'''作答'''
city = "北京"
population = "21540000万"
area = 16410.54

print("城市：" + city + ",人口：" + population)
print(f"面积：{area} 平方公里")

'''优化'''
city = "北京"
population = 21540000        # 纯整数，方便计算
area = 16410.54

# 推荐全部用 f-string，避免 + 号连接混用
print(f"城市：{city}，人口：{population}万")
print(f"面积：{area} 平方公里")
