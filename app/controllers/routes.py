from flask import render_template, redirect, url_for, request
from flask_login import UserMixin, login_required, LoginManager, login_user, logout_user, current_user
from app import app, bcrypt, login_manager, db
from datetime import datetime

from app.models.tables import User, Questao, QuestaoCA,QuestaoCE, Alternativa, Exame
from app.models.forms import LoginForm, RegisterForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home():
        # # Excluindo todos os dados da tabela Questao
        # db.session.query(Questao).delete()
        # db.session.commit()

        # # Excluindo todos os dados da tabela Alternativa
        # db.session.query(Alternativa).delete()
        # db.session.commit()
        return render_template('home.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
            # if user.password == form.password.data:
                login_user(user)
                return redirect(url_for('user'))
    return render_template('login.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        
        new_user = User(username=form.username.data, email = form.email.data, password=hashed_password)
       
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
    questoes = Questao.query.all()
    return render_template('questoes.html', questoes = questoes)


@app.route("/criarME", methods=['GET', 'POST'])
@login_required
def cria_questaoME():
    if request.method == 'POST':
        # Capturando dados do formulário
        enunciado = request.form.get('enunciado')
        alternativa1 = request.form.get('alternativa1')
        alternativa2 = request.form.get('alternativa2')
        alternativa3 = request.form.get('alternativa3')
        alternativa4 = request.form.get('alternativa4')
        correta = int(request.form.get('correta'))

        # Criação da instância da questao
        questao = Questao(enunciado=enunciado)
        db.session.add(questao)
        db.session.commit()

        # Amarrando as alternativas às questões
        alternativas = [
            Alternativa(texto=alternativa1, correta=(correta == 0), questao_id=questao.id),
            Alternativa(texto=alternativa2, correta=(correta == 1), questao_id=questao.id),
            Alternativa(texto=alternativa3, correta=(correta == 2), questao_id=questao.id),
            Alternativa(texto=alternativa4, correta=(correta == 3), questao_id=questao.id)
        ]

        # Salvando as alternativas
        for alternativa in alternativas:
            db.session.add(alternativa)
        db.session.commit()

        return redirect(url_for('questoes'))

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

@app.route("/exames",methods=['GET','POST'])
@login_required
def exames():
    exames = Exame.query.all()
    return render_template('exames.html',exames = exames)

@app.route("/criarE",methods=['GET','POST'])
@login_required
def criar_exame():
    valor = request.form.get('valor')
    if request.method == 'POST':
        nome = request.form.get('exame_name')
        horario_inicio_str = request.form.get('horario_inicio')
        horario_inicio = datetime.strptime(horario_inicio_str, '%Y-%m-%dT%H:%M')

        horario_fim_str = request.form.get('horario_fim')
        horario_fim = datetime.strptime(horario_fim_str, '%Y-%m-%dT%H:%M')

        qtd_questoes = request.form.get('qtd_questoes')

        valor = request.form.get('valor')
        exame = Exame(nome=nome, horario_inicio=horario_inicio, horario_fim=horario_fim, qtd_questoes=qtd_questoes, valor=valor)
        db.session.add(exame)
        db.session.commit()
        return redirect(url_for('exames'))
    return render_template('criarE.html')



@app.route("/adiciona",methods=['GET','POST'])
@login_required
def add_questao():
    questions = Questao.query.all()
    return render_template('add_questao.html', questions = questions)

# flask --app run run --debug


