# -*- coding: utf-8 -*-
"""acrypto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A-qfv-LVe0CZKcKN57eSeNGf4F8hAYJc
"""

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pickle

url = "https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=0&period2=9999999999&interval=1d&events=history"
df = pd.read_csv(url)

features = ['Open', 'High', 'Low', 'Close', 'Volume']

data = df[features]

data['Target'] = data['Close'].shift(-1)

data = data.dropna()

X = data[features]
y = data['Target']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the trained model to a pickle file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

st.title("Crypto Price Prediction App")

st.sidebar.header("User Input")
open_price = st.sidebar.slider("Open Price", float(df['Open'].min()), float(df['Open'].max()), float(df['Open'].mean()))
high_price = st.sidebar.slider("High Price", float(df['High'].min()), float(df['High'].max()), float(df['High'].mean()))
low_price = st.sidebar.slider("Low Price", float(df['Low'].min()), float(df['Low'].max()), float(df['Low'].mean()))
close_price = st.sidebar.slider("Close Price", float(df['Close'].min()), float(df['Close'].max()), float(df['Close'].mean()))
volume = st.sidebar.slider("Volume", float(df['Volume'].min()), float(df['Volume'].max()), float(df['Volume'].mean()))

user_input = pd.DataFrame({'Open': [open_price], 'High': [high_price], 'Low': [low_price], 'Close': [close_price], 'Volume': [volume]})

prediction = model.predict(user_input)

st.subheader("Prediction for Next Day's Close Price:")
st.write(f"${prediction[0]:.2f}")

#!pip install streamlit