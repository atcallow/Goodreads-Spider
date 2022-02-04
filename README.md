# Goodreads-Spider
This crawls Goodreads urls for book summary pages and extracts book title, author, and ratings.


The first portion of the code logically is the spider. Due to the construction of the goodreads webiste and that I was looking for all their book data,
I needed the CrawlSpider object. We allow only goodreads domains so the spider doesn't go off into the great wild yonder.

'''
class GoodReadsspider(CrawlSpider):
    name = 'goodreads'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/']
    base_url = 'https://www.goodreads.com/'
'''

The main rule we need is the link ectractor which tells the spider to only explore urls with the "book/show/" information. these are the urls that
are the dedicated book summary pages. Then we tell the spider to call the below "parse_filter_book" function if it has found a book page. T
hen we tell the spider to keep following links.

'''
    link_search = LinkExtractor(allow=r'book/show/')
    rule_for_book = Rule(link_search, callback='parse_filter_book',
                         follow=True)
    rules = (
        rule_for_book,
        )
'''

This is the item object to collect the yeild data.

'''
class BookstoscrapeItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    rating = scrapy.Field()
    pass
'''    

This is parse function which extracts the data we want from the desired urls.

'''
def parse_filter_book(self, response):
     book_data = response.css('#topcol')
     item = BookstoscrapeItem()
     for data in book_data: # making the extractions from a for loop means the output is clean

          item['title'] = data.css('h1::text').extract()
          item['author'] = data.css('.authorName span::text').extract()
          item['rating'] = data.css('.notranslate+ span::text').extract_first()
            yield item
 '''           
            
 
 
 
