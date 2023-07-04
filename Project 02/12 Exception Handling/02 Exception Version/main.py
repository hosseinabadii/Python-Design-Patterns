import os
os.system('clear')

from flask import Flask, jsonify, abort
from db import fetch_blogs, fetch_blog, NotFoundError, NotAuthorizedError

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="blogs">blogs</a>'

@app.route("/blogs")
def get_blogs():
    return jsonify(fetch_blogs())

@app.route("/blogs/<id>")
def get_blog(id):
    try:
        return jsonify(fetch_blog(id))
    except NotFoundError:
        abort(404, description='Resource not found')
    except NotAuthorizedError:
        abort(403, description="Access denied")


app.run()

