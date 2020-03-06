'''
爬取任一贴吧，任意内容
1、将图片存储一个路径
2、视频存储一个路径
3、其他，存储一个路径
'''

import requests
from bs4 import BeautifulSoup
import os


url = 'http://tieba.baidu.com/f?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

data = {'kw': 'python',
'ie': 'utf-8',
'pn': '50'}

img_count = 1
text_count = 1
video_count = 1
def get_html_soup(url, kw, offset):
    data['kw'] = kw
    data['pn'] = offset
    response = requests.post(url, params = data,headers = headers )
    # response = requests.post(url, params=data)
    # print(response.headers)
    html = response.text
    soup = BeautifulSoup(html,'lxml')
    # print(soup.prettify())
    return soup

def write_file(text, name, attr):
    path = './images'
    if not os.path.isdir(path):
        os.mkdir('./images')

    path = './txts'
    if not os.path.isdir(path):
        os.mkdir('./txts')

    path = './videos'
    if not os.path.isdir(path):
        os.mkdir('./videos')

    if attr == 'txt':
        name = './txts/' + name + '.' + attr
        with open(name, 'a') as w:
            w.write(text)

    if attr == 'png':
        name = './images/' + name + '.' + attr
        with open(name, 'wb') as w:
            w.write(text)

    if attr == 'mp4':
        name = './videos/' + name + '.' + attr
        with open(name, 'wb') as w:
            w.write(text)

def get_img(soup):
    global img_count
    result = soup.select('a[class="thumbnail vpic_wrap"] img')
    if result != []:
        for i in result:
            # print(i.attrs['bpic'])
            print('正在下载图片',img_count,'...')
            img_url = i.attrs['bpic']
            response = requests.get(img_url, headers = headers)
            write_file(response.content, 'image' + str(img_count), 'png')
            img_count += 1
    # print(result)

def get_video(soup):
    global video_count
    result = soup.select('a[class="threadlist_btn_play j_m_flash"]')
    if result != []:
        for i in result:
            print('正在下载视频',video_count,'...')
            video_url = i.attrs['data-video']
            # print(i.attrs['data-video'])
            response = requests.get(video_url, headers = headers)
            write_file(response.content, 'viedo' + str(video_count), 'mp4')
            video_count += 1

def get_others(soup):
    global text_count
    titles = soup.select('a[class="j_th_tit "]')
    authors = soup.select('span[class="tb_icon_author "]')
    contents = soup.select('div[class="threadlist_abs threadlist_abs_onlyline "]')
    replyers = soup.select('span[class="tb_icon_author_rely j_replyer"]')
    last_reply_data = soup.select('span[class="threadlist_reply_date pull_right j_reply_data"]')
    if len(titles) == 0:
        print('贴吧不存在，退出')
        exit()
    print('正在写入第',str(text_count),'页')
    for i in range(0,len(titles) - 1):
        title = '题目: ' + titles[i].attrs['title'] + '\n'
        write_file(title,'page' + str(text_count), 'txt')

        author = authors[i].attrs['title'].strip() + '\n'
        write_file(author,'page' + str(text_count), 'txt')

        content = contents[i].text.strip() + '\n'
        write_file(content, 'page' + str(text_count), 'txt')

        replyer = replyers[i].attrs['title'].strip() + '\n'
        write_file(replyer, 'page' + str(text_count), 'txt')

        data = '最后回复时间: ' + last_reply_data[i].get_text().strip() + '\n\n'
        write_file(data, 'page' + str(text_count), 'txt')
    text_count += 1



def main():
    global text_count
    kw = input('输入贴吧名字：')
    begin_page = int(input("输入起始页码："))
    end_page = int(input("输入截止页码："))
    text_count = begin_page
    for i in range(begin_page, end_page+1):
        soup = get_html_soup(url, kw, (i-1) * 50)
        get_img(soup)
        get_video(soup)
        get_others(soup)

main()