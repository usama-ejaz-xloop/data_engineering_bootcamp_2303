from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/add/{number_1}/{number_2}")
def read_item(number_1: int, number_2: int):
    return {"sum": number_1 + number_2}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
