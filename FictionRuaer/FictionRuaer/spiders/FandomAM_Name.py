# -*- coding: utf-8 -*-
# @Author  : XFishalways
# @Time    : 2022/7/30 8:00 PM
# @Function: Get all fandoms' name from 'Anime & Manga'

from ..items import FictionruaerItem

import scrapy


class FandomAM_NameSpider(scrapy.Spider):
    name = 'FandomAM_Name'
    allowed_domains = ['archiveofourown.org']
    start_urls = ['https://archiveofourown.org/media/Anime%20*a*%20Manga/fandoms']
    custom_settings = {
        'ITEM_PIPELINES': {'FictionRuaer.pipelines.FandomAMNamePipeline': 500}
    }

    def parse(self, response):
        fandomAMList = response.xpath('//li[@class="letter listbox group"]/ul[@class="tags index group"]')

        for fandomAM in fandomAMList:
            fandomAMNameList = fandomAM.xpath('./child::li/a/text()').extract()

            for fandomAMName in fandomAMNameList:
                item = FictionruaerItem(fandomAMName=fandomAMName)

                yield item
