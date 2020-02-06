API_ENDPOINT = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-analysis"
API_KEY = "c4e383cc40msh3aef1fa6e6bc3edp16c9a8jsnf7ad84b3fe46"

import requests
import json

class Stock:

    ticker = ""
    data = {}
    # data fields needed

    def __init__(self, ticker):
        self.ticker = ticker
        self.data = self.fetch_API_data()


    def fetch_API_data(self):
        #api info needed, what is the best way to represent this?
        response = requests.get(
            API_ENDPOINT,
            headers={'X-RapidAPI-Key': API_KEY},
            params={'symbol': self.ticker}
        )
        if response:
            return response.json()
        else:
            print("Error retrieving API data for " + self.ticker)
            return json.dumps({})

    def getTicker(self):
        return self.ticker

    def getData(self):
        return self.data
