# -*- coding: utf-8 -*-
# @Author  : XFishalways
# @Time    : 2022/7/31 11:00 AM
# @Function: Get certain fiction's info and content with the searching engine

import scrapy


class WorkSpider(scrapy.Spider):
    name = 'Work'
    allowed_domains = ['archiveofourown.org']
    start_urls = ['http://archiveofourown.org/']

    def parse(self, response):
        pass

