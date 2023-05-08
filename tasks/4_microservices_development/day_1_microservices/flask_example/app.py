from flask import Flask

app = Flask(__name__)


@app.route("/add/<int:number_1>/<int:number_2>/")
def main(number_1: int, number_2: int):
    return {"sum": number_1 + number_2}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
