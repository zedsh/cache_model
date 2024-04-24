from typing import Any, AsyncGenerator  # noqa: UP035

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings


engine = create_async_engine(settings.DATABASE_URL, poolclass=NullPool)

async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, Any]:
    """Dependency for getting async session"""
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass
