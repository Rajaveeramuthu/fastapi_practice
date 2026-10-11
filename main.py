
from fastapi import FastAPI

app = FastAPI()

# Home API
@app.get("/")
def home():
    return {
        "message": "Hello! FastAPI is working successfully."
    }

# User API
@app.get("/user")
def get_user():
    return {
        "id": 1,
        "name": "Raja",
        "role": "Developer" 
    }

# Addition API
@app.get("/add")
def add_numbers(a: int, b: int):
    return {
        "number1": a,
        "number2": b,
        "result": a + b
    }
