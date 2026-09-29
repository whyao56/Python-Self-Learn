'''目标'''
'''
进入综合实战：天气 API → 数据处理 → CSV 保存

你已经掌握了所有必要的技能：变量、循环、函数、文件读写、CSV 操作、requests、JSON 解析、pandas 操作、绘图。
现在我们把它们串联起来，完成一个有实际用途的项目！

### 🎯 项目目标
1. **调用 Open-Meteo 天气 API**（无需注册、免费、无需 API Key）
2. **解析返回的 JSON**，提取未来 7 天的日期、最高温、最低温
3. **用 pandas 整理数据**，计算平均温度等统计量
4. **保存为 CSV 文件** `weather_forecast.csv`
5. **（可选）画一个温度趋势折线图**

这个 API 的接口格式为：
```
https://api.open-meteo.com/v1/forecast?latitude=纬度&longitude=经度&daily=temperature_2m_max,temperature_2m_min&timezone=Asia/Shanghai
```
例如北京（纬度 39.9, 经度 116.4）：
```
https://api.open-meteo.com/v1/forecast?latitude=39.9&longitude=116.4&daily=temperature_2m_max,temperature_2m_min&timezone=Asia/Shanghai
```
直接在浏览器打开就能看到 JSON 数据。
'''


'''指导'''
'''
### 第一步：获取并解析 API 数据
```python
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 39.9,       # 北京纬度
    "longitude": 116.4,     # 北京经度
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "Asia/Shanghai"
}

response = requests.get(url, params=params)   # 用 params 参数更清晰
data = response.json()
# print(data)   # 可以先打印看看 JSON 结构
```

**请完成**：
- 运行这段代码，打印 `data` 的 `keys()`，找到 `daily` 键对应的子字典，将其赋给变量 `daily_data`。
- 然后打印 `daily_data` 的 `keys()`，看看里面有哪些信息。
'''


import requests
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 39.9,
    "longitude": 116.4,
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "Asia/Shanghai"
}

response = requests.get(url, params=params)
data = response.json()
print(data)
print(data.keys())

daily_data = data['daily']
print(daily_data.keys())  # 查看 daily 下的键

print("=======================================")

import pandas as pd
df = pd.DataFrame(daily_data)
print(df.head())  # 预览前几行

df.to_csv('weather_forecast.csv', encoding='utf-8', index=False)
print("天气数据已保存为 weather_forecast.csv")

print(f"未来 7 天平均最高温：{df['temperature_2m_max'].mean():.2f}℃")
print(f"未来 7 天平均最低温：{df['temperature_2m_min'].mean():.2f}℃")
print(f"最高温度出现在：{df.loc[df['temperature_2m_max'].idxmax(), 'time']},为 {df['temperature_2m_max'].max()}℃")


import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot(df['time'], df['temperature_2m_max'], marker='o', label='最高温')
plt.plot(df['time'], df['temperature_2m_min'], marker='s', label='最低温')
plt.title('北京未来7天温度趋势')
plt.xlabel('日期')
plt.ylabel('温度（℃）')
plt.xticks(rotation=45)   # 让日期斜着显示，避免重叠
plt.legend()
plt.tight_layout()
plt.show()