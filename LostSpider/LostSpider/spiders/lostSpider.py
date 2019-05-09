# -*- coding: utf-8 -*-
import re

import scrapy

from LostSpider.items import LostspiderItem


class LostspiderSpider(scrapy.Spider):
    name = 'lostSpider'
    allowed_domains = ['xunren.baidu.com']
    start_urls = ['http://xunren.baidu.com/index.Admin/?p=' + str(i) for i in range(1,4001)]

    def parse(self, response):
        lost_list = response.xpath("//div[@class='box2']/div")

        for lost in lost_list:
            item = LostspiderItem()
            item["l_name"] = lost.xpath(".//img/@title").extract_first()
            item["l_img"] = "http://xunren.baidu.com/" + lost.xpath(".//img/@src").extract_first()

            next_url = "http://xunren.baidu.com" + lost.xpath(".//a[@class='btn']/@href").extract_first()

            # yield item

            yield scrapy.Request(url=next_url, callback=self.parse_info, meta={"item": item})

    def parse_info(self,response):
        # print(response)
        item = response.meta['item'] # 获取一级页面中的item
        # print(item)
        # 解析二级页面
        item["l_sex"] = response.xpath("//div[@class='text1']/div[2]/div/p/text()").extract_first() or ''
        item["l_age"] = re.findall(r"\d+",response.xpath("//div[@class='text1']/div[3]/div/p/text()").extract_first())[0] or ''
        l_height = response.xpath("//div[@class='text1']/div[4]/div/p/text()").extract_first() or ''
        try:
            item["l_height"] = re.findall(r"\d+\.?\d*",l_height)[0]
        except:
            item["l_height"] = ''

        item["l_feature"] = response.xpath("//div[@class='text1']/div[5]/div/p/text()").extract_first() or ''
        item["l_f_feature"] = response.xpath("//div[@class='text1']/div[6]/div/p/text()").extract_first() or ''
        item["l_isdna"] = response.xpath("//div[@class='text2']/div[1]/div/p/text()").extract_first() or ''
        item["l_f_date"] = response.xpath("//div[@class='text2']/div[2]/div/p/text()").extract_first() or ''
        item["l_f_site"] = response.xpath("//div[@class='text2']/div[3]/div/p/text()").extract_first() or ''
        item["l_r_tel"] = response.xpath("//div[@class='text2']/div[4]/div/p/text()").extract_first() or ''
        item["l_r_unit"] = response.xpath("//div[@class='text2']/div[5]/div/p/text()").extract_first() or ''
        item["l_p_date"] = response.xpath("//div[@class='text2']/div[6]/div/p/text()").extract_first() or ''
        item["l_r_info"] = response.xpath("//div[@class='text2']/div[7]/div/p/text()").extract_first() or ''

        yield item