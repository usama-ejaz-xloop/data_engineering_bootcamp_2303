import json
import logging
import threading
import time
import os

from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

logging.basicConfig(
    filename="logs.txt",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)


TODO_FILE_NAME = "todo.json"
if os.path.exists(TODO_FILE_NAME):
    with open(TODO_FILE_NAME) as f:
        TODO_ITEMS = json.load(f)
else:
    TODO_ITEMS = []


def periodically_save_todo_items():
    time.sleep(10)
    with open(TODO_FILE_NAME, "w") as f:
        json.dump(TODO_ITEMS, f)


saving_thread = threading.Thread(target=periodically_save_todo_items)
saving_thread.start()


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form["content"]
        TODO_ITEMS.append(content)

    return render_template("index.html", todo_items=TODO_ITEMS)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
