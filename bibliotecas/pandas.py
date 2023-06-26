#importamos la librería 
import pandas as pd


#con la función .read_csv lo cargamos en la variable "df" y con nrows le decimos la cantidad que tiene que leer
df = pd.read_csv("nombre del dataframe", nrows = 1000)


df.head(10)
# mostramos las primeras 10 líneas del df 

df.tail(10)
las 10 últimas filas 

df.colums
#muestra las columnas

#df."nombre de la columna"
#enseña los datos de la columna












