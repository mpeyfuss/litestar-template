from piccolo.engine.postgres import PostgresEngine
from piccolo.conf.apps import AppRegistry

# TODO: add dotenv database url stuff

DB = PostgresEngine(
    config={
        "database": "db",
        "user": "user",
        "password": "password",
        "host": "localhost",
        "port": 5440,
    }
)

APP_REGISTRY = AppRegistry(
    apps=[
        "general.piccolo_app",
        "piccolo_admin.piccolo_app",
        "users.piccolo_app",
    ]
)
