from flask import Flask
from gena import fib
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Привет, Мир!</p>"

@app.route("/<int:n>")
def fibonachi_number(n):
    return list(fib(n))

@app.errorhandler(404)
def page_not_found(e):
    return "Ошибка! Введите '/число!'"

if __name__ == "__main__":
    app.run(debug=True)