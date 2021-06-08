""" Utility module for running tests and debug versions of the application. """

import os
import sys

import pytest

PROJECT_DIR = f"{os.getcwd()}/recipe_manager"
TEST_DIR = f"{os.getcwd()}/tests"

# Setup environment paths
os.environ["PYTHONPATH"] = PROJECT_DIR
sys.path.append(PROJECT_DIR)


def _run(command):
    """Run a shell command and assert that is was successful."""

    exit_code = os.system(command)

    assert exit_code == 0, f"'{command}' failed with exit code {exit_code}"


def run():
    """Run the application in production mode."""

    os.environ["APPLICATION_MODE"] = "prod"
    os.environ["FLASK_RUN_HOST"] = "0.0.0.0"
    os.environ["FLASK_RUN_PORT"] = "12345"

    # TODO: Replace flask dev server with production ready one
    _run("flask run")


def debug():
    """Run the application in debug mode."""

    os.environ["APPLICATION_MODE"] = "dev"
    os.environ["FLASK_ENV"] = "development"

    _run("flask run")


def test():
    """Run tests for the application."""

    os.environ["APPLICATION_MODE"] = "test"
    os.environ["FLASK_ENV"] = "testing"

    pytest.main(["--cov"])


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
