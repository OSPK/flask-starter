from flask import Flask
from .views.root import root
from .views.admin import admin
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(root)
app.register_blueprint(admin, url_prefix='/admin')

app.config.from_object('config')

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
