'''题目'''
'''
如果不安装 `requests` 就运行 `import requests`，会报什么错误？你遇到过这种错误吗？如何解决
'''

'''回答'''
'''不清楚'''


'''答案'''
'''
如果不安装 requests 就运行 import requests，Python 会抛出：
ModuleNotFoundError: No module named 'requests'
意思是“找不到名为 requests 的模块”。这是因为 requests 不是 Python 自带的，而是第三方库，需要先通过 pip install requests 安装。

解决方法：
打开终端（PyCharm 底部的 Terminal 标签，或系统终端）。
输入 pip install requests 并回车。
等待安装完成，再运行代码即可。
'''