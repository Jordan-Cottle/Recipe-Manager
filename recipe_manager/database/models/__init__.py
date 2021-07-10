""" Package for containing all of the database models. """
# pylint: disable=wrong-import-position

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def setup_database(engine):
    """Initialize all of the database models."""

    Base.metadata.create_all(engine)


from .ingredient import Ingredient
from .step import Step
from .recipe import Recipe, RecipeIngredient, RecipeStep
