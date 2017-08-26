from sqlalchemy.orm import sessionmaker
from models import Articles, db_connect, create_articles_table

class ArticlesPipeline(object):
	def __init__(self):
		engine = db_connect()
		create_articles_table(engine)
		self.Session = sessionmaker(bind=engine) # Establishes all conversations with the database and represents a staging zone for objects loaded into session object until committed

	def process_item(self, item, spider):
		"""Save deals in the database.
		This method is called for every item pipeline component
		"""
		session = self.Session()
		article = Articles(**item)

		try:
			session.add(article)
			session.commit()
		except :
			session.rollback()
			raise
		finally:
			session.close()

		return item