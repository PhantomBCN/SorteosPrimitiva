import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import premios_combinacion
import datetime


df_resultados = pd.read_csv('static/SorteosPrimitiva_SinJOKER_CSV.csv', sep=';', header=None,
                names=['Fecha', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'Complementario', 'Reintegro','Tot_Sorteos'],
                dtype=str, parse_dates=['Fecha'], dayfirst=True)

df_resultados = df_resultados.sort_values('Fecha')


app = Flask(__name__) # Sensitive: CSRFProtect is missing

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    num1 = request.form['num1']
    num2 = request.form['num2']
    num3 = request.form['num3']
    num4 = request.form['num4']
    num5 = request.form['num5']
    num6 = request.form['num6']
    complementario = request.form['complementario']
    reintegro = request.form['reintegro']
    fecha_ini = request.form['fecha_ini']
    fecha_fin = request.form['fecha_fin']

    if fecha_ini == "":
        fecha_ini= '1985-10-17'
    if fecha_fin == "":
        fecha_fin = datetime.date.today()

    print(fecha_ini)
    print(fecha_fin)


    dic_resultado={}
    dic_porcent = {}
    dic_parametros = {}

    dic_resultado = premios_combinacion.comprobar_resultados(df_resultados, num1, num2, num3, num4, num5, num6, complementario, reintegro, fecha_ini, fecha_fin)
    dic_porcent = {'0': str(round((100*dic_resultado['0'])/dic_resultado['Tot_Sorteos'],2))+"%", 
                   '1': str(round((100*dic_resultado['1'])/dic_resultado['Tot_Sorteos'],2))+"%",
                   '2': str(round((100*dic_resultado['2'])/dic_resultado['Tot_Sorteos'],2))+"%",
                   '3': str(round((100*dic_resultado['3'])/dic_resultado['Tot_Sorteos'],2))+"%",
                   '4': str(round((100*dic_resultado['4'])/dic_resultado['Tot_Sorteos'],2))+"%",
                   '5': str(round((100*dic_resultado['5'])/dic_resultado['Tot_Sorteos'],2))+"%",
                   '5C': str(round((100*dic_resultado['5C'])/dic_resultado['Tot_Sorteos'],2))+"%",
                   '6': str(round((100*dic_resultado['6'])/dic_resultado['Tot_Sorteos'],2))+"%",
                   '6R': str(round((100*dic_resultado['6R'])/dic_resultado['Tot_Sorteos'],2))+"%",
                   'Complementario': str(round((100*dic_resultado['Complementario'])/dic_resultado['Tot_Sorteos'],2))+"%",
                   'Reintegro': str(round((100*dic_resultado['Reintegro'])/dic_resultado['Tot_Sorteos'],2))+"%",
                   'Tot_Sorteos': str(round((100*dic_resultado['Tot_Sorteos'])/dic_resultado['Tot_Sorteos'],2))+"%",}
    
    dic_parametros = {'dic_res' : dic_resultado, 'dic_por': dic_porcent}

    print(dic_resultado)

    # Datos para el grafico
    x = ["0", "1", "2", "3", "4", "5", "5C", "6", "6R"]
    y = [dic_resultado['0'], dic_resultado['1'], dic_resultado['2'], dic_resultado['3'], dic_resultado['4'], dic_resultado['5'], dic_resultado['5C'], dic_resultado['6'], dic_resultado['6R'] ]

    # Gráfico de barras
    fig, ax = plt.subplots()
    rects = ax.bar(x = x, height = y)

    # Agregar etiquetas a las barras
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

    # Mostrar el gráfico
    plt.savefig('static\dist_premios.png')

    return render_template('resultado.html', resultado=dic_parametros)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
