from sqlalchemy import create_engine

engine = create_engine('sqlite:///example.db', echo=True)

#orm초기화
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

session_maker = sessionmaker(bind=engine)
session = session_maker()

Base = declarative_base()

#테이블정의
from sqlalchemy import Column, Integer, String

class Demo(Base):
    __tablename__ = 'demos'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

#metadata->데이터 베이스 반영

Base.metadata.create_all(engine)
#세션에 객체추가
##객체생성
demo = Demo(name="hello", password="world")
session.add(demo)
# 생성한 객체 조회
find_demos = session.query(Demo).filter_by(name="hello").all()

for demo in find_demos:
    print(demo.name)
#세션커밋
session.commit()