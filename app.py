from flask import Flask, jsonify, request
import yfinance as yf

# Initialize the Flask application
app = Flask(__name__)

# Define an API endpoint for fetching and predicting stock data
@app.route('/api/predict', methods=['GET'])
def get_prediction():
    # Get the stock ticker from the request URL (e.g., /api/predict?ticker=AAPL)
    ticker_symbol = request.args.get('ticker', default='AAPL', type=str)

    try:
        # Fetch historical data for the ticker using yfinance
        ticker = yf.Ticker(ticker_symbol)
        history = ticker.history(period="1mo")

        # Check if data was found
        if history.empty:
            return jsonify({"error": "No data found for this ticker"}), 404

        # For this MVP, we will simulate a "prediction" by returning recent close prices.
        # This shows the data fetching logic is in place for a future ML model.
        predicted_data = history['Close'].tail(5).tolist()

        # Return a JSON response with the stock data
        return jsonify({
            "ticker": ticker_symbol,
            "predicted_prices_next_5_days": predicted_data,
            "status": "success",
            "message": "This is a simulated prediction. The actual ML model is in development."
        })
    except Exception as e:
        # Handle any errors gracefully
        return jsonify({"error": str(e)}), 500

# Run the app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)