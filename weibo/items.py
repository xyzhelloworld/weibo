# -*- coding: utf-8 -*-

import scrapy


class WeiboItem(scrapy.Item):
    weibo = scrapy.Field()
    hashcode = scrapy.Field()
    user_id = scrapy.Field()

class PersonInfoItem(scrapy.Item):
	user_id = scrapy.Field()
	nickname = scrapy.Field()
    certification = scrapy.Field()
    gender = scrapy.Field()
    zone = scrapy.Field()
    birthday = scrapy.Field()
    tag = scrapy.Field()
    experience = scrapy.Field()    # experience = {company1: {name: xxxx, time: xxxx-xxxx}}
    education = scrapy.Field()    # school = {university: {name: anhui university, time: 2012}}
    register = scrapy.Field()    

'''
基本信息
昵称:赵武在路上
认证:安全软件Pangolin、JSky作者。
性别:男
地区:北京 朝阳区
认证信息：安全软件Pangolin、JSky作者。
简介:补天漏洞响应平台负责人；网站安全检测，主机卫士，关注网站安全关注我就对了。
标签:Web安全 网站安全 产品经理 更多>>

学习经历
·湘潭大学 01级

工作经历
·北京家里蹲科技有限公司 2015年-至今
·奇虎360 2011年-2015年
·深圳市宇造诺赛科技有限公司 2009年-2011年
·华为技术有限公司 2004年-2009年

其他信息
互联网:http://weibo.com/zwell
手机版:http://weibo.cn/zwell
'''