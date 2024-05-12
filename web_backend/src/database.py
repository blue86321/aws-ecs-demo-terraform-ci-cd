import os

from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_NAME:
    raise ValueError("`DATABASE_NAME` is required in environment variables")
if not DATABASE_URL:
    raise ValueError("`DATABASE_URL` is required in environment variables")

SQLALCHEMY_DATABASE_URL = f"{DATABASE_URL}/{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_db():
    if not database_exists(engine.url):
        try:
            create_database(engine.url)
            print(f"Database '{DATABASE_NAME}' created successfully!")
        except exc.OperationalError as e:
            print(f"Error creating database '{DATABASE_NAME}': {e}")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
