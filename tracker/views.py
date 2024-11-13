from django.shortcuts import render
from .models import TokenData
from django.http import HttpResponse
# Create your views here.
import json
from datetime import datetime
import requests
from django.shortcuts import render
from django.http import JsonResponse

# def fetch_historical_data(token_id="ethereum", vs_currency="usd", days="365"):
#     url = f"https://api.coingecko.com/api/v3/coins/ethereum/market_chart"
#     params = {
#         "vs_currency": vs_currency,
#         "days": days,  # "30" for 30 days; "1" for 24 hours; "max" for max available data
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     return data


# def format_for_d3(data):
#     formatted_data = []

#     for i in range(len(data['prices'])):
#         timestamp = data['prices'][i][0] / 1000  # Convert to seconds
#         date = datetime.fromtimestamp(timestamp).isoformat()
#         price = data['prices'][i][1]
#         volume = data['total_volumes'][i][1]
#         market_cap = data['market_caps'][i][1]

#         formatted_data.append({
#             "date": date,
#             "price": price,
#             "volume": volume,
#             "market_cap": market_cap
#         })

#     return json.dumps(formatted_data)  # Convert to JSON for frontend


# def chart_view(request):
#     data = fetch_historical_data()
#     formatted_data = format_for_d3(data)
#     return JsonResponse(formatted_data, safe=False)  # JSON response for D3

# def render_chart(request):
#     return render(request, 'templates/chart.html')

# tracker/views.py
import requests
import json
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render

def render_chart(request):
    # Fetch data from CoinGecko API
    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "365",  # Change to "30" for 30 days; "1" for 24 hours; "max" for max available data
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Format data for D3
        formatted_data = []
        for i in range(len(data['prices'])):
            timestamp = data['prices'][i][0] / 1000  # Convert to seconds
            date = datetime.fromtimestamp(timestamp).isoformat()
            price = data['prices'][i][1]
            volume = data['total_volumes'][i][1]
            market_cap = data['market_caps'][i][1]

            formatted_data.append({
                "date": date,
                "price": price,
                "volume": volume,
                "market_cap": market_cap
            })

        # Pass formatted data to template as JSON
        context = {
            "chart_data": json.dumps(formatted_data)  # Convert to JSON for the frontend
        }
        import pdb; pdb.set_trace()
        return render(request, "templates/chart.html", context)

    # Handle API error if response code is not 200
    return JsonResponse({"error": "Failed to fetch data from CoinGecko"}, status=500)
