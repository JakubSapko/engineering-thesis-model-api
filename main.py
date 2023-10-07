from fastapi import FastAPI, Request


app = FastAPI()


@app.post("/")
async def root(request: Request):
    print("test")
    result = await request.body()
    print(result)
    return {"message": "Hello World"}
