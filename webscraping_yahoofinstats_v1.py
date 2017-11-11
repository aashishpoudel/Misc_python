# -*- coding: utf-8 -*-

#### Authors - Aashish and Sandeep ###

import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

"""
#response = urlopen("https://api.github.com/users?since=100")
response = urlopen("https://finance.yahoo.com/quote/NVDA/key-statistics?p=NVDA")
response_json = response.read().decode('utf-8')
print(response_json)
# remember loads takes response.read() while load takes only response
"""


# Source: http://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined
# This function is necessary. Else, UTF-8 encoding issue is seen while printing
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

#uprint('foo')
#uprint('Antonín Dvořák')
#uprint('foo', 'bar', u'Antonín Dvořák')

#url = "https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL"

tickers = ["MSFT", "AAPL", "NVDA", "AMZN", "TSLA"]  #MANAT
#urls = ["https://finance.yahoo.com/quote/"+x+"/key-statistics?p="+x for x in tickers]
def get_url(ticker):
    return "https://finance.yahoo.com/quote/"+ticker+"/key-statistics?p="+ticker

page = urlopen(get_url(tickers[0])) #testing for NVDA
soup = BeautifulSoup(page.read(), 'html.parser')
count = 0
count_line = 0
for line in soup:
    count += 1
    if count == 2:
        final_page = str(line)


tempstr = final_page.split("root.App.main")[1].strip().split("(this)")[0].strip()
print("\n", len(tempstr))

jsonstrinng = tempstr[2:len(tempstr)-3]
jsondata = json.loads(jsonstrinng)
print("\n\n\n")
#print(jsondata["context"])  # using print will throw errors


"""
# later we can use exception as below form
struct = {}
try: #try parsing to dict
    dataform = str(response_json).strip("'<>() ").replace('\'', '\"')
    struct = json.loads(dataform)
except:
    #print(response_json)
    print(sys.exc_info())
finally:
    pass
"""

"""
# WORKS FOR api.github.com website but not for yahoo statistics

response = urlopen("https://api.github.com/users?since=100")
#response = urlopen("https://finance.yahoo.com/quote/NVDA/key-statistics?p=NVDA")
#just doing json.load(response.read()) produces error ERROR - TypeError: the JSON object must be str, not 'bytes'

str_response = response.read().decode('utf-8')
webdata_in_str = json.loads(str_response)
# for some webpage like yahoo stats, it throws error saying "# for some webpage like yahoo stats, it throws error saying"
# the issue occurs if i)non-JSON conforming quoting ii) XML/HTML output (that is, a string starting with <)
# iii) incompatible character encoding
# so for any webpage this is an issue since any webpage contains <html>, only separating json string will help

print(webdata_in_str)
"""

"""
import requests
r = requests.get(url)
print(r.json())
"""

"""
with open('data.json') as data_file:
    data = json.load(data_file)
pprint(data)
"""

"""
ISSUES
 - "LANG_MANDARIN_LABEL":"普通话"
 - '\u002F'
 - Solution: i) use uprint ii) mention coding comment in the first line ==> # -*- coding: utf-8 -*-
"""

"""
Interested in
context > dispatcher > stores > QuoteSummaryStore > summaryDetail > marketCap > fmt: 57.53B
context > dispatcher > stores > QuoteSummaryStore > summaryDetail > fiftyTwoWeekLow > fmt: 24.75
context > dispatcher > stores > QuoteSummaryStore > summaryDetail > trailingPE > fmt: 70.13
context > dispatcher > stores > QuoteSummaryStore > summaryDetail > fiftyTwoWeekHigh > fmt: 119.93
context > dispatcher > stores > QuoteSummaryStore > price > averageDailyVolume10Day > fmt: 30.15M

"marketCap":{"raw":57532858368,"fmt":"57.53B","longFmt":"57,532,858,368"}
"""

root_var_string = str(jsondata)
root_var_dict = eval(root_var_string)

def filter_non_printable(str):
  return ''.join([c for c in str if ord(c) > 31 or ord(c) == 9])


def gen_space(level):
    mystr = "    "
    for i in range(level):
        mystr += "    "
    return mystr


def myprint(d, level):
    lvl = level
    num_of_keys=1
    mystr = gen_space(lvl)
    for k, v in d.items():
        if isinstance(v, dict):
            lbl = lvl
            lbl += 1
            num_of_keys += 1
            mystr = gen_space(lvl)
            #print(mystr, str(k), ": ", "levelstr", str(lvl))
            #print(mystr, str(k), ": ")
            print_string = mystr + str(k) +": "
            uprint(print_string)
            myprint(v, lbl)
        else:
            lbl = lvl
            mystr = gen_space(lbl)
            #print(mystr, str(k), ":", v, "level", str(lbl))
            print_string = mystr + str(k) +": " + str(v)
            uprint(print_string)
            #print(mystr, str(k), ":", str(v))

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
            #uprint(print_string)
            #print(mystr, str(k), ":", str(v))


#myprint(new_var_dict, 1)
keystats_list = ["marketCap", "fiftyTwoWeekLow", "trailingPE", "fiftyTwoWeekHigh", "averageDailyVolume10Day"]

for keystats in keystats_list:
    findstats(root_var_dict, keystats)

