'''理论'''
'''
简单折线图与柱状图
```python
import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
df = pd.DataFrame({
    '月份': ['1月','2月','3月','4月'],
    '销售额': [120, 200, 150, 180]
})

# 画折线图
plt.plot(df['月份'], df['销售额'])
plt.title('月度销售额')     # 标题
plt.xlabel('月份')          # X轴标签
plt.ylabel('销售额（万元）') # Y轴标签
plt.show()                  # 显示图形
```

**用 pandas 自带的 plot 更快捷**：
```python
df.plot(x='月份', y='销售额', kind='bar')   # kind='bar' 表示柱状图
plt.show()
'''

'''题目'''
'''
使用你的 `weather.csv`（或之前创建的任意含数值列的 CSV），完成下面任务：
1. 用 pandas 读取数据。
2. 画一个**柱状图**，X 轴为城市名称，Y 轴为最高温。
3. 设置标题为“城市最高温度对比”，X 轴标签为“城市”，Y 轴标签为“温度（℃）”。
4. 用 `plt.show()` 显示图像。
'''

'''回答'''
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('weather.csv')
# df.plot(x = '城市', y = '最高温', kind = 'bar')
# plt.title('城市最高温度对比')
# plt.xlabel('城市')
# plt.ylabel('温度（℃）')
# plt.show()


'''优化'''
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']   # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False     # 解决负号显示为方块的问题

df = pd.read_csv('weather.csv')
df.plot(x = '城市', y = '最高温', kind = 'bar')
plt.title('城市最高温度对比')
plt.xlabel('城市')
plt.ylabel('温度（℃）')
plt.show()