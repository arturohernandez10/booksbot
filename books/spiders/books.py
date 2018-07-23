# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = [
        'https://www.irs.gov/e-file-providers/e-file-for-excise-tax-filers',
    ]

    def parse(self, response):
		line = 0
		lineResponse = {}
        for provider_url in response.css("p a").extract():
			line = line + 1
		
			item = {}
			item["text"] = provider_url.css(" ::text").extract_first()
			item["href"] = provider_url.css(" ::href").extract_first()
			
			
			yield item
			
			if item["href"] == "https://www.i2290.com/index.aspx":
				lineResponse["result"] = line
				
		yield lineResponse
	
	
	