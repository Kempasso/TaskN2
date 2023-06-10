from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship

from tables import BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    login = Column(Unicode(255), unique=True)
    uuid = Column(Unicode(255))
    files = relationship("Files", lazy='subquery', backref='files')


