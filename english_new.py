import urlparse
import scrapy
from scrapy.selector import Selector
from items import PersonItem
from loaders import EnglishPersonLoader


class englishSpider(scrapy.Spider):
    name = 'english grad students'
    start_urls = ['https://english.princeton.edu/people/graduate-students']

    def parse(self, response):
        for sel in response.xpath("//span[@class='field-content']/div[@class='staff-contact']"):
            yield self.parsePerson(response, sel)

    def parsePerson(self, response, sel):
        l = EnglishPersonLoader(item=PersonItem(), selector=sel)
        l.add_xpath('fullname', "span[@class='name']/a/text()")
        l.add_xpath('email', "./a/text()")
        l.add_xpath('office_address', "span[@class='office']/text()")

        # fetch info from url on this page
        relative_link = sel.xpath("span[@class='name']/a/@href").extract_first()
        url_profile_link = urlparse.urljoin(response.url, relative_link.strip())

        return scrapy.Request(url_profile_link, meta={
            'loader': l
        }, callback=self.parseBio)

    def parseBio(self, response):
        l = response.request.meta['loader']
        l.selector = Selector(response)

        # bio
        l.add_xpath('bio', "//div[@class='field-items']/div/p/text()")
        return l.load_item()
