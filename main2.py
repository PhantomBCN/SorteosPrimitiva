import pandas as pd

# Lee el archivo CSV con los datos de la Primitiva
# Separa por ';' porque así está estructurado el archivo
# Indica que no hay cabecera (header=None) y nombra las columnas manualmente
# Indica que todos los valores son de tipo str (string)
# Convierte la columna 'Fecha' a formato datetime y asume que el día está primero
df = pd.read_csv('SorteosPrimitiva_SinJOKER_CSV.csv', sep=';', header=None,
                 names=['Fecha', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'Complementario', 'Reintegro'],
                 dtype=str, parse_dates=['Fecha'], dayfirst=True)

# Crea un diccionario para contar las repeticiones de cada número en los sorteos
# Inicializa cada clave (número) con un valor de 0
# Se utiliza la función zfill para agregar un 0 a los números del 1 al 9
repeticiones = {str(num).zfill(2): 0 for num in range(1, 50)}

# Crea un diccionario que contiene las combinaciones ganadoras de la Primitiva
aciertos = {1: '05 19 21 27 33 35', 2: '06 11 26 34 40 48'}

# Crea un DataFrame vacío para almacenar los resultados
df_resultados = pd.DataFrame(columns=['Fecha', 'Combinación', 'Aciertos'])

# Itera sobre cada sorteo para contar los aciertos y las repeticiones
for index, row in df.iterrows():
    # Extrae los valores de la combinación actual
    valores = row[['N1', 'N2', 'N3', 'N4', 'N5', 'N6']].tolist()
    # Añade una unidad a la cuenta de cada número en el diccionario de repeticiones
    for valor in valores:
        repeticiones[valor] += 1
    # Verifica si la combinación actual es una combinación ganadora
    # y agrega una fila al DataFrame de resultados si es el caso
    for i in range(1, 3):
        if sum([1 for v in valores if v in aciertos[i].split()]) > 2:
            df_resultados.loc[len(df_resultados)] = [row['Fecha'], i, sum([1 for v in valores if v in aciertos[i].split()])]

# Imprime los resultados
# Cuenta el número de filas en el DataFrame de resultados donde la columna 'Aciertos' es igual a 3, 4, 5 o 6
print(df_resultados)

print("3 aciertos : {}".format(len(df_resultados.query("Aciertos == 3"))))
print("4 aciertos : {}".format(len(df_resultados.query("Aciertos == 4"))))
print("5 aciertos : {}".format(len(df_resultados.query("Aciertos == 5"))))
print("6 aciertos : {}".format(len(df_resultados.query("Aciertos == 6"))))

print(repeticiones)
