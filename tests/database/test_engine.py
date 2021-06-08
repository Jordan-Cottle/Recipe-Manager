""" Verify that the database can be connected to. """

from database import Database


def test_database():
    """Test that database setup works independently from the flask app context."""

    database = Database({"url": "sqlite:///:memory:"})

    with database.session as session:
        result = session.execute("select 'This is a test'").one()

        assert len(result) == 1, "Only one item should be returned."
        assert (
            result[0] == "This is a test"
        ), "The database should return the selected string"
