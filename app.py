from flask import Flask, jsonify, send_file
import yfinance as yf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/stock/<ticker>')
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1mo")
    return jsonify(data[['Open', 'High', 'Low', 'Close', 'Volume']].to_dict())

@app.route('/')
def serve_index():
    return send_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
