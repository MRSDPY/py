import scrapy
from ..items import CoronaItem


class Scraper(scrapy.Spider):
    name = "corona"
    start_urls = [
        "https://covidindia.org/"
    ]

    def parse(self, response):
        state = response.css("td.column-1::text").getall()
        case = response.css("td.column-2::text").getall()
        recovery = response.css("td.column-3::text").getall()
        deaths = response.css("td.column-4::text").getall()
        # state = response.xpath('//tc[@class="column-2"]/text()').getall()

        item = CoronaItem()
        item['state'] = state
        item['case'] = case
        item['recovery'] = recovery
        item['death'] = deaths

        yield item
