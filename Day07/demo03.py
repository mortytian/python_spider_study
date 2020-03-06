from bs4 import BeautifulSoup
import requests

url = 'http://www.baidu.com'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,'lxml')

# print(soup.prettify())

for child in soup.body.children:
    print(child)
    print('1')
    break

# for i in soup.body.descendants:
#     print(i)

# print(soup.body.children)
# print(soup.body.contents)