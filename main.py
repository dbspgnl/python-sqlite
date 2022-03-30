import sqlite3

from sqlalchemy import create_engine, String
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

print("hello world")
print(sqlite3.version)
print(sqlite3.sqlite_version)

# DB 생성 (오토 커밋)
# conn = sqlite3.connect("test.db", isolation_level=None)
# 커서 획득
# c = conn.cursor()
# # 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
# c.execute("CREATE TABLE IF NOT EXISTS table1 \
#     (id integer PRIMARY KEY, name text, birthday text)")

conn_string = 'sqlite:///test.db'
engine = create_engine(conn_string, echo=True)
# Base = declarative_base()
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
# =================== 테이블 정의 ==================
class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    date = Column(Integer)
    rank = Column(Integer)
    movieNm = Column(String(30))
    movieCd = Column(Integer)
    salesAmt = Column(Integer)
    audiCnt = Column(Integer)

# =================== 생성 처리 ==================
Movie.__table__.create(bind=engine, checkfirst=True)
movie_list=Movie(date=20190625, rank=1, movieNm='toystory', movieCd=12345, salesAmt=1234545123, audiCnt=342)
session.add(movie_list)
session.commit()

# =================== 드롭 처리 ==================
# Movie.__table__.drop(engine)