API_ENDPOINT = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-analysis"
API_KEY = "c4e383cc40msh3aef1fa6e6bc3edp16c9a8jsnf7ad84b3fe46"

import requests
import json

class Stock:

    ticker = ""
    name = ""
    # data fields needed

    def __init__(self, ticker):
        self.ticker = ticker
        data = self.fetch_data()
        print(data["price"])
        print(data["price"]["shortName"])
        name = data["price"]["shortName"]

    def fetch_data(self):
        #api info needed, what is the best way to represent this?
        response = requests.get(
            API_ENDPOINT,
            headers={'X-RapidAPI-Key': API_KEY},
            params={'symbol': self.ticker}
        )
        if (response.status_code == 200):
            return response.json()
        else:
            return json.dumps({})

    def getName(self):
        return self.name
