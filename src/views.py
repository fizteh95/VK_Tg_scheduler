from aiohttp import web
from sqlalchemy.future import select

from models import Connection, Group, User
from src.database import async_session


class Test(web.View):
    async def get(self):
        print("ha")
        return web.json_response({"testing": "ok"})


class AddUser(web.View):
    async def post(self):
        async with async_session() as session:
            data = await self.request.json()
            username = data["username"]
            new_user = User(user=username)
            session.add(new_user)
            await session.commit()
            chpok = await session.execute(select(User).order_by(User.id).limit(10))
            result = chpok.scalars().all()
            for r in result:
                print(r.user)
        return web.json_response({"result": True})


class AddGroup(web.View):
    async def post(self):
        async with async_session() as session:
            data = await self.request.json()
            vk_url = data["group_url"]
            new_group = Group(vk_url=vk_url)
            session.add(new_group)
            await session.commit()
            chpok = await session.execute(select(Group).order_by(Group.id).limit(10))
            result = chpok.scalars().all()
            for r in result:
                print(r.vk_url)
        return web.json_response({"result": True})


class AddConnection(web.View):
    async def post(self):
        async with async_session() as session:
            data = await self.request.json()
            username = data["username"]
            group_url = data["group_url"]

            user = await session.execute(
                select(User).where(User.c.user == username).limit(1)
            )
            group = await session.execute(
                select(Group).where(Group.c.vk_url == group_url).limit(1)
            )

            conn = Connection(user=user, group=group)
            session.add(conn)
            await session.commit()
            # chpok = await session.execute(select(User).order_by(User.id).limit(10))
            # result = chpok.scalars().all()
            # for r in result:
            #     print(r.user)
        return web.json_response({"result": True})
