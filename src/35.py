import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def load_data(file_path):
    data = pd.read_csv(file_path)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    return X, y

X, y = load_data('your_file.csv')
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(train_X, train_y)
score = model.score(test_X, test_y)
print(f"Model score: {score}")
