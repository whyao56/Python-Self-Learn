'''理论'''
'''
现在你已经能读取数据并做简单统计，但实际工作中我们往往只关心部分数据。例如：
- 只看最高温 > 20℃ 的城市
- 只看名字叫“小”开头的用户

pandas 中通过 **布尔索引** 来筛选，和 Python 的条件判断很像，但它是针对整列进行的。

### 🌰 例子：筛选最高温大于 20 的城市
```python
import pandas as pd

df = pd.read_csv("weather.csv", encoding="utf-8-sig")
print("原始数据：")
print(df)

# 创建条件：最高温列 > 20，得到一个布尔 Series
condition = df["最高温"] > 20
print(condition)   # 会输出 True/False 的序列

# 把条件放到 df[...] 里，返回满足条件的行
hot_cities = df[condition]
print("\n最高温大于 20 的城市：")
print(hot_cities)
```

**也可以一行搞定**：`df[df["最高温"] > 20]`

### 📖 解释
- `df["最高温"]` 是一列数据（Series）。
- `> 20` 会对每个元素进行比较，返回一个**布尔 Series**（例如 `[True, False, True]`）。
- 把布尔 Series 放入 `df[...]`，就会保留 `True` 对应的行，舍弃 `False` 的行。
- 这与 Excel 的“筛选”功能一模一样。

'''


'''题目'''
'''
使用 `weather.csv`（之前创建的文件，有城市、最高温、最低温三列），完成以下操作：
1. 筛选出**最高温大于等于 25** 的城市，将结果存为 `hot`。
2. 打印这些城市的名称和最高温（只打印这两列）。
3. 计算这些城市**最低温的平均值**并打印。
'''


'''回答'''


# import pandas as pd
# df = pd.read_csv("weather.csv", encoding="utf-8-sig")
# print("原始数据是：")
# print(df)
#
# condition = df["最高温"] >= 25
# print(condition)
#
# hot = df[condition]
# print("\n最高温大于等于 25 的城市：")
# print(hot)
# print(f"{hot['城市']}：{hot['最高温']}")
#
# print(f"最低温的平均值：{df['最低温'].mean()}")


'''优化'''
import pandas as pd
df = pd.read_csv("weather.csv", encoding="utf-8-sig")
hot = df[df["最高温"] >= 25]  # df["最高温"] >= 25 进行比较，得到布尔值（True/False）序列
# df[布尔序列] 只保留条件为 True 的行

print("最高温大于等于 25 的城市：")
print(hot[['城市', '最高温']])            # hot[['城市', '最高温']] 只选择"城市"和"最高温"两列（双括号表示选择多列）
print(f"这些城市的最低平均温：{hot['最低温'].mean()}")