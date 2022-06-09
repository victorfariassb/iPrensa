import gspread
import pandas as pd
import datetime
import numpy as np
import time

def contagem_candidatos(base, contagem):
    dataframe = pd.DataFrame(base.get_all_records())
    chave = dataframe['classe'][0]
    
    if 'destaque-topo' in chave:
        linha = 2
    elif "Política" in chave:
        linha = 8
    elif 'c-main-headline__title' in chave:
        linha = 14
    elif "principal" in chave:
        linha = 20
    elif 'headlineMain__link' in chave:
        linha = 226
    elif 'sem editoria' in chave:
        linha = 32
    else:
        linha = 38
    coluna = 6

    presidenciaveis = ['Bolsonaro', 'Lula', 'Ciro', 'Tebet', 'Janones', 'Bivar']
    for presidenciavel in presidenciaveis:
        
        hoje = datetime.datetime.now()
        semana = hoje - datetime.timedelta(days=7, hours=3)
        semana = np.datetime64(semana)

        dataframe['data'] = pd.to_datetime(dataframe['data'], format='%d/%m/%Y %H:%M:%S')
        dataframe['titulo'] = dataframe['titulo'].str.replace('Carlos Bolsonaro', 'Carlos B.')
        dataframe['titulo'] = dataframe['titulo'].str.replace('Flávio Bolsonaro', 'Flávio B.')
        dataframe['titulo'] = dataframe['titulo'].str.replace('Eduardo Bolsonaro', 'Eduardo B.')
        dataframe['titulo'] = dataframe['titulo'].str.replace('Ciro Nogueira', 'Ciro N.')


        df_semana = dataframe[dataframe['data'] >= semana]

        termo_semana = df_semana[['link']][df_semana['titulo'].str.contains(f'{presidenciavel}')].drop_duplicates().reset_index(drop=True)
        termo_semana = len(termo_semana)

        # Mes
        mes = hoje - datetime.timedelta(days=30, hours=3)
        mes = np.datetime64(mes)

        df_mes = dataframe[dataframe['data'] >= mes]

        termo_mes = df_mes[['link']][df_mes['titulo'].str.contains(f'{presidenciavel}')].drop_duplicates().reset_index(drop=True)
        termo_mes = len(termo_mes)

        # Ano
        ano = datetime.datetime(2022, 1, 1, 0, 0, 0)

        df_ano = dataframe[dataframe['data'] >= ano]

        termo_ano = df_ano[['link']][df_ano['titulo'].str.contains(f'{presidenciavel}')].drop_duplicates().reset_index(drop=True)
        termo_ano = len(termo_ano)
        
        time.sleep(3)
        contagem.update_cell(linha, coluna, termo_semana)
        contagem.update_cell(linha, coluna + 1, termo_mes)
        contagem.update_cell(linha, coluna + 2, termo_ano)
        linha += 1

