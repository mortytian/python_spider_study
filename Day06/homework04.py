import requests
import re
import User_Agent
import random
from requests.exceptions import RequestException

def get_one_page(url):
    try:

        list=User_Agent.Agent
        headers=random.choice(list)
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
    except RequestException:
        return None

def write_to_file(content):
    print(content)
    with open('./猫眼.txt', 'a') as f:
        f.write(content+'\n')

def print_one_page(url,offset):
    offset = str(offset)
    url = url + offset
    html = get_one_page(url)
    rank = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?title="(.*?)".*?主演：(.*?)\n.*?上映时间：(.*?)</p>.*?"integer">(.*?)<.*?"fraction">(.*?)<',re.S)
    result = re.findall(rank,html)
    for item in result:
        write_to_file('标题:'+item[2])
        write_to_file('主演:'+ item[3])
        write_to_file('时间:'+ item[4])
        write_to_file('\n')



def main():
    url = 'http://maoyan.com/board/4?offset='
    offset =  (x * 10 for x in range(10))
    print('读取成功\n正在保存..')
    for i in range(10):
        print_one_page(url, next(offset) )

main()