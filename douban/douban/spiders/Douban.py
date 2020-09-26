import sys

import scrapy
sys.path.append('D:\Scrapy_crawl\douban\douban')
from douban.items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'Douban'
    allowed_domains = ['movie.douban.com']
    url = 'https://movie.douban.com/top250?start='
    set_number = 0
    start_urls =(
        url+str(set_number),
    )

    def parse(self, response):
        item = DoubanItem()
        moives = response.xpath("//div[@class='info']")
        for each in moives:
             item['title']=each.xpath('.//div/h1/span/text()').extract[0]
             item['classer']=each.xpath('.//span[@class="top250-no"[1]/text()').extract()[0]
             item['pf']=each.xpath('.//strong/text()').extract()[0]
             item['im']=each.xpath('.//span[@class="short"]/span/text()').extract()[0].strip()
             qutoes=each.xpath('.//p/span/text()').extract()[0]
             if len(qutoes) != 0:
                 item['quote'] = qutoes[0]
             yield item
             if self.set_number < 225:
                 self.set_number += 25

                 yield scrapy.Request(self.url + str(self.set_number), callback=self.parse)

