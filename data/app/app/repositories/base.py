from sqlalchemy import delete, insert, select, update

from app.database import async_session_maker


class BaseRepository:
    model = None

    @classmethod
    async def find_one_or_none(cls, filter_data: dict):  # noqa: ANN206, ANN102
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_data)
            result = await session.execute(query)

            return result.scalar_one_or_none()

    @classmethod
    async def add_with_returning_full_model(cls, fields_data: dict):  # noqa: ANN206, ANN102
        async with async_session_maker() as session:
            query = insert(cls.model).values(**fields_data).returning(cls.model)

            res = await session.execute(query)
            await session.commit()
            return res.scalar_one_or_none()

    @classmethod
    async def add(cls, **kwargs) -> None:  # noqa: ANN102, ANN003
        async with async_session_maker() as session:
            query = insert(cls.model).values(**kwargs)

            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, model_id, **kwargs):  # noqa: ANN206, ANN102, ANN003, ANN001
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == model_id).values(**kwargs)

            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, filter_data: dict):  # noqa: ANN206, ANN102
        async with async_session_maker() as session:
            query = delete(cls.model).where(**filter_data)
            await session.execute(query)
            await session.commit()
