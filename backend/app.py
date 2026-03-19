from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

SRC_DIR = os.path.join(os.path.dirname(__file__), "..", "src")

# Load CSV files
sentence_df = pd.read_csv("sentence_to_keywords.csv")
keyword_df = pd.read_csv("keywords_to_yoga.csv")
yoga_df = pd.read_csv("yoga_to_yt.csv")

@app.route("/")
def index():
    return send_from_directory(SRC_DIR, "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(SRC_DIR, filename)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    user_text = data.get("user_text", "").lower()

    matched = sentence_df[
        sentence_df["keyword"].apply(lambda x: x in user_text)
    ]

    if matched.empty:
        return jsonify([])

    categories = matched["category"].unique()

    yoga_types = keyword_df[
        keyword_df["category"].isin(categories)
    ]["yoga_type"]

    playlist = yoga_df[
        yoga_df["yoga_type"].isin(yoga_types)
    ]

    return jsonify(playlist.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
