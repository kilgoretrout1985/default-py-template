# uncomment this to use async tests in pytest

# import asyncio
# from typing import Generator

# import pytest
# import pytest_asyncio


# # needed for fixtures more global than function-scope
# # https://github.com/pytest-dev/pytest-asyncio#async-fixtures
# # https://medium.com/@estretyakov/the-ultimate-async-setup-fastapi-sqlmodel-alembic-pytest-ae5cdcfed3d4
# @pytest.fixture(scope="session")
# def event_loop(request) -> Generator:  # type: ignore[type-arg]
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()
