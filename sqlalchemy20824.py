from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#reference: https://docs.sqlalchemy.org/en/14/orm/session_api.html#session-and-sessionmaker
engine = create_engine('sqlite:///example.db', echo=True)
Session = sessionmaker(engine)
Base = declarative_base()

#테이블 생성
from sqlalchemy import Column, Integer, String

class Demo(Base):
    __tablename__ = 'demos'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    
Base.metadata.create_all(engine)
#트랜잭션 테스트
session = Session()

user1 = Demo(name="user1", password="password")
user2 = Demo(name="user2", password="password")
user3 = Demo(name="user3", password="password")

session.add(user1)
session.add(user2)
session.add(user3)

session.query(Demo).all()

result = session.query(Demo).all()

session.commit()
session.close()