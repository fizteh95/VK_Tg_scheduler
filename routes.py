from src.views import (
    AddConnection,
    AddGroup,
    AddUser,
    AllConnections,
    AllGroups,
    AllUsers,
    Healthcheck,
    Test,
    UserGroups,
)

routes = [
    ("GET", "/test", Test, "test"),
    ("POST", "/add_user", AddUser, "add_user"),
    ("POST", "/add_group", AddGroup, "add_group"),
    ("POST", "/add_connection", AddConnection, "add_connection"),
    ("GET", "/all_connections", AllConnections, "all_connections"),
    ("GET", "/all_users", AllUsers, "all_users"),
    ("GET", "/all_groups", AllGroups, "all_groups"),
    ("POST", "/user_groups", UserGroups, "user_groups"),
    ("GET", "/healthcheck", Healthcheck, "healthcheck"),
]
