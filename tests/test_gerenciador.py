from fastapi.testclient import TestClient
from fastapi import status
from gerenciador_tarefas.gerenciador import app, TAREFAS

# testando o status code
def test_quando_listar_tarefas_devo_ter_como_retorno_codigo_de_status_200():
    cliente = TestClient(app)  # criando cliente passando o app criado como parametro por meio da biblioteca TestClient
    resposta = cliente.get("/tarefas")  # passando o endereço do caminho
    assert resposta.status_code == status.HTTP_200_OK

# testando se o retortno é no formato json - o fastapi já faz isso
def test_quando_listar_tarefas_formato_de_retorno_deve_ser_json():
    cliente = TestClient(app)  # criando um novo cliente
    resposta = cliente.get("/tarefas")
    assert resposta.headers["Content-Type"] == "application/json"

# testando se o retorno está no formato de lista
def test_quando_listar_tarefas_retorno_deve_ser_uma_lista():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert isinstance(resposta.json(), list)  # isinstance é uma função do python que verifica se algo(resposta.json) é uma lista

# testando se as tarefas retornadas da minha lista possuem todos os requisitos pedidos (id, titulo, descrição ....)
def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_id():
    TAREFAS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "titulo": "titulo 1",
            "descricao": "descricao 1",
            "estado": "finalizado",
        }
    )
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "id" in resposta.json().pop()  # pegando o retorno do json(dicionario) convertendo em python e pegando o primeiro elemento(primeira tarefa)
    TAREFAS.clear()  # limpar o recurso
