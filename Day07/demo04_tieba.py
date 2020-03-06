import requests
from lxml import etree
import os
'''
利用xpath 实现百度贴吧图片爬取
'''

url = 'http://tieba.baidu.com/f?'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

data = {'kw': 'python',
'ie': 'utf-8',
'pn': '50'}
count = 1
def get_html(url):
    # response = requests.post(url, params = data,headers = headers )
    response = requests.post(url, params=data)
    # print(response.headers)
    text = response.text
    html = etree.HTML(text)
    return html

def get_img_url(html):
    pattern = '//div[contains(@class,"small_list_gallery")]//ul[contains(@class,"threadlist_media")]//img/@bpic'
    result = html.xpath(pattern)
    return result

def write_file(links):
    global count
    path = './images'
    if not os.path.isdir(path):
        os.mkdir('./images')
    filename = './images/picture'
    for link in links:
        image = requests.get(link)
        with open(filename + str(count) +'.png', 'wb') as w:
            print('正在下载文件..', str(count))
            w.write(image.content)
            count += 1
    print('下载完成')
def main():
    kw = input('请输入贴吧名字: ')
    begin_page = int(input('请输入起始页: '))
    end_page = int(input('请输入截止页: '))
    data['kw'] = kw
    for i in range(begin_page-1,end_page):
        data['pn'] = i * 50
        html = get_html(url)
        links = get_img_url(html)
        # write_file(links)


main()
