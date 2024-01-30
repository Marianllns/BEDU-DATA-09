import pandas as pd


def convertir_a_datetime(hora_militar):
    hora_militar = hora_militar.zfill(4)

    horas = int(hora_militar[:2])
    minutos = int(hora_militar[2:])

    hora_completa = f'{horas:02d}:{minutos:02d}'

    return pd.to_datetime(hora_completa, format='%H:%M')

data = {
    'hora_militar': ['0700', '1800', '2000', '1500'],
    'actividades': ['desayuno', 'gym', 'cena', 'lectura']
}

dataframe = pd.DataFrame(data)

print(dataframe.head())

print("__________________")

dataframe['fecha_hora'] = dataframe['hora_militar'].map(convertir_a_datetime)

print(dataframe.head())