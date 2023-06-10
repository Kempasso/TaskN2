from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()



from .user import User
from .files import Files

