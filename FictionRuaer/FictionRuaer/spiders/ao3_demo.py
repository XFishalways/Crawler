import scrapy


class Ao3DemoSpider(scrapy.Spider):
    name = 'ao3_demo'
    allowed_domains = ['archiveofourown.org']
    start_urls = ['http://archiveofourown.org/']

    def parse(self, response):
        pass
