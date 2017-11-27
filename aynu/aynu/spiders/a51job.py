# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from aynu.items import WuyijobsItem
import datetime
from scrapy_redis.spiders import RedisCrawlSpider


class A51jobSpider(RedisCrawlSpider):
    name = '51job'
    allowed_domains = ['51job.com']
    # start_urls = ['http://www.51job.com']
    redis_key = 'wuyispider:urls'
    rules = (
        Rule(LinkExtractor(allow=r'http://www.51job.com/[a-z]+/$'), follow=True),
        Rule(LinkExtractor(allow=r'jobs.51job.com/[a-z]+/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = WuyijobsItem()
        item['job_url'] = response.url
        item['job_comp'] = response.css('.cname a::text').extract()[0]
        item['job_name'] = response.css('.cn h1::text').extract()[0]
        # 工资
        money = response.css('.cn strong::text').extract()
        if len(money) != 0:
            money = money[0]
            if '万/月' in money:
                item['job_smoney'] = float(money.replace('万/月', '').split('-')[0])*10
                item['job_emoney'] = float(money.replace('万/月', '').split('-')[1])*10
            elif '万/年' in money:
                # 薪水显示为万/年的情况下乘以0.8变为k/月
                item['job_smoney'] = float(money.replace('万/年', '').split('-')[0])*0.8
                item['job_emoney'] = float(money.replace('万/年', '').split('-')[1])*0.8
            elif '千' in money:
                item['job_smoney'] = float(money.replace('千/月', '').split('-')[0])
                item['job_emoney'] = float(money.replace('千/月', '').split('-')[1])
            elif '天' in money:
                item['job_smoney'] = float(money.replace('元/天', ''))
                item['job_emoney'] = float(money.replace('元/天', ''))
        else:
            item['job_smoney'] = 0
            item['job_emoney'] = 0

        item['job_address'] = response.css('.cn span::text').extract()[0]  # 工作地点

        comp_type = response.xpath('//p[@class="msg ltype"]/text()').extract()[0].split('|')

        # 公司类型
        item['job_comp_type'] = comp_type[0].strip()

        # 公司规模
        comp_snum = comp_type[1].strip()
        if '上' in comp_snum:
            item['job_comp_snum'] = int(comp_snum.split('人')[0])
            item['job_comp_enum'] = 10000  # 最大人数为0，代表为多少人以上
        elif '少' in comp_snum:
            item['job_comp_snum'] = 0  # 最少人数
            item['job_comp_enum'] = 50  # 最大人数
        elif '-' in comp_snum:
            item['job_comp_snum'] = comp_snum.split('-')[0]  # 最少人数
            item['job_comp_enum'] = comp_snum.split('-')[1].rstrip('人')  # 最大人数
        else:
            item['job_comp_snum'] = ''  # 有些公司没有标明人数
            item['job_comp_enum'] = ''

        # 公司主营
        if len(comp_type) == 3:  # 没有人数的公司，主营业务在第二项
            item['job_business'] = comp_type[2].strip()
        else:
            item['job_business'] = comp_type[1].strip()

        # 经验要求
        job_year = response.css('.t1 span::text').extract()[0]
        if '无' in job_year:
            item['job_syear'] = 0
            item['job_eyear'] = 0
        elif '-' in job_year:
            job_year = job_year.rstrip('年经验')
            item['job_syear'] = int(job_year.split('-')[0])
            item['job_eyear'] = int(job_year.split('-')[1])
        elif '上' in job_year:
            job_year = job_year.rstrip('年以上经验')  # n年经验以上
            item['job_syear'] = int(job_year)
            item['job_eyear'] = int(job_year)
        else:
            job_year = job_year.rstrip('年经验')  # n年经验
            item['job_syear'] = int(job_year)
            item['job_eyear'] = int(job_year)

        # 发布日期
        # 有的没有学历，发布日期则在第三项
        job_year = response.xpath(r'//div[@class="t1"]/span[3]/text()').extract()[0]
        if '发布' in job_year:
            item['job_date_pub'] = job_year.strip('发布')
        else:
            item['job_date_pub'] = response.xpath(r'//div[@class="t1"]/span[4]/text()').extract()[0].strip('发布')

        # 公司福利
        job_welfafe = response.xpath(r'//p[@class="t2"]/span/text()').extract()
        if len(job_welfafe) != 0:
            item['job_welfafe'] = str(job_welfafe).lstrip('[').rstrip(']')
        else:
            item['job_welfafe'] = 0  # 有些公司没有福利

        # 招聘人数
        job_people = response.xpath(r'//div[@class="t1"]/span[3]/text()').extract()[0]
        if '发布' not in job_people:
            if '若干' in job_people:
                item['job_people'] = '若干'
            else:
                item['job_people'] = job_people.lstrip('招').rstrip('人')
        else:
            job_people = response.xpath(r'//div[@class="t1"]/span[2]/text()').extract()[0]
            if '发布' not in job_people:
                if '若干' in job_people:
                    item['job_people'] = '若干'
                else:
                    item['job_people'] = job_people.lstrip('招').rstrip('人')

        # 学历要求
        job_degree = response.xpath(r'//div[@class="t1"]/span[2]/text()').extract()[0]
        if '人' not in job_degree:
            item['job_degree'] = job_degree
        else:
            item['job_degree'] = 0

        # 岗位职责
        job_desc = response.xpath(r'//div[@class="bmsg job_msg inbox"]/text()').extract()
        if len(job_desc) != 0:
            job_des = [i.strip() for i in job_desc]
            while '' in job_des:
                job_des.remove('')
            item['job_desc'] = str(job_des).lstrip('[').rstrip(']')
        elif len(job_desc) == 0:
            job_n = response.xpath(r'//div[@class="bmsg job_msg inbox"]/div/text()').extract()
            if len(job_n) != 0:
                job_des = [i.strip() for i in job_n]
                while '' in job_des:
                    job_des.remove('')
                item['job_desc'] = str(job_des).lstrip('[').rstrip(']')
            elif len(job_n) == 0:
                job_n = response.xpath(r'//div[@class="bmsg job_msg inbox"]/p/text()').extract()
                job_des = [i.strip() for i in job_n]
                while '' in job_des:
                    job_des.remove('')
                item['job_desc'] = str(job_des).lstrip('[').rstrip(']')
        if len(item['job_desc']) == 0:
            item['job_desc'] = '见详情页'

        # 岗位要求
        item['job_request'] = ''

        # 岗位标签
        job_tag = response.xpath(r'//div[@class="mt10"]//span[2]/text()').extract()
        item['job_tag'] = str(job_tag).lstrip('[').rstrip(']')

        # 采集时间
        item['job_datetime'] = datetime.datetime.now().strftime('%Y-%m-%d')

        yield item

