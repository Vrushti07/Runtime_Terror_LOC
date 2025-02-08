import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

df = pd.read_csv("ngo_demand.csv", parse_dates=["Date"], index_col="Date")
df = df[["Quantity (kg)"]]

scaler = MinMaxScaler()
df["Quantity (kg)"] = scaler.fit_transform(df)

SEQ_LENGTH = 10
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i : i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

data = df.values.flatten()
X, y = create_sequences(data, SEQ_LENGTH)

X = X.reshape((X.shape[0], X.shape[1], 1))
y = y.reshape(-1, 1)

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(SEQ_LENGTH, 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(25, activation="relu"),
    Dense(1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=20, batch_size=16)

model.save("lstm_food_demand.h5")
