import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Read the data
data = pd.read_csv('car data.csv')

# Prepare features
X = data[['Year', 'Present_Price', 'Kms_Driven', 'Owner']]
X['Year'] = 2025 - X['Year']  # Calculate car age

# Add encoded categorical features
X['Fuel_Type_Diesel'] = (data['Fuel_Type'] == 'Diesel').astype(int)
X['Fuel_Type_Petrol'] = (data['Fuel_Type'] == 'Petrol').astype(int)
X['Fuel_Type_CNG'] = (data['Fuel_Type'] == 'CNG').astype(int)
X['Seller_Type_Individual'] = (data['Seller_Type'] == 'Individual').astype(int)
X['Transmission_Manual'] = (data['Transmission'] == 'Manual').astype(int)

y = data['Selling_Price']

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
with open('car_model.pkl', 'wb') as f:
    pickle.dump(model, f) 