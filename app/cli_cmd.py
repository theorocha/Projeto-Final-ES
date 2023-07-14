from flask.cli import AppGroup
from app import db, bcrypt

from .models.tables import User, Questao, Alternativa, Exame, QuestaoExame, RespostasQuestoes, RespotasExameUser
from .seed import users, exames, questoes, alternativas, exames_questoes, resposta_exame_user, respostas_questoes
seed_cli = AppGroup("seed")


@seed_cli.command("questoes")
def seed_questions():
    for q in questoes:
        db.session.add(Questao(**q))
    db.session.commit()

@seed_cli.command("alternativas")
def seed_alternativas():
    for a in alternativas:
        db.session.add(Alternativa(**a))
    db.session.commit()

@seed_cli.command("exames")
def seed_exames():
    for e in exames:
        db.session.add(Exame(**e))
    db.session.commit()

@seed_cli.command("exames_questoes")
def seed_exame_questoes():
    for eq in exames_questoes:
        db.session.add(QuestaoExame(**eq))
    db.session.commit()

@seed_cli.command("user")
def seed_user():
    for user in users:
        user['password'] = bcrypt.generate_password_hash(user.get('password'))
        db.session.add(User(**user))
    db.session.commit()

@seed_cli.command("resposta_exame_user")
def seed_resposta_exame_user():
    for ru in resposta_exame_user:
        db.session.add(RespotasExameUser(**ru))
    db.session.commit()

@seed_cli.command("respostas_questoes")
def seed_respostas_questoes():
    for rq in respostas_questoes:
        db.session.add(RespostasQuestoes(**rq))
    db.session.commit()

@seed_cli.command("all")
def seed_all():
    seed_user()
    seed_questions()
    seed_alternativas()
    seed_exames()
    seed_exame_questoes()
    seed_resposta_exame_user()
    seed_respostas_questoes()


##Para adicionar os dados -> flask seed <command.name>
