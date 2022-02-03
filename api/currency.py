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

    try:
        if selected_currency not in currency_list:
            raise HTTPException(status_code=404, detail="Not currency")
        else:
            url = f'https://api.coinbase.com/v2/prices/spot?currency={selected_currency}'
            response = requests.get(url)
            data= response.json()
            return data
    except:
        return "Can't connect to the API"

@app.get("/health")
async def get_health():
    API_ENDPOINT = "http://127.0.0.1:8000"
    response = requests.get('http://64.225.84.48')
    if response.status_code == 200:
        return {"health":"ok"}
    else:
        return {"health": "API is not Healthy"}

