from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.url_map.strict_slashes = False

db = SQLAlchemy(app)
