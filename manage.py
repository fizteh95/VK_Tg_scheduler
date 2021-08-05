import asyncio
import sys
import subprocess

from aiohttp import web
import click

from routes import routes


@click.group()
def cli():
    pass


@cli.command()
def run():
    click.echo('run run run!')
    app = web.Application()
    for route in routes:
        app.router.add_route(route[0], route[1], route[2], name=route[3])
    # asyncio.ensure_future(test())
    web.run_app(app, port=8080)


@cli.command()
@click.option('--coverage', is_flag=True)
def test(coverage):
    # if not settings.TESTING_MODE:
    #     raise ValueError('...')
    args = ['pytest', 'tests']
    if coverage:
        args.append('--cov=src')
    completed_process = subprocess.run(args)
    sys.exit(completed_process.returncode)
    click.echo('testing app!')


if __name__ == '__main__':
    cli()
