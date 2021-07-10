""" Module for defining models related to recipe procedures. """

from sqlalchemy import Column, Integer, String

from database.models import Base


class Step(Base):
    """Model for tracking steps in a recipe."""

    __tablename__ = "Step"

    step_id: int = Column(Integer, primary_key=True)
    short_description: str = Column(String, nullable=False)
    long_description: str = Column(String, nullable=True)
