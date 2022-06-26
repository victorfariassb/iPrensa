import base64
import datetime
from datetime import datetime
import gspread
import json
import numpy as np
import pandas as pd
import pytz
import spacy.attrs
import os
import time
from collections import Counter


nlp = spacy.load('pt_core_news_sm')

def termos_dia(contagem):
    linha = 2
    coluna = 1
    jornais = ['uol', 'globo', 'jovem_pan', 'folha', 'estadao', 'cnn']
    now = datetime.now(pytz.timezone('Brazil/East'))
    contagem.update_cell(linha, coluna + 3, now)

    tabelas = []
    for jornal in jornais:
        # baixar e converter os dados
        df = spreadsheet.worksheet(jornal)
        df = pd.DataFrame(df.get_all_records())
        df = df[['materia', 'data', 'titulo']]
        tabelas.append(df)
    dados = pd.concat(tabelas).reset_index()
    dados.drop(columns={'index'}, inplace=True)

    # Filtro da data
    hoje = datetime.datetime.now()
    dia = hoje - datetime.timedelta(days=1, hours=3)
    dia = np.datetime64(dia)

    dados['data'] = pd.to_datetime(dados['data'], format='%d/%m/%Y %H:%M:%S')
    selecao = dados['data'] >= dia
    df_dia = dados[selecao]

    # Filtro da relevância
    df_dia['materia'] = pd.to_numeric(df_dia['materia'])
    df_dia = df_dia[df_dia['materia'] < 30]
    df_dia = df_dia['titulo'].drop_duplicates()

    # Contagem de termos
    text = ' '.join(df_dia)

    doc = nlp(text)
    
    palavras_deletadas = ['R$', 'Seção']

    labels = [x.text for x in doc.ents if x.text not in palavras_deletadas]
    dicionario = Counter(labels)

    palavras = [palavra for palavra in dicionario.most_common(20)]
    for palavra in palavras:
        contagem.update_cell(linha, coluna, palavra[0])
        contagem.update_cell(linha, coluna + 1, palavra[1])
        linha += 1
        coluna = 1
        
