from ..items import FictionruaerItem

import scrapy


class FandomAM_NameSpider(scrapy.Spider):
    name = 'FandomAM_Name'
    allowed_domains = ['archiveofourown.org']
    start_urls = ['https://archiveofourown.org/media/Anime%20*a*%20Manga/fandoms']

    def parse(self, response):
        liList = response.xpath('//li[@class="letter listbox group"]/ul[@class="tags index group"]')

        for li in liList:
            fandomAM_NameList = li.xpath("./child::li/a/text()").extract()

            for fandomAM_Name in fandomAM_NameList:
                item = FictionruaerItem(fandomAM_Name=fandomAM_Name)

                yield item
