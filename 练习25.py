'''理论'''
'''
我们常用的工具是 **`requests` 库**，它不属于 Python 内置，需要先用 `pip install requests` 安装。

### 📦 安装第三方库
在 PyCharm 的终端（Terminal）里输入：
```
pip install requests
```
（如果你用的是虚拟环境，确保已激活。PyCharm 会自动弹出提示，也可以使用“Python Packages”工具窗口安装。）

---

## 第十二课：用 `requests` 发送 HTTP 请求

### 🌐 生活类比：浏览器点外卖
- 你在浏览器里输入网址，就是向服务器**发送一个请求**。
- 服务器返回一个网页（HTML）或数据（JSON），就像外卖送到你手上。
- `requests` 库就是让你在 Python 里扮演“浏览器”的角色，发送请求并获取“外卖”。

### 🌰 例子：获取百度首页的 HTML
```python
import requests

url = "https://www.baidu.com"
response = requests.get(url)          # 发送 GET 请求
response.encoding = "utf-8"           # 设置编码，防止乱码
print(response.text)                  # 打印网页源代码（很长很乱）

print(f"状态码：{response.status_code}")   # 200 表示成功
```

### 📖 逐行解释
- `requests.get(url)`：发送一个 HTTP GET 请求，相当于你在浏览器里敲回车。
- `response` 对象包含了服务器返回的所有信息：文本内容、状态码、请求头等。
- `response.text`：以字符串形式返回响应体（通常是 HTML 或 JSON）。
- `response.status_code`：200 代表成功，404 代表找不到，500 代表服务器错误。

---
'''


'''题目'''
'''
请先确保已安装了 `requests` 库。然后：
1. 使用 `requests.get()` 获取网址 `https://api.github.com` 的响应。
2. 打印状态码。
3. 打印响应内容的**前 200 个字符**（用字符串切片），避免刷屏。
'''

'''回答'''
import requests
url = "https://api.github.com"
response = requests.get(url)
response.encoding = "utf-8"
print(response.text)
print(f"状态码：{response.status_code}")


'''优化'''
import requests
url = "https://api.github.com"
response = requests.get(url)
response.encoding = "utf-8"
print(response.text[:200])   # 只打印前200个字符
print(f"状态码：{response.status_code}")