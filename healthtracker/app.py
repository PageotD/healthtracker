from flask import Flask
from .router import register_routes

def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app
