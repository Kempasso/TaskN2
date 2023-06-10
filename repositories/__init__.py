from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from repositories.files import FilesRepo
from repositories.user import UserRepo
from settings import DB_URL
from tables import BaseModel


engine = create_engine(DB_URL)
session_maker = sessionmaker(engine)


def create_tables():
    BaseModel.metadata.create_all(engine)


user_repository = UserRepo(engine=engine, session_maker=session_maker)
files_repository = FilesRepo(engine=engine, session_maker=session_maker)
