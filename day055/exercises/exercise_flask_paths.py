from flask import Flask

app = Flask(__name__)


@app.route("/greet/<name>")
def greet_person(name):
    return "<head><style>" \
           "    div {" \
           "        text-align: center" \
           "    }" \
           "</style></head>" \
           f"<h1 style='text-align: center'>Hello, {name}!</h1>" \
           "<div>" \
           "    <img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExajlmZTF2OGJyc3d6djlqaDk1a3gyd2s1a3Y3a2xzMGt5dnZnb2RmZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MDJ9IbxxvDUQM/giphy.webp'>" \
           "</div>"


@app.route("/faulty/<int:number>")
def faulty_endpoint(number):
    return f"Take this: {number / 0}!"


if __name__ == "__main__":
    app.run(debug=True)
