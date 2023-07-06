from flask import render_template, redirect, url_for, request
from flask_login import UserMixin, login_required, LoginManager, login_user, logout_user, current_user
from app import app, bcrypt, login_manager, db

from app.models.tables import User, Questao, QuestaoCA,QuestaoCE, Alternativa
from app.models.forms import LoginForm, RegisterForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home():
        return render_template('home.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('user'))
    return render_template('login.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route("/user")
@login_required
def user():
    return render_template('user.html')


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/questoes",methods=['GET', 'POST'])
@login_required
def questoes():
    return render_template('questoes.html')


@app.route("/criarME",methods=['GET', 'POST'])
@login_required
def cria_questaoME():
    return render_template('criarME.html')

@app.route("/criarCE",methods=['GET', 'POST'])
@login_required
def cria_questaoCE():
    descricao = request.form.get('enunciado')
    if request.form.get('resposta') == 'certo':
        resposta_correta = True
    else:
        resposta_correta = False
    if request.method == 'POST':
        questao = QuestaoCE(descricao, resposta_correta)
        db.session.add(questao)
        db.session.commit()
        return redirect(url_for('questoes'))
    return render_template('criarCE.html')

@app.route("/criarCA",methods=['GET', 'POST'])
@login_required
def cria_questaoCA():
    descricao = request.form.get('enunciado')
    resposta_correta = request.form.get('ans')
    if request.method == 'POST':
        questao = QuestaoCA(descricao,resposta_correta)
        db.session.add(questao)
        db.session.commit()
        return redirect(url_for('questoes'))
    return render_template('criarCA.html')


# flask --app run run --debug