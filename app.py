from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

ivol_data = {
    "GOOG": {
        "prior_close": 189.95,
        "upper": 197.01,
        "lower": 182.89,
        "two_sigma_upper": 204.07,
        "two_sigma_lower": 175.83
    }
}

@app.route('/data')
def get_data():
    symbol = request.args.get('symbol')
    data = ivol_data.get(symbol.upper())
    if not data:
        return "na"
    return f"{data['prior_close']},{data['upper']},{data['lower']},{data['two_sigma_upper']},{data['two_sigma_lower']}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets this automatically
    app.run(host="0.0.0.0", port=port)
