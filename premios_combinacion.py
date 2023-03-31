import pandas as pd

def comprobar_resultados(df_resultados, num1, num2, num3, num4, num5, num6, complementario, reintegro):

    '''df_resultados = pd.read_csv('SorteosPrimitiva_SinJOKER_CSV.csv', sep=';', header=None,
                 names=['Fecha', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'Complementario', 'Reintegro'],
                 dtype=str, parse_dates=['Fecha'], dayfirst=True)
'''
    df_premios = pd.DataFrame(columns=['Fecha', 'Aciertos' , 'Complementario', 'Reintegro'])

    aciertos=0
    v_comp = 'N'
    v_reint= 'N'
    

    for index, row in df_resultados.iterrows():
        # Extrae los valores de la combinación actual
        valores = row[['N1', 'N2', 'N3', 'N4', 'N5', 'N6']].tolist()
        comp = row[['Complementario']].tolist()
        reint= row[['Reintegro']].tolist()
        
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
        if str(complementario).zfill(2) in comp:
            v_comp = "S"
        if str(reintegro) in reint:
            v_reint = "S"
        df_premios.loc[len(df_premios)] = [row['Fecha'], aciertos, v_comp, v_reint]

        aciertos=0
        v_comp = 'N'
        v_reint= 'N'

    dic_aciertos = {"0" : len(df_premios.query("Aciertos == 0")),
                   "1" : len(df_premios.query("Aciertos == 1")),
                   "2" : len(df_premios.query("Aciertos == 2")),
                   "3" : len(df_premios.query("Aciertos == 3")),
                   "4" : len(df_premios.query("Aciertos == 4")),
                   "5" : len(df_premios.query("Aciertos == 5 and Complementario == 'N'" )),
                   "5C" : len(df_premios.query("Aciertos == 5 and Complementario == 'S'" )),
                   "6" : len(df_premios.query("Aciertos == 6 and Reintegro == 'N'")),
                   "6R" : len(df_premios.query("Aciertos == 6 and Reintegro == 'S'")),
                   "Complementario" : len(df_premios.query("Complementario == 'S'")),
                   "Reintegro" : len(df_premios.query("Reintegro == 'S'")),
                   "Tot_Sorteos" : len(df_resultados)}


    return dic_aciertos