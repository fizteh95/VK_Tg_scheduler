from src.views import AddUser, Test

routes = [
    ("GET", "/test", Test, "test"),
    ("POST", "/add_user", AddUser, "add_user"),
]
