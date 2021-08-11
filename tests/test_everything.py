from src.utilities import mult_two_numbers

import pytest


from src.server import Server


@pytest.fixture
def cli(loop, aiohttp_client):
    app = Server(test=True).app
    return loop.run_until_complete(aiohttp_client(app))


async def test_all_user(cli):
    resp = await cli.get("/all_users")
    assert resp.status == 200


def test_mult_two_numbers():
    result = mult_two_numbers(2, 3)
    assert result == 6
