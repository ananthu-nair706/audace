import requests
from datetime import datetime

# CoinGecko API URL for market data
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/markets"

# Define the parameters to fetch ETH/USDT data in both USD and INR
params = {
    "vs_currency": "usd,inr",      # Retrieve prices in both USD and INR
    "ids": "ethereum",             # ID for the token, e.g., "ethereum" for ETH
    "order": "market_cap_desc",    # Sort by market cap
    "per_page": 1,                 # Limit results
    "page": 1,                     # Page number
    "sparkline": "false",          # No sparkline data
    "price_change_percentage": "24h"  # Get 24h price change
}

def fetch_data():
    try:
        # Send request to CoinGecko API
        response = requests.get(COINGECKO_API_URL, params=params)
        
        # Check for a successful response
        if response.status_code == 200:
            data = response.json()
            return data[0] if data else None
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def parse_data(data):
    try:
        # Extract relevant fields from the response
        token_name = data['name']
        symbol = data['symbol'].upper()
        current_price_usd = data['current_price']['usd']
        current_price_inr = data['current_price']['inr']
        market_cap_usd = data['market_cap']['usd']
        market_cap_inr = data['market_cap']['inr']
        total_volume_usd = data['total_volume']['usd']
        total_volume_inr = data['total_volume']['inr']
        price_change_24h = data['price_change_percentage_24h']
        
        # Display the metrics
        print(f"Token: {token_name} ({symbol})")
        print(f"Current Price (USD): ${current_price_usd:,.2f}")
        print(f"Current Price (INR): ₹{current_price_inr:,.2f}")
        print(f"Market Cap (USD): ${market_cap_usd:,.2f}")
        print(f"Market Cap (INR): ₹{market_cap_inr:,.2f}")
        print(f"24-Hour Volume (USD): ${total_volume_usd:,.2f}")
        print(f"24-Hour Volume (INR): ₹{total_volume_inr:,.2f}")
        print(f"24-Hour Price Change: {price_change_24h:.2f}%")
        
    except KeyError as e:
        print(f"Error in data structure: {e}")
    except Exception as e:
        print(f"An error occurred while parsing data: {e}")

if __name__ == "__main__":
    # Fetch data from the API
    data = fetch_data()
    
    # Parse and display the data if it was successfully fetched
    if data:
        parse_data(data)
