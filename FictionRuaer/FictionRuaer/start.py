# -*- coding: utf-8 -*-
# @Author  : XFishalways
# @Time    : 2022/7/30 8:00 PM
# @Function: run scrapy without using command line

from scrapy import cmdline

cmdline.execute('scrapy crawl FandomAM_Name'.split())
cmdline.execute('scrapy crawl Work'.split())
