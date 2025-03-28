from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/population")
def get_population():
    try:
        with open("population_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return "World Population API is running. Use /population to fetch data."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
