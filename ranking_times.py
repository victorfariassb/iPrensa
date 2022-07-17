import json
import gspread
import pandas as pd

def ranking_times(tabela1, tabela2, ranking):
    times = ['Palmeiras', 'Corinthians', 'Internacional', 'Athletico-PR', 'Atlético-MG',
            'Fluminense', 'Flamengo', 'São Paulo', 'Santos', 'Botafogo','Avaí', 'Bragantino|RB Bragantino',
             'Goiás', 'Ceará', 'Cuiabá', 'Coritiba', 'América-MG', 'Atlético-GO', 'Juventude', 'Fortaleza']

    tabelas = []

    # pegamos os dados do uol e da globo e juntamos
    tabela1 = pd.DataFrame(tabela1.get_all_records())
    tabela2 = pd.DataFrame(tabela2.get_all_records())
    df = pd.concat([tabela1, tabela2], ignore_index=True)
    df = df[['materia', 'data', 'titulo', 'link']]
    df = df.drop_duplicates(subset='link', keep='first').reset_index()

    # fazemos a contagem de vezes que cada time apareceu no titulo de uma matéria
    for time in times:
        mascara = (df['titulo'].str.contains(time) & df['link'].str.contains('esporte|futebol'))
        data = df[mascara]
        data.insert(1, 'time', time, True)
        tabelas.append(data)

    dados = pd.concat(tabelas).reset_index()
    dados = dados.groupby(['time'])['link'].count().reset_index()

    list_dados = dados.link.to_list()

    # pegamos a tabela em que vamos adicionar os dados
    ranking_times = ranking

    cell_list = ranking_times.range('C2:C21')

    for i, val in enumerate(list_dados):
        cell_list[i].value = val

    ranking_times.update_cells(cell_list)