from flask import Flask

from day055.exercises.decorators import make_bold, make_italic, make_underlined

app = Flask(__name__)


@app.route("/")
@make_bold
@make_italic
@make_underlined
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
