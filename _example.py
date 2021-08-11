# import asyncio
# import random
# from contextvars import ContextVar
#
# from aiohttp import web
#
# request_id: ContextVar[int] = ContextVar("request_id")
#
#
# async def perform_external_request():
#     # Cозданная задача всегда будет иметь контекст родительской
#     await asyncio.sleep(5)
#     print("request_id =", request_id.get())
#     # Здесь выполняем запрос к стороннему сервису
#
#
# async def test_handler(request):
#     r = random.randint(1, 100)
#     request_id.set(r)
#     asyncio.ensure_future(perform_external_request())
#     # await perform_external_request()
#     return web.Response(text="ok")
#
#
# async def test():
#     while True:
#         await asyncio.sleep(3)
#         print("its working!")
#
#
# app = web.Application()
# app.router.add_route("GET", "/test", test_handler)
# asyncio.ensure_future(test())
#
# web.run_app(app, port=8080)


class Test:
    a = 1

    def __init__(self):
        self.b = 3


Test.a = 4

t1 = Test()
t2 = Test()
print(t1.a)
print(t1.b)
print("****")
print(t2.a)
print(t2.b)
print("****")
print("****")
t1.b = 7
print(t1.a)
print(t1.b)
print("****")
print(t2.a)
print(t2.b)
print("****")
print("****")
# t1.a = 8
# Test.a = 8
print(t1.a)
print(t1.b)
print("****")
print(t2.a)
print(t2.b)
print("****")
t3 = Test()
print(t3.a)
