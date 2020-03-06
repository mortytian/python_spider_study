import urllib.request
import urllib.parse
import json
import requests
# content由浏览器中得到
content = '''i: 你好
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15623081610056
sign: 79fe75b4a8f5c718a6a93c1b480fcdb4
ts: 1562308161005
bv: 263c25b5c0271e7e864b798e36beddbd
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME'''

def get_dic(content):
    content = content.strip()
    content = content.split('\n')
    dic = {}
    for i in content:
        kv = i.split(':')
        dic[kv[0].strip()] = kv[1].strip()
    return dic


post_form = get_dic(content)

word = input('输入查询的单词: ')
post_form['i'] = word

# url = 'http://fanyi.youdao.com'
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

data = urllib.parse.urlencode(post_form).encode('utf-8')
header = {'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
}

req = urllib.request.Request(url,data,header)
response = urllib.request.urlopen(req)

trans_json = response.read().decode('utf-8')
trans_dict = json.loads(trans_json)
# print(trans_dict)
result = trans_dict['translateResult'][0][0]['tgt']


print(result)

