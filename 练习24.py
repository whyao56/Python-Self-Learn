'''改错'''
'''
下面代码试图读取 `data.csv` 文件并将所有“成绩”列加 5 分后写回原文件。但运行时发现成绩没变，甚至文件被清空了。请找出错误并给出修改思路（不必完整重写）。
```python
import csv

rows = []
with open("data.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        row[1] = int(row[1]) + 5   # 假设第2列是成绩
        rows.append(row)

with open("data.csv", "w", encoding="utf-8-sig") as f:   # 错误在这里
    writer = csv.writer(f)
    writer.writerows(rows)
```
（提示：思考 `"w"` 模式打开文件的时机，以及 `newline` 参数。）
'''

'''回答'''
# import csv
#
# rows = []
# with open("data.csv", "r", encoding="utf-8-sig") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         row[1] = int(row[1]) + 5   # 假设第2列是成绩
#         rows.append(row)
#
# with open("data.csv", "w+", encoding="utf-8-sig") as f:   # 错误在这里
#     writer = csv.writer(f)
#     writer.writerows(rows)


'''优化'''
import csv

rows = []
with open("data.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)      # 先读取文件内容
    header = next(reader)       # 读取第1行 → ["姓名", "成绩"]，指针现在指向第2行
    rows.append(header)         # 把表头保存到 rows
    for row in reader:          # 从第2行开始读
        row[1] = int(row[1]) + 5
        rows.append(row)

# 写入临时文件，避免直接覆盖原文件导致数据丢失
with open("data_temp.csv", "w", newline="", encoding="utf-8-sig") as f:  # 加上了newline=""
    writer = csv.writer(f)
    writer.writerows(rows)

# 确认无误后可手动替换，或使用 os.replace
# 其中如果data.csv未按要求存在空行空列，会直接报错（毕竟还未学到try...except）