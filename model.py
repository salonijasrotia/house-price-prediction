import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("house_data.csv")

X = data[['area', 'bedrooms', 'age']]
y = data['price']

model = LinearRegression()
model.fit(X, y)

def predict_price(area, bedrooms, age):
    return model.predict([[area, bedrooms, age]])[0]