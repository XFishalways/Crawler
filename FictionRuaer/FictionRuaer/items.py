# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FictionruaerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # created for FandomAM_Name
    fandomAMName = scrapy.Field()

    # created for Work's parse function
    fictionSearchName = scrapy.Field()  # 搜索页面标题
    fictionSearchSummary = scrapy.Field()  # 搜索页面文章简介

    # created for Work's article_parse function
    fictionRating = scrapy.Field()
    fictionArchiveWarning = scrapy.Field()
    fictionCategories = scrapy.Field()
    fictionContentName = scrapy.Field()  # 文章页面标题
    fictionLanguage = scrapy.Field()
    fictionPublishDate = scrapy.Field()
    fictionWords = scrapy.Field()
    fictionHits = scrapy.Field()
    fictionTitle = scrapy.Field()
    fictionPreface = scrapy.Field()
    fictionContent = scrapy.Field()
