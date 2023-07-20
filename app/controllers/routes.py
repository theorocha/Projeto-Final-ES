from flask import render_template, redirect, url_for, request, jsonify, flash
from flask_login import UserMixin, login_required, LoginManager, login_user, logout_user, current_user
from app import app, bcrypt, login_manager, db
from datetime import datetime
from werkzeug.exceptions import abort

from app.models.tables import User, Questao, Alternativa, Exame, QuestaoExame, RespostasQuestoes, RespotasExameUser
from app.models.forms import LoginForm, RegisterForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def get_questao(questao_id):
    questao = Questao.query.filter_by(id=questao_id).first()
    if questao is None:
        abort(404)
    return questao

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
        
        new_user = User(username=form.username.data, email = form.email.data, password=hashed_password,professor = form.professor.data)
       
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route("/user")
@login_required
def user():
    now = datetime.now()
    if current_user.professor == True:
        return render_template('prof.html')
    else:
        exames = Exame.query.all()
        respondidas_id = [r.exame_id for r in RespotasExameUser.query.all()]
        exames_nao_respondidos = list()
        exames_respondidos = list()
        for e in exames:
            if(e.id not in respondidas_id):
                exames_nao_respondidos.append(e)
            else:
                exames_respondidos.append(e)
        return render_template('aluno.html', exames_nao_respondidos=exames_nao_respondidos, exames_respondidos=exames_respondidos)


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/questoes",methods=['GET'])
@login_required
def questoes():
    questoes = Questao.query.all()
    return render_template('questoes_view.html', questoes = questoes)

@app.route("/editQuestoes/<int:id>",methods=['GET', 'POST'])
@login_required
def editQuestao(id):
    questao = Questao.query.filter_by(id = id).first()
    return render_template('editQuestao.html', questao = questao)

@app.route("/deleteQuestao/<int:id>", methods=['GET','POST'])
@login_required
def delete_questao(id):
    questao = Questao.query.get(id)

    if not questao:
        flash("Questão não encontrada.")
        return redirect(url_for('questoes')) 
    
    if questao.tipo == 'ME':
        for alternativa in questao.alternativas:
            db.session.delete(alternativa)

    db.session.delete(questao)
    db.session.commit()

    flash("Questão excluída com sucesso.")
    return redirect(url_for('questoes'))



@app.route("/updateQuestao/<int:id>", methods=['POST','GET'])
@login_required
def update_questao(id):
    # Obtenha a questão com base no ID
    questao = Questao.query.get(id)

    # Verifique se a questão existe
    if not questao:
        flash("Questão não encontrada.")
        return redirect(url_for('questoes'))  # Redirecione para a página de questões

    # Atualize os dados da questão com base nos valores enviados pelo formulário
    questao.enunciado = request.form.get('enunciado')
    
    if questao.tipo == 'ME':
        alternativas = request.form.getlist('alternativas')
        correta_index = int(request.form.get('alternativa_correta'))
        for i, alternativa in enumerate(questao.alternativas):
            alternativa.texto = alternativas[i]
            alternativa.correta = (i == correta_index)
    
    if questao.tipo == 'CE' or questao.tipo == 'CA':
        questao.correta = request.form.get('resposta_correta')

    # Salve as alterações no banco de dados
    db.session.commit()

    flash("Questão atualizada com sucesso.")
    return redirect(url_for('questoes'))  # Redirecione para a página de questões





@app.route("/questoes/add",methods=['GET'])
@login_required
def add_questoes_view(): return render_template('add_questao.html')

