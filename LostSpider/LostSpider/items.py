# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LostspiderItem(scrapy.Item):
    # define the fields for your item here like:
    l_name = scrapy.Field()
    l_img = scrapy.Field()
    next_url = scrapy.Field()

    l_sex = scrapy.Field()
    l_age = scrapy.Field()
    l_height = scrapy.Field()
    l_feature = scrapy.Field()
    l_f_feature = scrapy.Field()
    l_isdna = scrapy.Field()
    l_f_date = scrapy.Field()
    l_f_site = scrapy.Field()
    l_r_tel = scrapy.Field()
    l_r_unit = scrapy.Field()
    l_p_date = scrapy.Field()
    l_r_info = scrapy.Field()
