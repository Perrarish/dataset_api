from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return "Dataset API is running!"

@app.route("/data")
def get_data():
    df = pd.read_csv("dataset.csv")  # rename your file to dataset.csv
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
