from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from app.models.tables import User


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Matrícula"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Senha"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user__username = User.query.filter_by(username=username.data).first()
        if existing_user__username:
            raise ValidationError("That username already exists. Please choose a different one.")
        

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Matrícula"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Senha"})
    submit = SubmitField("Login")

class ClassForm(FlaskForm):
    name = StringField(validators=[InputRequired()], render_kw={"placeholder": "Nome"})
    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "Digite a senha"})
    submit = SubmitField("Create")
    
