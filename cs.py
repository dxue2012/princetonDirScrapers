import scrapy
# from scrapy.selector import Selector
from items import PersonItem


class csSpider(scrapy.Spider):
    name = 'cs grad students'
    start_urls = ['https://www.cs.princeton.edu/people/grad']

    def parse(self, response):
        for block in response.css('.person-details'):
            personItem = PersonItem()

            # name
            personItem['fullname'] = block.xpath("h2[@class='person-name']/text()").extract_first().strip()
            if len(personItem['fullname']) == 0:
                personItem['fullname'] = block.xpath("h2[@class='person-name']/a/text()").extract_first().strip()

            # link to personal page
            personItem['link'] = block.xpath("div[@class='person-links']/a/@href").extract_first()

            # email
            email_xpath = block.xpath(
                "div[@class='person-address']/span/\
                span[@class='glyphicon glyphicon-envelope']/../text()")
            if len(email_xpath) > 1:
                email_text = email_xpath[1].extract()
                personItem['email'] = email_text.split()[0] + \
                    "@cs.princeton.edu"
            else:
                personItem['email'] = None

            # office address
            office_addr_xpath = block.xpath(
                "div[@class='person-address']/span/\
                span[@class='glyphicon glyphicon-briefcase']/../text()")
            if len(office_addr_xpath) > 1:
                personItem['office_address'] = office_addr_xpath[
                    1].extract().strip()
            else:
                personItem['office_address'] = None

            # phone
            phone_xpath = block.xpath(
                "div[@class='person-address']/span/\
                span[@class='glyphicon glyphicon-earphone']/../text()")
            if len(phone_xpath) > 1:
                personItem['phone'] = phone_xpath[1].extract().strip()
            else:
                personItem['phone'] = None

            yield personItem
