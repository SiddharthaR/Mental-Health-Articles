from scrapy.spiders import Spider
from scrapy import Request
from mhnewsbot_app.items import SOUItem
import sys

mh_search_terms = ["Depression", "Grooming"]

articles = {'title': [], 'teaser': [], 'link': [], 'date': [], 'author': []}

class SOUSpider(Spider):
	name = 'scienceofus'
	start_urls = [
    	'http://nymag.com/scienceofus/',
	]

	def parse(self, response):
		for article in response.xpath('//ul[@class="newsfeed-article-list"]'):
			title = article.xpath('.//li[contains(@class, "newsfeed-article")]/div[@class="headline-wrapper"]/a[@class="headline-link"]/h3[@class="headline"]/text()').extract()
	        for i in title:
	        	for search_term in mh_search_terms:
		        	if search_term in i:
						articles['title'].append(article.xpath('.//li[contains(@class, "newsfeed-article")]/div[@class="headline-wrapper"]/a[@class="headline-link"]/h3[@class="headline"]/text()').extract()[title.index(i)])
						articles['teaser'].append(article.xpath('.//li[contains(@class, "newsfeed-article")]/p[@class = "teaser"]/text()').extract()[title.index(i)])
						articles['link'].append(article.xpath('.//li[contains(@class, "newsfeed-article")]/a/@href').extract()[title.index(i)])
						articles['date'].append(article.xpath('.//li[contains(@class, "newsfeed-article")]/div[@class="headline-wrapper"]/div[@class="headline-above"]/time/text()').extract()[title.index(i)])
						articles['author'].append(article.xpath('.//li[contains(@class, "newsfeed-article")]/span[@class="by-authors"]/span/span[@class="author"]/text()').extract()[title.index(i)])
		return articles