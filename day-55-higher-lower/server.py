import random

from flask import Flask

app = Flask(__name__)


@app.route('/')
def guess_number():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


def random_number():
    n = random.randint(0, 9)
    return n


@app.route('/<int:number>')
def check_number(number):
    user_feedback = ''
    if number < random_number():
        user_feedback = '<h1 style="color: red"> Too low, try again! </h1>' \
                        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > random_number():
        user_feedback = '<h1 style="color: purple"> Too high, try again! </h1>' \
                        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        user_feedback = '<h1 style="color: green"> You found me! </h1>' \
                        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    return user_feedback


if __name__ == "__main__":
    app.run(debug=True)
