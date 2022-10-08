import math
import pandas as pd
def trasladarValores(df,diccionario):
    for i in range(df['length'].size):
        if df['origin'][i] not in diccionario:
            diccionario[df['origin'][i]]=[]
        weight=math.sqrt((math.pow(df['length'][i],2)+math.pow(df['harassmentRisk'][i]*100,2)))
        weight=round(weight,2)
        if [df['destination'][i],weight] not in diccionario[df['origin'][i]]:
            diccionario[df['origin'][i]].append([df['destination'][i],weight])
        if not df['oneway'][i]:
            if df['destination'][i] not in diccionario:
                diccionario[df['destination'][i]]=[[df['origin'][i],weight]]
            elif [df['origin'][i],weight] not in diccionario[df['destination'][i]]:
                diccionario[df['destination'][i]].append([df['origin'][i], weight])
    return diccionario
df=pd.read_csv('calles_de_medellin_con_acoso.csv', sep=';')
df['harassmentRisk'].fillna(df['harassmentRisk'].mean(),inplace=True)
diccionario=dict()
diccionario=trasladarValores(df,diccionario)