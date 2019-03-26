from sqlalchemy import Table, Column, Integer, String

from connection import Base, engine
from functions import toJSON, fromJSON


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __repr__(self):
        return "<User (user='%d')>" % (self.user)

    def toJson(self): return toJSON(self)

    def fromJson(self, data): return fromJSON(self, data)
