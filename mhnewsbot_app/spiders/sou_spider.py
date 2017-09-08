from scrapy.spiders import Spider
from scrapy import Request
from mhnewsbot_app.items import SOUItem
import string

mh_search_terms = ["DEPRESS", "MENTAL HEALTH", "EMOTIONAL HEALTH", "MENTAL DISORDER", "DIGITAL MEDICINE", "ANXI", "PSYCH", "THERAPY", "THERAPIST"]
tbl = string.maketrans('-', ' ') #To protect against cases where the article has hyphens or other special characters

#articles = {'title': [], 'teaser': [], 'link': [], 'date': [], 'author': [], 'source': []}

# Create list of urls for scrapy to crawl. Hardcoded to follow Science of us format. 
def url_lister():
	url_list = []
	article_count = 0
	while article_count < 150: 											# Arbitrary limit, this goes up to the thousands
		url = 'http://nymag.com/scienceofus/?start=%s' %article_count
		url_list.append(url)
		article_count += 50
	return url_list

class SOUSpider(Spider):
	name = 'scienceofus'
	start_urls = url_lister()

	def parse(self, response):
		for article in response.xpath('//ul[@class="newsfeed-article-list"]'):
			title = article.xpath('.//li[contains(@class, "newsfeed-article")]/div[@class="headline-wrapper"]/a[@class="headline-link"]/h3[@class="headline"]').extract()
	        for i in title:
	        	for search_term in mh_search_terms:
		        	if search_term in i.upper().strip():
						article_item = {}
						article_item['title'] = article.xpath('.//li[contains(@class, "newsfeed-article")]/div[@class="headline-wrapper"]/a[@class="headline-link"]/h3[@class="headline"]/text()').extract()[title.index(i)]
						article_item['teaser'] = article.xpath('.//li[contains(@class, "newsfeed-article")]/p[@class = "teaser"]/text()').extract()[title.index(i)]
						article_item['link'] = article.xpath('.//li[contains(@class, "newsfeed-article")]/a[@class = "read-more"]/@href').extract()[title.index(i)]
						article_item['date'] = article.xpath('.//li[contains(@class, "newsfeed-article")]/div[@class="headline-wrapper"]/div[@class="headline-above"]/time/text()').extract()[title.index(i)]
						article_item['author'] = article.xpath('.//li[contains(@class, "newsfeed-article")]/span[@class="by-authors"]/span/span[@class="author"]/text()').extract()[title.index(i)]
						article_item['source'] ='Science Of Us'
						yield article_item