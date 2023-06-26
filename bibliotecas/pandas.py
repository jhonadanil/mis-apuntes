#importamos la librería 
import pandas as pd

#con la función .read_csv lo cargamos en la variable "df" y con nrows le decimos la cantidad que tiene que leer
df = pd.read_csv("nombre del dataframe", nrows = 1000)


df.head()
# mostramos las primeras 5 líneas del df 








