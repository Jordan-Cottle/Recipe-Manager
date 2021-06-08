""" Configuration settings for the flask application. """

# pylint: disable=too-few-public-methods

import os


class Config:
    """Common/default configuration values."""

    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(32))


class ProductionConfig(Config):
    """Production configuration settings."""


class DevelopmentConfig(Config):
    """Development configuration settings."""


class TestingConfig(DevelopmentConfig):
    """Testing configration settings."""

    TESTING = True
