import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://postgres:{POSTGRES_PASSWORD}@db:5432/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    with SessionLocal() as db:
        yield db
