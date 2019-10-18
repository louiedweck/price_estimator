from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    return 'Hello, world!'


if __name__ == '__main__':
    app.run()
