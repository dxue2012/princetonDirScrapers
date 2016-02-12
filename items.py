import scrapy

class PersonItem(scrapy.Item):
    fullname = scrapy.Field()
    office_address = scrapy.Field()
    email_address = scrapy.Field()
    advisers = scrapy.Field()
