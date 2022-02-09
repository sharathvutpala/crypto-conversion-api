import json
from urllib import response
from fastapi import FastAPI, HTTPException, Request
import requests
from typing import Optional

app = FastAPI()

currency_list = ["USD",
    "EUR",
    "RUB",
    "CAD",
    "PHP",
    "DKK"]  

@app.get("/")

def home():
    return {"message": "Hello, you are@home"}

@app.get("/currency/{selected_currency}")

async def get_currency(selected_currency: Optional[str] = "INR", max_length=3):
    if len(selected_currency) !=3:
        return {"details": "Currency length must be 3 Characters"}

    elif selected_currency.upper() not in currency_list and len(selected_currency) ==3:
        return {"details": "Currency Details Not Found"}
    
    else:
        url = f'https://api.coinbase.com/v2/prices/spot?currency={selected_currency}'
        response = requests.get(url)
        data= response.json()
        return data

@app.get("/health")
async def get_health():
    response = requests.get('https://crypto-api-demo.sharath.tech/')
    if response.status_code == 200:
        return {"health":"ok"}
    else:
        return {"health": "API is not Healthy"}

