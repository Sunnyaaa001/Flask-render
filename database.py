import os
from flask import Flask
from dotenv import load_dotenv
from model import db

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(BASE_DIR, os.environ.get("DB_PATH"))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_file}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()