from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)
DATA_FOLDER = "data"

@app.route("/data", methods=["GET"])
def get_data():
    file = request.args.get("file")
    if not file:
        return jsonify({"error": "Missing 'file' parameter"}), 400

    path = os.path.join(DATA_FOLDER, file)
    if not os.path.exists(path):
        return jsonify({"error": f"File '{file}' not found"}), 404

    df = pd.read_csv(path)
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
