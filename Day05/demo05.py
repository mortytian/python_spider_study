'''
诗词名句网
    1、爬取固定书籍
    2、爬取书名
    3、爬取本部书的掌回目录
    4、灵活处理，爬取任意书籍的章回目录
    5、加入异常处理
    6、爬取任意书籍全部内容

'''
import requests
from lxml import etree

url = 'http://www.shicimingju.com'
headers = {'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
}

def write_text(text,name):
    txt_name = './' + name + '.txt'
    with open(txt_name, 'a') as w:
        w.write(text)

def get_url_html(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    result = etree.tostring(html, encoding="utf-8")
    result = result.decode('utf-8')
    html = etree.HTML(result)
    return html

def get_book_url(url):
    bookName = input('输入书名（中文）: ')
    print('正在查找...')
    name = bookName
    html = get_url_html(url)
    bookName = bookName +'"]/@href'
    pattern = '//ul/li/a[text()="' + bookName
    result = html.xpath(pattern)[0]
    book_url = url + result
    return book_url, name

def get_chapter_name(book_url, book_name):
    html = get_url_html(book_url)
    pattern = '//div[@class = "book-mulu"]//a/text()'
    result = html.xpath(pattern)
    name = book_name + ' 目录'
    for i in result:
        i = i + '\n'
        write_text(i,name)

def get_book_content(book_url, book_name):
    html = get_url_html(book_url)
    pattern = '//div[@class = "book-mulu"]//a/@href'
    result = html.xpath(pattern)
    name = book_name + ' 内容'
    for i in result:
        chapter_url = url + i
        html = get_url_html(chapter_url)
        pattern = '//div[@class = "www-main-container www-shadow-card "]/h1/text()  '
        chapter = html.xpath(pattern)
        chapter = chapter[0] + '\n'
        write_text(chapter, name)
        print(chapter)
        pattern = '//div[@class="chapter_content"]//text()'
        content = html.xpath(pattern)
        for j in content:
            j = j.strip()
            j += '\n'
            write_text(j, name)





def main():
    choose = int(input('查找目录输入1\n查找章节输入2\n'))
    try:
        book_url, book_name = get_book_url(url)
    except IndexError as e:
        print('没有这本书，查找失败')
        exit()
    if choose == 1:
        get_chapter_name(book_url, book_name)
    else:
        get_book_content(book_url, book_name)
    print('查找成功')


main()