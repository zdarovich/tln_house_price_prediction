import scrapy
from scrapy.loader import ItemLoader
from city24.items import PropertyItem
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from city24.Util import has_printable_characters
from twisted.internet import reactor


class City24Spider(scrapy.Spider):
    name = "city24"

    def start_requests(self):
        start_urls = ['https://city24.postimees.ee/et/nimekiri/muuk/korter']
        yield scrapy.Request(url=start_urls[0], callback=self.parse)

    def parse(self, response):
        link_list = response.xpath('//span[@class="address-wrap"]/a[@class="addressLink"]/@href').extract()
        for house_page in link_list:
            if house_page is not None:
                self.log("House page link {}".format(house_page))
                yield scrapy.Request(house_page, callback=self.parse_property)

        next_page = response.xpath('///a[@class="next"]/@href').extract_first()
        if next_page is not None:
            self.log("Next page link {}".format(next_page))
            yield response.follow(next_page, self.parse)

    def parse_property(self, response):
        dictionary = {}
        general_dict = self.parse_property_general(response)
        tables_dict = self.parse_property_tables_by_row(response)
        broker_dict = self.parse_property_broker(response)
        dictionary.update(general_dict)
        dictionary.update(tables_dict)
        dictionary.update(broker_dict)
        yield dictionary

    def parse_property_tables(self, response):
        tables_selectors = response.xpath('//table[@class="itemFacts clear zebra"]')
        table_keys = []
        table_values = []
        for table in tables_selectors:
            table_keys_raw = table.css('tr th span::text').extract()
            table_keys = table_keys + [key[:-1] for key in table_keys_raw]
            table_values_raw = table.css('tr td span::text').extract()
            table_values = table_values + [value for value in table_values_raw if has_printable_characters(value)]
        dictionary = dict(zip(table_keys, table_values))
        self.log(dictionary)
        return dictionary

    def parse_property_tables_by_row(self, response):
        tables_rows = response.xpath('//table[@class="itemFacts clear zebra"]/tr')
        dictionary = {}
        for row in tables_rows:
            table_key = row.css('th span::text').extract()
            table_value = row.css('td span::text').extract()
            if table_key and table_value:
                dictionary[table_key[0]] = table_value[0]

        self.log(dictionary)
        return dictionary

    def parse_property_general(self, response):
        name = response.xpath('//div[@class="itemTitle"]/div[@class="itemTitleColumnLeft"]/h1/text()').extract()
        first_image_link = response.xpath('//a[@id="firstImageLink"]/img/@src').extract()
        description = response.xpath('//pre[@class="property_description clear"]/text()').extract()
        self.log(name)
        return {"address": name, "first_image_link": first_image_link, "description": description}

    def parse_property_broker(self, response):
        broker_name = response.xpath('//div[@class="contact_details"]/ul[@class="contactDetails"]/li[1]/h3/text()').extract()
        broker_company = response.xpath('//div[@class="contact_details"]/ul[@class="contactDetails"]/li[2]/text()').extract()
        self.log(broker_name)
        return {"broker_name": broker_name, "broker_company": broker_company}


def run():

    settings = get_project_settings()
    settings.set('FEED_FORMAT', 'CSV')

    configure_logging()
    runner = CrawlerRunner(settings)
    runner.crawl(City24Spider)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()  # the script will block here until all crawling jobs are finished


if __name__ == '__main__':
    run()







