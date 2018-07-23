# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["www.irs.gov"]
    start_urls = [
        'https://www.irs.gov/e-file-providers/e-file-for-excise-tax-filers',
    ]

    def parse(self, response):
	itemList = []
        for anchor in response.css("p > a"):
	    item = {}
	    item["ref"] = anchor.css('::attr(href)').extract_first()
	    itemList.append(item)
	response = {}
	response["providers"] = itemList
        response
