"""Test module to ensure recipe tables are constructed and linked properly."""

from typing import List


from sqlalchemy.orm import Session
import pytest

from database.models import Ingredient, Step, RecipeIngredient, RecipeStep, Recipe


@pytest.fixture(name="ingredients")
def create_test_ingredients(session: Session) -> List[Ingredient]:
    """Set up test ingredient data."""

    ingredients = [
        Ingredient(name="spam", description="Test ingredient #1"),
        Ingredient(name="eggs", description="Test ingredient #2"),
    ]

    session.add_all(ingredients)
    session.commit()

    return ingredients


@pytest.fixture(name="steps")
def create_test_steps(session: Session) -> List[Step]:

    steps = [
        Step(short_description="start test"),
        Step(
            short_description="end test",
            long_description="This should be the last step in a test recipe",
        ),
    ]
    session.add_all(steps)
    session.commit()

    return steps


def test_recipe(session, ingredients: List[Ingredient], steps: List[Step]):
    """Ensure a recipe with simple steps and ingredients can be created."""

    recipe = Recipe(
        name="Test recipe", description="A simple test recipe", author="Test User"
    )

    ingredient_amount = 1
    ingredient_units = "count"

    for ingredient in ingredients:
        recipe.add_ingredient(ingredient, ingredient_amount, ingredient_units)

    for step in steps:
        recipe.add_step(step)

    session.add(recipe)
    session.commit()

    recipe_steps = session.query(RecipeStep).all()
    assert len(recipe_steps) == len(steps)

    recipe_ingredients = session.query(RecipeIngredient).all()
    assert len(recipe_ingredients) == len(ingredients)

    for recipe_ingredient in recipe.ingredients:
        assert recipe_ingredient.amount == ingredient_amount
        assert recipe_ingredient.units == ingredient_units

    for i, step in enumerate(recipe.steps):
        assert step.sequence_number == i + 1
        assert step.short_description == steps[i].short_description
        assert step.long_description == steps[i].long_description
