from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Numeric
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_required, LoginManager, login_user, logout_user, current_user


class User(db.Model, UserMixin):
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(9), nullable=False, unique=True)
    email = db.Column(String(150), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

  
###############################################################################################################

#QUESTÃO MULTIPLA ESCOLHA 

class Questao(db.Model):
    id = Column(Integer, primary_key=True)
    enunciado = Column(String(255), nullable=False)
    alternativas = relationship('Alternativa', backref='questao', lazy='select')

    def __init__(self, enunciado):
        self.enunciado = enunciado

class Alternativa(db.Model):
    id = Column(Integer, primary_key=True)
    texto = Column(String(255), nullable=False)
    correta = Column(Boolean, nullable=False)
    questao_id = Column(Integer, ForeignKey('questao.id'))

    
    def __init__(self, texto, correta, questao_id):
        self.texto = texto
        self.correta = correta
        self.questao_id = questao_id

###############################################################################################################
    
#QUESTÃO CERTO OU ERRADO.
class QuestaoCE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, nullable = False)
    resposta_correta = Column(Boolean, nullable=False)

    def __init__(self, descricao, resposta_correta):
        self.descricao = descricao
        self.resposta_correta = resposta_correta

###############################################################################################################
    
#QUESTÃO CAMPO ABERTO
class QuestaoCA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, nullable = False)
    resposta_correta = Column(Integer, nullable=False)

    def __init__(self, descricao, resposta_correta):
        self.descricao = descricao
        self.resposta_correta = resposta_correta

###############################################################################################################

#EXAMES
