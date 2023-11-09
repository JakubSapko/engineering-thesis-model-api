from fastapi import FastAPI, Request

from middlewares.auth import AuthMiddleware

import pandas as pd


app = FastAPI()

app.add_middleware(AuthMiddleware)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/api")
async def handle_anki_data(request: Request):
    data = await request.json()
    for deck in data["cards"].items():
        pd.DataFrame(deck[1]["result"]).to_csv("data.csv")
    return {"message": "Hello World"}
