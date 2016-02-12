import scrapy

class PersonItem(scrapy.Item):
    fullname = scrapy.Field()
    office_address = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    advisor = scrapy.Field()
    link = scrapy.Field()
