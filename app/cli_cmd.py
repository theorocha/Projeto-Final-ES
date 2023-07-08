from flask.cli import AppGroup
from app import db, bcrypt

from .models.tables import User, Questao, Alternativa, Exame, QuestaoExame
from .seed import users, exames, questoes, alternativas, exames_questoes
seed_cli = AppGroup("seed")


@seed_cli.command("questoes")
def seed_questionCE():
    for q in questoes:
        db.session.add(Questao(**q))
    db.session.commit()

@seed_cli.command("alternativas")
def seed_questionCE():
    for a in alternativas:
        db.session.add(Alternativa(**a))
    db.session.commit()

@seed_cli.command("exames")
def seed_questionCE():
    for e in exames:
        db.session.add(Exame(**e))
    db.session.commit()

@seed_cli.command("exames_questoes")
def seed_questionCE():
    for eq in exames_questoes:
        db.session.add(QuestaoExame(**eq))
    db.session.commit()

@seed_cli.command("user")
def seed_user():
    for user in users:
        user['password'] = bcrypt.generate_password_hash(user.get('password'))
        db.session.add(User(**user))
    db.session.commit()



##Para adicionar os dados -> flask seed <command.name>
