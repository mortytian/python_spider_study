import requests
# url = 'https://www.xicidaili.com/?tdsourcetag=s_pctim_aiomsg'
url = 'http://www.baidu.com/s'
kw = {'wd' : '长城'}
headers = {'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
}

# proxies = {
#     'http' : 'http://36.255.87.252:83',
#     'https': 'http://49.236.151.91:80'
# }

# response = requests.get(url, params = kw, headers = headers, proxies = proxies)
# response = requests.get(url, params = kw, headers = headers)
# response = requests.get(url, headers= headers)


# print(type(response))

# response.encoding = 'utf-8'
# doc = response.text
# print(doc)

# html =response.content
# doc = str(html, 'utf-8')

#查看完整网址
# print(response.url)

#查看响应码
# print(response.status_code)

# 将cookjar转化为字典
# cookjar = response.cookies
# cookiedice = requests.utils.dict_from_cookiejar(cookjar)
# print(cookiedice)

# 创建session对象 可以保存Cookie值

ssion = requests.session()
headers = {'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
}

# 需要登陆的用户名和密码
data = {'email' : 'xxx', 'password' : 'xxx'}

# 发送附带用户名和密码的请求，并获取登陆后的cookie值，并保存在ssion里

ssion.post(url, data = data)

# ssion包含用户登录后的cookie值
# 可以直接访问那些登陆后才可以访问的界面
response = ssion.get(url)

print(response.text)


