from app import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_required, LoginManager, login_user, logout_user, current_user


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(9), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


 
    