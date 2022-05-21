from fastapi import FastAPI

TAREFAS = []

# Cria uma aplicação do zero
app = FastAPI()

@app.get("/tarefas")
def listar():
    return TAREFAS  # retornando uma lista vazia
