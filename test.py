# Importar la biblioteca pandas para el manejo de datos en formato CSV
import pandas as pd

# Importar el módulo premios_combinacion que contiene la función comprobar_resultados
import premios_combinacion

# Leer el archivo CSV que contiene los resultados de la Primitiva
df_resultados = pd.read_csv('SorteosPrimitiva_SinJOKER_CSV.csv', sep=';', header=None,
                names=['Fecha', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'Complementario', 'Reintegro'],
                dtype=str, parse_dates=['Fecha'], dayfirst=True)

# Crear un diccionario vacío para almacenar los resultados de la función comprobar_resultados
resultado={}

# Llamar a la función comprobar_resultados y pasar los números del sorteo como argumentos
resultado = premios_combinacion.comprobar_resultados(df_resultados, 3, 9, 12, 14, 26, 44, 17, 2)

# Imprimir los resultados
print(resultado)
