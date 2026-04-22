from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "This is my first API!"}

@app.get("/name")
def read_root1():
    return {"message": "This is mithra!"}

