# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LostspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    img = scrapy.Field()
    next_url = scrapy.Field()

    age = scrapy.Field()
    height = scrapy.Field()
    feature = scrapy.Field()
    f_feature = scrapy.Field()
    isdna = scrapy.Field()
    f_date = scrapy.Field()
    f_site = scrapy.Field()
    r_tel = scrapy.Field()
    r_unit = scrapy.Field()
    p_date = scrapy.Field()
    r_info = scrapy.Field()
