# import asyncio
import subprocess
import sys

import click
from aiohttp import web

from routes import routes
from src.database import engine


@click.group()
def cli():
    pass


async def startup_tasks(app):
    app["engine"] = engine


async def cleanup_tasks(app):
    await app["engine"].dispose()


@cli.command()
def run():
    click.echo("run run run!")
    app = web.Application()
    for route in routes:
        app.router.add_route(route[0], route[1], route[2], name=route[3])
    # asyncio.ensure_future(test())
    app.on_startup.append(startup_tasks)
    app.on_cleanup.append(cleanup_tasks)
    web.run_app(app, port=8080)


@cli.command()
@click.option("--coverage", is_flag=True)
def test(coverage):
    # if not settings.TESTING_MODE:
    #     raise ValueError('...')
    args = ["pytest", "tests"]
    if coverage:
        args.append("--cov=src")
    completed_process = subprocess.run(args)
    sys.exit(completed_process.returncode)
    click.echo("testing app!")


if __name__ == "__main__":
    cli()
