from lxml import etree
text = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>今天The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom a well.</p>
<p class="story">...</p>
'''

html = etree.HTML(text)

result = etree.tostring(html, encoding = 'utf-8')

print(result.decode('utf-8'))

# 读取外部文件 shuihu.html
html = etree.parse('./shuihu.html')
result = html.xpath('//li[last()]/a/@href')