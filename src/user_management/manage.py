import redis
from flask import Flask

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
redis_instance = redis.Redis()