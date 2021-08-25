import subprocess
import sys

import click

from src.server import Server


@click.group()
def cli():
    pass


@cli.command()
def run():
    server = Server()
    server.run(host="localhost", port=8080)


@cli.command()
@click.option("--coverage", is_flag=True)
def test(coverage):
    args = ["pytest", "tests"]
    if coverage:
        args.append("--cov=src")
    completed_process = subprocess.run(args)
    sys.exit(completed_process.returncode)


if __name__ == "__main__":
    cli()
