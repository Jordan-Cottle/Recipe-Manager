""" Models for tracking recipes. """

from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import Mapper, relationship

from database.models import Base, Ingredient, Step


class Recipe(Base):
    """Meta data for a recipe.

    Recipes are defined as a collection of ingredients combined with a collection
    of instructions.

    Relationships between instructions and ingredients will contain the bulk of
    the data for a recipe. This table itself should only contain meta data about
    the recipe.
    """

    __tablename__ = "Recipe"

    recipe_id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)
    author: str = Column(String, nullable=False)

    def add_ingredient(
        self, ingredient: Ingredient, amount: float, units: str, optional: bool = False
    ):
        """Register an ingredient as part of this recipe."""

        return RecipeIngredient(
            ingredient=ingredient,
            recipe=self,
            amount=amount,
            units=units,
            optional=optional,
        )

    def add_step(self, step: Step, optional: bool = False):
        """Add a step to this recpie."""

        return RecipeStep(
            step=step,
            recipe=self,
            optional=optional,
        )

    def __str__(self) -> str:
        return f'Recipe "{self.name}" by {self.author}'

    def __repr__(self) -> str:
        return (
            "Recipe("
            f"recipe_id={self.recipe_id}, "
            f"name='{self.name}', "
            f"description='{self.description}', "
            f"author='{self.author}')"
        )


class RecipeIngredient(Base):
    """Table to track which ingredients are in a recipe."""

    __tablename__ = "RecipeIngredient"

    ingredient_id: int = Column(
        Integer, ForeignKey(Ingredient.ingredient_id), primary_key=True
    )
    recipe_id: int = Column(Integer, ForeignKey(Recipe.recipe_id), primary_key=True)

    amount: float = Column(Float, nullable=False)
    units: str = Column(String, nullable=False)
    optional: bool = Column(Boolean, default=False, nullable=False)

    ingredient = relationship(Ingredient)
    recipe = relationship(Recipe, backref="ingredients")

    def __init__(
        self,
        recipe: Recipe,
        ingredient: Ingredient,
        amount: float,
        units: str,
        optional: bool = False,
    ) -> None:

        self.recipe = recipe
        self.ingredient = ingredient
        self.amount = amount
        self.units = units
        self.optional = optional

    def __getattr__(self, name):
        mapper: Mapper = inspect(Ingredient)

        if name in mapper.attrs:
            return getattr(self.ingredient, name)

        return super().__getattribute__(name)

    def __repr__(self) -> str:
        return f"RecipeIngredient(ingredient={self.ingredient}, recipe={self.recipe})"


class RecipeStep(Base):
    """Table to track steps in a recipe."""

    __tablename__ = "RecipeStep"

    step_id: int = Column(Integer, ForeignKey(Step.step_id), primary_key=True)
    recipe_id: int = Column(Integer, ForeignKey(Recipe.recipe_id), primary_key=True)

    sequence_number: int = Column(Integer, nullable=False)
    optional: bool = Column(Boolean, default=False, nullable=False)

    step = relationship(Step)
    recipe = relationship(Recipe, backref="steps")

    def __init__(self, recipe: Recipe, step: Step, optional: bool = False) -> None:
        self.sequence_number = len(recipe.steps) + 1
        self.optional = optional

        self.recipe = recipe
        self.step = step

    def __getattr__(self, name):
        mapper: Mapper = inspect(Step)

        if name in mapper.attrs:
            return getattr(self.step, name)

        return super().__getattribute__(name)
