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


class AllUsers(web.View):
    async def get(self):
        async with async_session() as session:
            chpok = await session.execute(select(User).order_by(User.id).limit(10))
            result = chpok.scalars().all()
            response = []
            for r in result:
                print(r.user)
            for r in result:
                response.append(r.user)
        return web.json_response(response)


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


class AllGroups(web.View):
    async def get(self):
        async with async_session() as session:
            chpok = await session.execute(select(Group).order_by(Group.id).limit(10))
            result = chpok.scalars().all()
            response = []
            for r in result:
                print(r.vk_url)
            for r in result:
                response.append(r.vk_url)
        return web.json_response(response)


class AddConnection(web.View):
    async def post(self):
        async with async_session() as session:
            data = await self.request.json()
            username = data["username"]
            group_url = data["group_url"]

            user = await session.execute(
                select(User).where(User.user == username).limit(1)
            )
            user = user.scalars().all()[0]
            group = await session.execute(
                select(Group).where(Group.vk_url == group_url).limit(1)
            )
            group = group.scalars().all()[0]

            conn = Connection(user=user, group=group)
            session.add(conn)
            await session.commit()
            chpok = await session.execute(
                select(Connection).order_by(Connection.id).limit(10)
            )
            result = chpok.scalars().all()
            for r in result:
                print(r.user.user, r.group.vk_url)
        return web.json_response({"result": True})


class AllConnections(web.View):
    async def get(self):
        print("all_connections")
        async with async_session() as session:
            chpok = await session.execute(
                select(Connection).order_by(Connection.id).limit(10)
            )
            result = chpok.scalars().all()
            response = []
            for r in result:
                print(r.user, r.group)
            for r in result:
                # print(r.user.user, r.group.vk_url)
                response.append([r.user.user, r.group.vk_url])
        return web.json_response(response)
