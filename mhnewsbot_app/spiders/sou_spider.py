from scrapy.spiders import Spider
from scrapy import Request
from mhnewsbot_app.items import SOUItem
import string

mh_search_terms = ["DEPRESS", "MENTAL HEALTH", "EMOTIONAL HEALTH", "MENTAL DISORDER", "DIGITAL MEDICINE", "ANXI", "PSYCH", "THERAPY", "THERAPIST"]
tbl = string.maketrans('-', ' ') #To protect against cases where the article has hyphens or other special characters

articles = {'title': [], 'teaser': [], 'link': [], 'date': [], 'author': [], 'source': []}

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
		        	if search_term in i.upper().strip():
						articles['title'].append(article.xpath('.//li[contains(@class, "newsfeed-article")]/div[@class="headline-wrapper"]/a[@class="headline-link"]/h3[@class="headline"]/text()').extract()[title.index(i)])
						articles['teaser'].append(article.xpath('.//li[contains(@class, "newsfeed-article")]/p[@class = "teaser"]/text()').extract()[title.index(i)]) #currently broken, sometimes indexes article right before the one in question
						articles['link'].append(article.xpath('.//li[contains(@class, "newsfeed-article")]/a[@class = "read-more"]/@href').extract()[title.index(i)])
						articles['date'].append(article.xpath('.//li[contains(@class, "newsfeed-article")]/div[@class="headline-wrapper"]/div[@class="headline-above"]/time/text()').extract()[title.index(i)])
						articles['author'].append(article.xpath('.//li[contains(@class, "newsfeed-article")]/span[@class="by-authors"]/span/span[@class="author"]/text()').extract()[title.index(i)])
						articles['source'].append('Science Of Us')
		return articles