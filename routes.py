from src.views import AddGroup, AddUser, Test

routes = [
    ("GET", "/test", Test, "test"),
    ("POST", "/add_user", AddUser, "add_user"),
    ("POST", "/add_group", AddGroup, "add_group"),
]
