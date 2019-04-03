import os
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import datetime as dt
import urllib.request, json
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

# df = pd.read_csv(os.path.join('Stocks','hpq.us.txt'),delimiter=',',usecols=['Date','Open','High','Low','Close'])
df = pd.read_csv('yahoo.txt',delimiter=',',usecols=['Date','High','Low','Open','Close', 'Volume', 'Adj Close'])
print('Loaded data from the Kaggle')

df = df.sort_values('Date')
print(df.head())

# #Visualization

# plt.figure(figsize = (18,9))
# plt.plot(range(df.shape[0]),(df['Low']+df['High'])/2.0)
# plt.xticks(range(0,df.shape[0],500),df['Date'].loc[::500],rotation=45)
# plt.xlabel('Date',fontsize=18)
# plt.ylabel('Mid Price',fontsize=18)
# plt.show()

#Breaking the data into train and test and normalizing the data

# First calculate the mid prices from the highest and lowest 
high_prices = df.loc[:,'High'].values
low_prices = df.loc[:,'Low'].values
mid_prices = (high_prices+low_prices)/2.0

# div = int(2770/2)
div = int(len(df) - 1)
print (div)

#Breaking into train and test
train_data = mid_prices[div-100:div]
test_data = mid_prices[div:]

# Scale the data to be between 0 and 1
# When scaling remember! You normalize both test and train data w.r.t training data
# Because you are not supposed to have access to test data
# scaler = MinMaxScaler()
# train_data = train_data.reshape(-1,1)
# test_data = test_data.reshape(-1,1)

# Train the Scaler with training data and smooth data 
# smoothing_window_size = 25
# for di in range(0,80,smoothing_window_size):
#     scaler.fit(train_data[di:di+smoothing_window_size,:])
#     train_data[di:di+smoothing_window_size,:] = scaler.transform(train_data[di:di+smoothing_window_size,:])

# You normalize the last bit of remaining data 
# scaler.fit(train_data[di+smoothing_window_size:,:])
# train_data[di+smoothing_window_size:,:] = scaler.transform(train_data[di+smoothing_window_size:,:])

# Reshape both train and test data
# train_data = train_data.reshape(-1)

# Normalize test data
# test_data = scaler.transform(test_data).reshape(-1)


# Now perform exponential moving average smoothing
# So the data will have a smoother curve than the original ragged data
# EMA = 0.0
# gamma = 0.1
# for ti in range(div):
#   EMA = gamma*train_data[ti] + (1-gamma)*EMA
#   train_data[ti] = EMA

# Used for visualization and test purposes
all_mid_data = np.concatenate([train_data,test_data],axis=0)
