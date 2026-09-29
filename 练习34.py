'''题目'''
'''
下面代码想统计每个产品在不同地区的平均销售额，但报错 `KeyError`。请找到错误并改正：
```python
import pandas as pd
df = pd.read_csv("sales.csv")
result = df.groupby("产品")["地区"].mean()
print(result)
```
（提示：要对销售额求平均，键名是什么？）
'''


'''回答'''
import pandas as pd
df = pd.read_csv("sales.csv")
result = df.groupby(["产品","地区"]).mean()
print(result)


'''优化'''
import pandas as pd
df = pd.read_csv("sales.csv")
result = df.groupby(["产品", "地区"])["销售额"].mean()
print(result)