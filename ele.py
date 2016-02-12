import scrapy
# from scrapy.selector import Selector
from items import PersonItem


class eleSpider(scrapy.Spider):
    name = 'ele grad students'
    start_urls = ['https://www.cs.princeton.edu/people/grad']

    def parse(self, response):
        for block in response.css('.person-details'):
            self.parse_person(block)

    def parse_person(self, response):
        personItem = PersonItem()
        personItem.fullname = response.css(".person-name")
