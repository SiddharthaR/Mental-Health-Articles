import scrapy

# Define container for scraped data
class SOUItem(scrapy.Item):
	title = scrapy.Field()
	teaser = scrapy.Field()
	link = scrapy.Field()
	date = scrapy.Field()
	author = scrapy.Field()
	source = scrapy.Field()