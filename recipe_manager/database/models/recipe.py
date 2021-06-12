""" Models for tracking recipes. """

from sqlalchemy import Column, Integer, String

from database.models import Base


class Recipe(Base):
    """Meta data for a recipe.

    Recipes are defined as a collection of ingredients combined with a collection
    of instructions.

    Relationships between instructions and ingredients will contain the bulk of
    the data for a recipe. This table itself should only contain meta data about
    the recipe.
    """

    __tablename__ = "Recipe"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)
    author: str = Column(String, nullable=False)

    def __str__(self) -> str:
        return f"Recipe {self.name} by {self.author}"

    def __repr__(self) -> str:
        return (
            "Recipe("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"description='{self.description}', "
            f"author='{self.author}')"
        )
