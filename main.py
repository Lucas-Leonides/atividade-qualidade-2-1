from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo para os dados
class Item(BaseModel):
    id: int
    nome: str
    descricao: str = None

# Banco de dados simulado
db: List[Item] = []

# Endpoint GET
@app.get("/itens", response_model=List[Item])
def listar_itens():
    return db

# Endpoint POST
@app.post("/itens", response_model=Item)
def adicionar_item(item: Item):
    # Verifica se já existe o item com o mesmo ID
    for existente in db:
        if existente.id == item.id:
            raise HTTPException(status_code=400, detail="ID já existe.")
    db.append(item)
    return item
