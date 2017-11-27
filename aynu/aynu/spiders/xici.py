# -*- coding: utf-8 -*-
import scrapy
from aynu.items import XiciItem
import requests


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com']

    def parse(self, response):
        proxy_list = response.css('table#ip_list tr')[1:]
        for proxy in proxy_list:
            item = XiciItem()
            # css 选择器获取代理信息
            td_list = proxy.css('td::text').extract()
            host = td_list[0]
            port = td_list[1]
            http_type = td_list[5]
            if http_type.strip() == '':
                http_type = 'http'
            daili = host + ':' + port
            proxy = {
                'http': daili,
                'https': daili,
            }
            # 判断代理是否有效，访问百度
            try:
                response = requests.get('https://www.baidu.com/', proxies=proxy, timeout=3)
                if response.status_code == 200:
                    item['host'] = host
                    item['port'] = port
                    item['http_type'] = http_type

                    yield item
            except:
                pass


