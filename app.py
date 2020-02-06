#!/usr/bin/env python

from stock import Stock
import utils
from pandas import DataFrame
import sys


# Enable to print additional information
DEBUG = False


companies = []
stocks = []
fields = {}

# dataframe object
df = {}

# the file where stock ticker list can be found
# defaults to companies.txt 
src_file = "companies.txt"

export_file = "export.csv" 


def debug_print(s):
    if DEBUG:
        print(s)

def bad_input():
    print("Usage: app [-f sourcefile] [-o outputfile]")
    sys.exit(0)

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

    # try to open file containing company list
    try:
        f1 = open(src_file, "r+")
        companies = f1.readlines()
        f1.close()
    except:
        bad_input()

    # try to open file containing desired fields
    try:
        f2 = open("data_mapping.json", "r+")
        fields = utils.file_to_dict(f2.readlines())
        f2.close()
    except:
        bad_input()

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
        if sys.argv[i] == "-f":
            debug_print("-f flag found")
            if i < len(sys.argv) - 1:
                src_file = sys.argv[i+1]
            else:
                bad_input()
        elif sys.argv[i] == "-o":
            debug_print("-o flag found")
            if i <len(sys.argv) - 1:
                export_file = sys.argv[i+1]
            else:
                bad_input()
    main()