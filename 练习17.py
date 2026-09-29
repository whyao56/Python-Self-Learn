'''理论'''
'''
我们在前面的学习中已经用了很多 **内置函数**：`print()`, `input()`, `int()`, `float()`, `len()`, `type()` 等。这些都是 Python 自带的，可以直接使用。
但 Python 的宝藏远不止这些，还有很多功能被封装在 **模块（Module）** 里，需要用 `import` 把模块“请”进来才能使用。

### 🧰 生活化类比：工具箱
- **内置函数**：就像你家里自带的螺丝刀、剪刀，随手可用。
- **模块**：就像一间工具房，里面有电钻、水平仪等专业工具。你需要先打开工具房（`import`），才能取用。

---

## 第八课：导入模块——用别人写好的功能
我们以两个常用模块为例：
1) `random`：生成随机数
2) `math`：数学函数和常数

### 🌰 例子：猜数字游戏升级版（随机生成目标数）
```python
import random                  # 导入 random 模块

target = random.randint(1, 10) # 随机生成 1~10 的整数
guess = 0

while guess != target:
    guess = int(input("猜一个 1~10 的数字："))
    if guess > target:
        print("太大了")
    elif guess < target:
        print("太小了")

print(f"猜对了！答案就是 {target}")
```

### 📖 逐行解释
- `import random`：告诉 Python 我们要使用 `random` 模块里的工具。
- `random.randint(1, 10)`：调用模块中的 `randint` 函数，生成一个在 1~10 之间的随机整数（包含两端）。
- 其余是 while 循环和 if 判断，你已经非常熟悉了。

再比如 `math` 模块：
```python
import math

print(math.sqrt(16))   # 开根号，输出 4.0
print(math.pi)         # 圆周率 π，输出 3.141592653589793
```

**使用模块内函数的通用格式**：`模块名.函数名()`
**使用模块内常数**：`模块名.常数名`

'''

'''题目'''
'''
写一个模拟掷骰子的程序：
- 导入 `random` 模块
- 定义一个函数 `roll_dice()`，它没有参数，内部随机生成 1~6 的整数并返回
- 调用函数3次，打印每次掷出的点数（提示：用 for 循环）
'''



'''回答'''
# import random
#
# def roll_dice():
#     return random.randint(1, 6)
# for i in range(3):
#     roll_dice()
#     print(roll_dice())



'''优化'''
import random

def roll_dice():
    return random.randint(1, 6)

for i in range(3):
    result = roll_dice()    # 调用一次，存起来
    print(f"第{i+1}次掷出：{result}")


