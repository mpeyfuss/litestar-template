import os
import sys
import pytest
from piccolo.utils.warnings import colored_warning
from collections.abc import Generator
from litestar import Litestar
from litestar.testing import TestClient

from app import app


def pytest_configure(*args):
    if os.environ.get("PICCOLO_TEST_RUNNER") != "True":
        colored_warning(
            "\n\n"
            "We recommend running Piccolo tests using the "
            "`piccolo tester run` command, which wraps Pytest, and makes "
            "sure the test database is being used. "
            "To stop this warning, modify conftest.py."
            "\n\n"
        )
        sys.exit(1)


@pytest.fixture(scope="function")
def api_client() -> Generator[TestClient[Litestar]]:
    with TestClient(app=app) as client:
        yield client
