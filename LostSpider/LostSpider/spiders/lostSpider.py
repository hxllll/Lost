# -*- coding: utf-8 -*-
import scrapy

from LostSpider.items import LostspiderItem


class LostspiderSpider(scrapy.Spider):
    name = 'lostSpider'
    allowed_domains = ['xunren.baidu.com']
    start_urls = ['http://xunren.baidu.com/index.html']

    def parse(self, response):
        lost_list = response.xpath("//div[@class='box2']/div")

        for lost in lost_list:
            item = LostspiderItem()
            item["name"] = lost.xpath(".//img/@title").extract_first()
            item["img"] = "http://xunren.baidu.com/" + lost.xpath(".//img/@src").extract_first()

            next_url = "http://xunren.baidu.com" + lost.xpath(".//a[@class='btn']/@href").extract_first()

            # yield item

            yield scrapy.Request(url=next_url, callback=self.parse_info, meta={"item": item})

    def parse_info(self,response):
        # print(response)
        item = response.meta['item'] # 获取一级页面中的item
        # print(item)
        # 解析二级页面
        item["age"] = response.xpath("//div[@class='text1']/div[3]/div/p/text()").extract_first() or ''
        item["height"] = response.xpath("//div[@class='text1']/div[4]/div/p/text()").extract_first() or ''
        item["feature"] = response.xpath("//div[@class='text1']/div[5]/div/p/text()").extract_first() or ''
        item["f_feature"] = response.xpath("//div[@class='text1']/div[6]/div/p/text()").extract_first() or ''
        item["isdna"] = response.xpath("//div[@class='text2']/div[1]/div/p/text()").extract_first() or ''
        item["f_date"] = response.xpath("//div[@class='text2']/div[2]/div/p/text()").extract_first() or ''
        item["f_site"] = response.xpath("//div[@class='text2']/div[3]/div/p/text()").extract_first() or ''
        item["r_tel"] = response.xpath("//div[@class='text2']/div[4]/div/p/text()").extract_first() or ''
        item["r_unit"] = response.xpath("//div[@class='text2']/div[5]/div/p/text()").extract_first() or ''
        item["p_date"] = response.xpath("//div[@class='text2']/div[6]/div/p/text()").extract_first() or ''
        item["r_info"] = response.xpath("//div[@class='text2']/div[7]/div/p/text()").extract_first() or ''

        yield item