import scrapy
import  sys
sys.path.append('D:\Scrapy_crawl\Qutoes_crawl\Qutoes_crawl')
from items import QutoesCrawlItem

class QutoesSpider(scrapy.Spider):
    name = 'Qutoes'
    allowed_domains = ['qutoes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    def parse(self, response):
        # print(response.text)
        quotes = response.css('.quote')
        for quote in quotes:
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()
            # print(text,author,tags)
            item = QutoesCrawlItem()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item
        next_url = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next_url)
        yield scrapy.Request(url=url, callback=self.parse)