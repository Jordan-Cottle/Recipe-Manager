""" Utility module for running tests and debug versions of the application. """

import os

import pytest


def debug():
    """Run the application in debug mode."""

    os.chdir("recipe_manager")
    os.environ["FLASK_ENV"] = "development"

    exit_code = os.system("flask run")
    print(f"Application exitcode: {exit_code}")


def test():
    """Run tests for the application."""

    pytest.main(["--cov"])
