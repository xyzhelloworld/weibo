# -*- coding: utf-8 -*-

import scrapy
from scrapy import log
from scrapy.selector import Selector
from scrapy.spiders import Spider, Rule, CrawlSpider
from scrapy.http.request import Request  
from scrapy.linkextractors import LinkExtractor

from weibo.items import WeiboItem, PersonInfoItem


class DoubanSpider(CrawlSpider):
    name = 'weibo'
    start_urls = [
        'http://weibo.cn'
    ]
    allow_domains = [
        'weibo.cn'
    ]
    rules=[
        Rule(LinkExtractor(allow=(r'http://weibo.cn/u/([a-zA-Z]+|\d+)(\?page=\d+)?')), callback='process_weibo'),
        Rule(LinkExtractor(allow=(r'http://weibo.cn/u/([a-zA-Z]+|\d+)/follow(\?page=\d+)?')), callback='process_follow'),
        Rule(LinkExtractor(allow=(r'http://weibo.cn/u/([a-zA-Z]+|\d+)/fans(\?page=\d+)?')), callback='process_fans'),
        Rule(LinkExtractor(allow=(r'http://weibo.cn/([a-zA-Z]+|\d+)/info')), callback='process_person_info'),
        Rule(LinkExtractor(allow=(r'http://weibo.cn/account/privacy/tags/?uid=\d+')), callback='process_tags'),
    ]

    def start_requests(self):
        cookies = {'un': '941023812@qq.com', 'myuid': '3239297934', 'login_sid_t': '04fe66b57c306c6bd67b325c9bdfa8fa', 'TC-Ugrow-G0': '968b70b7bcdc28ac97c8130dd353b55e', 'TC-Page-G0': 'cdcf495cbaea129529aa606e7629fea7', 'SUS': 'SID-3239297934-1442824715-XD-csy0a-86b29a3ee512dba3ec997a8230e75104', 'SUE': 'es%3Dff04ec704f622fe74bf5df9b6f3fba09%26ev%3Dv1%26es2%3D5a89e105afb255de51237133a3844358%26rs0%3DFfKy%252FprXBED07kQOGuklBiZe2LqK2rSPYyPR%252B%252BAHX9lH2FuTrWa2XZyH1cah63QR2HAiHBM6r8lfMPe5ZsHlKiZ8q5guCMgYgU898OknbWDr4qSWCYeTXXRRm8eoQjEsbhoc4lPxfbQielqUnEkBlAFolD%252BA8p4%252FESI2oIVZrqk%253D%26rv%3D0', 'SUP': 'cv%3D1%26bt%3D1442824715%26et%3D1442911115%26d%3Dc909%26i%3D5104%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D3239297934%26name%3D941023812%2540qq.com%26nick%3D%25E9%25A3%258E%25E9%25A3%2598%25E7%25B5%25AE_78785%26fmp%3D%26lcp%3D', 'SUB': '_2A254-7JbDeTxGeVM6FsT-SnFyDiIHXVYcKSTrDV8PUNbuNAPLWjlkW-H8CvJzLI8tCK_6EUVsuLwSUwhqw..', 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WhzC8z8ZEOx49h2bNJDr2lf5JpX5K2t', 'SUHB': '0sqROQ1ZGC6k0i', 'ALF': '1474360714', 'SSOLoginState': '1442824715', 'un': '941023812@qq.com', 'wvr': '6', 'TC-V5-G0': '10672b10b3abf31f7349754fca5d2248'}
        for url in self.start_urls:
            yield Request(url=url, cookies=cookies)

    def process_weibo(self, response):
        pass

    def process_follow(self, response):
        pass

    def process_fans(self, response):
        pass

    def process_person_info(self, response):
        pass

    def process_tags(self, response):
        pass