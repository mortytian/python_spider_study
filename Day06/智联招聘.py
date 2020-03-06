'''
https://sou.zhaopin.com/?jl=489&sf=0&st=0&kw=python&kt=3
https://sou.zhaopin.com/?p=4&jl=489&kw=python&kt=3&sf=0&st=0https://sou.zhaopin.com/?p=3&jl=489&kw=python&kt=3&sf=0&st=0
https://sou.zhaopin.com/?p=4&jl=489&kw=python&kt=3&sf=0&st=0
'''

from bs4 import BeautifulSoup
import requests
from lxml import etree


url = 'https://fe-api.zhaopin.com/c/i/sou?start='

headers = {'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
}


def get_url(base_url,start_page,kw = 'python', cityid = '489',salary = '0',
            workEx = '-1', edu = '-1', company = '-1', employ = '-1',jobwelfa = '-1'):
    new_url = base_url + str(start_page) +'&pageSize=90&cityId='+ cityid \
    +'&salary=' + salary +',0&workExperience=' + workEx+'&education=' + edu + \
              '&companyType=' + company + '&employmentType=' + employ + '&jobWelfareTag=' + jobwelfa  + \
                '&kw=' + kw + '&kt=3&=0&_v=0.63737848&x-zp-page-request-id=7c08cbfa9b4347a99f9e7cea850fc4a4-' \
                '1562393246154-830689&x-zp-client-id=dca55c7d-3e6b-4f45-aee3-1aa891e0956e'

    return new_url

def get_url_html(url):
    response = requests.get(url, headers=headers)
    text = response.text
    # html = etree.HTML(text)
    # result = etree.tostring(html, encoding="utf-8")
    # result = result.decode('utf-8')
    # html = etree.HTML(result)
    return text

new_url = get_url(url, )
html = get_url_html(new_url)
print(html)

