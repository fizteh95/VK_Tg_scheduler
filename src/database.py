from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@localhost/postgres",
    echo=False,  # False чтобы в логах не было запросов
)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
