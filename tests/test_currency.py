from fastapi.testclient import TestClient
import json
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from api.currency  import app

client = TestClient(app)

def test_curency():
    response = client.get("/currency")
#    error_keyword = str(response["errors"][0]['id'])
#    assert "invalid_request" not in error_keyword
    assert response.json() != {"errors":[{"id":"invalid_request","message":"Currency is invalid"}]} 
    assert response.json() != {"errors":[{"id":"not_found","message":"Invalid currency"}]}
    assert response.status_code != 404