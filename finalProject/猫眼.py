import requests
import os
from fontTools.ttLib import TTFont
import re
import json
from lxml import etree
from pypinyin import pinyin,lazy_pinyin
import difflib

class maoyan():
    def __init__(self):
        self.headers =  {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
        }

        # cookie中ci为城市id    猫眼不同城市的url一样 通过id区分
        self.cookie = 'uuid_n_v=v1; uuid=658C74309C6E11E9BB4073F72C86D4DC9476F78900694EC5AAD5299440DBB9D8; ' \
                      '_csrf=c87aebaba4ebe601dce3e9f8da672e720c5ae72d34ca45480a990f4222a96e8c;' \
                      ' _lxsdk_cuid=16bb0718a39c8-09a032369841c2-37677e02-13c680-16bb0718a39c8;' \
                      ' _lxsdk=658C74309C6E11E9BB4073F72C86D4DC9476F78900694EC5AAD5299440DBB9D8;' \
                      ' __mta=45389211.1562404938754.1562507789545.1562507824803.61;' \
                      ' _lxsdk_s=16bccb8b1b2-72-04f-09c%7C%7C16; ci='


        # self.url = 'https://maoyan.com/cinema/16424?poi=115508290'
        self.url = 'https://maoyan.com/cinemas'
        self.digit = {
            'uniE7F2' : '1', 'uniE7CC' : '7', 'uniE6C6' : '8', 'uniEF57' : '4',
            'uniEC28' : '3', 'uniE773' : '5', 'uniE18F' : '2', 'uniF42F' : '0',
            'uniF6B6' : '6', 'uniEA83' : '9'
        }
        self.font = TTFont('./fonts/base_font.woff')
        self.web_font = ''
        self.web_html = ''
        self.web_html_text = ''

    def set_url_html(self, url):
        # 这里用于固定查询价格时网页的html内容 多次访问 font会变
        response = requests.get(url, headers = self.headers)
        self.web_html = response.content
        self.web_html_text = response.text

    def get_utl_html(self, url):
        response = requests.get(url, headers = self.headers)
        return response.content


    def set_font(self, font_file):
        # 得到当前网页的字体文件
        path = './fonts/' + font_file
        if not os.path.exists(path):
            url = 'http://vfile.meituan.net/colorstone/' + font_file
            file = self.get_utl_html(url)
            with open(path, 'wb') as w:
                w.write(file)
        self.web_font = TTFont('./fonts/' + font_file)

    def get_font_name(self):
        html = str(self.web_html,'utf-8')
        pattern = '//vfile.meituan.net/colorstone/(.*?.woff)'
        name = re.findall(pattern,html)
        return name


    def modify_price(self, data):
        # &#xecb6 -> uniECB6
        data = data.upper()
        data = data.replace('&#X', 'uni')
        new_data = ''
        # print(data)
        base_glyorder = self.font.getGlyphOrder()[2:]
        web_font_obj = self.web_font['glyf'][data]
        for i in base_glyorder:
            base_font_obj = self.font['glyf'][i]
            if base_font_obj == web_font_obj:
                new_data = self.digit[i]
                break
        return new_data

    def get_film_price_origin(self, show_time, film_name):
        html = str(self.web_html,'utf-8')
        hour = show_time['hour']
        minite = show_time['minite']
        begin_time = hour + ':' + minite
        pattern = 'class="movie-name">' + film_name + '.*?' + 'begin-time">' + begin_time  + \
                  '.*?sell-price">.*?">(.*?)</'
        price = re.findall(pattern, html, re.S)
        price = re.findall('(&.*?);', price[0])
        return price

    def get_film_price_decode(self, show_time, film_name, cinema_url):
        self.set_url_html(cinema_url)
        prices = self.get_film_price_origin(show_time, film_name)
        font_name = self.get_font_name()[0]
        self.set_font(font_name)
        myprice = ''
        for price in prices:
            myprice += self.modify_price(price)

        return myprice

    def price_decode(self, prices):
        font_name = self.get_font_name()[0]
        self.set_font(font_name)
        myprice = ''
        for price in prices:
            myprice += self.modify_price(price)
        return myprice





    def get_city_id(self, city):
        #   json 格式 以北京为例
        #   id_json['letterMap']['B'][0]['id']

        city_id = -1
        with open('city.json', 'r') as r:
            id = r.read()
        id_json = json.loads(id)

        letter = lazy_pinyin(city)[0][0].upper()
        if city == '浚县':
            letter = 'X'
        for i in id_json['letterMap'][letter]:
            if i['nm'] == city:
                city_id = i['id']
                break
        return city_id



    def get_city_html(self, city, offset = 0):
        # 根据城市id 更改cookie构造一个新的headers
        city_id = self.get_city_id(city)
        headers = self.headers
        cookie = self.cookie + str(city_id)
        headers['Cookie'] = cookie
        url = self.url + '?offset=' + str(offset)
        response = requests.get(url, headers=self.headers)
        return response.text


    def get_price(self, city,cinema_name, show_time, film_name):
        cinema_url = self.get_cinema_url(city, cinema_name)
        price = self.get_film_price_decode(show_time, film_name, cinema_url)
        return price


    def get_cinema_url(self, city, cinema_name):
        try:
            cinema_name = cinema_name.replace('+', '\+')
            pattern = re.compile('a href="(.*)" class="cinema.*?' + cinema_name)
            city_html = self.get_city_html(city)
            # 获取最大页面
            result = etree.HTML(city_html)
            max_page = result.xpath('//div[@class = "cinema-pager"]//li[last()-1]/a/text()')
            if max_page == []:
                max_page = 1
            else:
                max_page = int(max_page[0])
            for i in range(0,max_page):
                city_html = self.get_city_html(city, i * 12)
                url = re.findall(pattern, city_html)
                if url != []:
                    break
            cinema_url = 'https://maoyan.com' + url[0]
            return cinema_url
        except BaseException:
            return '这个有问题'

    def get_city_area_id(self, city):
        city_html = self.get_city_html(city)
        # print(city_html)
        pattern = '<a data-act="tag-click" data-val.*?href="(.*?)" data-bid="b_arz3865r">(.*?)</a>'
        results = re.findall(pattern, city_html)
        results = results[2:]
        return results



    def get_city_aera_html(self,city, districId, offset = 0):
        url = self.url + '?areaId=-1&districtId='+str(districId) + '&offset=' + str(offset)
        city_id = self.get_city_id(city)
        headers = self.headers
        cookie = self.cookie + str(city_id)
        headers['Cookie'] = cookie
        data = {'areaId' : -1, 'districtId' : 1}
        data['districtId'] = districId
        response = requests.get(url, headers = headers)
        html = response.text
        return html

    def get_city_area_cinema(self, html):
        pattern = '<a href="/cinema/.*?}">(.*?)</a'
        results = re.findall(pattern, html)
        return results

    def get_city_all_area_cinema(self):
        flag = 0
        with open('city.json', 'r') as r:
            id = r.read()
        id_json = json.loads(id)
        for upperletter in id_json['letterMap']:
            if upperletter >= 'S':
                citys = id_json['letterMap'][upperletter]
                for mycity in range(0, len(citys)):
                    city = id_json['letterMap'][upperletter][mycity]['nm']
                    if city == '泗洪':
                        flag = 1

                    if flag == 1:
                        area_ids = self.get_city_area_id(city)
                        for ids in area_ids:
                            area_name = ids[1]
                            districId = re.findall("\d+", ids[0])[0]
                            # 获取最大页面
                            html = self.get_city_aera_html(city, districId=districId, offset= 0)
                            result = etree.HTML(html)
                            max_page = result.xpath('//div[@class = "cinema-pager"]//li[last()-1]/a/text()')
                            if max_page == []:
                                max_page = 1
                            else:
                                max_page = int(max_page[0])

                            for i in range(0,max_page):
                                html = self.get_city_aera_html(city,districId=districId, offset= i * 12)
                                city_area_cinema = self.get_city_area_cinema(html)
                                print(city_area_cinema)
                                for cinema_name in city_area_cinema:
                                    cinema_url = self.get_cinema_url(city, cinema_name)
                                    with open('smaoyan.txt', 'a') as w:
                                        w.write(city + ' ' + area_name + ' ' + cinema_name + ' ' + cinema_url + '\n')
                                        print(city,area_name,cinema_name,cinema_url)



    def get_all_movie_name(self):
        base_url = 'https://maoyan.com/films?showType=1&offset='
        url = base_url + '0'
        response = requests.get(url, headers = self.headers)
        html = response.text
        result = etree.HTML(html)
        max_page = result.xpath('//div[@class = "movies-pager"]//li[last()-1]/a/text()')
        max_page = int(max_page[0])
        movie_name = []
        for i in range(0,max_page):
            url = base_url + str(i * 30)
            response = requests.get(url, headers=self.headers)
            html = response.text
            result = etree.HTML(html)
            movie_name.extend(result.xpath('//div[contains(@class,"movie-item-title")]/@title'))

        return movie_name


    def get_timetable_from_maoyan(self, data_mark= '1', cinema_url='https://maoyan.com/cinema/17000?poi=150594634', movie_name='爱宠'):
        try:
            movie_names = self.get_all_movie_name()
        except :
            print('获取所有电影院名字发生错误')
            return []

        score = 0
        temp = ''
        for selected_moive_name in movie_names:
            p = difflib.SequenceMatcher(None, selected_moive_name, movie_name).quick_ratio()
            if  p > score:
                score = p
                temp = selected_moive_name
        movie_name  = temp


        data_mark = int(data_mark)
        try:
            self.set_url_html(cinema_url)
            html = self.web_html_text
        except:
            print('电影院链接解析错误')
            return []

        try:
            pattern = 'class="movie-name">' + movie_name + '.*?<div class="show-date">(.*?)</div'
            # data_all 是所有的观影时间的html 类似 今天7月9 明天7月10 。。。
            data_all = re.findall(pattern,html,re.S)
            # datas 是观影时间的列表 ['今天 7月9', '明天 7月10', '后天 7月11']
            datas = re.findall('".*?>(.*?\d.*?)</span', data_all[0], re.S)
            if '天' not in datas[0]:
                print('没有那天的电影')
                return []
            print(datas)
        except :
            print('获取观影时间错误')

            return []
        # length 是总的可选天数
        length = len(datas)
        if data_mark > length:
            print('没有那天的电影信息')
            return []

        # content是从当前电影开始 到网页html结尾的全部内容
        try:
            content = re.findall('class="movie-name">' + movie_name + '.*?(<table class="plist">.*)',html, re.S)
            # content_tbody是以天为分隔的html的内容的列表
            content_tbody = re.findall('<tbody>(.*?)</tbody>', content[0], re.S)

            result_tbody = content_tbody[0:length]
            one_result = etree.HTML(result_tbody[data_mark])
        except:
            print('电影信息获取错误')

        begin_times = one_result.xpath('//span[@class="begin-time"]/text()')

        end_times = one_result.xpath('//span[@class="end-time"]/text()')
        for i  in range(len(end_times)):
            end_times[i] = end_times[i].replace('散场','')

        langs = one_result.xpath('//span[@class="lang"]/text()')

        halls = one_result.xpath('//span[@class="hall"]/text()')

        prices = re.findall('<span class="stonefont">(.*?)</span>', result_tbody[data_mark])

        for i in range(0 , len(prices)):
            p = prices[i].split(';')[0:2]
            prices[i] = self.price_decode(p)

        results = []
        for i in range(0 , len(begin_times)):
            result = (begin_times[i], end_times[i], langs[i], halls[i], prices[i])
            results.append(result)
        return results






m =  maoyan()
print(m.get_timetable_from_maoyan(data_mark='1', cinema_url='https://maoyan.com/cinema/17000?poi=150594634', movie_name='狮子王'))
print(difflib.SequenceMatcher(None, '狮子王', '狮子王').quick_ratio())

font = TTFont('d4b4cdd6058e697ca8f90b6ada0645dd2084.woff')
font.saveXML('selt.xml')



