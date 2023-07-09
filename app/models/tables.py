from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Numeric, Enum
from sqlalchemy.orm import relationship, mapped_column, Mapped
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_required, LoginManager, login_user, logout_user, current_user


class User(db.Model, UserMixin):
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(9), nullable=False, unique=True)
    email = db.Column(String(150), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

'''
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
'''
#EXAMES
# questoes = db.Table('questoes',
#     db.Column('questaoCE_id', db.Integer, db.ForeignKey('questao_ce.id'), primary_key=True),
#     db.Column('exame_id', db.Integer, db.ForeignKey('exame.id'), primary_key=True)
# )

# class Exame(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String,nullable = False)
#     horario_inicio = db.Column(db.DateTime, nullable = False)
#     horario_fim = db.Column(db.DateTime, nullable = False)
#     questoes = db.relationship('QuestaoCE',secondary = questoes, lazy='subquery',
#                                backref = db.backref('exames',lazy=True))

'''
questoes = db.Table('questoes',
    db.Column('questao_id', db.Integer, db.ForeignKey('questao.id'), primary_key=True),
    db.Column('exame_id', db.Integer, db.ForeignKey('exame.id'), primary_key=True)
)

questoesCE = db.Table('questoesCE',
    db.Column('questaoCE_id', db.Integer, db.ForeignKey('questao_ce.id'), primary_key=True),
    db.Column('exame_id', db.Integer, db.ForeignKey('exame.id'), primary_key=True)
)

questoesCA = db.Table('questoesCA',
    db.Column('questaoCA_id', db.Integer, db.ForeignKey('questao_ca.id'), primary_key=True),
    db.Column('exame_id', db.Integer, db.ForeignKey('exame.id'), primary_key=True)
)
'''

class Questao(db.Model):
    __tablename__ = 'questoes'

    id = Column(Integer, primary_key=True)
    tipo = Column(Enum('ME', 'CE', 'CA'), nullable=False)
    enunciado = Column(String(255), nullable=False)
    correta = Column(String(255))
    alternativas:  Mapped[list["Alternativa"]] = relationship(back_populates="questao")

class Alternativa(db.Model):
    __tablename__ = 'alternativas'

    id = Column(Integer, primary_key=True)
    texto = Column(String(255), nullable=False)
    correta = Column(Boolean, nullable=False)
    questao_id: Mapped["Questao"] = mapped_column(ForeignKey('questoes.id'))

    questao: Mapped["Questao"] = relationship(foreign_keys="Alternativa.questao_id")


class Exame(db.Model):
    __tablename__ = 'exames'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String,nullable = False)
    qtd_questoes = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.String, nullable=False)
    horario_inicio = db.Column(db.DateTime, nullable = False)
    horario_fim = db.Column(db.DateTime, nullable = False)
    questoes:  Mapped[list["QuestaoExame"]] = relationship(back_populates="exame")

    '''
    questoes = db.relationship('Questao',secondary = questoes, lazy='subquery',
                               backref = db.backref('exames',lazy=True))
    questoesCE = db.relationship('QuestaoCE',secondary = questoesCE, lazy='subquery',
                               backref = db.backref('exames',lazy=True))
    questoesCA = db.relationship('QuestaoCA',secondary = questoesCA, lazy='subquery',
                               backref = db.backref('exames',lazy=True))
    '''


class QuestaoExame(db.Model):
    __tablename__ = 'questao_exames'

    id = Column(Integer, primary_key=True)
    exame_id: Mapped["Exame"] = mapped_column(ForeignKey("exames.id"))
    questao_id: Mapped["Questao"] = mapped_column(ForeignKey("questoes.id"))

    exame: Mapped["Exame"] = relationship(foreign_keys="QuestaoExame.exame_id")
    questao: Mapped["Questao"] = relationship(foreign_keys="QuestaoExame.questao_id")


class RespotasExameUser(db.Model):
    __tablename__ = 'respostas_exame'

    id = Column(Integer, primary_key=True)
    exame_id: Mapped["Exame"] = mapped_column(ForeignKey("exames.id"))
    user_id: Mapped["User"] = mapped_column(ForeignKey("user.id"))
    respostas:  Mapped[list["RespostasQuestoes"]] = relationship(back_populates="resposta")
    
    exame: Mapped["Exame"] = relationship(foreign_keys="RespotasExameUser.exame_id")
    user: Mapped["User"] = relationship(foreign_keys="RespotasExameUser.user_id")


class RespostasQuestoes(db.Model):
    __tablename__ = 'respostas_questoes'

    id = Column(Integer, primary_key=True)
    resposta = Column(String)
    questao_id: Mapped["Questao"] = mapped_column(ForeignKey("questoes.id"))
    reposta_exame_id: Mapped["RespotasExameUser"] = mapped_column(ForeignKey("respostas_exame.id"))

    questao: Mapped["Questao"] = relationship(foreign_keys="RespostasQuestoes.questao_id")
    resposta: Mapped["RespotasExameUser"] = relationship(foreign_keys="RespostasQuestoes.reposta_exame_id")

