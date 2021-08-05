import aiohttp

from src.utilities import mult_two_numbers
# from src.views import Test
# from aiohttp import web
# from aiohttp.test_utils import make_mocked_request
# import pytest


def test_mult_two_numbers():
    result = mult_two_numbers(2, 3)
    assert result == 6


# @pytest.mark.asyncio
# async def test_test_view():
#     request = make_mocked_request('GET', '/test', headers={'token': 'x'})
#     view = Test(request)
#     response = await view.get()
#     print(response.status)
#     assert response == web.json_response({'testing': 'ok'})
