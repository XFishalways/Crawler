# -*- coding: utf-8 -*-
# @Author  : XFishalways
# @Time    : 2022/7/31 11:00 PM
# @Function: Get certain fiction's info and content with the searching engine

import scrapy


def make_search_url(field, title, author, completion, language, rating, warnings, categories):
    searchUrl = 'https://archiveofourown.org/works/'

    searchUrl += 'search?&commit=Search&page='  # 执行查询 初始页数为1

    searchUrl += '&work_search%5Bquery%5D=' + field  # 关键词
    searchUrl += '&work_search%5Btitle%5D=' + title  # 标题
    searchUrl += '&work_search%5Bcreators%5D=' + author  # 作者
    searchUrl += '&work_search%5Brevised_at%5D='  # 日期
    searchUrl += '&work_search%5Bcomplete%5D=' + completion  # 是否完成
    searchUrl += '&work_search%5Bcrossover%5D='  # 合作
    searchUrl += '&work_search%5Bsingle_chapter%5D='  # 单章节
    searchUrl += '&work_search%5Bword_count%5D='  # 字数
    searchUrl += '&work_search%5Blanguage_id%5D=' + language  # 语言
    searchUrl += '&work_search%5Bfandom_names%5D='  # fandom 名
    searchUrl += '&work_search%5Brating_ids%5D=' + rating  # 级别
    searchUrl += '&work_search%5Barchive_warning_ids%5D%5B%5D=' + warnings  # 警告
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

    field = input("输入关键词:")
    title = input("输入标题:")

    start_urls = [make_search_url(field, title, author, completion, language, rating, warnings, categories)]

    def parse(self, response):
        pass
