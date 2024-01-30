import pandas as pd

data = {'A': [1, 2, 2, 3, 4], 'B': ['x', 'y', 'y', 'z', 'z']}
dataframe = pd.DataFrame(data)

print(dataframe.head())

print("__________________")

dupes_in_A =dataframe[dataframe.duplicated(subset='A')]

print(dupes_in_A)

print("__________________")
dupes_in_B =dataframe[dataframe.duplicated(subset='B')]

print(dupes_in_B)

print("__________________")

no_dupes_A =dataframe.drop_duplicates(subset='A')
print(no_dupes_A)

print("__________________")

no_dupes_B =dataframe.drop_duplicates(subset='B')
print(no_dupes_B)