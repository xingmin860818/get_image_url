from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from get_img_url import get_img_url2

db = create_engine('mysql://recp:123456@192.168.1.124')
db.execute('use conference')

Base = declarative_base()

class User(Base):
	__tablename__ = 'urls'
	id = Column(Integer,primary_key=True)
	websit = Column(String(49))
	img_url = Column(String(40))

Base.metadata.create_all(db)

url = 'http://www.sina.com'
img_urls = get_img_url2(url)
Session = sessionmaker(bind=db)
session = Session()
for i in img_urls:
	user = User(websit=url,img_url=i)
	session.add(user)
	session.commit()
session.close()
