Projeto desenvolvido por Theo Rocha e Matheus Lopes, Matheus de Paula e Oseias.
Consiste em uma simulação de um sistema para realizacao de provas.
Foi utilizado o SQL-Alchemy para manipulação dos bancos de dados.
Para executar o código, basta rodar as seguintes linhas no terminal do computador:

pip install -r requirements.txt
flask db init
flask db migrate -m "init"
flask db upgrade

e para executar com debugger on:

flask --app run run --debug
