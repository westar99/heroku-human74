from sqlalchemy import create_engine

# memory sqlite db
# reference: https://docs.sqlalchemy.org/en/14/core/engines.html#sqlite
db_url = 'sqlite://'#메모리를 사용하기에 데이터 베이스 불필요
engine = create_engine(db_url, echo=True)

## 테이블생성
conn = engine.connect()

# referemce: https://www.pythonsheets.com/notes/python-sqlalchemy.html
engine.execute('CREATE TABLE "EX1" ('
               'id INTEGER NOT NULL,'
               'name VARCHAR, '
               'PRIMARY KEY (id));')
## 테이블 삽입
engine.execute('INSERT INTO "EX1" '
              '(id, name) '
              'VALUES (1, "raw")')
## 테이터 조회
select_query = 'select * from EX1;'
result = conn.execute(select_query)
for _r in result:
   print(_r)