from pandas_datareader import data as pdr
import pandas as pd
import csv
import os
from pandas_datareader import DataReader
from datetime import datetime

data = DataReader('SPY',  'yahoo', datetime(2008, 1, 1), datetime(2019, 4, 3))
# length = len(data.index)
# listOfTicker = ['SPY'] * length
# data['name'] = listOfTicker
# data2 = DataReader('MSFT',  'yahoo', datetime(2008, 1, 1), datetime(2019, 1, 1))
# frames = [data, data2]
# data = pd.concat(frames)
# print(data.head())
# print(data.tail())


# print(data.head())
# print(data2.head())

# counter = 0 
# for line in file:
#     counter += 1
#     print(counter)
#     tic = str(line.split()[0])
    
#     try:
#         data2 = DataReader(tic,  'yahoo', datetime(2008, 1, 1), datetime(2019, 1, 1))
#         length = len(data2.index)
#         listOfTicker = [tic] * length
#         data2['name'] = listOfTicker
#         frames = [data, data2]
#         data = pd.concat(frames)
#     except:
#         print("couldn't find ticker")

data.to_csv("yahoo.txt", sep=',')