# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WereadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hasMore = scrapy.Field()
    synckey = scrapy.Field()
    totalCount = scrapy.Field()
    books = scrapy.Field()
    category = scrapy.Field()
    index = scrapy.Field()
#
# class BookItem(scrapy.Item):
#     bookInfo = scrapy.Field()
#     readingCount = scrapy.Field()
#     searchIdx = scrapy.Field()
#     type = scrapy.Field()
#
#
# class BookInfo(scrapy.item):
#     author = scrapy.Field()
#     bookId = scrapy.Field()
#     bookStatus = scrapy.Field()
#     category = scrapy.Field()
#     centPrice = scrapy.Field()
#     cover = scrapy.Field()
#     cpid = scrapy.Field()
#     finished = scrapy.Field()
#     format = scrapy.Field()
#     free = scrapy.Field()
#     hasLecture = scrapy.Field()
#     intro = scrapy.Field()
#     ispub = scrapy.Field()
#     lastChapterIdx = scrapy.Field()
#     maxFreeChapter = scrapy.Field()
#     mcardDiscount = scrapy.Field()
#     originalPrice = scrapy.Field()
#     payType = scrapy.Field()
#     price = scrapy.Field()
#     ratingCount = scrapy.Field()
#     soldout = scrapy.Field()
#     source = scrapy.Field()
#     star = scrapy.Field()
#     title = scrapy.Field()
#     type = scrapy.Field()
#     version = scrapy.Field()

