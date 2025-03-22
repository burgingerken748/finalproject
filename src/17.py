import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [20, 30, 40],
    'gender': ['female', 'male', 'male']
}

df = pd.DataFrame(data)
print(df)
