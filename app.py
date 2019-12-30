#!/usr/bin/env python3

from openpyxl import Workbook
import sys

# True to print debug info, False to ignore
DEBUG = True

def init_workbook():
    global companies, wb
    f = open(src_file, "r+")
    companies = f.readlines()
    f.close()
    wb = Workbook()
    ws = wb.active
    ws["A1"] = "Company"
    ws["B1"] = "Price"
    ws["C1"] = "Prev Close Price"
    ws["D1"] = "Market Cap"
    ws["E1"] = "P/E"
    wb.save(save_file)

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
    
    init_workbook()
    #add_companies()

