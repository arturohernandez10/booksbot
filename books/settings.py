# -*- coding: utf-8 -*-

BOT_NAME = 'books'

SPIDER_MODULES = ['books.spiders']
NEWSPIDER_MODULE = 'books.spiders'

ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True

DOWNLOADER_MIDDLEWARES = {'scrapy_crawlera.CrawleraMiddleware': 300}
CRAWLERA_ENABLED = True
CRAWLERA_APIKEY = '4b092d2f10124a47a07653a5f6d87977'
