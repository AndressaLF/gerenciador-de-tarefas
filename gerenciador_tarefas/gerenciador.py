from fastapi import FastAPI

# Cria uma aplicação do zero
app = FastAPI


TAREFAS = []


@app.get("/tarefas")
def listar():
    return TAREFAS  # retornando uma lista vazia
