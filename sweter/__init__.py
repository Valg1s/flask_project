from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


BASE_DIR = Path(__file__).parent.parent

TEMPLATE_DIR = BASE_DIR / 'templates/'
STATIC_DIR = TEMPLATE_DIR / "static/"

app = Flask(__name__, template_folder=TEMPLATE_DIR , static_folder=STATIC_DIR)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wawe.db"

db = SQLAlchemy(app)

from . import models, routs