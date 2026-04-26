from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
# Explicitly open CORS for the frontend domain
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
BASE_DIR = os.path.dirname(__file__)
PROD_DIR = os.path.join(BASE_DIR, "..", "dist")
DEV_DIR = os.path.join(BASE_DIR, "..", "src")
SRC_DIR = PROD_DIR if os.path.exists(PROD_DIR) else DEV_DIR

# Load CSV files
sentence_df = pd.read_csv(os.path.join(BASE_DIR, "sentence_to_keywords.csv"))
keyword_df = pd.read_csv(os.path.join(BASE_DIR, "keywords_to_yoga.csv"))
yoga_df = pd.read_csv(os.path.join(BASE_DIR, "yoga_to_yt.csv"))

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
