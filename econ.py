import scrapy
from items import PersonItem

class econSpider(scrapy.Spider):
    name = 'econ grad students'
    start_urls = ['http://economics.princeton.edu/graduate-program/graduate-student-directory']

    def parse(self, response):
        for block in response.css('.field-item').xpath("//tbody/tr"):
            yield self.parse_person(block)

    def parse_person(self, sel):
        item = PersonItem()

        # name
        item['fullname'] = sel.xpath("td/strong/text()").extract_first()
        if item['fullname'] is None:
            item['fullname'] = sel.xpath("td/p/strong/text()").extract_first()

        if item['fullname'] is not None:
            item['fullname'] = ' '.join(item['fullname'].split()[0:-1])

        # email
        item['email'] = sel.xpath("td/a/text()").extract_first()
        if item['email'] is None:
            item['email'] = sel.xpath("td/p/a/text()").extract_first()
        return item
