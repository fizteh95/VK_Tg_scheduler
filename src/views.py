from aiohttp import web

from models import User
from src.database import async_session


class Test(web.View):
    async def get(self):
        print("ha")
        return web.json_response({"testing": "ok"})


class AddUser(web.View):
    async def post(self):
        async with async_session() as session:
            data = await self.request.json()
            print(data)
            username = data["username"]
            new_user = User(user=username, groups=None)
            session.add(new_user)
            await session.commit()
        return web.json_response({"result": True})
