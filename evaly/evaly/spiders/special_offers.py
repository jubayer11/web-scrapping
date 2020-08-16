# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.daraz.com.bd']
    start_urls = ['http://https://www.daraz.com.bd/']

    def parse(self, response):
        pass
