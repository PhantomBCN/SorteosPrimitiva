# Importar la librería pandas y leer el archivo CSV con los datos de la Primitiva
import pandas as pd
df = pd.read_csv('SorteosPrimitiva_SinJOKER_CSV.csv', 
                 sep=';', 
                 names=['Fecha', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'Complementario', 'Reintegro'], 
                 parse_dates=['Fecha'], 
                 dayfirst=True, 
                 dtype={'N1': str, 'N2': str, 'N3': str, 'N4': str, 'N5': str, 'N6': str, 'Complementario': str, 'Reintegro': str}, 
                 header=None)

# Crear un diccionario para contar las repeticiones de cada número en los sorteos
repeticiones = {str(num).zfill(2): 0 for num in range(1, 50)}

df_resultados = pd.DataFrame(columns=['Fecha', 'Combinación', 'Aciertos'])

# Definir las combinaciones de números a jugar
J1, J2, J3, J4, J5, J6 = "05 19 21 27 33 35".split()
K1, K2, K3, K4, K5, K6 = "06 11 26 34 40 48".split()
i=0
nueva_fila = ""

# Contar los aciertos para cada combinación de números en cada sorteo y mostrar los resultados si hay más de 2 aciertos
aciertos1, aciertos2 = 0, 0
for index, row in df.iterrows():
    valores = row[['N1', 'N2', 'N3', 'N4', 'N5', 'N6']].tolist()
    for valor in valores:
        repeticiones[valor] += 1
    if J1 in valores:
        aciertos1 += 1
    if J2 in valores:
        aciertos1 += 1
    if J3 in valores:
        aciertos1 += 1
    if J4 in valores:
        aciertos1 += 1
    if J5 in valores:
        aciertos1 += 1
    if J6 in valores:
        aciertos1 += 1
    if K1 in valores:
        aciertos2 += 1
    if K2 in valores:
        aciertos2 += 1
    if K3 in valores:
        aciertos2 += 1
    if K4 in valores:
        aciertos2 += 1
    if K5 in valores:
        aciertos2 += 1
    if K6 in valores:
        aciertos2 += 1

    if aciertos1 > 2:
        nueva_fila = [row['Fecha'], '1', aciertos1]
        df_resultados.loc[len(df_resultados)]=nueva_fila
    if aciertos2 > 2:
        nueva_fila = [row['Fecha'], '2', aciertos2]
        df_resultados.loc[len(df_resultados)]=nueva_fila
    aciertos1, aciertos2 = 0, 0
print("3 aciertos : {}".format(len(df_resultados.query("Aciertos == 3"))))
print("4 aciertos : {}".format(len(df_resultados.query("Aciertos == 4"))))
print("5 aciertos : {}".format(len(df_resultados.query("Aciertos == 5"))))
print("6 aciertos : {}".format(len(df_resultados.query("Aciertos == 6"))))