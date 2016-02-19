import scrapy
from items import PersonItem
from loaders import ElePersonLoader

class eleSpider(scrapy.Spider):
    name = 'ele grad students'
    start_urls = ['http://www.ee.princeton.edu/people/grad-students']

    def parse(self, response):
        for block in response.xpath("//*[contains(concat(' ', @class, ' '), ' views-row ')]"):
            yield self.parse_person(block)

    def parse_person(self, sel):
        l = ElePersonLoader(item=PersonItem(), selector=sel)

        l.add_xpath('fullname', "div[contains(@class, 'views-field-title')]/span/a/text()")
        l.add_xpath('office_address', "div[contains(@class, 'views-field-field-office-number')]/div/text()")
        l.add_xpath('phone', "div[contains(@class, 'views-field-field-office-phone')]/div/text()")
        l.add_xpath('email', "div[contains(@class, 'views-field-field-email')]/div/a/text()")
        l.add_xpath('advisor', "div[contains(@class, 'views-field-field-academic-advisor')]/div/a/text()")
        l.add_xpath('advisor', "div[contains(@class, 'views-field-field-academic-advisor')]/div/text()")
        return l.load_item()
    #
        # if item['advisor'] is None:
        #     item['advisor'] = sel.xpath(
        #         "div[contains(@class, 'views-field-field-academic-advisor')]/div/text()"
        #     ).extract_first()
        #
        # # personal link
        # # TODO: None?
        # return item
