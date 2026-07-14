import os

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://postgres:{POSTGRES_PASSWORD}@db:5432/postgres"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
