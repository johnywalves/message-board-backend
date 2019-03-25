from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import SingletonThreadPool

Base = declarative_base()
engine = create_engine('sqlite:///mydb.db', poolclass=SingletonThreadPool)
