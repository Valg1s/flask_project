from flask import render_template

from sweter import app, db
from .models import Statement,Services


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")
