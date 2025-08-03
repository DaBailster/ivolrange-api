from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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
