from flask import Flask, render_template, request, url_for, jsonify, json, redirect


app = Flask(__name__)
cache = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST", "GET"])
def add():
    #cache["first"] = json.loads(request.json)
    if request.method == "POST":
        data = request.json
        global cache
        cache = data
        print("from POST")
        print(data)
        print(cache["descriptors"])
        return jsonify(data)
    if request.method == "GET":
        #data = {"WHYYYYYYYYYYYYYYYYYYYYYYY": "KMPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"}
        #data = cache["first"]
        print("from GET!")
        print(cache)
        return render_template("output.html", cache=cache)
    return render_template("output.html")

@app.route("/output", methods=["GET"])
def output():
    if request.method=="GET":
        dataOutput = request.json
        return jsonify(dataOutput)


if __name__ == "__main__":
    app.run(host="localhost", port=2000, debug=True)
