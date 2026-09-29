'''理论'''
'''
大多数 API 返回的是 **JSON** 格式的数据（JavaScript Object Notation），它和 Python 的字典/列表几乎一模一样，只是以文本形式传输。
`requests` 库可以直接把 JSON 转换成 Python 对象，方法就是 `response.json()`。

### 🌰 例子：获取 GitHub API 的 JSON 数据并解析
```python
import requests

url = "https://api.github.com"
response = requests.get(url)
data = response.json()                # 将 JSON 字符串转为 Python 字典

# 现在 data 就是一个字典，可以像操作普通字典一样使用
print(f"当前用户URL: {data['current_user_url']}")
print(f"仓库URL: {data['repository_url']}")
for key, value in data.items():
    print(f"{key}: {value}")
```

### 📖 解释
- `response.json()` 做了两件事：① 读取响应文本；② 用 `json.loads()` 把它转成 Python 的字典或列表。
- 如果 API 返回的 JSON 结构是一个**列表**（比如数组），那 `data` 就会是一个 Python 列表，里面可能嵌套字典。
- 从此，处理 API 数据就像处理普通字典一样简单。
'''

'''题目'''
'''
使用 `https://api.github.com/users/octocat` 这个 API 端点，它返回的是 GitHub 用户 `octocat` 的信息（JSON 格式）。请：
1. 发送 GET 请求，获取 JSON。
2. 打印该用户的 `login`（用户名）、`id`、`html_url`（主页地址）。
3. 再用一个 for 循环遍历字典的所有键值对，打印出来。
'''


'''回答'''


import requests
url = "https://api.github.com/users/octocat"
response = requests.get(url)
data = response.json()

print(f"用户名：{data['login']}")
print(f"id：{data['id']}")
print(f"主页地址：{data['html_url']}")

for key, value in data.items():
    print(f"{key}: {value}")