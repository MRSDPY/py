import scrapy


class CornaScraperSpider(scrapy.Spider):
    name = 'corna_scraper'
    allowed_domains = ['https://www.mohfw.gov.in/']
    start_urls = ['https://www.mohfw.gov.in//']

    def parse(self, response):
        pass
