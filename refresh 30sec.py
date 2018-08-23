import json
import pandas as pd
import urllib.request
from pandas.io.json import json_normalize
import time
import urllib.request, urllib.error, urllib.parse
import datetime
import threading


def createTimeString():
    curr_Time = datetime.datetime.now() # get current timestamp
    curr_Time = 'Date[{0:%x}] Time[{0:%X}]'.format(curr_Time) # convert to readable form
    return curr_Time # return time as string


donnes1=pd.read_json("https://www.cryptopia.co.nz/api/GetMarkets/BTC/1")
b1=json_normalize(donnes1["Data"])
c1=b1[["Label","AskPrice","BidPrice","BaseVolume"]]
d1=c1.set_index('Label')


for i in range(180):
    
    

    donnes2=pd.read_json("https://www.cryptopia.co.nz/api/GetMarkets/BTC/1")
    b2=json_normalize(donnes2["Data"])
    c2=b2[["Label","AskPrice","BidPrice","BaseVolume"]]
    d2=c2.set_index('Label')

    d=100*(d2-d1)/d1
#   mise a jour chaque iteration!!
    d1=d2
    time_string = createTimeString()
    print(time_string)
    print((d["AskPrice"].idxmax()),"----AskPrice %------->",(d["AskPrice"][d["AskPrice"].idxmax()]))
    print((d["BidPrice"].idxmax()),"----BidPrice %------->",(d["BidPrice"][d["BidPrice"].idxmax()]))
    print((d["BaseVolume"].idxmax()),"----BaseVolume %----->",(d["BaseVolume"][d["BaseVolume"].idxmax()]))
    print("")
    #print("Total Cryptopia Volume (1 HOUR) is :",d2[["BaseVolume"]].sum())
       
