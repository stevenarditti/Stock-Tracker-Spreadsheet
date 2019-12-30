#!/usr/bin/env python3

import sys

# True to print debug info, False to ignore
DEBUG = True

if __name__ == "__main__":
    ii = 0 
    while len(sys.argv) > ii:
        if sys.argv[ii] == "-p" and len(sys.argv) > ii + 1:
            src_file = sys.argv[ii+1]
            try:
                save_file = src_file.split(".")[0] + ".xlsx"
            except:
                save_file = src_file + ".xlsx" 
        ii+=1
    
    #utils.getStockData("appl")
    #init_workbook()
    #add_companies()

