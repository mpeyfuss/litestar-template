from litestar import Litestar, asgi
from litestar.static_files import StaticFilesConfig
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin
from litestar.types import Receive, Scope, Send
from piccolo.engine import engine_finder
from piccolo_admin.endpoints import create_admin
from piccolo.apps.user.piccolo_app import APP_CONFIG as PICCOLO_USER_APP_CONFIG

from general.endpoints import GeneralController
from general.piccolo_app import APP_CONFIG as GENERAL_APP_CONFIG
from users.piccolo_app import APP_CONFIG as USERS_APP_CONFIG

# TODO: config based on prod vs dev


# mounting Piccolo Admin
@asgi("/admin/", is_mount=True)
async def admin(scope: "Scope", receive: "Receive", send: "Send") -> None:
    all_tables = [
        *PICCOLO_USER_APP_CONFIG.table_classes,
        *GENERAL_APP_CONFIG.table_classes,
        *USERS_APP_CONFIG.table_classes,
    ]
    await create_admin(tables=all_tables)(scope, receive, send)


async def open_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
    except Exception:
        print("Unable to connect to the database")


async def close_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
    except Exception:
        print("Unable to connect to the database")


app = Litestar(
    route_handlers=[admin, GeneralController],
    static_files_config=[
        StaticFilesConfig(directories=["static"], path="/static/"),
    ],
    on_startup=[open_database_connection_pool],
    on_shutdown=[close_database_connection_pool],
    openapi_config=OpenAPIConfig(
        title="API",
        version="1.0.0",
        description="My API docs",
        path="/docs",
        render_plugins=[ScalarRenderPlugin()],
    ),
)
