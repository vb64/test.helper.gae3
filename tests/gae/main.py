"""Test GAE app."""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    """Root page."""
    return "Test app"
