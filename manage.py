import asyncio

from aiohttp import web
import click


@click.group()
def cli():
    pass


@cli.command()
def run():
    click.echo('run run run!')
    app = web.Application()
    app.router.add_route('GET', '/test', test_handler)
    asyncio.ensure_future(test())
    web.run_app(app, port=8080)


@cli.command()
def test():
    click.echo('testing app!')


if __name__ == '__main__':
    cli()
