# -*- coding: utf-8 -*-
import scrapy


class AaabotSpider(scrapy.Spider):
    name = 'AAAbot'
    allowed_domains = ['https://gasprices.aaa.com/state-gas-price-averages/']
    start_urls = ['http://https://gasprices.aaa.com/state-gas-price-averages//']

    def parse(self, response):
        states = response.css("
