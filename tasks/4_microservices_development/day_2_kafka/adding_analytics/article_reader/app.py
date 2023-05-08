from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/article/<int:article_id>")
def article(article_id: int):
    return render_template("article.html", article_id=article_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
