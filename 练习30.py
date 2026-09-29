'''题目'''
'''
运行 `df["最高温"].plot()` 可能会看到什么？如果还没学可视化，可以先运行试试，然后告诉我你看到了什么（或报什么错）。
（提示：需要先 `import matplotlib.pyplot as plt`，并加上 `plt.show()` 才能显示图形。）
'''


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv", encoding="utf-8-sig")
print(df["最高温"].plot())



'''优化'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv", encoding="utf-8-sig")
df["最高温"].plot()          # 生成图形，但还没显示
plt.show()                  # 显示窗口