from flask import Flask

app = Flask(__name__)


@app.route("/greet/<name>")
def greet_person(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run()
