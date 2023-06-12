class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}


DB_URL = 'postgresql://postgres:12345678@db:5432/Task2'
BASE_FILE_URL = 'http://localhost:8000/record'