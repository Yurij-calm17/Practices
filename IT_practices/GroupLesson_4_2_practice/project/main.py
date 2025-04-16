

from fastapi import FastAPI, HTTPException

app = FastAPI()

myList = [12, 34, 346, 552, 347]  # Оголошуємо список ДО функцій, які його використовують

@app.get("/")
def f1():
    return "Hello world"

@app.get("/id")
def f2():
    return {"id": None, "counts": myList}

@app.get("/id/{id}")
def f3(id: int):
    if id < 0 or id >= len(myList):
        raise HTTPException(status_code=404, detail="ID out of range")
    return {"id": id, "counts": myList[id]}
