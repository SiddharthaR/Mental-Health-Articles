BOT_NAME = 'soubot'

SPIDER_MODULES = ['mhnewsbot_app.spiders']
NEWSPIDER_MODULE = 'mhnewsbot_app.spiders'

ROBOTSTXT_OBEY = True

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'sidr',
    'password': '',
    'database': 'scrape'
}