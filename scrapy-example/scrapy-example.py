try:
    import scrapy
except:
    !pip install scrapy
    import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://www.toscrape.com/"]
    
    def parse(self, response):
        self.log('I just visited: ',  response.url)
        yield {
            'author_name': response.css('small.author::text').extract_first(),
            'text': response.css('span.text::text').extract_first(),
            'tags': response.css('a.tag::text').extract()
        }
    
