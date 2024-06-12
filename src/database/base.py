from src import Config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    Config().bot["db_url"],
    pool_size=20, 
    max_overflow=0
)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()