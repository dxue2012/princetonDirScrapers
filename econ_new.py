import scrapy
from loaders import EconPersonLoader
from items import PersonItem

class econSpider(scrapy.Spider):
    name = 'econ grad students'
    start_urls = ['http://economics.princeton.edu/graduate-program/graduate-student-directory']

    def parse(self, response):
        for block in response.css('.field-item').xpath("//tbody/tr"):
            yield self.parse_person(block)

    def parse_person(self, sel):
        l = EconPersonLoader(item=PersonItem(), selector=sel)
        l.add_xpath('fullname', "td/strong/text()")
        l.add_xpath('fullname', "td/p/strong/text()")

        l.add_xpath('email', "td/a/text()")
        l.add_xpath('email', "td/p/a/text()")

        return l.load_item()
