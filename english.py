import urlparse
import scrapy
# from scrapy.selector import Selector
from items import PersonItem


class englishSpider(scrapy.Spider):
    name = 'english grad students'
    start_urls = ['https://english.princeton.edu/people/graduate-students']

    def parse(self, response):
        for sel in response.xpath("//span[@class='field-content']/div[@class='staff-contact']"):
            yield self.parsePerson(response, sel)

    def parsePerson(self, response, sel):
        personItem = PersonItem()

        personItem['fullname'] = sel.css(
            ".name").xpath("a/text()").extract_first()
        office = sel.xpath("span[@class='office']/text()").extract_first()
        if office is not None and len(office.strip()) > 0:
            personItem['office_address'] = office.strip()
        else:
            personItem['office_address'] = None

        personItem['phone'] = sel.xpath(
            "span[@class='phone']/text()").extract_first()

        relative_link = sel.xpath("span[@class='name']/a/@href").extract_first()
        url_profile_link = urlparse.urljoin(response.url, relative_link.strip())

        return scrapy.Request(url_profile_link, meta={
            'item': personItem
        }, callback=self.parseBio)

    def parseBio(self, response):
        personItem = response.request.meta['item']

        # bio
        bio = response.xpath("//div[@class='field-items']/div/p/text()").extract()
        personItem['bio'] = '\n'.join(bio)
        return personItem
