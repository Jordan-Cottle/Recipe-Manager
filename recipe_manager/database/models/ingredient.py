""" Module for defining models related to ingredients. """

from sqlalchemy import Column, Integer, String

from database.models import Base


class Ingredient(Base):
    """Model for tracking ingredients."""

    __tablename__ = "Ingredient"

    ingredient_id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Ingredient(name={self.name}, description={self.description})"
