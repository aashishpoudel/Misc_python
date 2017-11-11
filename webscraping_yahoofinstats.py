# -*- coding: utf-8 -*-

#### Authors - Aashish and Sandeep ###

import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

tickers = ["MSFT", "AAPL", "NVDA", "AMZN", "TSLA"]  #MANAT
keystats = ["marketCap", "fiftyTwoWeekLow", "trailingPE", "fiftyTwoWeekHigh", "averageDailyVolume10Day"]

def get_url(ticker):
    return "https://finance.yahoo.com/quote/"+ticker+"/key-statistics?p="+ticker

def get_ticker_jsonstring(ticker):
    page = urlopen(get_url(ticker))
    soup = BeautifulSoup(page.read(), 'html.parser')
    count = 0
    for line in soup:
        count += 1
        if count == 2:
            final_page = str(line)
    tempstr = final_page.split("root.App.main")[1].strip().split("(this)")[0].strip()
    tempstr = tempstr[2:len(tempstr)-3]
    jsondata = json.loads(tempstr)
    json_string = str(jsondata)
    return json_string

"""
Interested in
context > dispatcher > stores > QuoteSummaryStore > summaryDetail > marketCap > fmt: 57.53B
context > dispatcher > stores > QuoteSummaryStore > price > averageDailyVolume10Day > fmt: 30.15M
"marketCap":{"raw":57532858368,"fmt":"57.53B","longFmt":"57,532,858,368"}
"""

def findstats(d, keystats):
    for k, v in d.items():
        if isinstance(v, dict):
            if keystats in k:
                print_string = str(k) + ": "
                print(print_string)
                print(v["fmt"])
            else:
                findstats(v, keystats)
        else:
            pass
            #print_string = str(k) +": " + str(v) + "\n"
            #print(mystr, str(k), ":", str(v))


for ticker in tickers:
    print("\nPrinting stats for " + str(ticker))
    ticker_string = get_ticker_jsonstring(ticker)
    ticker_dict = eval(ticker_string)
    for keystat in keystats:
        findstats(ticker_dict, keystat)

