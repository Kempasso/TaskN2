from sqlalchemy import Column, Integer, ForeignKey, LargeBinary, Unicode

from tables import BaseModel


class Files(BaseModel):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True)
    file_uuid = Column(Unicode(255))
    file_data = Column(LargeBinary)
    user_id = Column(ForeignKey('user.id'))
