
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello! FastAPI is working successfully."
    }


@app.get("/user")
def get_user():
    return {
        "id": 1,
        "name": "Raja",
        "role": "Developer" 
    }


@app.get("/add")
def add_numbers(a: int, b: int):
    return {
        "number1": a,
        "number2": b,
        "result": a + b
    }
