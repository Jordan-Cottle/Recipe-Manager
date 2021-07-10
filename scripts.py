""" Utility module for running tests and debug versions of the application. """

import os
import sys

# Setup environment paths
PROJECT_DIR = f"{os.getcwd()}/recipe_manager"
TEST_DIR = f"{os.getcwd()}/tests"
os.environ["PYTHONPATH"] = PROJECT_DIR
sys.path.append(PROJECT_DIR)

from config import get_config
from database import Database
from database.models import setup_database


ENV_MAP = {
    "prod": "production",
    "dev": "development",
    "test": "testing",
}


def _run(command):
    """Run a shell command and assert that is was successful."""

    exit_code = os.system(command)

    assert exit_code == 0, f"'{command}' failed with exit code {exit_code}"


def _set_flask_env(mode):
    """Setup flask environment variables."""

    print(f"Activating application mode: {mode}")
    os.environ["APPLICATION_MODE"] = mode
    os.environ["FLASK_ENV"] = ENV_MAP.get(mode, mode)

    if mode == "prod":
        os.environ["FLASK_RUN_HOST"] = "0.0.0.0"
        os.environ["FLASK_RUN_PORT"] = "12345"


def run():
    """Run the application in production mode."""

    _set_flask_env("prod")

    # TODO: Replace flask dev server with production ready one
    _run("flask run")


def debug():
    """Run the application in debug mode."""

    _set_flask_env("dev")
    _run("flask run")


def test():
    """Run tests for the application."""

    _set_flask_env("test")
    _run("pytest --cov -v")


def static_analysis():
    """Run static analysis checks on the code."""

    selection = sys.argv[1] if len(sys.argv) > 1 else None

    commands = {
        "black": f"black -v --diff --check {PROJECT_DIR} {TEST_DIR}",
        "pylint": f"pylint {PROJECT_DIR} {TEST_DIR}",
    }

    if selection in commands:
        commands = {selection: commands[selection]}

    for name, command in commands.items():
        print(f"Running {name} check")
        _run(command)


def setup_db(mode="dev"):
    """Initial setup for the database."""

    _set_flask_env(mode)

    config = get_config()
    database = Database(config.DATABASE_CONFIG)

    setup_database(database.engine)
