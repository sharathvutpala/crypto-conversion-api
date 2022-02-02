from fastapi import FastAPI, HTTPException, Request
import requests
from typing import Optional

app = FastAPI()

@app.get("/health")
async def get_health():
    API_ENDPOINT = "http://127.0.0.1:8000"
    response = requests.get('http://64.225.84.48')
    #response = urllib.request.urlopen(API_ENDPOINT)
    if response.status_code == 200:
        return {"health":"ok"}
    else:
        return {"health": "API is not Healthy"}
