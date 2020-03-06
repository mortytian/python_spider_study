'''
批量爬取百度贴吧页面数据
先写一个main,提示用户输入贴吧地址

'''
import urllib
import re

def get_response_urlopen(url):
    response = urllib.request.urlopen(url)
    return response


def get_response_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/65.0.3325.163 Safari/537.36'
    }

    request = urllib.request.Request(url, headers=headers)
    response = get_response_urlopen(request)
    return response

def get_content(url):
    res = get_response_request(url)
    content = res.read().decode('utf-8')
    return content

def get_titles(url):
    content = get_content(url)
    pattern = re.compile('<.*?noreferrer.*?title="(.*?)" target="_blank"',re.I)
    titles = re.findall(pattern,content)
    print(len(titles))
    for i in titles:
        print(i)
    return titles

def get_lastPage(url):
    content = get_content(url)
    pattern = re.compile('<a href.*?(/d+)"')
    last = re.findall(pattern, content)
    print(last)

def tiebaSpider():
    kw = input('输入贴吧名字: ')
    # beginPage = int(input('请输入起始页: '))
    # endPage = int(input('请输入截止页: '))
    url = 'http://tieba.baidu.com/f?'
    kw = urllib.parse.urlencode({'kw':kw})
    url = url + kw + '&ie=utf-8&pn='+'0'
    get_lastPage(url)

    # for i in range(beginPage, endPage + 1):
    #     newurl = url + str((i-1)*50)
    #     get_titles(newurl)

if __name__ == '__main__':
    tiebaSpider()


