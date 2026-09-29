'''理论'''
'''
写入文件——让程序“生产”内容

### 📝 生活类比：在纸上写字
还是那张纸，但现在你要**写新东西**。注意，有两种模式：
- `"w"`（write）模式：**覆盖写入**——原来纸上的字全擦掉，写新的。
- `"a"`（append）模式：**追加写入**——保留原内容，在末尾接着写。

### 🌰 例子：把一段话写入新文件
```python
# 使用 "w" 模式创建（或覆盖）一个文件
with open("diary.txt", "w", encoding="utf-8") as file:
    file.write("今天是学习 Python 的第 N 天。\n")   # \n 是换行符
    file.write("一切都很顺利！\n")
```
运行后，项目文件夹里会出现 `diary.txt`，内容就是那两行。

**注意**：`write()` 不会自动换行，需要自己加 `\n`。

'''

'''题目'''
'''
写一个程序，询问用户“今天想记录什么？”，然后用 `"w"` 模式把用户输入的内容写入 `note.txt`（编码 utf-8），并友好提示“保存成功！”。
'''


'''回答'''
with open("note.txt", "w", encoding="utf-8") as file:
    file.write(input("今天想记录什么？\n"))
    print("保存成功!")


'''优化'''
content = input("今天想记录什么？\n")
if content:
    with open("note.txt", "w", encoding="utf-8") as file:
        file.write(content)
    print("保存成功!")
else:
    print("内容为空，未保存。")