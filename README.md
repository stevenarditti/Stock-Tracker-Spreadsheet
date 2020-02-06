
# Stock Tracker Spreadsheet

App to create csv file of key stock data for a watchlist of companies.

Pulls data from RapidAPI's Yahoo Finance API.
  

## Components
**app.py** - Main python application.

**utils.py** - Python file containing utility helper methods.

**data_mapping.json** - json file mapping each stock data field to the position in the  API json where the value is found. See [https://rapidapi.com/apidojo/api/yahoo-finance1?endpoint=apiendpoint_5bdfea14-a708-4492-a9c1-fe4b90cc3ffd](https://rapidapi.com/apidojo/api/yahoo-finance1?endpoint=apiendpoint_5bdfea14-a708-4492-a9c1-fe4b90cc3ffd) for API json structure.

**watchlist.txt** - Default watchlist. Each line should be its own stock ticker.