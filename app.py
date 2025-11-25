from flask import Flask, jsonify, send_file
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return "Dataset API is running!"

# Serve dataset as JSON
@app.route("/data")
def get_data():
    df = pd.read_csv("dataset.csv")
    return jsonify(df.to_dict(orient="records"))

# Serve dataset as raw CSV (FIX!)
@app.route("/dataset.csv")
def serve_csv():
    return send_file("dataset.csv", mimetype="text/csv")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
