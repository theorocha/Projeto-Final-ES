from flask.cli import AppGroup
from app import db
from .models.tables import QuestaoCE
from .seed import questionCE
seed_cli = AppGroup("seed")


@seed_cli.command("questionCE")
def seed_movies():
    "Add seed data to the database."
    for question in questionCE:
        db.session.add(QuestaoCE(**question))
    db.session.commit()


