from flask import Flask, render_template, request

import bad_persistence


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    try:
        if request.method == "POST":
            content = request.form["content"]
            bad_persistence.add_todo_item(content)

        return render_template(
            "index.html",
            todo_items=bad_persistence.list_todo_items(request.args.get("filter", "")),
        )
    except Exception as e:
        # Normally you wouldn't get such detailed exception information - this is to help you perform the attack.
        return render_template(
            "index.html", error=e.pgerror if hasattr(e, "pgerror") else repr(e)
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
