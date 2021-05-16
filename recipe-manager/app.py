from flask import Flask, render_template
from http import HTTPStatus

app = Flask(
    "recipe-manager",
)


@app.route("/health")
def index_page():
    """ Send the index page to the user. """

    return {"status": "ok"}, HTTPStatus.OK


if __name__ == "__main__":
    app.run(debug=True)
