import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from models import A, B, Base


async def clear_db(engine):
    # удаляем и создаем таблицы (без записей)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_test_data(session):
    async with session.begin():
        session.add_all(
            [
                A(bs=[B(), B()], data="a1"),
                A(bs=[B()], data="a2"),
                A(bs=[B(), B()], data="a3"),
            ]
        )


async def async_main():
    engine = create_async_engine(
        "postgresql+asyncpg://postgres:postgres@localhost/postgres",
        echo=True,  # False чтобы в логах не было запросов
    )

    # await clear_db(engine)

    # expire_on_commit=False will prevent attributes from being expired
    # after commit.
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    async with async_session() as session:
        # await add_test_data(session)

        # # access attribute subsequent to commit; this is what
        # # expire_on_commit=False allows
        # print(a1.data)

        chpok = await session.execute(
            select(A).order_by(A.id).limit(10)
        )
        result = chpok.scalars().all()
        for r in result:
            print(r.data)

        # new_a = A(data='hophop3')
        # session.add(new_a)

        # result[1].data = 'abru'
        #await session.commit()

    # for AsyncEngine created in function scope, close and
    # clean-up pooled connections
    await engine.dispose()


asyncio.run(async_main())
