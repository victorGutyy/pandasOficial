# importa la libreria pandas, que es fundamental para el analisis de datos.
import pandas as pd

# define la ruta del archivo CSV que contiene los datos.
# si el archivo esta en el mismo directorio que el script, basta con poner el nombre del archivo.
path = 'Online_Retail.csv'

# lee el archivo CSV usando la funcion 'read_csv' de pandas.
# se especifica la codificacion 'latin1' (tambien conocidod como ISO-8859-1) para manejar caracteres especiales
retail_data = pd.read_csv(path, encoding='latin1')

# muestra el tipo de la variable 'retail_data' para confirmar que es DataFrame
# un DataFrame es una estructura de datos bidimensional (filas y columnas) similar a una tabla.
print(type(retail_data))

# imprime todo el contenido del DataFrame 'retail_data para visualizar los datos que fueron leidos del archivo CSV.
print(retail_data)
