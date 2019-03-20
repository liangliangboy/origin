# -*- coding: utf-8 -*-
import io
import sys

import scrapy

from zhihu.items import ZhihuItem

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

class ZhSpider(scrapy.Spider):
    name = 'ZH'
    allowed_domains = ['zhihu.com/topics']
    start_urls = ['https://www.zhihu.com/topic/19550517/hot']
    count = 0
    def parse(self, response):
        titles = response.xpath('//*[@id="TopicMain"]/div[3]/div/div/div//div[@class="List-item TopicFeedItem"]//h2/text()').extract()
        for title in titles:
            count += 1
            zh_item = ZhihuItem()
            zh_item['title'] = title
            print(zh_item)
            yield zh_item
        print('获得',count,'个数据')
