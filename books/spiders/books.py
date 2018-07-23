# -*- coding: utf-8 -*-
import scrapy
import logging

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["www.irs.gov"]
    start_urls = [
        'https://www.irs.gov/e-file-providers/e-file-for-excise-tax-filers',
    ]

    def parse(self, response):   
        item = {}
        for anchor in response.css("p > a"):

            item["ref"] = anchor.css('::attr(href)').extract_first()
            logging.log(logging.WARNING, item["ref"])
        yield item
