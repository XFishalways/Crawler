from ..items import FictionruaerItem

import scrapy


class Ao3DemoSpider(scrapy.Spider):
    name = 'ao3_demo'
    allowed_domains = ['archiveofourown.org']
    start_urls = ['https://archiveofourown.org/media/Anime%20*a*%20Manga/fandoms']

    def parse(self, response):
        liList = response.xpath('//li[@class="letter listbox group"]/ul[@class="tags index group"]')
        print(len(liList))

        for li in liList:
            fandomAM_Name = li.xpath("./li[1]/a/text()").extract()[0]

            item = FictionruaerItem(fandomAM_Name=fandomAM_Name)

            yield item