@app.route("/questoes/add",methods=['POST'])
@login_required
def add_questoes():
    tipo = request.form.get("tipo")
    enunciado = request.form.get("enunciado")
    resposta_correta = request.form.get("resposta_correta")
    certo_errado = request.form.get("certo_errado")
    alternativas = request.form.getlist("alternativas")
    alternativa_correta = request.form.get("alternativa_correta")

    if tipo == "ME":
        questao = Questao(tipo=tipo, enunciado=enunciado, correta=None)
        db.session.add(questao)
        db.session.commit()
        i=0
        for a in alternativas:
            alternativa = Alternativa(
                texto=a,
                correta=(i==int(alternativa_correta)),
                questao_id = questao.id
            )
            db.session.add(alternativa)
            i+=1
        db.session.commit()
        
    elif tipo=="CE":
        if certo_errado: certo_errado = "CERTO"
        else: certo_errado = "ERRADO"
        questao = Questao(tipo=tipo, enunciado=enunciado, correta=certo_errado)
        db.session.add(questao)
        db.session.commit()

    elif tipo=="CA":
        questao = Questao(tipo=tipo, enunciado=enunciado, correta=resposta_correta)
        db.session.add(questao)
        db.session.commit()

    return redirect(url_for('questoes'))

'''
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
'''

@app.route("/exames",methods=['GET'])
@login_required
def exames():
    now = datetime.now()
    exames = Exame.query.all()
    return render_template('exames.html', exames=exames, now=now)

@app.route("/exames/edit/<id>",methods=['GET'])
@login_required
def exames_edit(id):
    # carga de questões
    questoes = [(a.id, a.enunciado) for a in Questao.query.all()]

    return render_template('exame_edit.html', id=id, questoes=questoes)


@app.route("/exames/edit/<id>/update",methods=['GET', 'POST'])
@login_required
def exames_update(id):
    # obtenção das questoes
    questoes = request.form.getlist('questoes')
    # salvando as questoes
    print("# inserindo questoes no exame", questoes)
    for q in questoes:
        quest = QuestaoExame(exame_id=int(id), questao_id=int(q))
        db.session.add(quest)

    db.session.commit()
    return redirect(url_for("exames"))

@app.route("/exames/relatorio/<id>",methods=['GET'])
@login_required
def exames_relatorio(id):
    questao_exames = QuestaoExame.query.filter_by(exame_id=id).all()
    questoes = list()
    for q in questao_exames:
        questoes.append(Questao.query.filter_by(id=q.questao_id).first().enunciado)

    respostas = RespotasExameUser.query.filter_by(exame_id=id).all()
    return render_template('exames_relatorio.html', questoes=questoes, respostas=respostas)


@app.route("/criarE",methods=['GET','POST'])
@login_required
def criar_exame():
    valor = request.form.get('valor')
    if request.method == 'POST':
        nome = request.form.get('exame_name')
        horario_inicio_str = request.form.get('horario_inicio')
        horario_fim_str = request.form.get('horario_fim')
        qtd_questoes = request.form.get('qtd_questoes')
        valor = request.form.get('valor')
        horario_fim = datetime.strptime(horario_fim_str, '%Y-%m-%dT%H:%M')
        horario_inicio = datetime.strptime(horario_inicio_str, '%Y-%m-%dT%H:%M')

        exame = Exame(nome=nome, horario_inicio=horario_inicio, horario_fim=horario_fim, qtd_questoes=qtd_questoes, valor=valor)
        db.session.add(exame)
        db.session.commit()
        return redirect(url_for('exames'))
    questoes = Questao.query.all();
    return render_template('criarE.html' , questoes_disponiveis = questoes)


@app.route("/exame/<id>/",methods=['GET'])
@login_required
def responde_exame_view(id):
    exame = Exame.query.filter_by(id=id).first()
    questoes = [Questao.query.filter_by(id=e.questao_id).first() for e in exame.questoes]
    return render_template('responde_exame.html', exame=exame, questoes=questoes)

@app.route("/exame/<id>/",methods=['POST'])
@login_required
def responde_exame(id):
    respostas = list()

    questions_id = request.form.getlist('questions_id')
    respostas += request.form.getlist('respostasCE')
    respostas += request.form.getlist('respostasME')
    respostas += request.form.getlist('respostasCA')
    
    respostaExame = RespotasExameUser(exame_id=id, user_id=current_user.id)
    db.session.add(respostaExame)
    db.session.commit()

    for i,q in enumerate(questions_id):
        respostasQuestoes = RespostasQuestoes(resposta_user=respostas[i], questao_id=int(q), reposta_exame_id=int(respostaExame.id))
        db.session.add(respostasQuestoes)
    db.session.commit()

    return redirect(url_for("user"))

