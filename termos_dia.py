import base64
import datetime
import gspread
import json
import numpy as np
import pandas as pd
import spacy.attrs
import os
from collections import Counter


nlp = spacy.load('pt_core_news_sm')

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) 
spreadsheet = service_account.open_by_key(spreadsheet_id) 

palavras_dia = spreadsheet.worksheet('palavras_dias') 


def termos_dia(contagem):
    linha = 2
    coluna = 1
    jornais = ['uol', 'globo', 'jovem_pan', 'folha', 'oglobo', 'estadao']

    tabelas = []
    for jornal in jornais:
        # baixar e converter os dados
        df = spreadsheet.worksheet(jornal)
        df = pd.DataFrame(df.get_all_records())
        tabelas.append(df)
    dados = pd.concat(tabelas).reset_index()

    # Filtro da data
    hoje = datetime.datetime.now()
    dia = hoje - datetime.timedelta(days=1, hours=3)
    dia = np.datetime64(dia)

    dados['data'] = pd.to_datetime(dados['data'])

    df_dia = dados[dados['data'] >= dia]

    # Filtro da relevância
    df_dia['materia'] = pd.to_numeric(df_dia['materia'])
    df_dia = df_dia[df_dia['materia'] < 31]
    df_dia = df_dia['titulo'].drop_duplicates()

    # Contagem de termos
    text = ' '.join(df_dia)

    doc = nlp(text)

    labels = [x.text for x in doc.ents if x.text != 'R$']
    dicionario = Counter(labels)

    palavras = [palavra for palavra in dicionario.most_common(20)]
    for palavra in palavras:
        contagem.update_cell(linha, coluna, palavra[0])
        contagem.update_cell(linha, coluna + 1, palavra[1])
        linha += 1
        coluna = 1

termos_dia(palavras_dia)
        
