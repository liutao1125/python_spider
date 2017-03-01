# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from douban.items import DoubanItem

class DoubanspdSpider(CrawlSpider):
    name = "doubanspd"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/tag/恐怖']
    
    rules = [ 
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/tag/%E6%81%90%E6%80%96\?start=\d+.*')),),
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+')),callback="parse_item"),
        ] 

    def parse_item(self, response):
        item = {}
        item = DoubanItem()
        item['name'] = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['score'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()
        item['link'] = response.url
        yield item
