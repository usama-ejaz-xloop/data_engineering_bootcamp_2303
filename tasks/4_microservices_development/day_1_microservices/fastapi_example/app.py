from fastapi import FastAPI

app = FastAPI()


@app.get("/add/{number_1}/{number_2}")
def read_item(number_1: int, number_2: int):
    return {"sum": number_1 + number_2}
