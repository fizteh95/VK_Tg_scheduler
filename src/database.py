from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


class DB:
    engine = None
    async_session = None
    pg_address = None

    @classmethod
    def create_engine_and_session(cls):
        cls.engine = create_async_engine(
            cls.pg_address,
            echo=False,  # False чтобы в логах не было запросов
        )
        cls.async_session = sessionmaker(
            cls.engine, expire_on_commit=False, class_=AsyncSession
        )
