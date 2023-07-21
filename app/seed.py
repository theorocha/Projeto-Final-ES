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
    {
        "nome": "teste 1",
        "qtd_questoes": 5,
        "valor": "10",
        "horario_inicio": datetime.datetime.now(),
        "horario_fim": datetime.datetime.now()
    },
    {
        "nome": "teste 2",
        "qtd_questoes": 5,
        "valor": "10",
        "horario_inicio": datetime.datetime.now(),
        "horario_fim": datetime.datetime.now()
    }
]

exames_questoes = [
    {
        "exame_id": 1,
        "questao_id": 1
    },
    {
        "exame_id": 1,
        "questao_id": 2
    },
    {
        "exame_id": 1,
        "questao_id": 3
    }
]

resposta_exame_user = [
    {
        "exame_id": 1, # teste 1
        "user_id": 2 # ester
    }
]

respostas_questoes = [
    {
        "resposta_user": "20",
        "questao_id": 1,
        "reposta_exame_id": 1
    },
    {
        "resposta_user": "ERRADO",
        "questao_id": 2,
        "reposta_exame_id": 1
    },
    {
        "resposta_user": "2023",
        "questao_id": 3,
        "reposta_exame_id": 1
    }
]

