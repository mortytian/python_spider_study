import urllib.request
import urllib.parse

#1、确定爬取网页的url地址
url ='http://www.baidu.com/s'
header = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Connection" : "keep-alive"
}


wd = {'wd':'吴京'}
urlwd = urllib.parse.urlencode(wd)
url = url+'?'+urlwd
#2、根据url获取网页信息
urlRequest = urllib.request.Request(url, headers=header)


response = urllib.request.urlopen(urlRequest)

# print(type(urlRequest))
# print(type(response))
# print(response.getcode())
# print(response.getheader(name="User-Agent"))
# print(urlRequest.get_header('Connection'))
# print(urlRequest.get_header("User-Agent"))

print(response.geturl())
print(response.read().decode('utf-8'))