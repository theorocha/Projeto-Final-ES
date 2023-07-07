from flask.cli import AppGroup
from app import db, bcrypt

from .models.tables import User
from .seed import questionCE, users
seed_cli = AppGroup("seed")


#flask seed questionCE
'''
@seed_cli.command("questionCE")
def seed_questionCE():
    for question in questionCE:
        db.session.add(QuestaoCE(**question))
    db.session.commit()
'''

@seed_cli.command("user")
def seed_user():
    for user in users:
        user['password'] = bcrypt.generate_password_hash(user.get('password'))
        db.session.add(User(**user))
    db.session.commit()



##Para adicionar os dados -> flask seed <command.name>
