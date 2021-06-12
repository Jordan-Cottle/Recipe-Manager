""" Configuration settings for the flask application. """

# pylint: disable=too-few-public-methods

import os

# Objects used for flask config need ALL_CAPS attributes
# pylint: disable=invalid-name
class Config:
    """Common/default configuration values."""

    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(32))

    @property
    def DATABASE_CONFIG(self):
        """Get database configuration values."""
        return {"url": "sqlite:///recipes.db"}


class ProductionConfig(Config):
    """Production configuration settings."""


class DevelopmentConfig(Config):
    """Development configuration settings."""

    @property
    def DATABASE_CONFIG(self):
        config = super().DATABASE_CONFIG

        config["url"] = "sqlite:///dev-recipes.db"

        return config


class TestingConfig(DevelopmentConfig):
    """Testing configration settings."""

    TESTING = True

    @property
    def DATABASE_CONFIG(self):
        config = super().DATABASE_CONFIG

        config["url"] = "sqlite:///:memory:"

        return config


CONFIG_MAP = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "test": TestingConfig,
}


def get_config():
    """Get configuration object based on environment."""
    application_mode = os.getenv("APPLICATION_MODE", "dev")

    return CONFIG_MAP[application_mode]()
