from typing import Literal
from litestar import Controller, Request, get
from pydantic import BaseModel


class Health(BaseModel):
    status: Literal["ok", "not ok"]


class GeneralController(Controller):
    path = "/"

    @get(path="/", include_in_schema=False)
    async def home(request: Request) -> str:
        return "Hello World."

    @get(path="/health", tags=["General"])
    async def health(request: Request) -> Health:
        return Health(status="ok")
