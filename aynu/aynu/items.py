# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AynuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class XiciItem(scrapy.Item):
    host = scrapy.Field()
    port = scrapy.Field()
    http_type = scrapy.Field()


class WuyijobsItem(scrapy.Item):
    job_url = scrapy.Field()  # 职位详情链接
    job_comp = scrapy.Field()  # 公司名
    job_name = scrapy.Field()  # 职位名
    job_smoney = scrapy.Field()  # 最少薪资
    job_emoney = scrapy.Field()  # 最大薪资
    job_address = scrapy.Field()  # 工作地点
    job_comp_type = scrapy.Field()  # 公司类别
    job_comp_snum = scrapy.Field()  # 公司规模 最少人数
    job_comp_enum = scrapy.Field()  # 最大人数
    job_business = scrapy.Field()  # 公司主营
    job_syear = scrapy.Field()  # 经验要求 最小
    job_eyear = scrapy.Field()  # 最大经验年限
    job_date_pub = scrapy.Field()  # 发布日期
    job_datetime = scrapy.Field()  # 收录时间
    job_welfafe = scrapy.Field()  # 公司福利
    job_people = scrapy.Field()  # 招聘人数
    job_desc = scrapy.Field()  # 岗位职责
    job_request = scrapy.Field()  # 岗位要求
    job_tag = scrapy.Field()  # 工作标签
    job_degree = scrapy.Field()  # 学历
