import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exporters import XmlItemExporter

class BookstoscrapeItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    rating = scrapy.Field()
    pass

class GoodReadsspider(CrawlSpider):
    name = 'goodreads'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/']
    base_url = 'https://www.goodreads.com/'
    link_search = LinkExtractor(allow=r'book/show/')
    rule_for_book = Rule(link_search, callback='parse_filter_book',
                         follow=True)
    rules = (
        rule_for_book,
        )

    def parse_filter_book(self, response):
        book_data = response.css('#topcol')
        item = BookstoscrapeItem()
        for data in book_data: # making the extractions from a for loop means the output is clean

            item['title'] = data.css('h1::text').extract()
            item['author'] = data.css('.authorName span::text').extract()
            item['rating'] = data.css('.notranslate+ span::text').extract_first()
            yield item