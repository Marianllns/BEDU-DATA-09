import pandas as pd

data = {'A': [1, 2, 2, 3, 4], 'B': ['x', 'y', 'y', 'z', 'z']}
dataframe = pd.DataFrame(data)

print(dataframe.head())

print(dataframe.duplicated())

duplicates = dataframe[dataframe.duplicated()]

print(duplicates)

no_dupes = dataframe.drop_duplicates()
print(no_dupes)