# -*- coding: utf-8 -*-
"""crypto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hRYR-Moo-tPrlSRr5HO5C55xK45DHBu3
"""

# crypto_price_deploy_app.py

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the cryptocurrency price data
url = "https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=0&period2=9999999999&interval=1d&events=history"
df = pd.read_csv(url)

# Select relevant features (adjust if needed)
features = ['Open', 'High', 'Low', 'Close', 'Volume']

# Create a new DataFrame with only the selected features
data = df[features]

# Add a new column for the next day's closing price (target variable)
data['Target'] = data['Close'].shift(-1)

# Drop rows with NaN values
data = data.dropna()

# Split the data into features and target
X = data[features]
y = data['Target']

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Streamlit App
st.title("Crypto Price Prediction App")

# Sidebar with user input
st.sidebar.header("User Input")
open_price = st.sidebar.slider("Open Price", float(df['Open'].min()), float(df['Open'].max()), float(df['Open'].mean()))
high_price = st.sidebar.slider("High Price", float(df['High'].min()), float(df['High'].max()), float(df['High'].mean()))
low_price = st.sidebar.slider("Low Price", float(df['Low'].min()), float(df['Low'].max()), float(df['Low'].mean()))
close_price = st.sidebar.slider("Close Price", float(df['Close'].min()), float(df['Close'].max()), float(df['Close'].mean()))
volume = st.sidebar.slider("Volume", float(df['Volume'].min()), float(df['Volume'].max()), float(df['Volume'].mean()))

# Create a user input DataFrame with the same features as the training data
user_input = pd.DataFrame({'Open': [open_price], 'High': [high_price], 'Low': [low_price], 'Close': [close_price], 'Volume': [volume]})

# Make predictions
prediction = model.predict(user_input)

# Display the prediction
st.subheader("Prediction for Next Day's Close Price:")
st.write(f"${prediction[0]:.2f}")
#streamlit run crypty.py

#pip install streamlit