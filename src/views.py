from aiohttp import web


class Test(web.View):
    async def get(self):
        print("ha")
        return web.json_response({"testing": "ok"})
