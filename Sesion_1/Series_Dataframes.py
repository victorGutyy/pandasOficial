# Importamos la biblioteca panda y la llamamos pd
import pandas as pd
# creamos una serie de pandas que es como una lista con etiquetas
# los valores son nombres de jugadores de PSG
# el indice especifica los numeros de camisetas de esos jugadores

psg_players = pd.Series (
    ['Navas', 'Mbappe', 'Neymar', 'Messi']#, # Lista de jugadores
#    index = [1, 7, 10, 30] # Lista de Camisetas
)

# creamos un diccionario que asocia numeros de camisetas con nombre de jugadores
psg_dict = { 1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi'}

# cremos una serie de pandas usando el diccionario
psg_players_dict = pd.Series(psg_dict)

# Imprimimos la serie creada a partir del diccionario
print(psg_players_dict)

# imprimimos la serie creada a partir del diccionario
print(psg_players_dict[7])
print(psg_players_dict[0:3])


# Diccionario con datos de jugadores
dict = { 'jugador': ['Navas', 'Mbappe', 'Neymar', 'Messi'],
        'Altura': [183.0, 170.0, 170.0, 165.0],
        'Goles': [2, 200, 150, 200]}

# Crear un Dataframe con el diccionario y indices personalizados
df = pd.DataFrame(dict, index=[1,7, 10, 30])

# imprimir el DataFrame
print(df)