import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = ["https://bluelimelearning.github.io/my-fav-quotes/"]

    def parse(self, response):
        # self represents the instance of the class
        # selectors: mechanism for extracting data from website
        # selects certain expressions from html
        for quote in response.css('div.quotes'):
            # generator is an iterator
            # yield is keyword that tells you what to return
            yield {
                'quote': quote.css('p.aquote::text').extract(),
                'author': quote.css('p.author::text').extract_first(),
            }
