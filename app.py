#!/usr/bin/env python36

from stock import Stock
import utils
from pandas import DataFrame
import sys

companies = []
stocks = []
fields = {}

# dataframe object
df = {}

# the file where stock ticker list can be found
# defaults to companies.txt 
src_file = "companies.txt"

export_file = "export.csv" 


# exports data as a csv
def export_to_csv():
    df.to_csv(export_file)

# creates the DataFrame object from the stock list
def create_dataframe():
    global df

    # initialize data dictionary with header names
    data = {}
    for name in fields:
        data[name] = []

    # iterate through each stock
    for stock in stocks:
        stock_data = stock.getData()

        # iterate through desired fields
        for name in fields:
            # fields[name] specifies how to access intended value from the dict structure
            # value can be pulled from stock_data using eval
            val = eval("stock_data" + fields[name])
            data[name].append(val)
            
    # create a DataFrame out of the pulled data
    df = DataFrame(data)
    df = df.set_index("Name") 


# fetches stock data for each company in src_file
def init_stocks():
    global fields

    # open file containing company list 
    f1 = open(src_file, "r+")
    companies = f1.readlines()
    f1.close()

    # open file containing desired fields
    f2 = open("data_mapping.json", "r+")
    fields = utils.file_to_dict(f2.readlines())
    f2.close()

    # each stock will fetch data upon initialization
    for ticker in companies:
        stocks.append(Stock(ticker))


def main():
    init_stocks()
    create_dataframe()
    export_to_csv()


if __name__ == "__main__":

    # argument parsing
    for i in range(1, len(sys.argv)):
        
        # -f flag specifies the source file of the stock list
        if len(sys.argv) < i + 1:
            if sys.argv[i] == "-f":
                src_file = sys.argv[i+1]
                i += 1
            if sys.argv[i] == "-o":
                export_file = sys.argv[i+1]
                i += 1
        else:
            print("Usage: app [-f sourcefile]")
            sys.exit(0)
    main()