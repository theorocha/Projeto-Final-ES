import datetime


users = [
    {
        "username": "pedro",
        "email":"pedro@unb.br",
        "password":"asdfg" ,
        "professor": True
    },
    {
        "username": "ester",
        "email": "ester@unb.br",
        "password":  "asdfg",
        "professor": False
    }
]

questoes = [
    {
        "tipo": "ME",
        "enunciado": "10+10",
        "correta": "20"
    },
    {
        "tipo": "CE",
        "enunciado": "A Terra é plana?",
        "correta": "ERRADO"
    },
    {
        "tipo": "CA",
        "enunciado": "Em que ano estamos",
        "correta": "2023"
    }
]

alternativas = [
    {
        "texto": "10",
        "correta": 0,
        "questao_id": 1
    },
    {
        "texto": "20",
        "correta": 1,
        "questao_id": 1
    },
    {
        "texto": "30",
        "correta": 0,
        "questao_id": 1
    },
    {
        "texto": "40",
        "correta": 0,
        "questao_id": 1
    }
]

exames = [
    { # exame 1: encerrado e respondido por ester
        "nome": "teste 1",
        "qtd_questoes": 3,
        "valor": "6",
        "horario_inicio": datetime.datetime.now(),
        "horario_fim": datetime.datetime.now()
    },
    {# exame 2: não encerrado e deve ser respondido
        "nome": "teste 2",
        "qtd_questoes": 3,
        "valor": "6",
        "horario_inicio": datetime.datetime.now(),
        "horario_fim": datetime.datetime.max #9999-12-31 23:59:59.999999
    }
]

exames_questoes = [
    {# exame 1
        "exame_id": 1,
        "questao_id": 1,
        "peso": 1.0
    },
    {
        "exame_id": 1,
        "questao_id": 2,
        "peso": 2.0
    },
    {
        "exame_id": 1,
        "questao_id": 3,
        "peso": 3.0
    },
    {# exame 2
        "exame_id": 2,
        "questao_id": 1,
        "peso": 2.0
    },
    {
        "exame_id": 2,
        "questao_id": 2,
        "peso": 2.0
    },
    {
        "exame_id": 2,
        "questao_id": 3,
        "peso": 2.0
    }
]

resposta_exame_user = [
    {# exame 1 respondido pela ester
        "exame_id": 1,
        "user_id": 2,
        "nota": 6.0
    }
]

respostas_questoes = [
    { # respostas da ester no exame 1
        "resposta_user": "20",
        "questao_id": 1,
        "reposta_exame_id": 1,
        "acertou": True
    },
    {
        "resposta_user": "ERRADO",
        "questao_id": 2,
        "reposta_exame_id": 1,
        "acertou": True
    },
    {
        "resposta_user": "2023",
        "questao_id": 3,
        "reposta_exame_id": 1,
        "acertou": True
    }
]

