import scrapy
from scrapy.loader import ItemLoader

class dieselAAA(scrapy.Spider):
	name = "diesel_AAA"
	start_urls = ['https://gasprices.aaa.com/state-gas-price-averages/']

	def parse(self, response):
		SET_SELECTOR = '.sortable-table'
		for dieselAAA in response.css(SET_SELECTOR):
			STATE_SELECTOR = './/td/a/text()'
			DIESEL_SELECTOR = './/td[@class="diesel"]/text()'
			order = [dieselAAA.xpath(STATE_SELECTOR).extract(), dieselAAA.xpath(DIESEL_SELECTOR).extract()]
			Request = list(zip(*order))
			yield {
				'Info': order
