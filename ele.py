import scrapy
from items import PersonItem


class eleSpider(scrapy.Spider):
    name = 'ele grad students'
    start_urls = ['http://www.ee.princeton.edu/people/grad-students']

    def parse(self, response):
        for block in response.xpath("//*[contains(concat(' ', @class, ' '), ' views-row ')]"):
            yield self.parse_person(block)

    def parse_person(self, sel):
        item = PersonItem()

        # name
        item['fullname'] = sel.xpath(
            "div[contains(@class, 'views-field-title')]/span/a/text()").extract_first()

        # office
        item['office_address'] = sel.xpath(
            "div[contains(@class, 'views-field-field-office-number')]/div/text()"
        ).extract_first()

        # phone
        item['phone'] = sel.xpath(
            "div[contains(@class, 'views-field-field-office-phone')]/div/text()"
        ).extract_first()

        # email
        item['email'] = sel.xpath(
            "div[contains(@class, 'views-field-field-email')]/div/a/text()"
        ).extract_first()

        # advisor
        item['advisor'] = sel.xpath(
            "div[contains(@class, 'views-field-field-academic-advisor')]/div/a/text()"
        ).extract_first()

        if item['advisor'] is None:
            item['advisor'] = sel.xpath(
                "div[contains(@class, 'views-field-field-academic-advisor')]/div/text()"
            ).extract_first()

        # personal link
        # TODO: None?
        return item
