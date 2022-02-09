from fastapi.testclient import TestClient
import json
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from api.currency  import app

client = TestClient(app)

def test_curency():
    response = client.get("/currency/EUR")
    assert response.json() != {"details":"Currency Details Not Found"}
    assert response.json() != {"details": "Currency length must be 3 Characters"} 
    assert response.status_code != 404
