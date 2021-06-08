""" Utility module for running tests and debug versions of the application. """

import os
import sys

import pytest

PROJECT_DIR = f"{os.getcwd()}/recipe_manager"

# Setup environment paths
os.environ["PYTHONPATH"] = PROJECT_DIR
sys.path.append(PROJECT_DIR)


def run(command):
    """Run a shell command and assert that is was successful."""

    exit_code = os.system(command)

    assert exit_code == 0, f"'{command}' failed with exit code {exit_code}"


def debug():
    """Run the application in debug mode."""

    os.environ["APPLICATION_MODE"] = "dev"
    os.environ["FLASK_ENV"] = "development"

    run("flask run")


def test():
    """Run tests for the application."""

    os.environ["APPLICATION_MODE"] = "test"
    os.environ["FLASK_ENV"] = "testing"

    pytest.main(["--cov"])
