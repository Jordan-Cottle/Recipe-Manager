""" Configuration settings for the flask application. """

# pylint: disable=too-few-public-methods

import os


class Config:
    """Common/default configuration values."""

    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(32))

    @property
    def DATABASE_CONFIG(self):
        return {"url": "sqlite:///recipes.db"}


class ProductionConfig(Config):
    """Production configuration settings."""


class DevelopmentConfig(Config):
    """Development configuration settings."""

    @property
    def DATABASE_CONFIG(self):
        config = super().DATABASE_CONFIG

        config["url"] = "sqlite:///:memory:"

        return config


class TestingConfig(DevelopmentConfig):
    """Testing configration settings."""

    TESTING = True
