""" Package for containing all of the database models. """

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def setup_database(engine):
    """Initialize all of the database models."""

    Base.metadata.create_all(engine)


# pylint: disable=wrong-import-position
from .recipe import Recipe
