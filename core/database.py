from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv

load_dotenv('.env')

ENGINE_URL = getenv('POSTGRESQL_ENGINE')


class Base(DeclarativeBase):
    pass


engine = create_engine(ENGINE_URL)
session_maker = sessionmaker(engine)
