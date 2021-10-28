from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/C3ADmBThxaNdS/giphy.gif" width=300px>'


def make_bold(function):
    def wrapper_function():
        output = function()
        return f'<b>{output}</b>'
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        output = function()
        return f'<em>{output}</em>'
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        output = function()
        return f'<u>{output}</u>'
    return wrapper_function


# Different routes using the app.route decorator
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'


# Creating variable paths and converting the path to a specified data type
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)

