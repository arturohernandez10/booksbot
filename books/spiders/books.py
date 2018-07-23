# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["www.irs.gov"]
    start_urls = [
        'https://www.irs.gov/e-file-providers/e-file-for-excise-tax-filers',
    ]

    def parse(self, response):
        for provider_url in response.css("p > a attr(::href)").extract():
            yield provider_url
				
