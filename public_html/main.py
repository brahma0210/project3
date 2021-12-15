from flask import Flask, render_template, request, json, jsonify
import pandas as pd
from calculations import *

app = Flask(__name__)





@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/F1_Layout", methods=["GET"])
def f1layout():
    return render_template("F1_Layout.html")

@app.route("/F2_Layout", methods=["GET"])
def f2layout():
    return render_template("F2_Layout.html")

@app.route("/oops", methods=["GET"])
def oops():
    return render_template("oops.html")

@app.route("/history", methods=["GET"])
def history():
    data = pd.read_csv("calculations.csv")
    return render_template("history.html", history = data.iterrows())

def isInvalid_calculate(req_data):
    if not "num1" in req_data or not isinstance(req_data["num1"], int):
        return True
    if not "num2" in req_data or not isinstance(req_data["num1"], int):
        return True
    if not "type" in req_data or not isinstance(req_data["type"], str):
        return True
    return False

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    error = isInvalid_calculate(data)

    if not error:
        result = None
        if data["type"] == "addition":
            result = addition(data["num1"], data["num2"])
        elif data["type"] == "substraction":
            result = subtraction(data["num1"], data["num2"])
        elif data["type"] == "multiplication":
            result = multiplication(data["num1"], data["num2"])
        elif data["type"] == "division":
            result = division(data["num1"], data["num2"])
            
        if result is not None:
            calculation = pd.DataFrame([[data["num1"], data["num2"], data["type"], result]], columns=['num1', 'num2', "type", "result"])
            calculation.to_csv("calculations.csv", mode='a', index=False, header=False)
            return jsonify({ "success": True, "result": result })

    return jsonify({ "success": False, "error": "Invalid data" })



if __name__ == "__main__":
    app.run(debug=True)