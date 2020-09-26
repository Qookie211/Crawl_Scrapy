# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#名字response.xpath('.//div/h1/span/text()').extract[0]
    classer = scrapy.Field()#排名  response.xpath('.//span[@class='top250-no'][1]/text()').extract()[0]
    pf = scrapy.Field()#评分response.xpath('.//strong/text()').extract()[0]
    im = scrapy.Field()#电影信息response.xpath('.//span[@class="short"]/span/text()').extract()[0].strip()
    quotes = scrapy.Field()#热点评语response.xpath('.//p/span/text()').extract()[0]



