import scrapy


class CoronaItem(scrapy.Item):
    # define the fields for your item here like:
    state = scrapy.Field()
    case = scrapy.Field()
    recovery = scrapy.Field()
    death = scrapy.Field()

