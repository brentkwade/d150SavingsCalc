# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DieselaaaItem(scrapy.Item):
    # define the fields for your item here like:
    # stateInfo = scrapy.Field()
    pass

class stateInfo(Item):
	STATE_SELECTOR = scrapy.Field()
	DIESEL_SELECTOR = scrapy.Field()
