# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertyItem(scrapy.Item):
    # property
    address = scrapy.Field()
    first_image_link = scrapy.Field()
    description = scrapy.Field()

    # main
    property_type = scrapy.Field()
    price = scrapy.Field()
    total_area = scrapy.Field()
    build_year = scrapy.Field()
    direct_link = scrapy.Field()
    price_per_sqrt_meter = scrapy.Field()

    # general
    cadastrial_number = scrapy.Field()
    has_lift = scrapy.Field()
    heating_system = scrapy.Field()
    energy_mark = scrapy.Field()
    ownership = scrapy.Field()
    condition = scrapy.Field()
    municipal_engineering = scrapy.Field()

    # area
    total_rooms = scrapy.Field()
    sleeping_rooms = scrapy.Field()
    wc_rooms = scrapy.Field()
    sqrt_meters = scrapy.Field()
    floors = scrapy.Field()
    extra_rooms = scrapy.Field()

    # extra
    communication = scrapy.Field()
    security = scrapy.Field()
    sanitary = scrapy.Field()

    # seller
    house_broker = scrapy.Field()
    broker_company = scrapy.Field()

    # meta
    last_updated = scrapy.Field()

