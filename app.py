import os

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    return 'Hello, world!'


if __name__ == '__main__':
    app.run()
