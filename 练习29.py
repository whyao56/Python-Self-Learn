'''理论'''
'''
**pandas** 是 Python 最强大的数据分析库，它可以把 CSV、Excel、数据库等数据读成一种叫做 **DataFrame** 的表格对象，然后轻松进行筛选、分组、统计等操作，还能画出简单的图表。

### 🧰 安装 pandas
在终端执行：
```
pip install pandas
```
同样，我们会用到另一个库 `matplotlib` 来画图，也一并安装：
```
pip install matplotlib
```
（pandas 的绘图功能依赖 matplotlib，但无需显式导入，pandas 会自动调用。）

---

## 第十四课：用 pandas 读取 CSV 文件

我们之前创建过 `weather.csv`，里面有城市、最高温、最低温。现在用 pandas 把它读进来，看看它长得什么样。

### 🌰 例子：读取 CSV 并显示
```python
import pandas as pd   # 约定俗成把 pandas 重命名为 pd，简洁

df = pd.read_csv("weather.csv", encoding="utf-8-sig")   # 读取 CSV 文件
print(df)              # 打印整个 DataFrame
print(df.head(2))      # 只显示前 2 行
print(df.info())       # 查看每列的数据类型和非空数量
print(df.describe())   # 查看数值列的基本统计（均值、标准差等）
```

### 📖 解释
- `pd.read_csv("文件名")`：读取 CSV，返回一个 **DataFrame**（可以理解为 Python 中的 Excel 表格）。
- `print(df)`：直接打印表格，整齐对齐。
- `df.head(n)`：显示前 n 行，默认 5。
- `df.info()`：显示列名、非空值数量、数据类型，用于快速了解数据集。
- `df.describe()`：针对数值列（自动识别）计算 count、mean、std、min、max 等，非常实用。
'''


'''题目'''
'''
使用你之前生成的 `weather.csv`（如果没有，就现在创建一个，包含“城市”“最高温”“最低温”三列，至少 4 个城市）。
1. 用 pandas 读取该 CSV，赋给变量 `df`。
2. 打印 `df` 的全部内容。
3. 打印 `df.info()` 和 `df.describe()`，观察哪些统计信息被计算了。
4. 用 `df["最高温"].mean()` 计算平均最高温度，并打印。
'''
# import pandas as pd   # 约定俗成把 pandas 重命名为 pd，简洁
#
# df = pd.read_csv("weather.csv", encoding="utf-8-sig")   # 读取 CSV 文件
# print(df)              # 打印整个 DataFrame
# print(df.head(2))      # 只显示前 2 行
# print(df.info())       # 查看每列的数据类型和非空数量
# print(df.describe())   # 查看数值列的基本统计（均值、标准差等）


import pandas as pd

df = pd.read_csv("weather.csv", encoding="utf-8-sig")
print(df)
print(df.info())
print(df.describe())
print(df["最高温"].mean())

'''细节'''
'''
df.info() 本身会打印信息到屏幕，但它并不会返回有用的值（返回 None）。你用 print(df.info()) 会额外打印一个 None，但不影响数据分析。建议以后直接写 df.info()。
'''