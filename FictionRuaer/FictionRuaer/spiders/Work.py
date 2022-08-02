# -*- coding: utf-8 -*-
# @Author  : XFishalways
# @Time    : 2022/7/31 11:00 PM
# @Function: Get certain fiction's info and content with the searching engine

from ..items import FictionruaerItem

import scrapy


def make_search_url(field, title, author, completion, language, rating, warnings, categories):
    searchUrl = 'https://archiveofourown.org/works/'

    searchUrl += 'search?&commit=Search&page='  # 执行查询 初始页数为1

    searchUrl += '&work_search%5Bquery%5D=' + field  # 关键词
    searchUrl += '&work_search%5Btitle%5D=' + title  # 标题
    searchUrl += '&work_search%5Bcreators%5D=' + author  # 作者
    searchUrl += '&work_search%5Brevised_at%5D='  # 日期
    searchUrl += '&work_search%5Bcomplete%5D=' + completion  # 完成度(是否完成)
    searchUrl += '&work_search%5Bcrossover%5D='  # 合作
    searchUrl += '&work_search%5Bsingle_chapter%5D='  # 单章节
    searchUrl += '&work_search%5Bword_count%5D='  # 字数
    searchUrl += '&work_search%5Blanguage_id%5D=' + language  # 语言
    searchUrl += '&work_search%5Bfandom_names%5D='  # fandom 名
    searchUrl += '&work_search%5Brating_ids%5D=' + rating  # 级别
    # Not Rated => 9
    # General Audiences => 10
    # Teen And Up Audiences => 11
    # Mature => 12
    # Explicit => 13

    searchUrl += '&work_search%5Barchive_warning_ids%5D%5B%5D=' + warnings  # 警告限制
    # Creator Chose Not To Use Archive Warnings => 14
    # Graphic Depictions Of Violence => 17
    # Major Character Death => 18
    # No Archive Warnings Apply => 16
    # Rape/Non-Con => 19
    # Underage => 20

    searchUrl += '&work_search%5Bcategory_ids%5D%5B%5D=116' + categories  # 类型
    # F/F => 116
    # F/M => 22
    # Gen => 21
    # M/M => 23
    # Multi => 2246
    # Other => 24

    searchUrl += '&work_search%5Bcharacter_names%5D='  # 角色名
    searchUrl += '&work_search%5Brelationship_names%5D='  # 关系名
    searchUrl += '&work_search%5Bfreeform_names%5D='  # 其他特点
    searchUrl += '&work_search%5Bhits%5D='  # 点击量
    searchUrl += '&work_search%5Bkudos_count%5D='  # 点赞数
    searchUrl += '&work_search%5Bcomments_count%5D='  # 评论数
    searchUrl += '&work_search%5Bbookmarks_count%5D='  # 书签数
    searchUrl += '&work_search%5Bsort_column%5D=_score'  # 排序方式
    searchUrl += '&work_search%5Bsort_direction%5D=desc'  # 排序顺序

    return searchUrl


class WorkSpider(scrapy.Spider):
    name = 'Work'
    allowed_domains = ['archiveofourown.org']

    print("Welcome to Fiction Searching Engine!")

    field = input("输入关键词: ")
    title = input("输入标题: ")
    author = input("输入作者: ")

    while True:
        whetherComplete = input("输入完成度: \n"
                                "已完结 => 1\n"
                                "更新中 => 0\n")
        if whetherComplete == "1":
            completion = "T"
            break
        elif whetherComplete == "0":
            completion = "F"
            break
        elif whetherComplete == "":
            completion = ""
            break
        else:
            print("Please input 0 or 1")

    while True:
        language = input("输入语言: \n"
                         "中文 => zh\n"
                         "英文 => en\n"
                         "日语 => ja\n")
        if language == "zh" or language == "en" or language == "ja":
            break

        print("Please input a valid value")

    while True:
        rating = input("输入级别: \n"
                       "Not Rated => 9\n"
                       "General Audiences => 10\n"
                       "Teen And Up Audiences => 11\n"
                       "Mature => 12\n"
                       "Explicit => 13\n")
        if rating == "9" or rating == "10" or rating == "11" or rating == "12" or rating == "13":
            break
        if rating == "":
            break

        print("Please input a valid value")

    while True:
        warnings = input("输入警告限制: \n"
                         "Creator Chose Not To Use Archive Warnings => 14\n"
                         "Graphic Depictions Of Violence => 17\n"
                         "Major Character Death => 18\n"
                         "No Archive Warnings Apply => 16\n"
                         "Rape/Non-Con => 19\n"
                         "Underage => 20\n")
        if warnings == "14" or warnings == "17" or warnings == "18" \
                or warnings == "16" or warnings == "19" or warnings == "20":
            break

        print("Please input a valid value")

    while True:
        categories = input("输入小说类型: \n"
                           "F/F => 116\n"
                           "F/M => 22\n"
                           "Gen => 21\n"
                           "M/M => 23\n"
                           "Multi => 2246\n"
                           "Other => 24\n")
        if categories == "116" or categories == "22" or categories == "21" \
                or categories == "23" or categories == "2246" or categories == "24":
            break

        print("Please input a valid value")

        print("Please")

    start_urls = [make_search_url(field, title, author, completion, language, rating, warnings, categories)]
    custom_settings = {
        'ITEM_PIPELINES': {'FictionRuaer.pipelines.WorkPipeline': 300}
    }

    def parse(self, response):
        fictionList = response.xpath('//ol[@class="work index group"]/li[@role="article"]')

        for fiction in fictionList:
            fictionSearchNameList = fiction.xpath('./div[@class="header module"]/h4/a[not(@rel="author")]/text()').extract()
            fictionSearchSummaryList = fiction.xpath('./blockquote[@class="userstuff summary"]/p/text()').extract()

            fictionDict = dict(zip(fictionSearchNameList, fictionSearchSummaryList))

            for key, value in fictionDict.items():
                print("- Name: {key}\n"
                      "  Summary: {value}\n".format(key=key, value=value))

    def article_parse(self, response):
        pass
