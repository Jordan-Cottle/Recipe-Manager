""" Setup the Sqlalchemy engine. """

from functools import cached_property

import sqlalchemy
from sqlalchemy import engine_from_config
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session


class DatabaseSession(Session):
    """Context manager extension of the sqlalchemy.orm.Session."""

    def __enter__(self):
        """Handle entering a with statement."""

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Handle exiting a with statement."""

        if exc_type is not None:
            self.rollback()
            self.close()
            return

        self.finalize()

    def finalize(self):
        """Attempt to finalize a transaction and close the session."""

        try:
            self.commit()
        except SQLAlchemyError:
            self.rollback()
        finally:
            self.close()


class Database:
    """Present the core sqlalchemy engine and sessions easily to the application."""

    def __init__(self, config) -> None:

        self.config = config

    @cached_property
    def engine(self) -> sqlalchemy.engine.Engine:
        """Setup and return a fresh sqlalchemy engine."""

        return engine_from_config(self.config, prefix="")

    @property
    def session(self) -> DatabaseSession:
        """Return a DatabaseSession bound to this database."""
        return DatabaseSession(bind=self.engine)
