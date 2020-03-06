import re
s2 = """张某某的邮箱是：zhang@qq.com,王某某的邮箱是是:wang@163.com.cn，李某某的邮箱是:li@tedu.cn"""


mail = re.findall('[a-zA-Z0-9]+@[a-zA-Z0-9.]+', s2)

print(mail)