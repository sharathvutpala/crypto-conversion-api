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

async def get_currency(selected_currency):

    url = f'https://api.coinbase.com/v2/prices/spot?currency={selected_currency}'
    response = requests.get(url)
    return response.json()

# async def get_currency(currency: Optional[str] = "USD", max_length=3):
#     try:

#         url = f'https://api.coinbase.com/v2/prices/spot?currency={currency}'
#         response = requests.get(url)

#         if currency not in currency_list:
#             raise HTTPException(status_code=404, detail="Invalid currency")
#         return response.json()
#     except requests.exceptions.RequestException:
#         raise HTTPException(status_code=500, detail="Error connecting, retry later")

