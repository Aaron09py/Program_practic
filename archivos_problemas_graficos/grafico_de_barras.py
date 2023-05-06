import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("archivos_problemas_graficos\\aaron.csv")

#creando graficos
sns.barplot(x="fuente",y="ingresos",data = df)

#OBTENIENDO TOTAL DE INGRESOS
total_ingreso = df["ingresos"].sum()

print(f"El total de ingresos es de: ${total_ingreso} USD")
#mostrando el grafico 
plt.show()