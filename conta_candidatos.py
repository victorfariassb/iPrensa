import gspread
import pandas as pd
import datetime
import numpy as np


def contagem_candidatos(dataframe, pagina):
    linha = 2
    coluna = 2

    presidenciaveis = ['Bolsonaro', 'Lula', 'Moro', 'Ciro', 'Doria', 'Pacheco', 'Tebet', 'Vieira']
    for presidenciavel in presidenciaveis:
        
        hoje = datetime.datetime.now()
        semana = hoje - datetime.timedelta(days=7, hours=3)
        semana = np.datetime64(semana)

        dataframe['data'] = pd.to_datetime(dataframe['data'])
        dataframe['titulo'] = dataframe['titulo'].str.replace('Carlos Bolsonaro', 'Carlos B.')
        dataframe['titulo'] = dataframe['titulo'].str.replace('Flávio Bolsonaro', 'Flávio B.')
        dataframe['titulo'] = dataframe['titulo'].str.replace('Eduardo Bolsonaro', 'Eduardo B.')

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

        worksheet2 = spreadsheet.worksheet(f'{pagina}')
        worksheet2.update_cell(linha, coluna, termo_semana)
        worksheet2.update_cell(linha, coluna + 1, termo_mes)
        worksheet2.update_cell(linha, coluna + 2, termo_ano)
        linha += 1

