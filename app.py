from flask import Flask, render_template, request, url_for, jsonify, json, redirect
import requests
import makeTable


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
        makeTable.tableData
        return jsonify(data)
    if request.method == "GET":
        #data = {"WHYYYYYYYYYYYYYYYYYYYYYYY": "KMPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"}
        data0 = requests.get('http://localhost:5000/vizier-db/api/v1/projects/12020d28/datasets/6070d166f8f846c2a609cdb0ea65ad12').content
        loadedData = json.loads(data0)
        data = loadedData["columns"]
        #data = cache["first"]
        print("from GET!")
        print(cache)
        print("length!!", makeTable.tableData(loadedData))
        #print(loadedData["columns"])
        return render_template("output.html", data=loadedData)
    return render_template("output.html")

@app.route("/output", methods=["GET"])
def output():
    if request.method=="GET":
        dataOutput = request.json
        return jsonify(dataOutput)


if __name__ == "__main__":
    app.run(host="localhost", port=2000, debug=True)
