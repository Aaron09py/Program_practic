#cambair tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas_simples\\datos.csv")
#comvertir a string los daos de una columna
df[' edad'] = df[' edad'].astype(str)

#mostras el tipo de dato de la primera columna de edad
#print(type(df[" edad"][0]))

#remplazando dato "aaron" por "good"( rempazarndo dato (x) por (x))
df['nombre'].replace("aaron", "good",inplace=True)

#eliminando las filas con datos vacios

df = df.dropna()

#eliminando filas con datos repetidos
df = df.drop_duplicates()

#creando un CSv con e df limpio
df.to_csv("archivos_problemas_simples\\datos_limpios.csv")