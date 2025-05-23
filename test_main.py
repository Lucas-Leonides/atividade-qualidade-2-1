from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_post_item():
    resposta = client.post("/itens", json={
        "id": 1,
        "nome": "Sensor de temperatura",
        "descricao": "Sensor para medir temperatura ambiente"
    })
    assert resposta.status_code == 200
    assert resposta.json()["id"] == 1
    assert resposta.json()["nome"] == "Sensor de temperatura"

def test_get_itens():
    resposta = client.get("/itens")
    assert resposta.status_code == 200
    itens = resposta.json()
    assert isinstance(itens, list)
    assert any(item["id"] == 1 for item in itens)

def test_post_item_duplicado():
    # Tentativa de inserir novamente o mesmo ID (1)
    resposta = client.post("/itens", json={
        "id": 1,
        "nome": "Outro sensor",
        "descricao": "Deve falhar"
    })
    assert resposta.status_code == 400
    assert resposta.json()["detail"] == "ID já existe."
