'''改错'''
'''
下面代码试图解析 API 返回的 JSON，但运行时却报错 `TypeError: string indices must be integers`。请根据输出解释为什么：

```python
import requests

url = "https://api.github.com/users/octocat"
response = requests.get(url)
data = response.text        # 注意这里用的是 .text 而不是 .json()
print(data["login"])
```
（实际上运行会报错；请先观察错误类型，再解释原因，并给出修改方法。）
'''

import requests

url = "https://api.github.com/users/octocat"
response = requests.get(url)
data = response.json()        # 注意这里用的是 .text 而不是 .json()
print(data["login"])


'''正确解释'''
'''
response.text → 得到的是一个 JSON 格式的字符串，例如 '{"login":"octocat",...}'。
字符串没有“键”的概念，所以 data["login"] 会引发类型错误。
必须用 response.json() 把 JSON 字符串解析成 Python 字典，才能用键访问。
'''