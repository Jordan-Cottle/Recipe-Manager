""" Verify that the database can be connected to and basic operations work. """

import pytest
from database import Database
from database.models import setup_database, Recipe


@pytest.fixture(name="database")
def create_database(config):
    """Create an in memory database for tests."""

    return Database(config.DATABASE_CONFIG)


def test_database(database):
    """Test that database setup works independently from the flask app context."""

    with database.session as session:
        result = session.execute("select 'This is a test'").one()

        assert len(result) == 1, "Only one item should be returned."
        assert (
            result[0] == "This is a test"
        ), "The database should return the selected string"


def test_model_create(database):
    """Test models can be created and qu."""

    setup_database(database.engine)

    name = "Test Recipe"
    description = "Test recipe for testing"
    author = "Test User"

    recipe = Recipe(
        name=name,
        description=description,
        author=author,
    )

    with database.session as session:
        session.add(recipe)

    with database.session as session:
        recipes = session.query(Recipe).all()

        assert len(recipes) == 1, "Should have one recipe in database now"

        recipe = recipes[0]

        assert recipe.id == 1, "Recipes should have id auto assigned"
        assert recipe.name == name
        assert recipe.description == description
        assert recipe.author == author
