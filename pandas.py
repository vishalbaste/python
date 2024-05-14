import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

df = pd.read_csv('data.csv')

min_age = df['Age'].min()
max_age = df['Age'].max()
median_age = df['Age'].median()