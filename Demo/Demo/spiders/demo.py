import re
import  sys
sys.path.append('D:\Scrapy_crawl\Demo\Demo')
import scrapy

from ..items import DemoItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        html = response.text
        reg = r'<img data-original="(.*?)">.*?<div class="li_txt">.*?<h3>(.*?)</h3>.*?<h4>(.*?)</h4>.*?<p>(.*?)</p>'
        infos = re.findall(reg,html,re.S    )

        for img,name,grade,talk in infos:
            item = DemoItem()
            item['name'] = name
            item['grade'] = grade
            item['info'] = talk
            item['img'] = self.allowed_domains[0]+img
            yield  item
