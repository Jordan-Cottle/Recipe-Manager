from flask import Flask, render_template

app = Flask(
    "task-manager",
)


@app.route("/")
def index_page():
    """ Send the index page to the user. """

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)