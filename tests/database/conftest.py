""" Common test set up for database tests. """

import pytest

from database import Database
from database.models import setup_database


@pytest.fixture(name="database")
def create_database(config):
    """Create an in memory database for tests."""

    database = Database(config.DATABASE_CONFIG)

    setup_database(database.engine)

    return database


@pytest.fixture(name="session")
def create_database_session(database: Database):
    """Create a session connected to the database."""

    with database.session as session:
        yield session
