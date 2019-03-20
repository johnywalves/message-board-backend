from sqlalchemy import Table, Column, Integer, String

from connection import Base, engine


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __repr__(self):
        return "<User (user='%d')>" % (self.user)
