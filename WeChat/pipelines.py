# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class WechatPipeline(object):
    def process_item(self, item, spider):
        return item
class writeMysql(object):
    def __init__(self):
        self.client = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',  #使用自己的用户名
            passwd='MIfeng888!',  # 使用自己的密码
            db='zyc',  # 数据库名
            charset='utf8mb4'
        )
        self.cur = self.client.cursor()
    def process_item(self,item,spider):
        sql = 'insert into wechat(title,writer,article) VALUES (%s,%s,%s)'
        lis = (item['title'], item['writer'], item['article'])
        self.cur.execute(sql, lis)
        self.client.commit()
        # self.cur.close()
        # self.client.close()

