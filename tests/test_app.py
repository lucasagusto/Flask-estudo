# tests/test_app.py
import pytest
from flask_estudo import create_app

@pytest.fixture
def client():
    app = create_app(testing=True)
    with app.test_client() as c:
        yield c

def test_home_ok(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"<html" in resp.data

def test_clientes_ok(client):
    resp = client.get("/clientes/")
    assert resp.status_code == 200