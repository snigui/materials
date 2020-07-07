from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        recData = request.get_json()
        print(recData)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=2000, debug=True)
