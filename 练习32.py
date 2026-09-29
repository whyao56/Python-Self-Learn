'''题目'''
'''
下面代码想筛选出“最高温大于 20 且最低温大于 10”的城市，但运行时只返回了布尔值，没有返回表格。请修改代码，让它正确输出满足条件的完整行：
```python
import pandas as pd
df = pd.read_csv("weather.csv", encoding="utf-8-sig")
result = df["最高温"] > 20 and df["最低温"] > 10
print(result)
```
（提示：pandas 中的“与”操作用 `&`，而不是 `and`，并且每个条件必须加括号；如果还是报错，想想 `and` 与 `&` 的区别。）
'''


'''回答'''
import pandas as pd
df = pd.read_csv("weather.csv", encoding="utf-8-sig")
result = (df["最高温"] > 20) & (df["最低温"] > 10)
city = df[result]
print(city)


