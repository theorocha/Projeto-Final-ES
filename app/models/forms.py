from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo
from app.models.tables import User


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Matrícula"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20),EqualTo('confirm_password', message='Password devem ser iguais.')], render_kw={"placeholder": "Senha"})
    confirm_password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)],render_kw={"placeholder": "Repita a senha"})
    email = StringField(validators=[InputRequired(),  Length(min=4, max=20)], render_kw={"placeholder": "Email"})
    professor = SelectField("Professor:",choices= [('False', 'não'),('True', 'sim')],coerce = lambda x: x == 'True')

    submit = SubmitField("Register")


    def validate_username(form, username):
        
        existing_user__username = User.query.filter_by(username=username.data).first()
        if existing_user__username:
            print("here")
            raise ValidationError("That username already exists. Please choose a different one.")
        


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Matrícula"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Senha"})
    submit = SubmitField("Login")

class ClassForm(FlaskForm):
    name = StringField(validators=[InputRequired()], render_kw={"placeholder": "Nome"})
    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "Digite a senha"})
    submit = SubmitField("Create")
    
