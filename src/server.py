from aiohttp import web
from .database import DB


async def startup_tasks(app):
    app["engine"] = DB.engine


async def cleanup_tasks(app):
    await app["engine"].dispose()


class Server:
    def __init__(self, test=False):
        self._app = web.Application()
        if not test:
            DB.pg_address = "postgresql+asyncpg://postgres:postgres@localhost/postgres"
        else:
            DB.pg_address = "postgresql+asyncpg://postgres:postgres@localhost/postgres"
        DB.create_engine_and_session()
        self.setup_routes()
        self.app.on_startup.append(startup_tasks)
        self.app.on_cleanup.append(cleanup_tasks)

    def setup_routes(self):
        from routes import routes

        for route in routes:
            self.app.router.add_route(route[0], route[1], route[2], name=route[3])

    @property
    def app(self):
        return self._app

    def run(self, host, port):
        print("start!")
        web.run_app(self.app, host=host, port=port)
