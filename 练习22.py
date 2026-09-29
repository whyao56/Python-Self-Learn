'''题目'''
'''
下面这段代码想记录三次用户输入，但运行时发现文件里只有最后一次输入的内容。请解释为什么，并修改代码实现**追加**所有输入：
```python
for i in range(3):
    with open("log.txt", "w", encoding="utf-8") as f:   # 每次循环都重新打开（覆盖）
        line = input(f"第{i+1}行内容：")
        f.write(line + "\n")
```
（实际上代码逻辑正确，但为什么会只留最后一句？——提示：`"w"` 模式的特性。）
'''


'''回答'''
with open("log.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        line = input(f"第{i+1}行内容：")
        f.write(line + "\n")
