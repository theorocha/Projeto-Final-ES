from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Numeric
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_required, LoginManager, login_user, logout_user, current_user


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(9), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

###############################################################################################################

#QUESTÃO MULTIPLA ESCOLHA 

class Questao(db.Model):
    id = Column(Integer, primary_key=True)
    enunciado = Column(String(255), nullable=False)
    alternativas = relationship('Alternativa', backref='questao', lazy='select')

class Alternativa(db.Model):
    id = Column(Integer, primary_key=True)
    texto = Column(String(255), nullable=False)
    correta = Column(Boolean, nullable=False)
    questao_id = Column(Integer, ForeignKey('questao.id'))

###############################################################################################################
    
#QUESTÃO CERTO OU ERRADO.
class QuestaoCE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, nullable = False)
    resposta_correta = Column(Boolean, nullable=False)

###############################################################################################################
    
#QUESTÃO CAMPO ABERTO
class QuestaoCA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, nullable = False)
    resposta_correta = Column(Integer, nullable=False)

###############################################################################################################

#EXAMES