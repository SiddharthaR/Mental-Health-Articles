from scrapy.spiders import Spider
from scrapy import Request
from mhnewsbot_app.items import SOUItem

class SOUSpider(Spider):
	name = 'scienceofus'
	start_urls = [
    	'http://nymag.com/scienceofus/',
	]

	def parse(self, response):
		for article in response.xpath('//ul[@class="newsfeed-article-list"]'):
			return {
	        'title': article.xpath('.//li[contains(@class, "newsfeed-article")]/div[@class="headline-wrapper"]/a[@class="headline-link"]/h3[@class="headline"]/text()').extract()
	        }