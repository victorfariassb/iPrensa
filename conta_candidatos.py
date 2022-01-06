import pandas as pd
import datetime
import numpy as np


def contagem_candidatos(termo, dataframe):
    hoje = datetime.datetime.now()
    semana = hoje - datetime.timedelta(days=7, hours=3)
    semana = np.datetime64(semana)

    dataframe['data'] = pd.to_datetime(dataframe['data'])
    dataframe['titulo'] = dataframe['titulo'].str.replace('Carlos Bolsonaro', 'Carlos B.')
    dataframe['titulo'] = dataframe['titulo'].str.replace('Flávio Bolsonaro', 'Flávio B.')
    dataframe['titulo'] = dataframe['titulo'].str.replace('Eduardo Bolsonaro', 'Eduardo B.')

    df_semana = dataframe[dataframe['data'] >= semana]

    termo_semana = df_semana[['titulo']][df_semana['titulo'].str.contains(f'{termo}')]
    termo_semana = termo_semana.drop_duplicates().reset_index(drop=True)
    termo_semana = len(termo_semana)

    # Mes
    mes = hoje - datetime.timedelta(days=30, hours=3)
    mes = np.datetime64(mes)

    df_mes = dataframe[dataframe['data'] >= mes]

    termo_mes = df_mes[['titulo']][df_mes['titulo'].str.contains(f'{termo}')]
    termo_mes = termo_mes.drop_duplicates().reset_index(drop=True)
    termo_mes = len(termo_mes)

    # Ano
    ano = datetime.datetime(2022, 1, 1, 0, 0, 0)

    df_ano = dataframe[dataframe['data'] >= ano]

    termo_ano = df_ano[['titulo']][df_ano['titulo'].str.contains(f'{termo}')]
    termo_ano = termo_ano.drop_duplicates().reset_index(drop=True)
    termo_ano = len(termo_ano)

    return termo_semana, termo_mes, termo_ano
