# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time

class DoubanPipeline(object):
    def exeSQL(self,sql):
        con = pymysql.connect(
            host='localhost',
            user='root',
            passwd='123456',
            db='spdRet',
            charset='utf8',
            local_infile = 1
        )    
        con.query(sql)
        con.commit()
        con.close()
    def process_item(self, item, spider):
        link_url = item['link']
        name_content = item['name'][0]
        name_content = name_content.replace("'","''")
        score = item['score'][0]
        try:
            sql="insert into douban(name,score,link) value('"+name_content+"','"+score+"','"+link_url+"')"
            self.exeSQL(sql)
        except Exception as er:
            print("插入错误，错误如下：")
            print(er)
        return item
