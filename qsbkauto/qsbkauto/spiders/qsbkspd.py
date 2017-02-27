# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qsbkauto.items import QsbkautoItem
from scrapy.http import Request


class QsbkspdSpider(CrawlSpider):
    name = 'qsbkspd'
    allowed_domains = ['qiushibaike.com']
    #start_urls = ['http://qiushibaike.com/']
    def start_requests(self):
        i_headers = {"User-Agent":"Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0"}
        yield Request('http://www.qiushibaike.com',headers=i_headers)

    rules = (
        Rule(LinkExtractor(allow=r'article/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i = QsbkautoItem()
        i['content'] = response.xpath("//div[@class='content']/text()").extract()
        i["link"] = response.xpath("//link[@rel='canonical']/@href").extract()
        return i
