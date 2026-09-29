'''理论'''
'''
现在你已经能读写普通文本了。但在数据分析和实际项目中，我们最常打交道的是 **CSV（逗号分隔值）** 文件，就像 Excel 表格的纯文本版本。
Python 内置了 `csv` 模块，专门用来处理这类文件。

### 🧾 生活类比：记账本
CSV 文件就像一个简单的记账本：每一行是一条记录，每个字段用逗号隔开。例如：
```
姓名,年龄,城市
小明,20,北京
小红,22,上海
```

---

## 第十一课：读写 CSV 文件

### 🌰 例子1：写入 CSV 文件
我们用 `csv.writer` 来写入，它会自动处理逗号、换行等细节。

```python
import csv

# 准备数据（一个二维列表，每行是一个列表）
data = [
    ["姓名", "年龄", "城市"],          # 表头
    ["小明", 20, "北京"],
    ["小红", 22, "上海"],
    ["小刚", 19, "广州"]
]

# 写入 CSV
with open("students.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(data)              # 一次性写入多行
print("CSV 文件已保存！")
```
- `newline=""`：避免 Windows 下出现多余空行，写入 CSV 时建议加上。
- `encoding="utf-8-sig"`：让 Excel 能正确识别中文（普通的 `utf-8` 在 Excel 里可能乱码）。
- `writerows(data)`：把整个二维列表写进去。

### 📖 例子2：读取 CSV 文件
用 `csv.reader` 读取刚才生成的 `students.csv`，并逐行打印。

```python
import csv

with open("students.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   # row 是一个列表，如 ['小明', '20', '北京']
```
输出：
```
['姓名', '年龄', '城市']
['小明', '20', '北京']
['小红', '22', '上海']
['小刚', '19', '广州']
```
'''

'''题目'''
'''
1. 创建一个新的 CSV 文件 `weather.csv`，包含以下三列：`城市`、`最高温`、`最低温`。
2. 写入至少三行数据（自己编几个城市，温度用整数即可）。
3. 用 `csv.reader` 读回该文件，逐行打印原始列表。
'''

'''回答'''
import csv

data = [
    ["城市", "最高温", "最低温"],
    ["北京", "20", "10"],
    ["南京", "25", "15"],
    ["开封", "25", "10"]
]

with open("weather.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(data)

with open("weather.csv", "r", newline="", encoding="utf-8-sig") as f:
    writer = csv.reader(f)
    for row in writer:
        print(row)


'''优化'''
import csv

data = [
    ["城市", "最高温", "最低温"],
    ["北京", 20, 10],    # 存为整数
    ["南京", 25, 15],
    ["开封", 25, 10]
]

with open("weather.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(data)

with open("weather.csv", "r", encoding="utf-8-sig") as f:   # 读取时去掉 newline=""
    reader = csv.reader(f)
    for row in reader:
        print(row)