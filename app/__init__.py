from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
bootstrap = Bootstrap()

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///storage.db'
app.config["SECRET_KEY"] = 'senhaseguraflask'

migrate = Migrate(app, db)
bcrypt.init_app(app)
db.init_app(app)
login_manager.init_app(app)
bootstrap.init_app(app)

login_manager.login_view = "login"


from app.models import tables, forms
from app.controllers import routes

