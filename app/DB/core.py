from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from os import getenv
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base

load_dotenv()
url = getenv("db_url")
engine = create_async_engine(
    url=url,
    echo=True
)
session_maker = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False, autocommit=False)

Base = declarative_base()
