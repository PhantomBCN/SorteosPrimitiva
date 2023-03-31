import pandas as pd
from flask import Flask, render_template, request
import premios_combinacion


df_resultados = pd.read_csv('SorteosPrimitiva_SinJOKER_CSV.csv', sep=';', header=None,
                names=['Fecha', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'Complementario', 'Reintegro'],
                dtype=str, parse_dates=['Fecha'], dayfirst=True)

app = Flask(__name__)

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
    reintegro = request.form['reintegro']
    
    dic_resultado={}
    dic_resultado = premios_combinacion.comprobar_resultados(df_resultados, num1, num2, num3, num4, num5, num6, reintegro)
    
    print(dic_resultado)

    return render_template('resultado.html', resultado=dic_resultado)

if __name__ == '__main__':
    app.run(debug=True)
