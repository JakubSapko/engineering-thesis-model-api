from fastapi import FastAPI, Request

from middlewares.auth import AuthMiddleware


app = FastAPI()

app.add_middleware(AuthMiddleware)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/api")
async def handle_anki_data(request: Request):
    print("tu")
    print(await request.json())
    print("tams")
    return {"message": "Hello World"}
