# Importar la biblioteca pandas para el manejo de datos en formato CSV
import pandas as pd
import matplotlib.pyplot as plt

# Importar el módulo premios_combinacion que contiene la función comprobar_resultados
import premios_combinacion

# Leer el archivo CSV que contiene los resultados de la Primitiva
df_resultados = pd.read_csv('SorteosPrimitiva_SinJOKER_CSV.csv', sep=';', header=None,
                names=['Fecha', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'Complementario', 'Reintegro'],
                dtype=str, parse_dates=['Fecha'], dayfirst=True)

# Crear un diccionario vacío para almacenar los resultados de la función comprobar_resultados
resultado={}

# Llamar a la función comprobar_resultados y pasar los números del sorteo como argumentos
dic_resultado = premios_combinacion.comprobar_resultados(df_resultados, 3, 9, 12, 14, 26, 44, 17, 2)

# Imprimir los resultados
print(dic_resultado)


# Datos
x = ["0", "1", "2", "3", "4", "5", "5C", "6", "6R"]
y = [dic_resultado['0'], dic_resultado['1'], dic_resultado['2'], dic_resultado['3'], dic_resultado['4'], dic_resultado['5'], dic_resultado['5C'], dic_resultado['6'], dic_resultado['6R'] ]
# Gráfico de barras
fig, ax = plt.subplots()
ax.bar(x = x, height = y)
#plt.show()
plt.savefig('dist_premios.png')