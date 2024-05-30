from flask import Flask

app = Flask(__name__)


@app.route("/greet/<name>")
def greet_person(name):
    return f"Hello, {name}!"


@app.route("/faulty/<int:number>")
def faulty_endpoint(number):
    return f"Take this: {number / 0}!"


if __name__ == "__main__":
    app.run(debug=True)
