import numpy as np
import pandas as pd

def load_data(filename):
    df = pd.read_csv(filename)
    X = df.values
    Y = df['target'].values
    return X, Y

filename = 'data.csv'
X, Y = load_data(filename)

# Use the data for analysis or further processing
