# -*- coding: utf-8 -*-
import json


import requests
import scrapy
from bs4 import BeautifulSoup
from requests.cookies import RequestsCookieJar

from WeChat.items import WechatItem


class WechatArticleSpider(scrapy.Spider):
    name = 'wechat_article'
    # 允许的域名 爬取这个文章的时候因为域名不是搜狗 所以需要注释掉 不然会无法访问
    # allowed_domains = ['weixin.sogou.com']
    wechat_item = WechatItem()

    def start_requests(self):
        # 第一个保险
        # 第二个买房
        start_urls = ['https://weixin.sogou.com/weixin?oq=&query=%E4%BF%9D%E9%99%A9&_sug_type_=1&sut=0&lkt=0%2C0%2C0&s_from=input&ri=1&_sug_=n&type=2&sst0=1551405515524&page=1&ie=utf8&p=40040108&dp=1&w=01015002&dr=1',
                      'https://weixin.sogou.com/weixin?query=%E4%B9%B0%E6%88%BF&_sug_type_=&s_from=input&_sug_=y&type=2&page=1&ie=utf8']
        # 倒入cookie
        with open("cookies.txt") as f:
            cookie_list = json.load(f)

        cookiejar = RequestsCookieJar()

        for cookie in cookie_list:
            cookiejar.set(cookie["name"], cookie["value"])
        #  转成字典
        cookie = requests.utils.dict_from_cookiejar(cookiejar)

        yield scrapy.Request(start_urls[1], cookies=cookie, callback=self.parse)

    def parse(self, response):

        soup = BeautifulSoup(response.body, "html.parser")
        news_list = soup.find_all(class_="img-box")
        print("len of list:", len(news_list))
        for news in news_list:
            a = news.find("a")
            href = a.get('href')
            print("list url:", href)
            yield scrapy.Request(href, callback=self.new_parse)

        a = soup.select('a[id="sogou_next"]')[0]

        next_link = a.get('href')

        if next_link:
            yield scrapy.Request("https://weixin.sogou.com/weixin"+next_link, self.parse)


    def new_parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")

        title = soup.find(id="activity-name")

        self.wechat_item['title'] = title.text.strip().replace("\n", "")

        writer = soup.find(class_="profile_nickname")

        self.wechat_item['writer'] = writer.text.strip().replace("\n", "")

        source = soup.find(id="js_content")

        self.wechat_item['article'] = source.get_text().strip().replace("\n", "")

        yield self.wechat_item












