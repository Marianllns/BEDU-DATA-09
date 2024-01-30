import pandas as pd

diccionario = {
    'A': [1,2,3],
    'B': [4,5,6],
    'C': [7,8,9]
}

print(type(diccionario))
print(diccionario)
print("----------------")

dataframe = pd.DataFrame.from_dict(diccionario)
print(type(dataframe))
print(dataframe)