# 生成垃圾数据的脚本,用于sql注入等
import random

data = [chr(i) for i in range(33, 125)]
data.remove("#") # 防止url被注释,话说这个#号还有点东西，最后再说。
data.remove("*") # 方便使用sqlmap报数据。
s = ""
for i in range(10000):
    s = s + random.choice(data)
print(s)
