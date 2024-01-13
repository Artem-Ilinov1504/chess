from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/figure")
def figure():
    return render_template("figure.html")



if __name__ == "__main__":
    app.run(debug=True)