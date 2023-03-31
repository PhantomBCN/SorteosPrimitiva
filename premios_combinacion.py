import pandas as pd

def comprobar_resultados(df_resultados, num1, num2, num3, num4, num5, num6, complementario, reintegro):

    '''df_resultados = pd.read_csv('SorteosPrimitiva_SinJOKER_CSV.csv', sep=';', header=None,
                 names=['Fecha', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'Complementario', 'Reintegro'],
                 dtype=str, parse_dates=['Fecha'], dayfirst=True)
'''
    df_premios = pd.DataFrame(columns=['Fecha', 'Aciertos'])

    aciertos=0
    

    for index, row in df_resultados.iterrows():
        # Extrae los valores de la combinación actual
        valores = row[['N1', 'N2', 'N3', 'N4', 'N5', 'N6']].tolist()
        
        if str(num1).zfill(2) in valores:
            aciertos+=1
        if str(num2).zfill(2) in valores:
            aciertos+=1
        if str(num3).zfill(2) in valores:
            aciertos+=1
        if str(num4).zfill(2) in valores:
            aciertos+=1
        if str(num5).zfill(2) in valores:
            aciertos+=1
        if str(num6).zfill(2) in valores:
            aciertos+=1
        df_premios.loc[len(df_premios)] = [row['Fecha'], aciertos]

        aciertos=0

    dic_aciertos = {"0" : len(df_premios.query("Aciertos == 0")),
                   "1" : len(df_premios.query("Aciertos == 1")),
                   "2" : len(df_premios.query("Aciertos == 2")),
                   "3" : len(df_premios.query("Aciertos == 3")),
                   "4" : len(df_premios.query("Aciertos == 4")),
                   "5" : len(df_premios.query("Aciertos == 5")),
                   "6" : len(df_premios.query("Aciertos == 6"))}


    return dic_aciertos