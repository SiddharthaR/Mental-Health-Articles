from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

Base = declarative_base()

def db_connect():
	return create_engine(URL(**settings.DATABASE))

def create_articles_table():
	Base.metadata.create_all(engine)

class Articles(Base):
	__tablename__ = 'articles'
	id = Column(Integer, primary_key=true)
	title = Column('title', String)
	teaser =  Column('teaser', String)
	link = Column('link', String)
	date = Column('date', String) # Maybe this should be another type but date is currently inconsistent so leaving as string until fixed
	author = Column('author', String)
	source = Column('source', String)