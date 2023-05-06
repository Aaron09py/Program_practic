import pandas as pd

# Usando la funcion read_csv para leer el archivo csv
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")
#obteniendo los datos de la columna nombre
nombre = df["nombre"]

# Ordenando el DataFrame por la columna de edad
df_ordenado = df.sort_values("nombre")

#ordenandolo de forma decendente
df_ordenado = df.sort_values("nombre", ascending=False)

#concatenando los dos dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a la primeras 2 filas con head()
primeras_fila = df.head(2)

#accediendo a las ultimas 2 filas con tail()
ultimas_filas = df.tail(2)

#accediendo a la cantidad de filas y columnas con shape

filas_totales,columnas_totales= df.shape

#obteniendo data estadistica del df
df_info = df.describe()

#accediendo a un elemento especifico (edad)con iloc
df_especifico_ilock = df.iloc[2,2]

#accediendo a un elemento especifico (edad)con loc
df_especifico = df.loc[2," edad"]

#accediendo a todas las filas de una columna
apellido = df.iloc[:,1] 
#accediendo a todas las columna de una filas (loc)
fila_3 = df.loc[2,:]
#accediendo a todas las columna de una filas (iloc)
fila_3 = df.iloc[2,:]

#accediendo filas donde eddad >30 ( datos donde ["edad"] > x / ["edad"] < x ) 
edad_mayor_30 = df.loc[df[" edad"]>30,:]
print(edad_mayor_30)


 